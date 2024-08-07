"""
Type annotations for ec2 service client.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html)

Usage::

    ```python
    import boto3
    from mypy_boto3_ec2 import EC2Client

    client: EC2Client = boto3.client("ec2")
    ```
"""

import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Optional, Type, Union, overload

from botocore.client import BaseClient, ClientMeta
from botocore.response import StreamingBody

from .literals import (
    AccountAttributeNameType,
    AddressFamilyType,
    AffinityType,
    ArchitectureTypeType,
    ArchitectureValuesType,
    AutoPlacementType,
    BootModeValuesType,
    CapacityReservationInstancePlatformType,
    CapacityReservationTenancyType,
    ConnectivityTypeType,
    DefaultInstanceMetadataEndpointStateType,
    DefaultInstanceMetadataTagsStateType,
    DeviceTrustProviderTypeType,
    DiskImageFormatType,
    DomainTypeType,
    EkPubKeyFormatType,
    EkPubKeyTypeType,
    EndDateTypeType,
    EventTypeType,
    ExcessCapacityTerminationPolicyType,
    ExportEnvironmentType,
    FleetEventTypeType,
    FleetExcessCapacityTerminationPolicyType,
    FleetTypeType,
    FlowLogsResourceTypeType,
    FpgaImageAttributeNameType,
    HostMaintenanceType,
    HostnameTypeType,
    HostRecoveryType,
    HostTenancyType,
    HttpTokensStateType,
    ImageAttributeNameType,
    InstanceAttributeNameType,
    InstanceAutoRecoveryStateType,
    InstanceInterruptionBehaviorType,
    InstanceMatchCriteriaType,
    InstanceMetadataEndpointStateType,
    InstanceMetadataProtocolStateType,
    InstanceMetadataTagsStateType,
    InstanceTypeType,
    InterfacePermissionTypeType,
    IpAddressTypeType,
    IpamPoolPublicIpSourceType,
    IpamResourceTypeType,
    IpamTierType,
    KeyFormatType,
    KeyTypeType,
    LocalGatewayRouteTableModeType,
    LocationTypeType,
    LockModeType,
    LogDestinationTypeType,
    MetadataDefaultHttpTokensStateType,
    ModifyAvailabilityZoneOptInStatusType,
    NetworkInterfaceAttributeType,
    NetworkInterfaceCreationTypeType,
    OfferingClassTypeType,
    OfferingTypeValuesType,
    OperationTypeType,
    PlacementStrategyType,
    ProtocolType,
    ReportInstanceReasonCodesType,
    ReportStatusTypeType,
    RIProductDescriptionType,
    RuleActionType,
    SelfServicePortalType,
    ShutdownBehaviorType,
    SnapshotAttributeNameType,
    SnapshotBlockPublicAccessStateType,
    SpotInstanceTypeType,
    SpreadLevelType,
    SubnetCidrReservationTypeType,
    TargetCapacityUnitTypeType,
    TenancyType,
    TrafficDirectionType,
    TrafficMirrorFilterRuleFieldType,
    TrafficMirrorRuleActionType,
    TrafficMirrorSessionFieldType,
    TrafficTypeType,
    TransportProtocolType,
    TrustProviderTypeType,
    UnlimitedSupportedInstanceFamilyType,
    UserTrustProviderTypeType,
    VerifiedAccessEndpointTypeType,
    VirtualizationTypeType,
    VolumeAttributeNameType,
    VolumeTypeType,
    VpcAttributeNameType,
    VpcEndpointTypeType,
)
from .paginator import (
    DescribeAddressesAttributePaginator,
    DescribeAddressTransfersPaginator,
    DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator,
    DescribeByoipCidrsPaginator,
    DescribeCapacityBlockOfferingsPaginator,
    DescribeCapacityReservationFleetsPaginator,
    DescribeCapacityReservationsPaginator,
    DescribeCarrierGatewaysPaginator,
    DescribeClassicLinkInstancesPaginator,
    DescribeClientVpnAuthorizationRulesPaginator,
    DescribeClientVpnConnectionsPaginator,
    DescribeClientVpnEndpointsPaginator,
    DescribeClientVpnRoutesPaginator,
    DescribeClientVpnTargetNetworksPaginator,
    DescribeCoipPoolsPaginator,
    DescribeDhcpOptionsPaginator,
    DescribeEgressOnlyInternetGatewaysPaginator,
    DescribeExportImageTasksPaginator,
    DescribeFastLaunchImagesPaginator,
    DescribeFastSnapshotRestoresPaginator,
    DescribeFleetsPaginator,
    DescribeFlowLogsPaginator,
    DescribeFpgaImagesPaginator,
    DescribeHostReservationOfferingsPaginator,
    DescribeHostReservationsPaginator,
    DescribeHostsPaginator,
    DescribeIamInstanceProfileAssociationsPaginator,
    DescribeImagesPaginator,
    DescribeImportImageTasksPaginator,
    DescribeImportSnapshotTasksPaginator,
    DescribeInstanceConnectEndpointsPaginator,
    DescribeInstanceCreditSpecificationsPaginator,
    DescribeInstanceEventWindowsPaginator,
    DescribeInstancesPaginator,
    DescribeInstanceStatusPaginator,
    DescribeInstanceTopologyPaginator,
    DescribeInstanceTypeOfferingsPaginator,
    DescribeInstanceTypesPaginator,
    DescribeInternetGatewaysPaginator,
    DescribeIpamPoolsPaginator,
    DescribeIpamResourceDiscoveriesPaginator,
    DescribeIpamResourceDiscoveryAssociationsPaginator,
    DescribeIpamScopesPaginator,
    DescribeIpamsPaginator,
    DescribeIpv6PoolsPaginator,
    DescribeLaunchTemplatesPaginator,
    DescribeLaunchTemplateVersionsPaginator,
    DescribeLocalGatewayRouteTablesPaginator,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
    DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
    DescribeLocalGatewaysPaginator,
    DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
    DescribeLocalGatewayVirtualInterfacesPaginator,
    DescribeMacHostsPaginator,
    DescribeManagedPrefixListsPaginator,
    DescribeMovingAddressesPaginator,
    DescribeNatGatewaysPaginator,
    DescribeNetworkAclsPaginator,
    DescribeNetworkInsightsAccessScopeAnalysesPaginator,
    DescribeNetworkInsightsAccessScopesPaginator,
    DescribeNetworkInsightsAnalysesPaginator,
    DescribeNetworkInsightsPathsPaginator,
    DescribeNetworkInterfacePermissionsPaginator,
    DescribeNetworkInterfacesPaginator,
    DescribePrefixListsPaginator,
    DescribePrincipalIdFormatPaginator,
    DescribePublicIpv4PoolsPaginator,
    DescribeReplaceRootVolumeTasksPaginator,
    DescribeReservedInstancesModificationsPaginator,
    DescribeReservedInstancesOfferingsPaginator,
    DescribeRouteTablesPaginator,
    DescribeScheduledInstanceAvailabilityPaginator,
    DescribeScheduledInstancesPaginator,
    DescribeSecurityGroupRulesPaginator,
    DescribeSecurityGroupsPaginator,
    DescribeSnapshotsPaginator,
    DescribeSnapshotTierStatusPaginator,
    DescribeSpotFleetInstancesPaginator,
    DescribeSpotFleetRequestsPaginator,
    DescribeSpotInstanceRequestsPaginator,
    DescribeSpotPriceHistoryPaginator,
    DescribeStaleSecurityGroupsPaginator,
    DescribeStoreImageTasksPaginator,
    DescribeSubnetsPaginator,
    DescribeTagsPaginator,
    DescribeTrafficMirrorFiltersPaginator,
    DescribeTrafficMirrorSessionsPaginator,
    DescribeTrafficMirrorTargetsPaginator,
    DescribeTransitGatewayAttachmentsPaginator,
    DescribeTransitGatewayConnectPeersPaginator,
    DescribeTransitGatewayConnectsPaginator,
    DescribeTransitGatewayMulticastDomainsPaginator,
    DescribeTransitGatewayPeeringAttachmentsPaginator,
    DescribeTransitGatewayPolicyTablesPaginator,
    DescribeTransitGatewayRouteTableAnnouncementsPaginator,
    DescribeTransitGatewayRouteTablesPaginator,
    DescribeTransitGatewaysPaginator,
    DescribeTransitGatewayVpcAttachmentsPaginator,
    DescribeTrunkInterfaceAssociationsPaginator,
    DescribeVerifiedAccessEndpointsPaginator,
    DescribeVerifiedAccessGroupsPaginator,
    DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator,
    DescribeVerifiedAccessInstancesPaginator,
    DescribeVerifiedAccessTrustProvidersPaginator,
    DescribeVolumesModificationsPaginator,
    DescribeVolumesPaginator,
    DescribeVolumeStatusPaginator,
    DescribeVpcClassicLinkDnsSupportPaginator,
    DescribeVpcEndpointConnectionNotificationsPaginator,
    DescribeVpcEndpointConnectionsPaginator,
    DescribeVpcEndpointServiceConfigurationsPaginator,
    DescribeVpcEndpointServicePermissionsPaginator,
    DescribeVpcEndpointServicesPaginator,
    DescribeVpcEndpointsPaginator,
    DescribeVpcPeeringConnectionsPaginator,
    DescribeVpcsPaginator,
    GetAssociatedIpv6PoolCidrsPaginator,
    GetAwsNetworkPerformanceDataPaginator,
    GetGroupsForCapacityReservationPaginator,
    GetInstanceTypesFromInstanceRequirementsPaginator,
    GetIpamAddressHistoryPaginator,
    GetIpamDiscoveredAccountsPaginator,
    GetIpamDiscoveredResourceCidrsPaginator,
    GetIpamPoolAllocationsPaginator,
    GetIpamPoolCidrsPaginator,
    GetIpamResourceCidrsPaginator,
    GetManagedPrefixListAssociationsPaginator,
    GetManagedPrefixListEntriesPaginator,
    GetNetworkInsightsAccessScopeAnalysisFindingsPaginator,
    GetSecurityGroupsForVpcPaginator,
    GetSpotPlacementScoresPaginator,
    GetTransitGatewayAttachmentPropagationsPaginator,
    GetTransitGatewayMulticastDomainAssociationsPaginator,
    GetTransitGatewayPolicyTableAssociationsPaginator,
    GetTransitGatewayPrefixListReferencesPaginator,
    GetTransitGatewayRouteTableAssociationsPaginator,
    GetTransitGatewayRouteTablePropagationsPaginator,
    GetVpnConnectionDeviceTypesPaginator,
    ListImagesInRecycleBinPaginator,
    ListSnapshotsInRecycleBinPaginator,
    SearchLocalGatewayRoutesPaginator,
    SearchTransitGatewayMulticastGroupsPaginator,
)
from .type_defs import (
    AcceptAddressTransferResultTypeDef,
    AcceptReservedInstancesExchangeQuoteResultTypeDef,
    AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef,
    AcceptTransitGatewayPeeringAttachmentResultTypeDef,
    AcceptTransitGatewayVpcAttachmentResultTypeDef,
    AcceptVpcEndpointConnectionsResultTypeDef,
    AcceptVpcPeeringConnectionResultTypeDef,
    AccessScopePathRequestTypeDef,
    AddIpamOperatingRegionTypeDef,
    AddPrefixListEntryTypeDef,
    AdvertiseByoipCidrResultTypeDef,
    AllocateAddressResultTypeDef,
    AllocateHostsResultTypeDef,
    AllocateIpamPoolCidrResultTypeDef,
    ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef,
    AsnAuthorizationContextTypeDef,
    AssignIpv6AddressesResultTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssignPrivateNatGatewayAddressResultTypeDef,
    AssociateAddressResultTypeDef,
    AssociateClientVpnTargetNetworkResultTypeDef,
    AssociateEnclaveCertificateIamRoleResultTypeDef,
    AssociateIamInstanceProfileResultTypeDef,
    AssociateInstanceEventWindowResultTypeDef,
    AssociateIpamByoasnResultTypeDef,
    AssociateIpamResourceDiscoveryResultTypeDef,
    AssociateNatGatewayAddressResultTypeDef,
    AssociateRouteTableResultTypeDef,
    AssociateSubnetCidrBlockResultTypeDef,
    AssociateTransitGatewayMulticastDomainResultTypeDef,
    AssociateTransitGatewayPolicyTableResultTypeDef,
    AssociateTransitGatewayRouteTableResultTypeDef,
    AssociateTrunkInterfaceResultTypeDef,
    AssociateVpcCidrBlockResultTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttachVerifiedAccessTrustProviderResultTypeDef,
    AttachVpnGatewayResultTypeDef,
    AttributeBooleanValueTypeDef,
    AttributeValueTypeDef,
    AuthorizeClientVpnIngressResultTypeDef,
    AuthorizeSecurityGroupEgressResultTypeDef,
    AuthorizeSecurityGroupIngressResultTypeDef,
    BlobAttributeValueTypeDef,
    BlockDeviceMappingTypeDef,
    BundleInstanceResultTypeDef,
    CancelBundleTaskResultTypeDef,
    CancelCapacityReservationFleetsResultTypeDef,
    CancelCapacityReservationResultTypeDef,
    CancelImageLaunchPermissionResultTypeDef,
    CancelImportTaskResultTypeDef,
    CancelReservedInstancesListingResultTypeDef,
    CancelSpotFleetRequestsResponseTypeDef,
    CancelSpotInstanceRequestsResultTypeDef,
    CapacityReservationSpecificationTypeDef,
    CidrAuthorizationContextTypeDef,
    ClientConnectOptionsTypeDef,
    ClientDataTypeDef,
    ClientLoginBannerOptionsTypeDef,
    ClientVpnAuthenticationRequestTypeDef,
    ConfirmProductInstanceResultTypeDef,
    ConnectionLogOptionsTypeDef,
    ConnectionTrackingSpecificationRequestTypeDef,
    CopyFpgaImageResultTypeDef,
    CopyImageResultTypeDef,
    CopySnapshotResultTypeDef,
    CpuOptionsRequestTypeDef,
    CreateCapacityReservationFleetResultTypeDef,
    CreateCapacityReservationResultTypeDef,
    CreateCarrierGatewayResultTypeDef,
    CreateClientVpnEndpointResultTypeDef,
    CreateClientVpnRouteResultTypeDef,
    CreateCoipCidrResultTypeDef,
    CreateCoipPoolResultTypeDef,
    CreateCustomerGatewayResultTypeDef,
    CreateDefaultSubnetResultTypeDef,
    CreateDefaultVpcResultTypeDef,
    CreateDhcpOptionsResultTypeDef,
    CreateEgressOnlyInternetGatewayResultTypeDef,
    CreateFleetResultTypeDef,
    CreateFlowLogsResultTypeDef,
    CreateFpgaImageResultTypeDef,
    CreateImageResultTypeDef,
    CreateInstanceConnectEndpointResultTypeDef,
    CreateInstanceEventWindowResultTypeDef,
    CreateInstanceExportTaskResultTypeDef,
    CreateInternetGatewayResultTypeDef,
    CreateIpamPoolResultTypeDef,
    CreateIpamResourceDiscoveryResultTypeDef,
    CreateIpamResultTypeDef,
    CreateIpamScopeResultTypeDef,
    CreateLaunchTemplateResultTypeDef,
    CreateLaunchTemplateVersionResultTypeDef,
    CreateLocalGatewayRouteResultTypeDef,
    CreateLocalGatewayRouteTableResultTypeDef,
    CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef,
    CreateLocalGatewayRouteTableVpcAssociationResultTypeDef,
    CreateManagedPrefixListResultTypeDef,
    CreateNatGatewayResultTypeDef,
    CreateNetworkAclResultTypeDef,
    CreateNetworkInsightsAccessScopeResultTypeDef,
    CreateNetworkInsightsPathResultTypeDef,
    CreateNetworkInterfacePermissionResultTypeDef,
    CreateNetworkInterfaceResultTypeDef,
    CreatePlacementGroupResultTypeDef,
    CreatePublicIpv4PoolResultTypeDef,
    CreateReplaceRootVolumeTaskResultTypeDef,
    CreateReservedInstancesListingResultTypeDef,
    CreateRestoreImageTaskResultTypeDef,
    CreateRouteResultTypeDef,
    CreateRouteTableResultTypeDef,
    CreateSecurityGroupResultTypeDef,
    CreateSnapshotsResultTypeDef,
    CreateSpotDatafeedSubscriptionResultTypeDef,
    CreateStoreImageTaskResultTypeDef,
    CreateSubnetCidrReservationResultTypeDef,
    CreateSubnetResultTypeDef,
    CreateTrafficMirrorFilterResultTypeDef,
    CreateTrafficMirrorFilterRuleResultTypeDef,
    CreateTrafficMirrorSessionResultTypeDef,
    CreateTrafficMirrorTargetResultTypeDef,
    CreateTransitGatewayConnectPeerResultTypeDef,
    CreateTransitGatewayConnectRequestOptionsTypeDef,
    CreateTransitGatewayConnectResultTypeDef,
    CreateTransitGatewayMulticastDomainRequestOptionsTypeDef,
    CreateTransitGatewayMulticastDomainResultTypeDef,
    CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef,
    CreateTransitGatewayPeeringAttachmentResultTypeDef,
    CreateTransitGatewayPolicyTableResultTypeDef,
    CreateTransitGatewayPrefixListReferenceResultTypeDef,
    CreateTransitGatewayResultTypeDef,
    CreateTransitGatewayRouteResultTypeDef,
    CreateTransitGatewayRouteTableAnnouncementResultTypeDef,
    CreateTransitGatewayRouteTableResultTypeDef,
    CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef,
    CreateTransitGatewayVpcAttachmentResultTypeDef,
    CreateVerifiedAccessEndpointEniOptionsTypeDef,
    CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef,
    CreateVerifiedAccessEndpointResultTypeDef,
    CreateVerifiedAccessGroupResultTypeDef,
    CreateVerifiedAccessInstanceResultTypeDef,
    CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef,
    CreateVerifiedAccessTrustProviderOidcOptionsTypeDef,
    CreateVerifiedAccessTrustProviderResultTypeDef,
    CreateVolumePermissionModificationsTypeDef,
    CreateVpcEndpointConnectionNotificationResultTypeDef,
    CreateVpcEndpointResultTypeDef,
    CreateVpcEndpointServiceConfigurationResultTypeDef,
    CreateVpcPeeringConnectionResultTypeDef,
    CreateVpcResultTypeDef,
    CreateVpnConnectionResultTypeDef,
    CreateVpnGatewayResultTypeDef,
    CreditSpecificationRequestTypeDef,
    DataQueryTypeDef,
    DeleteCarrierGatewayResultTypeDef,
    DeleteClientVpnEndpointResultTypeDef,
    DeleteClientVpnRouteResultTypeDef,
    DeleteCoipCidrResultTypeDef,
    DeleteCoipPoolResultTypeDef,
    DeleteEgressOnlyInternetGatewayResultTypeDef,
    DeleteFleetsResultTypeDef,
    DeleteFlowLogsResultTypeDef,
    DeleteFpgaImageResultTypeDef,
    DeleteInstanceConnectEndpointResultTypeDef,
    DeleteInstanceEventWindowResultTypeDef,
    DeleteIpamPoolResultTypeDef,
    DeleteIpamResourceDiscoveryResultTypeDef,
    DeleteIpamResultTypeDef,
    DeleteIpamScopeResultTypeDef,
    DeleteKeyPairResultTypeDef,
    DeleteLaunchTemplateResultTypeDef,
    DeleteLaunchTemplateVersionsResultTypeDef,
    DeleteLocalGatewayRouteResultTypeDef,
    DeleteLocalGatewayRouteTableResultTypeDef,
    DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef,
    DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef,
    DeleteManagedPrefixListResultTypeDef,
    DeleteNatGatewayResultTypeDef,
    DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef,
    DeleteNetworkInsightsAccessScopeResultTypeDef,
    DeleteNetworkInsightsAnalysisResultTypeDef,
    DeleteNetworkInsightsPathResultTypeDef,
    DeleteNetworkInterfacePermissionResultTypeDef,
    DeletePublicIpv4PoolResultTypeDef,
    DeleteQueuedReservedInstancesResultTypeDef,
    DeleteSubnetCidrReservationResultTypeDef,
    DeleteTrafficMirrorFilterResultTypeDef,
    DeleteTrafficMirrorFilterRuleResultTypeDef,
    DeleteTrafficMirrorSessionResultTypeDef,
    DeleteTrafficMirrorTargetResultTypeDef,
    DeleteTransitGatewayConnectPeerResultTypeDef,
    DeleteTransitGatewayConnectResultTypeDef,
    DeleteTransitGatewayMulticastDomainResultTypeDef,
    DeleteTransitGatewayPeeringAttachmentResultTypeDef,
    DeleteTransitGatewayPolicyTableResultTypeDef,
    DeleteTransitGatewayPrefixListReferenceResultTypeDef,
    DeleteTransitGatewayResultTypeDef,
    DeleteTransitGatewayRouteResultTypeDef,
    DeleteTransitGatewayRouteTableAnnouncementResultTypeDef,
    DeleteTransitGatewayRouteTableResultTypeDef,
    DeleteTransitGatewayVpcAttachmentResultTypeDef,
    DeleteVerifiedAccessEndpointResultTypeDef,
    DeleteVerifiedAccessGroupResultTypeDef,
    DeleteVerifiedAccessInstanceResultTypeDef,
    DeleteVerifiedAccessTrustProviderResultTypeDef,
    DeleteVpcEndpointConnectionNotificationsResultTypeDef,
    DeleteVpcEndpointServiceConfigurationsResultTypeDef,
    DeleteVpcEndpointsResultTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DeprovisionByoipCidrResultTypeDef,
    DeprovisionIpamByoasnResultTypeDef,
    DeprovisionIpamPoolCidrResultTypeDef,
    DeprovisionPublicIpv4PoolCidrResultTypeDef,
    DeregisterInstanceEventNotificationAttributesResultTypeDef,
    DeregisterInstanceTagAttributeRequestTypeDef,
    DeregisterTransitGatewayMulticastGroupMembersResultTypeDef,
    DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAddressesAttributeResultTypeDef,
    DescribeAddressesResultTypeDef,
    DescribeAddressTransfersResultTypeDef,
    DescribeAggregateIdFormatResultTypeDef,
    DescribeAvailabilityZonesResultTypeDef,
    DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef,
    DescribeBundleTasksResultTypeDef,
    DescribeByoipCidrsResultTypeDef,
    DescribeCapacityBlockOfferingsResultTypeDef,
    DescribeCapacityReservationFleetsResultTypeDef,
    DescribeCapacityReservationsResultTypeDef,
    DescribeCarrierGatewaysResultTypeDef,
    DescribeClassicLinkInstancesResultTypeDef,
    DescribeClientVpnAuthorizationRulesResultTypeDef,
    DescribeClientVpnConnectionsResultTypeDef,
    DescribeClientVpnEndpointsResultTypeDef,
    DescribeClientVpnRoutesResultTypeDef,
    DescribeClientVpnTargetNetworksResultTypeDef,
    DescribeCoipPoolsResultTypeDef,
    DescribeConversionTasksResultTypeDef,
    DescribeCustomerGatewaysResultTypeDef,
    DescribeDhcpOptionsResultTypeDef,
    DescribeEgressOnlyInternetGatewaysResultTypeDef,
    DescribeElasticGpusResultTypeDef,
    DescribeExportImageTasksResultTypeDef,
    DescribeExportTasksResultTypeDef,
    DescribeFastLaunchImagesResultTypeDef,
    DescribeFastSnapshotRestoresResultTypeDef,
    DescribeFleetHistoryResultTypeDef,
    DescribeFleetInstancesResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeFlowLogsResultTypeDef,
    DescribeFpgaImageAttributeResultTypeDef,
    DescribeFpgaImagesResultTypeDef,
    DescribeHostReservationOfferingsResultTypeDef,
    DescribeHostReservationsResultTypeDef,
    DescribeHostsResultTypeDef,
    DescribeIamInstanceProfileAssociationsResultTypeDef,
    DescribeIdentityIdFormatResultTypeDef,
    DescribeIdFormatResultTypeDef,
    DescribeImagesResultTypeDef,
    DescribeImportImageTasksResultTypeDef,
    DescribeImportSnapshotTasksResultTypeDef,
    DescribeInstanceConnectEndpointsResultTypeDef,
    DescribeInstanceCreditSpecificationsResultTypeDef,
    DescribeInstanceEventNotificationAttributesResultTypeDef,
    DescribeInstanceEventWindowsResultTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeInstanceStatusResultTypeDef,
    DescribeInstanceTopologyResultTypeDef,
    DescribeInstanceTypeOfferingsResultTypeDef,
    DescribeInstanceTypesResultTypeDef,
    DescribeInternetGatewaysResultTypeDef,
    DescribeIpamByoasnResultTypeDef,
    DescribeIpamPoolsResultTypeDef,
    DescribeIpamResourceDiscoveriesResultTypeDef,
    DescribeIpamResourceDiscoveryAssociationsResultTypeDef,
    DescribeIpamScopesResultTypeDef,
    DescribeIpamsResultTypeDef,
    DescribeIpv6PoolsResultTypeDef,
    DescribeKeyPairsResultTypeDef,
    DescribeLaunchTemplatesResultTypeDef,
    DescribeLaunchTemplateVersionsResultTypeDef,
    DescribeLocalGatewayRouteTablesResultTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef,
    DescribeLocalGatewaysResultTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef,
    DescribeLocalGatewayVirtualInterfacesResultTypeDef,
    DescribeLockedSnapshotsResultTypeDef,
    DescribeMacHostsResultTypeDef,
    DescribeManagedPrefixListsResultTypeDef,
    DescribeMovingAddressesResultTypeDef,
    DescribeNatGatewaysResultTypeDef,
    DescribeNetworkAclsResultTypeDef,
    DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef,
    DescribeNetworkInsightsAccessScopesResultTypeDef,
    DescribeNetworkInsightsAnalysesResultTypeDef,
    DescribeNetworkInsightsPathsResultTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeNetworkInterfacePermissionsResultTypeDef,
    DescribeNetworkInterfacesResultTypeDef,
    DescribePlacementGroupsResultTypeDef,
    DescribePrefixListsResultTypeDef,
    DescribePrincipalIdFormatResultTypeDef,
    DescribePublicIpv4PoolsResultTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeReplaceRootVolumeTasksResultTypeDef,
    DescribeReservedInstancesListingsResultTypeDef,
    DescribeReservedInstancesModificationsResultTypeDef,
    DescribeReservedInstancesOfferingsResultTypeDef,
    DescribeReservedInstancesResultTypeDef,
    DescribeRouteTablesResultTypeDef,
    DescribeScheduledInstanceAvailabilityResultTypeDef,
    DescribeScheduledInstancesResultTypeDef,
    DescribeSecurityGroupReferencesResultTypeDef,
    DescribeSecurityGroupRulesResultTypeDef,
    DescribeSecurityGroupsResultTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeSnapshotTierStatusResultTypeDef,
    DescribeSpotDatafeedSubscriptionResultTypeDef,
    DescribeSpotFleetInstancesResponseTypeDef,
    DescribeSpotFleetRequestHistoryResponseTypeDef,
    DescribeSpotFleetRequestsResponseTypeDef,
    DescribeSpotInstanceRequestsResultTypeDef,
    DescribeSpotPriceHistoryResultTypeDef,
    DescribeStaleSecurityGroupsResultTypeDef,
    DescribeStoreImageTasksResultTypeDef,
    DescribeSubnetsResultTypeDef,
    DescribeTagsResultTypeDef,
    DescribeTrafficMirrorFilterRulesResultTypeDef,
    DescribeTrafficMirrorFiltersResultTypeDef,
    DescribeTrafficMirrorSessionsResultTypeDef,
    DescribeTrafficMirrorTargetsResultTypeDef,
    DescribeTransitGatewayAttachmentsResultTypeDef,
    DescribeTransitGatewayConnectPeersResultTypeDef,
    DescribeTransitGatewayConnectsResultTypeDef,
    DescribeTransitGatewayMulticastDomainsResultTypeDef,
    DescribeTransitGatewayPeeringAttachmentsResultTypeDef,
    DescribeTransitGatewayPolicyTablesResultTypeDef,
    DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef,
    DescribeTransitGatewayRouteTablesResultTypeDef,
    DescribeTransitGatewaysResultTypeDef,
    DescribeTransitGatewayVpcAttachmentsResultTypeDef,
    DescribeTrunkInterfaceAssociationsResultTypeDef,
    DescribeVerifiedAccessEndpointsResultTypeDef,
    DescribeVerifiedAccessGroupsResultTypeDef,
    DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef,
    DescribeVerifiedAccessInstancesResultTypeDef,
    DescribeVerifiedAccessTrustProvidersResultTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumesModificationsResultTypeDef,
    DescribeVolumesResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DescribeVpcClassicLinkDnsSupportResultTypeDef,
    DescribeVpcClassicLinkResultTypeDef,
    DescribeVpcEndpointConnectionNotificationsResultTypeDef,
    DescribeVpcEndpointConnectionsResultTypeDef,
    DescribeVpcEndpointServiceConfigurationsResultTypeDef,
    DescribeVpcEndpointServicePermissionsResultTypeDef,
    DescribeVpcEndpointServicesResultTypeDef,
    DescribeVpcEndpointsResultTypeDef,
    DescribeVpcPeeringConnectionsResultTypeDef,
    DescribeVpcsResultTypeDef,
    DescribeVpnConnectionsResultTypeDef,
    DescribeVpnGatewaysResultTypeDef,
    DestinationOptionsRequestTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DetachVerifiedAccessTrustProviderResultTypeDef,
    DisableAddressTransferResultTypeDef,
    DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef,
    DisableEbsEncryptionByDefaultResultTypeDef,
    DisableFastLaunchResultTypeDef,
    DisableFastSnapshotRestoresResultTypeDef,
    DisableImageBlockPublicAccessResultTypeDef,
    DisableImageDeprecationResultTypeDef,
    DisableImageDeregistrationProtectionResultTypeDef,
    DisableImageResultTypeDef,
    DisableIpamOrganizationAdminAccountResultTypeDef,
    DisableSerialConsoleAccessResultTypeDef,
    DisableSnapshotBlockPublicAccessResultTypeDef,
    DisableTransitGatewayRouteTablePropagationResultTypeDef,
    DisableVpcClassicLinkDnsSupportResultTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    DisassociateClientVpnTargetNetworkResultTypeDef,
    DisassociateEnclaveCertificateIamRoleResultTypeDef,
    DisassociateIamInstanceProfileResultTypeDef,
    DisassociateInstanceEventWindowResultTypeDef,
    DisassociateIpamByoasnResultTypeDef,
    DisassociateIpamResourceDiscoveryResultTypeDef,
    DisassociateNatGatewayAddressResultTypeDef,
    DisassociateSubnetCidrBlockResultTypeDef,
    DisassociateTransitGatewayMulticastDomainResultTypeDef,
    DisassociateTransitGatewayPolicyTableResultTypeDef,
    DisassociateTransitGatewayRouteTableResultTypeDef,
    DisassociateTrunkInterfaceResultTypeDef,
    DisassociateVpcCidrBlockResultTypeDef,
    DiskImageDetailTypeDef,
    DiskImageTypeDef,
    DnsOptionsSpecificationTypeDef,
    DnsServersOptionsModifyStructureTypeDef,
    ElasticGpuSpecificationTypeDef,
    ElasticInferenceAcceleratorTypeDef,
    EnableAddressTransferResultTypeDef,
    EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef,
    EnableEbsEncryptionByDefaultResultTypeDef,
    EnableFastLaunchResultTypeDef,
    EnableFastSnapshotRestoresResultTypeDef,
    EnableImageBlockPublicAccessResultTypeDef,
    EnableImageDeprecationResultTypeDef,
    EnableImageDeregistrationProtectionResultTypeDef,
    EnableImageResultTypeDef,
    EnableIpamOrganizationAdminAccountResultTypeDef,
    EnableReachabilityAnalyzerOrganizationSharingResultTypeDef,
    EnableSerialConsoleAccessResultTypeDef,
    EnableSnapshotBlockPublicAccessResultTypeDef,
    EnableTransitGatewayRouteTablePropagationResultTypeDef,
    EnableVpcClassicLinkDnsSupportResultTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    EnaSrdSpecificationTypeDef,
    EnclaveOptionsRequestTypeDef,
    ExportClientVpnClientCertificateRevocationListResultTypeDef,
    ExportClientVpnClientConfigurationResultTypeDef,
    ExportImageResultTypeDef,
    ExportTaskS3LocationRequestTypeDef,
    ExportToS3TaskSpecificationTypeDef,
    ExportTransitGatewayRoutesResultTypeDef,
    FastLaunchLaunchTemplateSpecificationRequestTypeDef,
    FastLaunchSnapshotConfigurationRequestTypeDef,
    FilterTypeDef,
    FleetLaunchTemplateConfigRequestTypeDef,
    GetAssociatedEnclaveCertificateIamRolesResultTypeDef,
    GetAssociatedIpv6PoolCidrsResultTypeDef,
    GetAwsNetworkPerformanceDataResultTypeDef,
    GetCapacityReservationUsageResultTypeDef,
    GetCoipPoolUsageResultTypeDef,
    GetConsoleOutputResultTypeDef,
    GetConsoleScreenshotResultTypeDef,
    GetDefaultCreditSpecificationResultTypeDef,
    GetEbsDefaultKmsKeyIdResultTypeDef,
    GetEbsEncryptionByDefaultResultTypeDef,
    GetFlowLogsIntegrationTemplateResultTypeDef,
    GetGroupsForCapacityReservationResultTypeDef,
    GetHostReservationPurchasePreviewResultTypeDef,
    GetImageBlockPublicAccessStateResultTypeDef,
    GetInstanceMetadataDefaultsResultTypeDef,
    GetInstanceTpmEkPubResultTypeDef,
    GetInstanceTypesFromInstanceRequirementsResultTypeDef,
    GetInstanceUefiDataResultTypeDef,
    GetIpamAddressHistoryResultTypeDef,
    GetIpamDiscoveredAccountsResultTypeDef,
    GetIpamDiscoveredPublicAddressesResultTypeDef,
    GetIpamDiscoveredResourceCidrsResultTypeDef,
    GetIpamPoolAllocationsResultTypeDef,
    GetIpamPoolCidrsResultTypeDef,
    GetIpamResourceCidrsResultTypeDef,
    GetLaunchTemplateDataResultTypeDef,
    GetManagedPrefixListAssociationsResultTypeDef,
    GetManagedPrefixListEntriesResultTypeDef,
    GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef,
    GetNetworkInsightsAccessScopeContentResultTypeDef,
    GetPasswordDataResultTypeDef,
    GetReservedInstancesExchangeQuoteResultTypeDef,
    GetSecurityGroupsForVpcResultTypeDef,
    GetSerialConsoleAccessStatusResultTypeDef,
    GetSnapshotBlockPublicAccessStateResultTypeDef,
    GetSpotPlacementScoresResultTypeDef,
    GetSubnetCidrReservationsResultTypeDef,
    GetTransitGatewayAttachmentPropagationsResultTypeDef,
    GetTransitGatewayMulticastDomainAssociationsResultTypeDef,
    GetTransitGatewayPolicyTableAssociationsResultTypeDef,
    GetTransitGatewayPolicyTableEntriesResultTypeDef,
    GetTransitGatewayPrefixListReferencesResultTypeDef,
    GetTransitGatewayRouteTableAssociationsResultTypeDef,
    GetTransitGatewayRouteTablePropagationsResultTypeDef,
    GetVerifiedAccessEndpointPolicyResultTypeDef,
    GetVerifiedAccessGroupPolicyResultTypeDef,
    GetVpnConnectionDeviceSampleConfigurationResultTypeDef,
    GetVpnConnectionDeviceTypesResultTypeDef,
    GetVpnTunnelReplacementStatusResultTypeDef,
    HibernationOptionsRequestTypeDef,
    IamInstanceProfileSpecificationTypeDef,
    IcmpTypeCodeTypeDef,
    ImageAttributeTypeDef,
    ImageDiskContainerTypeDef,
    ImportClientVpnClientCertificateRevocationListResultTypeDef,
    ImportImageLicenseConfigurationRequestTypeDef,
    ImportImageResultTypeDef,
    ImportInstanceLaunchSpecificationTypeDef,
    ImportInstanceResultTypeDef,
    ImportKeyPairResultTypeDef,
    ImportSnapshotResultTypeDef,
    ImportVolumeResultTypeDef,
    InstanceAttributeTypeDef,
    InstanceBlockDeviceMappingSpecificationTypeDef,
    InstanceCreditSpecificationRequestTypeDef,
    InstanceEventWindowAssociationRequestTypeDef,
    InstanceEventWindowDisassociationRequestTypeDef,
    InstanceEventWindowTimeRangeRequestTypeDef,
    InstanceIpv6AddressTypeDef,
    InstanceMaintenanceOptionsRequestTypeDef,
    InstanceMarketOptionsRequestTypeDef,
    InstanceMetadataOptionsRequestTypeDef,
    InstanceNetworkInterfaceSpecificationTypeDef,
    InstanceRequirementsRequestTypeDef,
    InstanceRequirementsWithMetadataRequestTypeDef,
    InstanceSpecificationTypeDef,
    IntegrateServicesTypeDef,
    IpamCidrAuthorizationContextTypeDef,
    IpamPoolSourceResourceRequestTypeDef,
    IpPermissionTypeDef,
    Ipv4PrefixSpecificationRequestTypeDef,
    Ipv6PrefixSpecificationRequestTypeDef,
    KeyPairTypeDef,
    LaunchPermissionModificationsTypeDef,
    LaunchTemplateConfigTypeDef,
    LaunchTemplateSpecificationTypeDef,
    LicenseConfigurationRequestTypeDef,
    ListImagesInRecycleBinResultTypeDef,
    ListSnapshotsInRecycleBinResultTypeDef,
    LoadPermissionModificationsTypeDef,
    LockSnapshotResultTypeDef,
    ModifyAddressAttributeResultTypeDef,
    ModifyAvailabilityZoneGroupResultTypeDef,
    ModifyCapacityReservationFleetResultTypeDef,
    ModifyCapacityReservationResultTypeDef,
    ModifyClientVpnEndpointResultTypeDef,
    ModifyDefaultCreditSpecificationResultTypeDef,
    ModifyEbsDefaultKmsKeyIdResultTypeDef,
    ModifyFleetResultTypeDef,
    ModifyFpgaImageAttributeResultTypeDef,
    ModifyHostsResultTypeDef,
    ModifyInstanceCapacityReservationAttributesResultTypeDef,
    ModifyInstanceCreditSpecificationResultTypeDef,
    ModifyInstanceEventStartTimeResultTypeDef,
    ModifyInstanceEventWindowResultTypeDef,
    ModifyInstanceMaintenanceOptionsResultTypeDef,
    ModifyInstanceMetadataDefaultsResultTypeDef,
    ModifyInstanceMetadataOptionsResultTypeDef,
    ModifyInstancePlacementResultTypeDef,
    ModifyIpamPoolResultTypeDef,
    ModifyIpamResourceCidrResultTypeDef,
    ModifyIpamResourceDiscoveryResultTypeDef,
    ModifyIpamResultTypeDef,
    ModifyIpamScopeResultTypeDef,
    ModifyLaunchTemplateResultTypeDef,
    ModifyLocalGatewayRouteResultTypeDef,
    ModifyManagedPrefixListResultTypeDef,
    ModifyPrivateDnsNameOptionsResultTypeDef,
    ModifyReservedInstancesResultTypeDef,
    ModifySecurityGroupRulesResultTypeDef,
    ModifySnapshotTierResultTypeDef,
    ModifySpotFleetRequestResponseTypeDef,
    ModifyTrafficMirrorFilterNetworkServicesResultTypeDef,
    ModifyTrafficMirrorFilterRuleResultTypeDef,
    ModifyTrafficMirrorSessionResultTypeDef,
    ModifyTransitGatewayOptionsTypeDef,
    ModifyTransitGatewayPrefixListReferenceResultTypeDef,
    ModifyTransitGatewayResultTypeDef,
    ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef,
    ModifyTransitGatewayVpcAttachmentResultTypeDef,
    ModifyVerifiedAccessEndpointEniOptionsTypeDef,
    ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef,
    ModifyVerifiedAccessEndpointPolicyResultTypeDef,
    ModifyVerifiedAccessEndpointResultTypeDef,
    ModifyVerifiedAccessGroupPolicyResultTypeDef,
    ModifyVerifiedAccessGroupResultTypeDef,
    ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef,
    ModifyVerifiedAccessInstanceResultTypeDef,
    ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef,
    ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef,
    ModifyVerifiedAccessTrustProviderResultTypeDef,
    ModifyVolumeResultTypeDef,
    ModifyVpcEndpointConnectionNotificationResultTypeDef,
    ModifyVpcEndpointResultTypeDef,
    ModifyVpcEndpointServiceConfigurationResultTypeDef,
    ModifyVpcEndpointServicePayerResponsibilityResultTypeDef,
    ModifyVpcEndpointServicePermissionsResultTypeDef,
    ModifyVpcPeeringConnectionOptionsResultTypeDef,
    ModifyVpcTenancyResultTypeDef,
    ModifyVpnConnectionOptionsResultTypeDef,
    ModifyVpnConnectionResultTypeDef,
    ModifyVpnTunnelCertificateResultTypeDef,
    ModifyVpnTunnelOptionsResultTypeDef,
    ModifyVpnTunnelOptionsSpecificationTypeDef,
    MonitorInstancesResultTypeDef,
    MoveAddressToVpcResultTypeDef,
    MoveByoipCidrToIpamResultTypeDef,
    NetworkInterfaceAttachmentChangesTypeDef,
    NewDhcpConfigurationTypeDef,
    OnDemandOptionsRequestTypeDef,
    PathRequestFilterTypeDef,
    PeeringConnectionOptionsRequestTypeDef,
    PlacementTypeDef,
    PortRangeTypeDef,
    PriceScheduleSpecificationTypeDef,
    PrivateDnsNameOptionsRequestTypeDef,
    PrivateIpAddressSpecificationTypeDef,
    ProvisionByoipCidrResultTypeDef,
    ProvisionIpamByoasnResultTypeDef,
    ProvisionIpamPoolCidrResultTypeDef,
    ProvisionPublicIpv4PoolCidrResultTypeDef,
    PurchaseCapacityBlockResultTypeDef,
    PurchaseHostReservationResultTypeDef,
    PurchaseRequestTypeDef,
    PurchaseReservedInstancesOfferingResultTypeDef,
    PurchaseScheduledInstancesResultTypeDef,
    RegisterImageResultTypeDef,
    RegisterInstanceEventNotificationAttributesResultTypeDef,
    RegisterInstanceTagAttributeRequestTypeDef,
    RegisterTransitGatewayMulticastGroupMembersResultTypeDef,
    RegisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    RejectTransitGatewayMulticastDomainAssociationsResultTypeDef,
    RejectTransitGatewayPeeringAttachmentResultTypeDef,
    RejectTransitGatewayVpcAttachmentResultTypeDef,
    RejectVpcEndpointConnectionsResultTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReleaseHostsResultTypeDef,
    ReleaseIpamPoolAllocationResultTypeDef,
    RemoveIpamOperatingRegionTypeDef,
    RemovePrefixListEntryTypeDef,
    ReplaceIamInstanceProfileAssociationResultTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    ReplaceRouteTableAssociationResultTypeDef,
    ReplaceTransitGatewayRouteResultTypeDef,
    ReplaceVpnTunnelResultTypeDef,
    RequestIpamResourceTagTypeDef,
    RequestLaunchTemplateDataTypeDef,
    RequestSpotFleetResponseTypeDef,
    RequestSpotInstancesResultTypeDef,
    RequestSpotLaunchSpecificationTypeDef,
    ReservationFleetInstanceSpecificationTypeDef,
    ReservationResponseMetadataTypeDef,
    ReservedInstanceLimitPriceTypeDef,
    ReservedInstancesConfigurationTypeDef,
    ResetAddressAttributeResultTypeDef,
    ResetEbsDefaultKmsKeyIdResultTypeDef,
    ResetFpgaImageAttributeResultTypeDef,
    RestoreAddressToClassicResultTypeDef,
    RestoreImageFromRecycleBinResultTypeDef,
    RestoreManagedPrefixListVersionResultTypeDef,
    RestoreSnapshotFromRecycleBinResultTypeDef,
    RestoreSnapshotTierResultTypeDef,
    RevokeClientVpnIngressResultTypeDef,
    RevokeSecurityGroupEgressResultTypeDef,
    RevokeSecurityGroupIngressResultTypeDef,
    RunInstancesMonitoringEnabledTypeDef,
    RunScheduledInstancesResultTypeDef,
    S3ObjectTagTypeDef,
    ScheduledInstanceRecurrenceRequestTypeDef,
    ScheduledInstancesLaunchSpecificationTypeDef,
    SearchLocalGatewayRoutesResultTypeDef,
    SearchTransitGatewayMulticastGroupsResultTypeDef,
    SearchTransitGatewayRoutesResultTypeDef,
    SecurityGroupRuleDescriptionTypeDef,
    SecurityGroupRuleUpdateTypeDef,
    SlotDateTimeRangeRequestTypeDef,
    SlotStartTimeRangeRequestTypeDef,
    SnapshotDiskContainerTypeDef,
    SnapshotResponseMetadataTypeDef,
    SpotFleetRequestConfigDataTypeDef,
    SpotOptionsRequestTypeDef,
    StartInstancesResultTypeDef,
    StartNetworkInsightsAccessScopeAnalysisResultTypeDef,
    StartNetworkInsightsAnalysisResultTypeDef,
    StartVpcEndpointServicePrivateDnsVerificationResultTypeDef,
    StopInstancesResultTypeDef,
    StorageLocationTypeDef,
    StorageTypeDef,
    SubnetConfigurationTypeDef,
    TagSpecificationTypeDef,
    TagTypeDef,
    TargetCapacitySpecificationRequestTypeDef,
    TargetConfigurationRequestTypeDef,
    TerminateClientVpnConnectionsResultTypeDef,
    TerminateInstancesResultTypeDef,
    TrafficMirrorPortRangeRequestTypeDef,
    TransitGatewayConnectRequestBgpOptionsTypeDef,
    TransitGatewayRequestOptionsTypeDef,
    UnassignIpv6AddressesResultTypeDef,
    UnassignPrivateNatGatewayAddressResultTypeDef,
    UnlockSnapshotResultTypeDef,
    UnmonitorInstancesResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef,
    VerifiedAccessLogOptionsTypeDef,
    VerifiedAccessSseSpecificationRequestTypeDef,
    VolumeAttachmentResponseMetadataTypeDef,
    VolumeDetailTypeDef,
    VolumeResponseMetadataTypeDef,
    VpnConnectionOptionsSpecificationTypeDef,
    WithdrawByoipCidrResultTypeDef,
)
from .waiter import (
    BundleTaskCompleteWaiter,
    ConversionTaskCancelledWaiter,
    ConversionTaskCompletedWaiter,
    ConversionTaskDeletedWaiter,
    CustomerGatewayAvailableWaiter,
    ExportTaskCancelledWaiter,
    ExportTaskCompletedWaiter,
    ImageAvailableWaiter,
    ImageExistsWaiter,
    InstanceExistsWaiter,
    InstanceRunningWaiter,
    InstanceStatusOkWaiter,
    InstanceStoppedWaiter,
    InstanceTerminatedWaiter,
    InternetGatewayExistsWaiter,
    KeyPairExistsWaiter,
    NatGatewayAvailableWaiter,
    NatGatewayDeletedWaiter,
    NetworkInterfaceAvailableWaiter,
    PasswordDataAvailableWaiter,
    SecurityGroupExistsWaiter,
    SnapshotCompletedWaiter,
    SnapshotImportedWaiter,
    SpotInstanceRequestFulfilledWaiter,
    StoreImageTaskCompleteWaiter,
    SubnetAvailableWaiter,
    SystemStatusOkWaiter,
    VolumeAvailableWaiter,
    VolumeDeletedWaiter,
    VolumeInUseWaiter,
    VpcAvailableWaiter,
    VpcExistsWaiter,
    VpcPeeringConnectionDeletedWaiter,
    VpcPeeringConnectionExistsWaiter,
    VpnConnectionAvailableWaiter,
    VpnConnectionDeletedWaiter,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = ("EC2Client",)

class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str

class Exceptions:
    ClientError: Type[BotocoreClientError]

class EC2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EC2Client exceptions.
        """

    def accept_address_transfer(
        self,
        *,
        Address: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> AcceptAddressTransferResultTypeDef:
        """
        Accepts an Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.accept_address_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept_address_transfer)
        """

    def accept_reserved_instances_exchange_quote(
        self,
        *,
        ReservedInstanceIds: List[str],
        DryRun: bool = None,
        TargetConfigurations: List["TargetConfigurationRequestTypeDef"] = None
    ) -> AcceptReservedInstancesExchangeQuoteResultTypeDef:
        """
        Accepts the Convertible Reserved Instance exchange quote described in the
        GetReservedInstancesExchangeQuote call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.accept_reserved_instances_exchange_quote)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept_reserved_instances_exchange_quote)
        """

    def accept_transit_gateway_multicast_domain_associations(
        self,
        *,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None
    ) -> AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        Accepts a request to associate subnets with a transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.accept_transit_gateway_multicast_domain_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept_transit_gateway_multicast_domain_associations)
        """

    def accept_transit_gateway_peering_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> AcceptTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Accepts a transit gateway peering attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.accept_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept_transit_gateway_peering_attachment)
        """

    def accept_transit_gateway_vpc_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> AcceptTransitGatewayVpcAttachmentResultTypeDef:
        """
        Accepts a request to attach a VPC to a transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.accept_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept_transit_gateway_vpc_attachment)
        """

    def accept_vpc_endpoint_connections(
        self, *, ServiceId: str, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> AcceptVpcEndpointConnectionsResultTypeDef:
        """
        Accepts connection requests to your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.accept_vpc_endpoint_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept_vpc_endpoint_connections)
        """

    def accept_vpc_peering_connection(
        self, *, VpcPeeringConnectionId: str, DryRun: bool = None
    ) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        Accept a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.accept_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#accept_vpc_peering_connection)
        """

    def advertise_byoip_cidr(
        self, *, Cidr: str, Asn: str = None, DryRun: bool = None, NetworkBorderGroup: str = None
    ) -> AdvertiseByoipCidrResultTypeDef:
        """
        Advertises an IPv4 or IPv6 address range that is provisioned for use with your
        Amazon Web Services resources through bring your own IP addresses (BYOIP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.advertise_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#advertise_byoip_cidr)
        """

    def allocate_address(
        self,
        *,
        Domain: DomainTypeType = None,
        Address: str = None,
        PublicIpv4Pool: str = None,
        NetworkBorderGroup: str = None,
        CustomerOwnedIpv4Pool: str = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> AllocateAddressResultTypeDef:
        """
        Allocates an Elastic IP address to your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.allocate_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#allocate_address)
        """

    def allocate_hosts(
        self,
        *,
        AvailabilityZone: str,
        AutoPlacement: AutoPlacementType = None,
        ClientToken: str = None,
        InstanceType: str = None,
        InstanceFamily: str = None,
        Quantity: int = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        HostRecovery: HostRecoveryType = None,
        OutpostArn: str = None,
        HostMaintenance: HostMaintenanceType = None,
        AssetIds: List[str] = None
    ) -> AllocateHostsResultTypeDef:
        """
        Allocates a Dedicated Host to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.allocate_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#allocate_hosts)
        """

    def allocate_ipam_pool_cidr(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = None,
        Cidr: str = None,
        NetmaskLength: int = None,
        ClientToken: str = None,
        Description: str = None,
        PreviewNextCidr: bool = None,
        AllowedCidrs: List[str] = None,
        DisallowedCidrs: List[str] = None
    ) -> AllocateIpamPoolCidrResultTypeDef:
        """
        Allocate a CIDR from an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.allocate_ipam_pool_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#allocate_ipam_pool_cidr)
        """

    def apply_security_groups_to_client_vpn_target_network(
        self,
        *,
        ClientVpnEndpointId: str,
        VpcId: str,
        SecurityGroupIds: List[str],
        DryRun: bool = None
    ) -> ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef:
        """
        Applies a security group to the association between the target network and the
        Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.apply_security_groups_to_client_vpn_target_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#apply_security_groups_to_client_vpn_target_network)
        """

    def assign_ipv6_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List[str] = None,
        Ipv6PrefixCount: int = None,
        Ipv6Prefixes: List[str] = None
    ) -> AssignIpv6AddressesResultTypeDef:
        """
        Assigns one or more IPv6 addresses to the specified network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.assign_ipv6_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#assign_ipv6_addresses)
        """

    def assign_private_ip_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        AllowReassignment: bool = None,
        PrivateIpAddresses: List[str] = None,
        SecondaryPrivateIpAddressCount: int = None,
        Ipv4Prefixes: List[str] = None,
        Ipv4PrefixCount: int = None
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        Assigns one or more secondary private IP addresses to the specified network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.assign_private_ip_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#assign_private_ip_addresses)
        """

    def assign_private_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        PrivateIpAddresses: List[str] = None,
        PrivateIpAddressCount: int = None,
        DryRun: bool = None
    ) -> AssignPrivateNatGatewayAddressResultTypeDef:
        """
        Assigns private IPv4 addresses to a private NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.assign_private_nat_gateway_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#assign_private_nat_gateway_address)
        """

    def associate_address(
        self,
        *,
        AllocationId: str = None,
        InstanceId: str = None,
        PublicIp: str = None,
        AllowReassociation: bool = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        PrivateIpAddress: str = None
    ) -> AssociateAddressResultTypeDef:
        """
        Associates an Elastic IP address, or carrier IP address (for instances that are
        in subnets in Wavelength Zones) with an instance or a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_address)
        """

    def associate_client_vpn_target_network(
        self,
        *,
        ClientVpnEndpointId: str,
        SubnetId: str,
        ClientToken: str = None,
        DryRun: bool = None
    ) -> AssociateClientVpnTargetNetworkResultTypeDef:
        """
        Associates a target network with a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_client_vpn_target_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_client_vpn_target_network)
        """

    def associate_dhcp_options(
        self, *, DhcpOptionsId: str, VpcId: str, DryRun: bool = None
    ) -> None:
        """
        Associates a set of DHCP options (that you've previously created) with the
        specified VPC, or associates no DHCP options with the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_dhcp_options)
        """

    def associate_enclave_certificate_iam_role(
        self, *, CertificateArn: str, RoleArn: str, DryRun: bool = None
    ) -> AssociateEnclaveCertificateIamRoleResultTypeDef:
        """
        Associates an Identity and Access Management (IAM) role with an Certificate
        Manager (ACM) certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_enclave_certificate_iam_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_enclave_certificate_iam_role)
        """

    def associate_iam_instance_profile(
        self, *, IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef", InstanceId: str
    ) -> AssociateIamInstanceProfileResultTypeDef:
        """
        Associates an IAM instance profile with a running or stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_iam_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_iam_instance_profile)
        """

    def associate_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        AssociationTarget: "InstanceEventWindowAssociationRequestTypeDef",
        DryRun: bool = None
    ) -> AssociateInstanceEventWindowResultTypeDef:
        """
        Associates one or more targets with an event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_instance_event_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_instance_event_window)
        """

    def associate_ipam_byoasn(
        self, *, Asn: str, Cidr: str, DryRun: bool = None
    ) -> AssociateIpamByoasnResultTypeDef:
        """
        Associates your Autonomous System Number (ASN) with a BYOIP CIDR that you own in
        the same Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_ipam_byoasn)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_ipam_byoasn)
        """

    def associate_ipam_resource_discovery(
        self,
        *,
        IpamId: str,
        IpamResourceDiscoveryId: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None
    ) -> AssociateIpamResourceDiscoveryResultTypeDef:
        """
        Associates an IPAM resource discovery with an Amazon VPC IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_ipam_resource_discovery)
        """

    def associate_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        AllocationIds: List[str],
        PrivateIpAddresses: List[str] = None,
        DryRun: bool = None
    ) -> AssociateNatGatewayAddressResultTypeDef:
        """
        Associates Elastic IP addresses (EIPs) and private IPv4 addresses with a public
        NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_nat_gateway_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_nat_gateway_address)
        """

    def associate_route_table(
        self, *, RouteTableId: str, DryRun: bool = None, SubnetId: str = None, GatewayId: str = None
    ) -> AssociateRouteTableResultTypeDef:
        """
        Associates a subnet in your VPC or an internet gateway or virtual private
        gateway attached to your VPC with a route table in your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_route_table)
        """

    def associate_subnet_cidr_block(
        self,
        *,
        SubnetId: str,
        Ipv6CidrBlock: str = None,
        Ipv6IpamPoolId: str = None,
        Ipv6NetmaskLength: int = None
    ) -> AssociateSubnetCidrBlockResultTypeDef:
        """
        Associates a CIDR block with your subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_subnet_cidr_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_subnet_cidr_block)
        """

    def associate_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        TransitGatewayAttachmentId: str,
        SubnetIds: List[str],
        DryRun: bool = None
    ) -> AssociateTransitGatewayMulticastDomainResultTypeDef:
        """
        Associates the specified subnets and transit gateway attachments with the
        specified transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_transit_gateway_multicast_domain)
        """

    def associate_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool = None
    ) -> AssociateTransitGatewayPolicyTableResultTypeDef:
        """
        Associates the specified transit gateway attachment with a transit gateway
        policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_transit_gateway_policy_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_transit_gateway_policy_table)
        """

    def associate_transit_gateway_route_table(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool = None
    ) -> AssociateTransitGatewayRouteTableResultTypeDef:
        """
        Associates the specified attachment with the specified transit gateway route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_transit_gateway_route_table)
        """

    def associate_trunk_interface(
        self,
        *,
        BranchInterfaceId: str,
        TrunkInterfaceId: str,
        VlanId: int = None,
        GreKey: int = None,
        ClientToken: str = None,
        DryRun: bool = None
    ) -> AssociateTrunkInterfaceResultTypeDef:
        """
        Associates a branch network interface with a trunk network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_trunk_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_trunk_interface)
        """

    def associate_vpc_cidr_block(
        self,
        *,
        VpcId: str,
        AmazonProvidedIpv6CidrBlock: bool = None,
        CidrBlock: str = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
        Ipv6Pool: str = None,
        Ipv6CidrBlock: str = None,
        Ipv4IpamPoolId: str = None,
        Ipv4NetmaskLength: int = None,
        Ipv6IpamPoolId: str = None,
        Ipv6NetmaskLength: int = None
    ) -> AssociateVpcCidrBlockResultTypeDef:
        """
        Associates a CIDR block with your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.associate_vpc_cidr_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#associate_vpc_cidr_block)
        """

    def attach_classic_link_vpc(
        self, *, Groups: List[str], InstanceId: str, VpcId: str, DryRun: bool = None
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.attach_classic_link_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach_classic_link_vpc)
        """

    def attach_internet_gateway(
        self, *, InternetGatewayId: str, VpcId: str, DryRun: bool = None
    ) -> None:
        """
        Attaches an internet gateway or a virtual private gateway to a VPC, enabling
        connectivity between the internet and the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.attach_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach_internet_gateway)
        """

    def attach_network_interface(
        self,
        *,
        DeviceIndex: int,
        InstanceId: str,
        NetworkInterfaceId: str,
        DryRun: bool = None,
        NetworkCardIndex: int = None,
        EnaSrdSpecification: "EnaSrdSpecificationTypeDef" = None
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        Attaches a network interface to an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.attach_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach_network_interface)
        """

    def attach_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessInstanceId: str,
        VerifiedAccessTrustProviderId: str,
        ClientToken: str = None,
        DryRun: bool = None
    ) -> AttachVerifiedAccessTrustProviderResultTypeDef:
        """
        Attaches the specified Amazon Web Services Verified Access trust provider to the
        specified Amazon Web Services Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.attach_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach_verified_access_trust_provider)
        """

    def attach_volume(
        self, *, Device: str, InstanceId: str, VolumeId: str, DryRun: bool = None
    ) -> VolumeAttachmentResponseMetadataTypeDef:
        """
        Attaches an EBS volume to a running or stopped instance and exposes it to the
        instance with the specified device name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.attach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach_volume)
        """

    def attach_vpn_gateway(
        self, *, VpcId: str, VpnGatewayId: str, DryRun: bool = None
    ) -> AttachVpnGatewayResultTypeDef:
        """
        Attaches a virtual private gateway to a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.attach_vpn_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#attach_vpn_gateway)
        """

    def authorize_client_vpn_ingress(
        self,
        *,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = None,
        AuthorizeAllGroups: bool = None,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None
    ) -> AuthorizeClientVpnIngressResultTypeDef:
        """
        Adds an ingress authorization rule to a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.authorize_client_vpn_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#authorize_client_vpn_ingress)
        """

    def authorize_security_group_egress(
        self,
        *,
        GroupId: str,
        DryRun: bool = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None
    ) -> AuthorizeSecurityGroupEgressResultTypeDef:
        """
        Adds the specified outbound (egress) rules to a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.authorize_security_group_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#authorize_security_group_egress)
        """

    def authorize_security_group_ingress(
        self,
        *,
        CidrIp: str = None,
        FromPort: int = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> AuthorizeSecurityGroupIngressResultTypeDef:
        """
        Adds the specified inbound (ingress) rules to a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.authorize_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#authorize_security_group_ingress)
        """

    def bundle_instance(
        self, *, InstanceId: str, Storage: "StorageTypeDef", DryRun: bool = None
    ) -> BundleInstanceResultTypeDef:
        """
        Bundles an Amazon instance store-backed Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.bundle_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#bundle_instance)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.can_paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#can_paginate)
        """

    def cancel_bundle_task(
        self, *, BundleId: str, DryRun: bool = None
    ) -> CancelBundleTaskResultTypeDef:
        """
        Cancels a bundling operation for an instance store-backed Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_bundle_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_bundle_task)
        """

    def cancel_capacity_reservation(
        self, *, CapacityReservationId: str, DryRun: bool = None
    ) -> CancelCapacityReservationResultTypeDef:
        """
        Cancels the specified Capacity Reservation, releases the reserved capacity, and
        changes the Capacity Reservation's state to `cancelled`.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_capacity_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_capacity_reservation)
        """

    def cancel_capacity_reservation_fleets(
        self, *, CapacityReservationFleetIds: List[str], DryRun: bool = None
    ) -> CancelCapacityReservationFleetsResultTypeDef:
        """
        Cancels one or more Capacity Reservation Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_capacity_reservation_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_capacity_reservation_fleets)
        """

    def cancel_conversion_task(
        self, *, ConversionTaskId: str, DryRun: bool = None, ReasonMessage: str = None
    ) -> None:
        """
        Cancels an active conversion task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_conversion_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_conversion_task)
        """

    def cancel_export_task(self, *, ExportTaskId: str) -> None:
        """
        Cancels an active export task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_export_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_export_task)
        """

    def cancel_image_launch_permission(
        self, *, ImageId: str, DryRun: bool = None
    ) -> CancelImageLaunchPermissionResultTypeDef:
        """
        Removes your Amazon Web Services account from the launch permissions for the
        specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_image_launch_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_image_launch_permission)
        """

    def cancel_import_task(
        self, *, CancelReason: str = None, DryRun: bool = None, ImportTaskId: str = None
    ) -> CancelImportTaskResultTypeDef:
        """
        Cancels an in-process import virtual machine or import snapshot task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_import_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_import_task)
        """

    def cancel_reserved_instances_listing(
        self, *, ReservedInstancesListingId: str
    ) -> CancelReservedInstancesListingResultTypeDef:
        """
        Cancels the specified Reserved Instance listing in the Reserved Instance
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_reserved_instances_listing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_reserved_instances_listing)
        """

    def cancel_spot_fleet_requests(
        self, *, SpotFleetRequestIds: List[str], TerminateInstances: bool, DryRun: bool = None
    ) -> CancelSpotFleetRequestsResponseTypeDef:
        """
        Cancels the specified Spot Fleet requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_spot_fleet_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_spot_fleet_requests)
        """

    def cancel_spot_instance_requests(
        self, *, SpotInstanceRequestIds: List[str], DryRun: bool = None
    ) -> CancelSpotInstanceRequestsResultTypeDef:
        """
        Cancels one or more Spot Instance requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.cancel_spot_instance_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#cancel_spot_instance_requests)
        """

    def close(self) -> None:
        """
        Closes underlying endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.close)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#close)
        """

    def confirm_product_instance(
        self, *, InstanceId: str, ProductCode: str, DryRun: bool = None
    ) -> ConfirmProductInstanceResultTypeDef:
        """
        Determines whether a product code is associated with an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.confirm_product_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#confirm_product_instance)
        """

    def copy_fpga_image(
        self,
        *,
        SourceFpgaImageId: str,
        SourceRegion: str,
        DryRun: bool = None,
        Description: str = None,
        Name: str = None,
        ClientToken: str = None
    ) -> CopyFpgaImageResultTypeDef:
        """
        Copies the specified Amazon FPGA Image (AFI) to the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.copy_fpga_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#copy_fpga_image)
        """

    def copy_image(
        self,
        *,
        Name: str,
        SourceImageId: str,
        SourceRegion: str,
        ClientToken: str = None,
        Description: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        DestinationOutpostArn: str = None,
        DryRun: bool = None,
        CopyImageTags: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CopyImageResultTypeDef:
        """
        Initiates the copy of an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.copy_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#copy_image)
        """

    def copy_snapshot(
        self,
        *,
        SourceRegion: str,
        SourceSnapshotId: str,
        Description: str = None,
        DestinationOutpostArn: str = None,
        DestinationRegion: str = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        PresignedUrl: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CopySnapshotResultTypeDef:
        """
        Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.copy_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#copy_snapshot)
        """

    def create_capacity_reservation(
        self,
        *,
        InstanceType: str,
        InstancePlatform: CapacityReservationInstancePlatformType,
        InstanceCount: int,
        ClientToken: str = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        Tenancy: CapacityReservationTenancyType = None,
        EbsOptimized: bool = None,
        EphemeralStorage: bool = None,
        EndDate: Union[datetime, str] = None,
        EndDateType: EndDateTypeType = None,
        InstanceMatchCriteria: InstanceMatchCriteriaType = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        OutpostArn: str = None,
        PlacementGroupArn: str = None
    ) -> CreateCapacityReservationResultTypeDef:
        """
        Creates a new Capacity Reservation with the specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_capacity_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_capacity_reservation)
        """

    def create_capacity_reservation_fleet(
        self,
        *,
        InstanceTypeSpecifications: List["ReservationFleetInstanceSpecificationTypeDef"],
        TotalTargetCapacity: int,
        AllocationStrategy: str = None,
        ClientToken: str = None,
        Tenancy: Literal["default"] = None,
        EndDate: Union[datetime, str] = None,
        InstanceMatchCriteria: Literal["open"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateCapacityReservationFleetResultTypeDef:
        """
        Creates a Capacity Reservation Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_capacity_reservation_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_capacity_reservation_fleet)
        """

    def create_carrier_gateway(
        self,
        *,
        VpcId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        ClientToken: str = None
    ) -> CreateCarrierGatewayResultTypeDef:
        """
        Creates a carrier gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_carrier_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_carrier_gateway)
        """

    def create_client_vpn_endpoint(
        self,
        *,
        ClientCidrBlock: str,
        ServerCertificateArn: str,
        AuthenticationOptions: List["ClientVpnAuthenticationRequestTypeDef"],
        ConnectionLogOptions: "ConnectionLogOptionsTypeDef",
        DnsServers: List[str] = None,
        TransportProtocol: TransportProtocolType = None,
        VpnPort: int = None,
        Description: str = None,
        SplitTunnel: bool = None,
        DryRun: bool = None,
        ClientToken: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        SecurityGroupIds: List[str] = None,
        VpcId: str = None,
        SelfServicePortal: SelfServicePortalType = None,
        ClientConnectOptions: "ClientConnectOptionsTypeDef" = None,
        SessionTimeoutHours: int = None,
        ClientLoginBannerOptions: "ClientLoginBannerOptionsTypeDef" = None
    ) -> CreateClientVpnEndpointResultTypeDef:
        """
        Creates a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_client_vpn_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_client_vpn_endpoint)
        """

    def create_client_vpn_route(
        self,
        *,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None
    ) -> CreateClientVpnRouteResultTypeDef:
        """
        Adds a route to a network to a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_client_vpn_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_client_vpn_route)
        """

    def create_coip_cidr(
        self, *, Cidr: str, CoipPoolId: str, DryRun: bool = None
    ) -> CreateCoipCidrResultTypeDef:
        """
        Creates a range of customer-owned IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_coip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_coip_cidr)
        """

    def create_coip_pool(
        self,
        *,
        LocalGatewayRouteTableId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateCoipPoolResultTypeDef:
        """
        Creates a pool of customer-owned IP (CoIP) addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_coip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_coip_pool)
        """

    def create_customer_gateway(
        self,
        *,
        Type: Literal["ipsec.1"],
        BgpAsn: int = None,
        PublicIp: str = None,
        CertificateArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DeviceName: str = None,
        IpAddress: str = None,
        DryRun: bool = None,
        BgpAsnExtended: int = None
    ) -> CreateCustomerGatewayResultTypeDef:
        """
        Provides information to Amazon Web Services about your customer gateway device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_customer_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_customer_gateway)
        """

    def create_default_subnet(
        self, *, AvailabilityZone: str, DryRun: bool = None, Ipv6Native: bool = None
    ) -> CreateDefaultSubnetResultTypeDef:
        """
        Creates a default subnet with a size `/20` IPv4 CIDR block in the specified
        Availability Zone in your default VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_default_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_default_subnet)
        """

    def create_default_vpc(self, *, DryRun: bool = None) -> CreateDefaultVpcResultTypeDef:
        """
        Creates a default VPC with a size `/16` IPv4 CIDR block and a default subnet in
        each Availability Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_default_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_default_vpc)
        """

    def create_dhcp_options(
        self,
        *,
        DhcpConfigurations: List["NewDhcpConfigurationTypeDef"],
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateDhcpOptionsResultTypeDef:
        """
        Creates a custom set of DHCP options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_dhcp_options)
        """

    def create_egress_only_internet_gateway(
        self,
        *,
        VpcId: str,
        ClientToken: str = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateEgressOnlyInternetGatewayResultTypeDef:
        """
        [IPv6 only] Creates an egress-only internet gateway for your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_egress_only_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_egress_only_internet_gateway)
        """

    def create_fleet(
        self,
        *,
        LaunchTemplateConfigs: List["FleetLaunchTemplateConfigRequestTypeDef"],
        TargetCapacitySpecification: "TargetCapacitySpecificationRequestTypeDef",
        DryRun: bool = None,
        ClientToken: str = None,
        SpotOptions: "SpotOptionsRequestTypeDef" = None,
        OnDemandOptions: "OnDemandOptionsRequestTypeDef" = None,
        ExcessCapacityTerminationPolicy: FleetExcessCapacityTerminationPolicyType = None,
        TerminateInstancesWithExpiration: bool = None,
        Type: FleetTypeType = None,
        ValidFrom: Union[datetime, str] = None,
        ValidUntil: Union[datetime, str] = None,
        ReplaceUnhealthyInstances: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        Context: str = None
    ) -> CreateFleetResultTypeDef:
        """
        Creates an EC2 Fleet that contains the configuration information for On-Demand
        Instances and Spot Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_fleet)
        """

    def create_flow_logs(
        self,
        *,
        ResourceIds: List[str],
        ResourceType: FlowLogsResourceTypeType,
        DryRun: bool = None,
        ClientToken: str = None,
        DeliverLogsPermissionArn: str = None,
        DeliverCrossAccountRole: str = None,
        LogGroupName: str = None,
        TrafficType: TrafficTypeType = None,
        LogDestinationType: LogDestinationTypeType = None,
        LogDestination: str = None,
        LogFormat: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        MaxAggregationInterval: int = None,
        DestinationOptions: "DestinationOptionsRequestTypeDef" = None
    ) -> CreateFlowLogsResultTypeDef:
        """
        Creates one or more flow logs to capture information about IP traffic for a
        specific network interface, subnet, or VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_flow_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_flow_logs)
        """

    def create_fpga_image(
        self,
        *,
        InputStorageLocation: "StorageLocationTypeDef",
        DryRun: bool = None,
        LogsStorageLocation: "StorageLocationTypeDef" = None,
        Description: str = None,
        Name: str = None,
        ClientToken: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateFpgaImageResultTypeDef:
        """
        Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_fpga_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_fpga_image)
        """

    def create_image(
        self,
        *,
        InstanceId: str,
        Name: str,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        Description: str = None,
        DryRun: bool = None,
        NoReboot: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateImageResultTypeDef:
        """
        Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is
        either running or stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_image)
        """

    def create_instance_connect_endpoint(
        self,
        *,
        SubnetId: str,
        DryRun: bool = None,
        SecurityGroupIds: List[str] = None,
        PreserveClientIp: bool = None,
        ClientToken: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateInstanceConnectEndpointResultTypeDef:
        """
        Creates an EC2 Instance Connect Endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_instance_connect_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_instance_connect_endpoint)
        """

    def create_instance_event_window(
        self,
        *,
        DryRun: bool = None,
        Name: str = None,
        TimeRanges: List["InstanceEventWindowTimeRangeRequestTypeDef"] = None,
        CronExpression: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateInstanceEventWindowResultTypeDef:
        """
        Creates an event window in which scheduled events for the associated Amazon EC2
        instances can run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_instance_event_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_instance_event_window)
        """

    def create_instance_export_task(
        self,
        *,
        ExportToS3Task: "ExportToS3TaskSpecificationTypeDef",
        InstanceId: str,
        TargetEnvironment: ExportEnvironmentType,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateInstanceExportTaskResultTypeDef:
        """
        Exports a running or stopped instance to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_instance_export_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_instance_export_task)
        """

    def create_internet_gateway(
        self, *, TagSpecifications: List["TagSpecificationTypeDef"] = None, DryRun: bool = None
    ) -> CreateInternetGatewayResultTypeDef:
        """
        Creates an internet gateway for use with a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_internet_gateway)
        """

    def create_ipam(
        self,
        *,
        DryRun: bool = None,
        Description: str = None,
        OperatingRegions: List["AddIpamOperatingRegionTypeDef"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None,
        Tier: IpamTierType = None
    ) -> CreateIpamResultTypeDef:
        """
        Create an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_ipam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_ipam)
        """

    def create_ipam_pool(
        self,
        *,
        IpamScopeId: str,
        AddressFamily: AddressFamilyType,
        DryRun: bool = None,
        Locale: str = None,
        SourceIpamPoolId: str = None,
        Description: str = None,
        AutoImport: bool = None,
        PubliclyAdvertisable: bool = None,
        AllocationMinNetmaskLength: int = None,
        AllocationMaxNetmaskLength: int = None,
        AllocationDefaultNetmaskLength: int = None,
        AllocationResourceTags: List["RequestIpamResourceTagTypeDef"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None,
        AwsService: Literal["ec2"] = None,
        PublicIpSource: IpamPoolPublicIpSourceType = None,
        SourceResource: "IpamPoolSourceResourceRequestTypeDef" = None
    ) -> CreateIpamPoolResultTypeDef:
        """
        Create an IP address pool for Amazon VPC IP Address Manager (IPAM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_ipam_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_ipam_pool)
        """

    def create_ipam_resource_discovery(
        self,
        *,
        DryRun: bool = None,
        Description: str = None,
        OperatingRegions: List["AddIpamOperatingRegionTypeDef"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateIpamResourceDiscoveryResultTypeDef:
        """
        Creates an IPAM resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_ipam_resource_discovery)
        """

    def create_ipam_scope(
        self,
        *,
        IpamId: str,
        DryRun: bool = None,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateIpamScopeResultTypeDef:
        """
        Create an IPAM scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_ipam_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_ipam_scope)
        """

    def create_key_pair(
        self,
        *,
        KeyName: str,
        DryRun: bool = None,
        KeyType: KeyTypeType = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        KeyFormat: KeyFormatType = None
    ) -> KeyPairTypeDef:
        """
        Creates an ED25519 or 2048-bit RSA key pair with the specified name and in the
        specified PEM or PPK format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_key_pair)
        """

    def create_launch_template(
        self,
        *,
        LaunchTemplateName: str,
        LaunchTemplateData: "RequestLaunchTemplateDataTypeDef",
        DryRun: bool = None,
        ClientToken: str = None,
        VersionDescription: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateLaunchTemplateResultTypeDef:
        """
        Creates a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_launch_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_launch_template)
        """

    def create_launch_template_version(
        self,
        *,
        LaunchTemplateData: "RequestLaunchTemplateDataTypeDef",
        DryRun: bool = None,
        ClientToken: str = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        SourceVersion: str = None,
        VersionDescription: str = None,
        ResolveAlias: bool = None
    ) -> CreateLaunchTemplateVersionResultTypeDef:
        """
        Creates a new version of a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_launch_template_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_launch_template_version)
        """

    def create_local_gateway_route(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DestinationCidrBlock: str = None,
        LocalGatewayVirtualInterfaceGroupId: str = None,
        DryRun: bool = None,
        NetworkInterfaceId: str = None,
        DestinationPrefixListId: str = None
    ) -> CreateLocalGatewayRouteResultTypeDef:
        """
        Creates a static route for the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_local_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_local_gateway_route)
        """

    def create_local_gateway_route_table(
        self,
        *,
        LocalGatewayId: str,
        Mode: LocalGatewayRouteTableModeType = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateLocalGatewayRouteTableResultTypeDef:
        """
        Creates a local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_local_gateway_route_table)
        """

    def create_local_gateway_route_table_virtual_interface_group_association(
        self,
        *,
        LocalGatewayRouteTableId: str,
        LocalGatewayVirtualInterfaceGroupId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef:
        """
        Creates a local gateway route table virtual interface group association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table_virtual_interface_group_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_local_gateway_route_table_virtual_interface_group_association)
        """

    def create_local_gateway_route_table_vpc_association(
        self,
        *,
        LocalGatewayRouteTableId: str,
        VpcId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        Associates the specified VPC with the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_local_gateway_route_table_vpc_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_local_gateway_route_table_vpc_association)
        """

    def create_managed_prefix_list(
        self,
        *,
        PrefixListName: str,
        MaxEntries: int,
        AddressFamily: str,
        DryRun: bool = None,
        Entries: List["AddPrefixListEntryTypeDef"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateManagedPrefixListResultTypeDef:
        """
        Creates a managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_managed_prefix_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_managed_prefix_list)
        """

    def create_nat_gateway(
        self,
        *,
        SubnetId: str,
        AllocationId: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ConnectivityType: ConnectivityTypeType = None,
        PrivateIpAddress: str = None,
        SecondaryAllocationIds: List[str] = None,
        SecondaryPrivateIpAddresses: List[str] = None,
        SecondaryPrivateIpAddressCount: int = None
    ) -> CreateNatGatewayResultTypeDef:
        """
        Creates a NAT gateway in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_nat_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_nat_gateway)
        """

    def create_network_acl(
        self,
        *,
        VpcId: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateNetworkAclResultTypeDef:
        """
        Creates a network ACL in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_network_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_network_acl)
        """

    def create_network_acl_entry(
        self,
        *,
        Egress: bool,
        NetworkAclId: str,
        Protocol: str,
        RuleAction: RuleActionType,
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: "IcmpTypeCodeTypeDef" = None,
        Ipv6CidrBlock: str = None,
        PortRange: "PortRangeTypeDef" = None
    ) -> None:
        """
        Creates an entry (a rule) in a network ACL with the specified rule number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_network_acl_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_network_acl_entry)
        """

    def create_network_insights_access_scope(
        self,
        *,
        ClientToken: str,
        MatchPaths: List["AccessScopePathRequestTypeDef"] = None,
        ExcludePaths: List["AccessScopePathRequestTypeDef"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateNetworkInsightsAccessScopeResultTypeDef:
        """
        Creates a Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_network_insights_access_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_network_insights_access_scope)
        """

    def create_network_insights_path(
        self,
        *,
        Source: str,
        Protocol: ProtocolType,
        ClientToken: str,
        SourceIp: str = None,
        DestinationIp: str = None,
        Destination: str = None,
        DestinationPort: int = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        FilterAtSource: "PathRequestFilterTypeDef" = None,
        FilterAtDestination: "PathRequestFilterTypeDef" = None
    ) -> CreateNetworkInsightsPathResultTypeDef:
        """
        Creates a path to analyze for reachability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_network_insights_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_network_insights_path)
        """

    def create_network_interface(
        self,
        *,
        SubnetId: str,
        Description: str = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        PrivateIpAddress: str = None,
        PrivateIpAddresses: List["PrivateIpAddressSpecificationTypeDef"] = None,
        SecondaryPrivateIpAddressCount: int = None,
        Ipv4Prefixes: List["Ipv4PrefixSpecificationRequestTypeDef"] = None,
        Ipv4PrefixCount: int = None,
        Ipv6Prefixes: List["Ipv6PrefixSpecificationRequestTypeDef"] = None,
        Ipv6PrefixCount: int = None,
        InterfaceType: NetworkInterfaceCreationTypeType = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None,
        EnablePrimaryIpv6: bool = None,
        ConnectionTrackingSpecification: "ConnectionTrackingSpecificationRequestTypeDef" = None
    ) -> CreateNetworkInterfaceResultTypeDef:
        """
        Creates a network interface in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_network_interface)
        """

    def create_network_interface_permission(
        self,
        *,
        NetworkInterfaceId: str,
        Permission: InterfacePermissionTypeType,
        AwsAccountId: str = None,
        AwsService: str = None,
        DryRun: bool = None
    ) -> CreateNetworkInterfacePermissionResultTypeDef:
        """
        Grants an Amazon Web Services-authorized account permission to attach the
        specified network interface to an instance in their account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_network_interface_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_network_interface_permission)
        """

    def create_placement_group(
        self,
        *,
        DryRun: bool = None,
        GroupName: str = None,
        Strategy: PlacementStrategyType = None,
        PartitionCount: int = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        SpreadLevel: SpreadLevelType = None
    ) -> CreatePlacementGroupResultTypeDef:
        """
        Creates a placement group in which to launch instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_placement_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_placement_group)
        """

    def create_public_ipv4_pool(
        self, *, DryRun: bool = None, TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreatePublicIpv4PoolResultTypeDef:
        """
        Creates a public IPv4 address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_public_ipv4_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_public_ipv4_pool)
        """

    def create_replace_root_volume_task(
        self,
        *,
        InstanceId: str,
        SnapshotId: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ImageId: str = None,
        DeleteReplacedRootVolume: bool = None
    ) -> CreateReplaceRootVolumeTaskResultTypeDef:
        """
        Replaces the EBS-backed root volume for a `running` instance with a new volume
        that is restored to the original root volume's launch state, that is restored to
        a specific snapshot taken from the original root volume, or that is restored
        from an AMI that has the same key characteristics as that ...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_replace_root_volume_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_replace_root_volume_task)
        """

    def create_reserved_instances_listing(
        self,
        *,
        ClientToken: str,
        InstanceCount: int,
        PriceSchedules: List["PriceScheduleSpecificationTypeDef"],
        ReservedInstancesId: str
    ) -> CreateReservedInstancesListingResultTypeDef:
        """
        Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the
        Reserved Instance Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_reserved_instances_listing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_reserved_instances_listing)
        """

    def create_restore_image_task(
        self,
        *,
        Bucket: str,
        ObjectKey: str,
        Name: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateRestoreImageTaskResultTypeDef:
        """
        Starts a task that restores an AMI from an Amazon S3 object that was previously
        created by using `CreateStoreImageTask <https://docs.aws.amazon.com/AWSEC2/lates
        t/APIReference/API_CreateStoreImageTask.html>`__.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_restore_image_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_restore_image_task)
        """

    def create_route(
        self,
        *,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None,
        VpcEndpointId: str = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        CarrierGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
        CoreNetworkArn: str = None
    ) -> CreateRouteResultTypeDef:
        """
        Creates a route in a route table within a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_route)
        """

    def create_route_table(
        self,
        *,
        VpcId: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None
    ) -> CreateRouteTableResultTypeDef:
        """
        Creates a route table for the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_route_table)
        """

    def create_security_group(
        self,
        *,
        Description: str,
        GroupName: str,
        VpcId: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateSecurityGroupResultTypeDef:
        """
        Creates a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_security_group)
        """

    def create_snapshot(
        self,
        *,
        VolumeId: str,
        Description: str = None,
        OutpostArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> SnapshotResponseMetadataTypeDef:
        """
        Creates a snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_snapshot)
        """

    def create_snapshots(
        self,
        *,
        InstanceSpecification: "InstanceSpecificationTypeDef",
        Description: str = None,
        OutpostArn: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        CopyTagsFromSource: Literal["volume"] = None
    ) -> CreateSnapshotsResultTypeDef:
        """
        Creates crash-consistent snapshots of multiple EBS volumes and stores the data
        in S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_snapshots)
        """

    def create_spot_datafeed_subscription(
        self, *, Bucket: str, DryRun: bool = None, Prefix: str = None
    ) -> CreateSpotDatafeedSubscriptionResultTypeDef:
        """
        Creates a data feed for Spot Instances, enabling you to view Spot Instance usage
        logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_spot_datafeed_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_spot_datafeed_subscription)
        """

    def create_store_image_task(
        self,
        *,
        ImageId: str,
        Bucket: str,
        S3ObjectTags: List["S3ObjectTagTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateStoreImageTaskResultTypeDef:
        """
        Stores an AMI as a single object in an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_store_image_task)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_store_image_task)
        """

    def create_subnet(
        self,
        *,
        VpcId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        AvailabilityZone: str = None,
        AvailabilityZoneId: str = None,
        CidrBlock: str = None,
        Ipv6CidrBlock: str = None,
        OutpostArn: str = None,
        DryRun: bool = None,
        Ipv6Native: bool = None,
        Ipv4IpamPoolId: str = None,
        Ipv4NetmaskLength: int = None,
        Ipv6IpamPoolId: str = None,
        Ipv6NetmaskLength: int = None
    ) -> CreateSubnetResultTypeDef:
        """
        Creates a subnet in the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_subnet)
        """

    def create_subnet_cidr_reservation(
        self,
        *,
        SubnetId: str,
        Cidr: str,
        ReservationType: SubnetCidrReservationTypeType,
        Description: str = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateSubnetCidrReservationResultTypeDef:
        """
        Creates a subnet CIDR reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_subnet_cidr_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_subnet_cidr_reservation)
        """

    def create_tags(
        self, *, Resources: List[Any], Tags: Optional[List["TagTypeDef"]], DryRun: bool = None
    ) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2 resource
        or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_tags)
        """

    def create_traffic_mirror_filter(
        self,
        *,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        ClientToken: str = None
    ) -> CreateTrafficMirrorFilterResultTypeDef:
        """
        Creates a Traffic Mirror filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_traffic_mirror_filter)
        """

    def create_traffic_mirror_filter_rule(
        self,
        *,
        TrafficMirrorFilterId: str,
        TrafficDirection: TrafficDirectionType,
        RuleNumber: int,
        RuleAction: TrafficMirrorRuleActionType,
        DestinationCidrBlock: str,
        SourceCidrBlock: str,
        DestinationPortRange: "TrafficMirrorPortRangeRequestTypeDef" = None,
        SourcePortRange: "TrafficMirrorPortRangeRequestTypeDef" = None,
        Protocol: int = None,
        Description: str = None,
        DryRun: bool = None,
        ClientToken: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateTrafficMirrorFilterRuleResultTypeDef:
        """
        Creates a Traffic Mirror filter rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_traffic_mirror_filter_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_traffic_mirror_filter_rule)
        """

    def create_traffic_mirror_session(
        self,
        *,
        NetworkInterfaceId: str,
        TrafficMirrorTargetId: str,
        TrafficMirrorFilterId: str,
        SessionNumber: int,
        PacketLength: int = None,
        VirtualNetworkId: int = None,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        ClientToken: str = None
    ) -> CreateTrafficMirrorSessionResultTypeDef:
        """
        Creates a Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_traffic_mirror_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_traffic_mirror_session)
        """

    def create_traffic_mirror_target(
        self,
        *,
        NetworkInterfaceId: str = None,
        NetworkLoadBalancerArn: str = None,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None,
        ClientToken: str = None,
        GatewayLoadBalancerEndpointId: str = None
    ) -> CreateTrafficMirrorTargetResultTypeDef:
        """
        Creates a target for your Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_traffic_mirror_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_traffic_mirror_target)
        """

    def create_transit_gateway(
        self,
        *,
        Description: str = None,
        Options: "TransitGatewayRequestOptionsTypeDef" = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayResultTypeDef:
        """
        Creates a transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway)
        """

    def create_transit_gateway_connect(
        self,
        *,
        TransportTransitGatewayAttachmentId: str,
        Options: "CreateTransitGatewayConnectRequestOptionsTypeDef",
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayConnectResultTypeDef:
        """
        Creates a Connect attachment from a specified transit gateway attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_connect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_connect)
        """

    def create_transit_gateway_connect_peer(
        self,
        *,
        TransitGatewayAttachmentId: str,
        PeerAddress: str,
        InsideCidrBlocks: List[str],
        TransitGatewayAddress: str = None,
        BgpOptions: "TransitGatewayConnectRequestBgpOptionsTypeDef" = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayConnectPeerResultTypeDef:
        """
        Creates a Connect peer for a specified transit gateway Connect attachment
        between a transit gateway and an appliance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_connect_peer)
        """

    def create_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayId: str,
        Options: "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef" = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayMulticastDomainResultTypeDef:
        """
        Creates a multicast domain using the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_multicast_domain)
        """

    def create_transit_gateway_peering_attachment(
        self,
        *,
        TransitGatewayId: str,
        PeerTransitGatewayId: str,
        PeerAccountId: str,
        PeerRegion: str,
        Options: "CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef" = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Requests a transit gateway peering attachment between the specified transit
        gateway (requester) and a peer transit gateway (accepter).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_peering_attachment)
        """

    def create_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayPolicyTableResultTypeDef:
        """
        Creates a transit gateway policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_policy_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_policy_table)
        """

    def create_transit_gateway_prefix_list_reference(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PrefixListId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayPrefixListReferenceResultTypeDef:
        """
        Creates a reference (route) to a prefix list in a specified transit gateway
        route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_prefix_list_reference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_prefix_list_reference)
        """

    def create_transit_gateway_route(
        self,
        *,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayRouteResultTypeDef:
        """
        Creates a static route for the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_route)
        """

    def create_transit_gateway_route_table(
        self,
        *,
        TransitGatewayId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayRouteTableResultTypeDef:
        """
        Creates a route table for the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_route_table)
        """

    def create_transit_gateway_route_table_announcement(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PeeringAttachmentId: str,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayRouteTableAnnouncementResultTypeDef:
        """
        Advertises a new transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_route_table_announcement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_route_table_announcement)
        """

    def create_transit_gateway_vpc_attachment(
        self,
        *,
        TransitGatewayId: str,
        VpcId: str,
        SubnetIds: List[str],
        Options: "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef" = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        DryRun: bool = None
    ) -> CreateTransitGatewayVpcAttachmentResultTypeDef:
        """
        Attaches the specified VPC to the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_transit_gateway_vpc_attachment)
        """

    def create_verified_access_endpoint(
        self,
        *,
        VerifiedAccessGroupId: str,
        EndpointType: VerifiedAccessEndpointTypeType,
        AttachmentType: Literal["vpc"],
        DomainCertificateArn: str,
        ApplicationDomain: str,
        EndpointDomainPrefix: str,
        SecurityGroupIds: List[str] = None,
        LoadBalancerOptions: "CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef" = None,
        NetworkInterfaceOptions: "CreateVerifiedAccessEndpointEniOptionsTypeDef" = None,
        Description: str = None,
        PolicyDocument: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None,
        DryRun: bool = None,
        SseSpecification: "VerifiedAccessSseSpecificationRequestTypeDef" = None
    ) -> CreateVerifiedAccessEndpointResultTypeDef:
        """
        An Amazon Web Services Verified Access endpoint is where you define your
        application along with an optional endpoint-level access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_verified_access_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_verified_access_endpoint)
        """

    def create_verified_access_group(
        self,
        *,
        VerifiedAccessInstanceId: str,
        Description: str = None,
        PolicyDocument: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None,
        DryRun: bool = None,
        SseSpecification: "VerifiedAccessSseSpecificationRequestTypeDef" = None
    ) -> CreateVerifiedAccessGroupResultTypeDef:
        """
        An Amazon Web Services Verified Access group is a collection of Amazon Web
        Services Verified Access endpoints who's associated applications have similar
        security requirements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_verified_access_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_verified_access_group)
        """

    def create_verified_access_instance(
        self,
        *,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None,
        DryRun: bool = None,
        FIPSEnabled: bool = None
    ) -> CreateVerifiedAccessInstanceResultTypeDef:
        """
        An Amazon Web Services Verified Access instance is a regional entity that
        evaluates application requests and grants access only when your security
        requirements are met.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_verified_access_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_verified_access_instance)
        """

    def create_verified_access_trust_provider(
        self,
        *,
        TrustProviderType: TrustProviderTypeType,
        PolicyReferenceName: str,
        UserTrustProviderType: UserTrustProviderTypeType = None,
        DeviceTrustProviderType: DeviceTrustProviderTypeType = None,
        OidcOptions: "CreateVerifiedAccessTrustProviderOidcOptionsTypeDef" = None,
        DeviceOptions: "CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef" = None,
        Description: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        ClientToken: str = None,
        DryRun: bool = None,
        SseSpecification: "VerifiedAccessSseSpecificationRequestTypeDef" = None
    ) -> CreateVerifiedAccessTrustProviderResultTypeDef:
        """
        A trust provider is a third-party entity that creates, maintains, and manages
        identity information for users and devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_verified_access_trust_provider)
        """

    def create_volume(
        self,
        *,
        AvailabilityZone: str,
        Encrypted: bool = None,
        Iops: int = None,
        KmsKeyId: str = None,
        OutpostArn: str = None,
        Size: int = None,
        SnapshotId: str = None,
        VolumeType: VolumeTypeType = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        MultiAttachEnabled: bool = None,
        Throughput: int = None,
        ClientToken: str = None
    ) -> VolumeResponseMetadataTypeDef:
        """
        Creates an EBS volume that can be attached to an instance in the same
        Availability Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_volume)
        """

    def create_vpc(
        self,
        *,
        CidrBlock: str = None,
        AmazonProvidedIpv6CidrBlock: bool = None,
        Ipv6Pool: str = None,
        Ipv6CidrBlock: str = None,
        Ipv4IpamPoolId: str = None,
        Ipv4NetmaskLength: int = None,
        Ipv6IpamPoolId: str = None,
        Ipv6NetmaskLength: int = None,
        DryRun: bool = None,
        InstanceTenancy: TenancyType = None,
        Ipv6CidrBlockNetworkBorderGroup: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateVpcResultTypeDef:
        """
        Creates a VPC with the specified CIDR blocks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_vpc)
        """

    def create_vpc_endpoint(
        self,
        *,
        VpcId: str,
        ServiceName: str,
        DryRun: bool = None,
        VpcEndpointType: VpcEndpointTypeType = None,
        PolicyDocument: str = None,
        RouteTableIds: List[str] = None,
        SubnetIds: List[str] = None,
        SecurityGroupIds: List[str] = None,
        IpAddressType: IpAddressTypeType = None,
        DnsOptions: "DnsOptionsSpecificationTypeDef" = None,
        ClientToken: str = None,
        PrivateDnsEnabled: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        SubnetConfigurations: List["SubnetConfigurationTypeDef"] = None
    ) -> CreateVpcEndpointResultTypeDef:
        """
        Creates a VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_vpc_endpoint)
        """

    def create_vpc_endpoint_connection_notification(
        self,
        *,
        ConnectionNotificationArn: str,
        ConnectionEvents: List[str],
        DryRun: bool = None,
        ServiceId: str = None,
        VpcEndpointId: str = None,
        ClientToken: str = None
    ) -> CreateVpcEndpointConnectionNotificationResultTypeDef:
        """
        Creates a connection notification for a specified VPC endpoint or VPC endpoint
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_connection_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_vpc_endpoint_connection_notification)
        """

    def create_vpc_endpoint_service_configuration(
        self,
        *,
        DryRun: bool = None,
        AcceptanceRequired: bool = None,
        PrivateDnsName: str = None,
        NetworkLoadBalancerArns: List[str] = None,
        GatewayLoadBalancerArns: List[str] = None,
        SupportedIpAddressTypes: List[str] = None,
        ClientToken: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateVpcEndpointServiceConfigurationResultTypeDef:
        """
        Creates a VPC endpoint service to which service consumers (Amazon Web Services
        accounts, users, and IAM roles) can connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_vpc_endpoint_service_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_vpc_endpoint_service_configuration)
        """

    def create_vpc_peering_connection(
        self,
        *,
        VpcId: str,
        DryRun: bool = None,
        PeerOwnerId: str = None,
        PeerVpcId: str = None,
        PeerRegion: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateVpcPeeringConnectionResultTypeDef:
        """
        Requests a VPC peering connection between two VPCs: a requester VPC that you own
        and an accepter VPC with which to create the connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_vpc_peering_connection)
        """

    def create_vpn_connection(
        self,
        *,
        CustomerGatewayId: str,
        Type: str,
        VpnGatewayId: str = None,
        TransitGatewayId: str = None,
        DryRun: bool = None,
        Options: "VpnConnectionOptionsSpecificationTypeDef" = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> CreateVpnConnectionResultTypeDef:
        """
        Creates a VPN connection between an existing virtual private gateway or transit
        gateway and a customer gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_vpn_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_vpn_connection)
        """

    def create_vpn_connection_route(
        self, *, DestinationCidrBlock: str, VpnConnectionId: str
    ) -> None:
        """
        Creates a static route associated with a VPN connection between an existing
        virtual private gateway and a VPN customer gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_vpn_connection_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_vpn_connection_route)
        """

    def create_vpn_gateway(
        self,
        *,
        Type: Literal["ipsec.1"],
        AvailabilityZone: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        AmazonSideAsn: int = None,
        DryRun: bool = None
    ) -> CreateVpnGatewayResultTypeDef:
        """
        Creates a virtual private gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.create_vpn_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#create_vpn_gateway)
        """

    def delete_carrier_gateway(
        self, *, CarrierGatewayId: str, DryRun: bool = None
    ) -> DeleteCarrierGatewayResultTypeDef:
        """
        Deletes a carrier gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_carrier_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_carrier_gateway)
        """

    def delete_client_vpn_endpoint(
        self, *, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> DeleteClientVpnEndpointResultTypeDef:
        """
        Deletes the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_client_vpn_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_client_vpn_endpoint)
        """

    def delete_client_vpn_route(
        self,
        *,
        ClientVpnEndpointId: str,
        DestinationCidrBlock: str,
        TargetVpcSubnetId: str = None,
        DryRun: bool = None
    ) -> DeleteClientVpnRouteResultTypeDef:
        """
        Deletes a route from a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_client_vpn_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_client_vpn_route)
        """

    def delete_coip_cidr(
        self, *, Cidr: str, CoipPoolId: str, DryRun: bool = None
    ) -> DeleteCoipCidrResultTypeDef:
        """
        Deletes a range of customer-owned IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_coip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_coip_cidr)
        """

    def delete_coip_pool(
        self, *, CoipPoolId: str, DryRun: bool = None
    ) -> DeleteCoipPoolResultTypeDef:
        """
        Deletes a pool of customer-owned IP (CoIP) addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_coip_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_coip_pool)
        """

    def delete_customer_gateway(self, *, CustomerGatewayId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified customer gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_customer_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_customer_gateway)
        """

    def delete_dhcp_options(self, *, DhcpOptionsId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified set of DHCP options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_dhcp_options)
        """

    def delete_egress_only_internet_gateway(
        self, *, EgressOnlyInternetGatewayId: str, DryRun: bool = None
    ) -> DeleteEgressOnlyInternetGatewayResultTypeDef:
        """
        Deletes an egress-only internet gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_egress_only_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_egress_only_internet_gateway)
        """

    def delete_fleets(
        self, *, FleetIds: List[str], TerminateInstances: bool, DryRun: bool = None
    ) -> DeleteFleetsResultTypeDef:
        """
        Deletes the specified EC2 Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_fleets)
        """

    def delete_flow_logs(
        self, *, FlowLogIds: List[str], DryRun: bool = None
    ) -> DeleteFlowLogsResultTypeDef:
        """
        Deletes one or more flow logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_flow_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_flow_logs)
        """

    def delete_fpga_image(
        self, *, FpgaImageId: str, DryRun: bool = None
    ) -> DeleteFpgaImageResultTypeDef:
        """
        Deletes the specified Amazon FPGA Image (AFI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_fpga_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_fpga_image)
        """

    def delete_instance_connect_endpoint(
        self, *, InstanceConnectEndpointId: str, DryRun: bool = None
    ) -> DeleteInstanceConnectEndpointResultTypeDef:
        """
        Deletes the specified EC2 Instance Connect Endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_instance_connect_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_instance_connect_endpoint)
        """

    def delete_instance_event_window(
        self, *, InstanceEventWindowId: str, DryRun: bool = None, ForceDelete: bool = None
    ) -> DeleteInstanceEventWindowResultTypeDef:
        """
        Deletes the specified event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_instance_event_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_instance_event_window)
        """

    def delete_internet_gateway(self, *, InternetGatewayId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified internet gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_internet_gateway)
        """

    def delete_ipam(
        self, *, IpamId: str, DryRun: bool = None, Cascade: bool = None
    ) -> DeleteIpamResultTypeDef:
        """
        Delete an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_ipam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_ipam)
        """

    def delete_ipam_pool(
        self, *, IpamPoolId: str, DryRun: bool = None, Cascade: bool = None
    ) -> DeleteIpamPoolResultTypeDef:
        """
        Delete an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_ipam_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_ipam_pool)
        """

    def delete_ipam_resource_discovery(
        self, *, IpamResourceDiscoveryId: str, DryRun: bool = None
    ) -> DeleteIpamResourceDiscoveryResultTypeDef:
        """
        Deletes an IPAM resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_ipam_resource_discovery)
        """

    def delete_ipam_scope(
        self, *, IpamScopeId: str, DryRun: bool = None
    ) -> DeleteIpamScopeResultTypeDef:
        """
        Delete the scope for an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_ipam_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_ipam_scope)
        """

    def delete_key_pair(
        self, *, KeyName: str = None, KeyPairId: str = None, DryRun: bool = None
    ) -> DeleteKeyPairResultTypeDef:
        """
        Deletes the specified key pair, by removing the public key from Amazon EC2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_key_pair)
        """

    def delete_launch_template(
        self, *, DryRun: bool = None, LaunchTemplateId: str = None, LaunchTemplateName: str = None
    ) -> DeleteLaunchTemplateResultTypeDef:
        """
        Deletes a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_launch_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_launch_template)
        """

    def delete_launch_template_versions(
        self,
        *,
        Versions: List[str],
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None
    ) -> DeleteLaunchTemplateVersionsResultTypeDef:
        """
        Deletes one or more versions of a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_launch_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_launch_template_versions)
        """

    def delete_local_gateway_route(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DestinationCidrBlock: str = None,
        DryRun: bool = None,
        DestinationPrefixListId: str = None
    ) -> DeleteLocalGatewayRouteResultTypeDef:
        """
        Deletes the specified route from the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_local_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_local_gateway_route)
        """

    def delete_local_gateway_route_table(
        self, *, LocalGatewayRouteTableId: str, DryRun: bool = None
    ) -> DeleteLocalGatewayRouteTableResultTypeDef:
        """
        Deletes a local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_local_gateway_route_table)
        """

    def delete_local_gateway_route_table_virtual_interface_group_association(
        self, *, LocalGatewayRouteTableVirtualInterfaceGroupAssociationId: str, DryRun: bool = None
    ) -> DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef:
        """
        Deletes a local gateway route table virtual interface group association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table_virtual_interface_group_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_local_gateway_route_table_virtual_interface_group_association)
        """

    def delete_local_gateway_route_table_vpc_association(
        self, *, LocalGatewayRouteTableVpcAssociationId: str, DryRun: bool = None
    ) -> DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        Deletes the specified association between a VPC and local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_local_gateway_route_table_vpc_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_local_gateway_route_table_vpc_association)
        """

    def delete_managed_prefix_list(
        self, *, PrefixListId: str, DryRun: bool = None
    ) -> DeleteManagedPrefixListResultTypeDef:
        """
        Deletes the specified managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_managed_prefix_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_managed_prefix_list)
        """

    def delete_nat_gateway(
        self, *, NatGatewayId: str, DryRun: bool = None
    ) -> DeleteNatGatewayResultTypeDef:
        """
        Deletes the specified NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_nat_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_nat_gateway)
        """

    def delete_network_acl(self, *, NetworkAclId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_network_acl)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_network_acl)
        """

    def delete_network_acl_entry(
        self, *, Egress: bool, NetworkAclId: str, RuleNumber: int, DryRun: bool = None
    ) -> None:
        """
        Deletes the specified ingress or egress entry (rule) from the specified network
        ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_network_acl_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_network_acl_entry)
        """

    def delete_network_insights_access_scope(
        self, *, NetworkInsightsAccessScopeId: str, DryRun: bool = None
    ) -> DeleteNetworkInsightsAccessScopeResultTypeDef:
        """
        Deletes the specified Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_network_insights_access_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_network_insights_access_scope)
        """

    def delete_network_insights_access_scope_analysis(
        self, *, NetworkInsightsAccessScopeAnalysisId: str, DryRun: bool = None
    ) -> DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef:
        """
        Deletes the specified Network Access Scope analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_network_insights_access_scope_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_network_insights_access_scope_analysis)
        """

    def delete_network_insights_analysis(
        self, *, NetworkInsightsAnalysisId: str, DryRun: bool = None
    ) -> DeleteNetworkInsightsAnalysisResultTypeDef:
        """
        Deletes the specified network insights analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_network_insights_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_network_insights_analysis)
        """

    def delete_network_insights_path(
        self, *, NetworkInsightsPathId: str, DryRun: bool = None
    ) -> DeleteNetworkInsightsPathResultTypeDef:
        """
        Deletes the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_network_insights_path)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_network_insights_path)
        """

    def delete_network_interface(self, *, NetworkInterfaceId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_network_interface)
        """

    def delete_network_interface_permission(
        self, *, NetworkInterfacePermissionId: str, Force: bool = None, DryRun: bool = None
    ) -> DeleteNetworkInterfacePermissionResultTypeDef:
        """
        Deletes a permission for a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_network_interface_permission)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_network_interface_permission)
        """

    def delete_placement_group(self, *, GroupName: str, DryRun: bool = None) -> None:
        """
        Deletes the specified placement group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_placement_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_placement_group)
        """

    def delete_public_ipv4_pool(
        self, *, PoolId: str, DryRun: bool = None
    ) -> DeletePublicIpv4PoolResultTypeDef:
        """
        Delete a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_public_ipv4_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_public_ipv4_pool)
        """

    def delete_queued_reserved_instances(
        self, *, ReservedInstancesIds: List[str], DryRun: bool = None
    ) -> DeleteQueuedReservedInstancesResultTypeDef:
        """
        Deletes the queued purchases for the specified Reserved Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_queued_reserved_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_queued_reserved_instances)
        """

    def delete_route(
        self,
        *,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None
    ) -> None:
        """
        Deletes the specified route from the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_route)
        """

    def delete_route_table(self, *, RouteTableId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_route_table)
        """

    def delete_security_group(
        self, *, GroupId: str = None, GroupName: str = None, DryRun: bool = None
    ) -> None:
        """
        Deletes a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_security_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_security_group)
        """

    def delete_snapshot(self, *, SnapshotId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_snapshot)
        """

    def delete_spot_datafeed_subscription(self, *, DryRun: bool = None) -> None:
        """
        Deletes the data feed for Spot Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_spot_datafeed_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_spot_datafeed_subscription)
        """

    def delete_subnet(self, *, SubnetId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_subnet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_subnet)
        """

    def delete_subnet_cidr_reservation(
        self, *, SubnetCidrReservationId: str, DryRun: bool = None
    ) -> DeleteSubnetCidrReservationResultTypeDef:
        """
        Deletes a subnet CIDR reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_subnet_cidr_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_subnet_cidr_reservation)
        """

    def delete_tags(
        self,
        *,
        Resources: List[Any],
        DryRun: bool = None,
        Tags: Optional[List["TagTypeDef"]] = None
    ) -> None:
        """
        Deletes the specified set of tags from the specified set of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_tags)
        """

    def delete_traffic_mirror_filter(
        self, *, TrafficMirrorFilterId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorFilterResultTypeDef:
        """
        Deletes the specified Traffic Mirror filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_traffic_mirror_filter)
        """

    def delete_traffic_mirror_filter_rule(
        self, *, TrafficMirrorFilterRuleId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorFilterRuleResultTypeDef:
        """
        Deletes the specified Traffic Mirror rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_filter_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_traffic_mirror_filter_rule)
        """

    def delete_traffic_mirror_session(
        self, *, TrafficMirrorSessionId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorSessionResultTypeDef:
        """
        Deletes the specified Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_traffic_mirror_session)
        """

    def delete_traffic_mirror_target(
        self, *, TrafficMirrorTargetId: str, DryRun: bool = None
    ) -> DeleteTrafficMirrorTargetResultTypeDef:
        """
        Deletes the specified Traffic Mirror target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_traffic_mirror_target)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_traffic_mirror_target)
        """

    def delete_transit_gateway(
        self, *, TransitGatewayId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayResultTypeDef:
        """
        Deletes the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway)
        """

    def delete_transit_gateway_connect(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayConnectResultTypeDef:
        """
        Deletes the specified Connect attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_connect)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_connect)
        """

    def delete_transit_gateway_connect_peer(
        self, *, TransitGatewayConnectPeerId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayConnectPeerResultTypeDef:
        """
        Deletes the specified Connect peer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_connect_peer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_connect_peer)
        """

    def delete_transit_gateway_multicast_domain(
        self, *, TransitGatewayMulticastDomainId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayMulticastDomainResultTypeDef:
        """
        Deletes the specified transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_multicast_domain)
        """

    def delete_transit_gateway_peering_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Deletes a transit gateway peering attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_peering_attachment)
        """

    def delete_transit_gateway_policy_table(
        self, *, TransitGatewayPolicyTableId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayPolicyTableResultTypeDef:
        """
        Deletes the specified transit gateway policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_policy_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_policy_table)
        """

    def delete_transit_gateway_prefix_list_reference(
        self, *, TransitGatewayRouteTableId: str, PrefixListId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayPrefixListReferenceResultTypeDef:
        """
        Deletes a reference (route) to a prefix list in a specified transit gateway
        route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_prefix_list_reference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_prefix_list_reference)
        """

    def delete_transit_gateway_route(
        self, *, TransitGatewayRouteTableId: str, DestinationCidrBlock: str, DryRun: bool = None
    ) -> DeleteTransitGatewayRouteResultTypeDef:
        """
        Deletes the specified route from the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_route)
        """

    def delete_transit_gateway_route_table(
        self, *, TransitGatewayRouteTableId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayRouteTableResultTypeDef:
        """
        Deletes the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_route_table)
        """

    def delete_transit_gateway_route_table_announcement(
        self, *, TransitGatewayRouteTableAnnouncementId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayRouteTableAnnouncementResultTypeDef:
        """
        Advertises to the transit gateway that a transit gateway route table is deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_route_table_announcement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_route_table_announcement)
        """

    def delete_transit_gateway_vpc_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> DeleteTransitGatewayVpcAttachmentResultTypeDef:
        """
        Deletes the specified VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_transit_gateway_vpc_attachment)
        """

    def delete_verified_access_endpoint(
        self, *, VerifiedAccessEndpointId: str, ClientToken: str = None, DryRun: bool = None
    ) -> DeleteVerifiedAccessEndpointResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_verified_access_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_verified_access_endpoint)
        """

    def delete_verified_access_group(
        self, *, VerifiedAccessGroupId: str, ClientToken: str = None, DryRun: bool = None
    ) -> DeleteVerifiedAccessGroupResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_verified_access_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_verified_access_group)
        """

    def delete_verified_access_instance(
        self, *, VerifiedAccessInstanceId: str, DryRun: bool = None, ClientToken: str = None
    ) -> DeleteVerifiedAccessInstanceResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_verified_access_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_verified_access_instance)
        """

    def delete_verified_access_trust_provider(
        self, *, VerifiedAccessTrustProviderId: str, DryRun: bool = None, ClientToken: str = None
    ) -> DeleteVerifiedAccessTrustProviderResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access trust provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_verified_access_trust_provider)
        """

    def delete_volume(self, *, VolumeId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified EBS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_volume)
        """

    def delete_vpc(self, *, VpcId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_vpc)
        """

    def delete_vpc_endpoint_connection_notifications(
        self, *, ConnectionNotificationIds: List[str], DryRun: bool = None
    ) -> DeleteVpcEndpointConnectionNotificationsResultTypeDef:
        """
        Deletes the specified VPC endpoint connection notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_connection_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_vpc_endpoint_connection_notifications)
        """

    def delete_vpc_endpoint_service_configurations(
        self, *, ServiceIds: List[str], DryRun: bool = None
    ) -> DeleteVpcEndpointServiceConfigurationsResultTypeDef:
        """
        Deletes the specified VPC endpoint service configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_vpc_endpoint_service_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_vpc_endpoint_service_configurations)
        """

    def delete_vpc_endpoints(
        self, *, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> DeleteVpcEndpointsResultTypeDef:
        """
        Deletes the specified VPC endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_vpc_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_vpc_endpoints)
        """

    def delete_vpc_peering_connection(
        self, *, VpcPeeringConnectionId: str, DryRun: bool = None
    ) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        Deletes a VPC peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_vpc_peering_connection)
        """

    def delete_vpn_connection(self, *, VpnConnectionId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_vpn_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_vpn_connection)
        """

    def delete_vpn_connection_route(
        self, *, DestinationCidrBlock: str, VpnConnectionId: str
    ) -> None:
        """
        Deletes the specified static route associated with a VPN connection between an
        existing virtual private gateway and a VPN customer gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_vpn_connection_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_vpn_connection_route)
        """

    def delete_vpn_gateway(self, *, VpnGatewayId: str, DryRun: bool = None) -> None:
        """
        Deletes the specified virtual private gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.delete_vpn_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#delete_vpn_gateway)
        """

    def deprovision_byoip_cidr(
        self, *, Cidr: str, DryRun: bool = None
    ) -> DeprovisionByoipCidrResultTypeDef:
        """
        Releases the specified address range that you provisioned for use with your
        Amazon Web Services resources through bring your own IP addresses (BYOIP) and
        deletes the corresponding address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.deprovision_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deprovision_byoip_cidr)
        """

    def deprovision_ipam_byoasn(
        self, *, IpamId: str, Asn: str, DryRun: bool = None
    ) -> DeprovisionIpamByoasnResultTypeDef:
        """
        Deprovisions your Autonomous System Number (ASN) from your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.deprovision_ipam_byoasn)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deprovision_ipam_byoasn)
        """

    def deprovision_ipam_pool_cidr(
        self, *, IpamPoolId: str, DryRun: bool = None, Cidr: str = None
    ) -> DeprovisionIpamPoolCidrResultTypeDef:
        """
        Deprovision a CIDR provisioned from an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.deprovision_ipam_pool_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deprovision_ipam_pool_cidr)
        """

    def deprovision_public_ipv4_pool_cidr(
        self, *, PoolId: str, Cidr: str, DryRun: bool = None
    ) -> DeprovisionPublicIpv4PoolCidrResultTypeDef:
        """
        Deprovision a CIDR from a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.deprovision_public_ipv4_pool_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deprovision_public_ipv4_pool_cidr)
        """

    def deregister_image(self, *, ImageId: str, DryRun: bool = None) -> None:
        """
        Deregisters the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.deregister_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deregister_image)
        """

    def deregister_instance_event_notification_attributes(
        self,
        *,
        InstanceTagAttribute: "DeregisterInstanceTagAttributeRequestTypeDef",
        DryRun: bool = None
    ) -> DeregisterInstanceEventNotificationAttributesResultTypeDef:
        """
        Deregisters tag keys to prevent tags that have the specified tag keys from being
        included in scheduled event notifications for resources in the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.deregister_instance_event_notification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deregister_instance_event_notification_attributes)
        """

    def deregister_transit_gateway_multicast_group_members(
        self,
        *,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None
    ) -> DeregisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        Deregisters the specified members (network interfaces) from the transit gateway
        multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deregister_transit_gateway_multicast_group_members)
        """

    def deregister_transit_gateway_multicast_group_sources(
        self,
        *,
        TransitGatewayMulticastDomainId: str = None,
        GroupIpAddress: str = None,
        NetworkInterfaceIds: List[str] = None,
        DryRun: bool = None
    ) -> DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        Deregisters the specified sources (network interfaces) from the transit gateway
        multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.deregister_transit_gateway_multicast_group_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#deregister_transit_gateway_multicast_group_sources)
        """

    def describe_account_attributes(
        self, *, AttributeNames: List[AccountAttributeNameType] = None, DryRun: bool = None
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        Describes attributes of your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_account_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_account_attributes)
        """

    def describe_address_transfers(
        self,
        *,
        AllocationIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None
    ) -> DescribeAddressTransfersResultTypeDef:
        """
        Describes an Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_address_transfers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_address_transfers)
        """

    def describe_addresses(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        PublicIps: List[str] = None,
        AllocationIds: List[str] = None,
        DryRun: bool = None
    ) -> DescribeAddressesResultTypeDef:
        """
        Describes the specified Elastic IP addresses or all of your Elastic IP
        addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_addresses)
        """

    def describe_addresses_attribute(
        self,
        *,
        AllocationIds: List[str] = None,
        Attribute: Literal["domain-name"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None
    ) -> DescribeAddressesAttributeResultTypeDef:
        """
        Describes the attributes of the specified Elastic IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_addresses_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_addresses_attribute)
        """

    def describe_aggregate_id_format(
        self, *, DryRun: bool = None
    ) -> DescribeAggregateIdFormatResultTypeDef:
        """
        Describes the longer ID format settings for all resource types in a specific
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_aggregate_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_aggregate_id_format)
        """

    def describe_availability_zones(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        ZoneNames: List[str] = None,
        ZoneIds: List[str] = None,
        AllAvailabilityZones: bool = None,
        DryRun: bool = None
    ) -> DescribeAvailabilityZonesResultTypeDef:
        """
        Describes the Availability Zones, Local Zones, and Wavelength Zones that are
        available to you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_availability_zones)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_availability_zones)
        """

    def describe_aws_network_performance_metric_subscriptions(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef:
        """
        Describes the current Infrastructure Performance metric subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_aws_network_performance_metric_subscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_aws_network_performance_metric_subscriptions)
        """

    def describe_bundle_tasks(
        self,
        *,
        BundleIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeBundleTasksResultTypeDef:
        """
        Describes the specified bundle tasks or all of your bundle tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_bundle_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_bundle_tasks)
        """

    def describe_byoip_cidrs(
        self, *, MaxResults: int, DryRun: bool = None, NextToken: str = None
    ) -> DescribeByoipCidrsResultTypeDef:
        """
        Describes the IP address ranges that were specified in calls to
        ProvisionByoipCidr.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_byoip_cidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_byoip_cidrs)
        """

    def describe_capacity_block_offerings(
        self,
        *,
        InstanceType: str,
        InstanceCount: int,
        CapacityDurationHours: int,
        DryRun: bool = None,
        StartDateRange: Union[datetime, str] = None,
        EndDateRange: Union[datetime, str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeCapacityBlockOfferingsResultTypeDef:
        """
        Describes Capacity Block offerings available for purchase in the Amazon Web
        Services Region that you're currently using.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_capacity_block_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_capacity_block_offerings)
        """

    def describe_capacity_reservation_fleets(
        self,
        *,
        CapacityReservationFleetIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeCapacityReservationFleetsResultTypeDef:
        """
        Describes one or more Capacity Reservation Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_capacity_reservation_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_capacity_reservation_fleets)
        """

    def describe_capacity_reservations(
        self,
        *,
        CapacityReservationIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeCapacityReservationsResultTypeDef:
        """
        Describes one or more of your Capacity Reservations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_capacity_reservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_capacity_reservations)
        """

    def describe_carrier_gateways(
        self,
        *,
        CarrierGatewayIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeCarrierGatewaysResultTypeDef:
        """
        Describes one or more of your carrier gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_carrier_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_carrier_gateways)
        """

    def describe_classic_link_instances(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeClassicLinkInstancesResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_classic_link_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_classic_link_instances)
        """

    def describe_client_vpn_authorization_rules(
        self,
        *,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None
    ) -> DescribeClientVpnAuthorizationRulesResultTypeDef:
        """
        Describes the authorization rules for a specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_client_vpn_authorization_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_client_vpn_authorization_rules)
        """

    def describe_client_vpn_connections(
        self,
        *,
        ClientVpnEndpointId: str,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None
    ) -> DescribeClientVpnConnectionsResultTypeDef:
        """
        Describes active client connections and connections that have been terminated
        within the last 60 minutes for the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_client_vpn_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_client_vpn_connections)
        """

    def describe_client_vpn_endpoints(
        self,
        *,
        ClientVpnEndpointIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeClientVpnEndpointsResultTypeDef:
        """
        Describes one or more Client VPN endpoints in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_client_vpn_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_client_vpn_endpoints)
        """

    def describe_client_vpn_routes(
        self,
        *,
        ClientVpnEndpointId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeClientVpnRoutesResultTypeDef:
        """
        Describes the routes for the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_client_vpn_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_client_vpn_routes)
        """

    def describe_client_vpn_target_networks(
        self,
        *,
        ClientVpnEndpointId: str,
        AssociationIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeClientVpnTargetNetworksResultTypeDef:
        """
        Describes the target networks associated with the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_client_vpn_target_networks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_client_vpn_target_networks)
        """

    def describe_coip_pools(
        self,
        *,
        PoolIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeCoipPoolsResultTypeDef:
        """
        Describes the specified customer-owned address pools or all of your customer-
        owned address pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_coip_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_coip_pools)
        """

    def describe_conversion_tasks(
        self, *, ConversionTaskIds: List[str] = None, DryRun: bool = None
    ) -> DescribeConversionTasksResultTypeDef:
        """
        Describes the specified conversion tasks or all your conversion tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_conversion_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_conversion_tasks)
        """

    def describe_customer_gateways(
        self,
        *,
        CustomerGatewayIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeCustomerGatewaysResultTypeDef:
        """
        Describes one or more of your VPN customer gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_customer_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_customer_gateways)
        """

    def describe_dhcp_options(
        self,
        *,
        DhcpOptionsIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeDhcpOptionsResultTypeDef:
        """
        Describes your DHCP option sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_dhcp_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_dhcp_options)
        """

    def describe_egress_only_internet_gateways(
        self,
        *,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribeEgressOnlyInternetGatewaysResultTypeDef:
        """
        Describes your egress-only internet gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_egress_only_internet_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_egress_only_internet_gateways)
        """

    def describe_elastic_gpus(
        self,
        *,
        ElasticGpuIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeElasticGpusResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_elastic_gpus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_elastic_gpus)
        """

    def describe_export_image_tasks(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        ExportImageTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeExportImageTasksResultTypeDef:
        """
        Describes the specified export image tasks or all of your export image tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_export_image_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_export_image_tasks)
        """

    def describe_export_tasks(
        self, *, ExportTaskIds: List[str] = None, Filters: List["FilterTypeDef"] = None
    ) -> DescribeExportTasksResultTypeDef:
        """
        Describes the specified export instance tasks or all of your export instance
        tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_export_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_export_tasks)
        """

    def describe_fast_launch_images(
        self,
        *,
        ImageIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeFastLaunchImagesResultTypeDef:
        """
        Describe details for Windows AMIs that are configured for Windows fast launch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_fast_launch_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_fast_launch_images)
        """

    def describe_fast_snapshot_restores(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeFastSnapshotRestoresResultTypeDef:
        """
        Describes the state of fast snapshot restores for your snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_fast_snapshot_restores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_fast_snapshot_restores)
        """

    def describe_fleet_history(
        self,
        *,
        FleetId: str,
        StartTime: Union[datetime, str],
        DryRun: bool = None,
        EventType: FleetEventTypeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeFleetHistoryResultTypeDef:
        """
        Describes the events for the specified EC2 Fleet during the specified time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_fleet_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_fleet_history)
        """

    def describe_fleet_instances(
        self,
        *,
        FleetId: str,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribeFleetInstancesResultTypeDef:
        """
        Describes the running instances for the specified EC2 Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_fleet_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_fleet_instances)
        """

    def describe_fleets(
        self,
        *,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        FleetIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribeFleetsResultTypeDef:
        """
        Describes the specified EC2 Fleet or all of your EC2 Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_fleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_fleets)
        """

    def describe_flow_logs(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        FlowLogIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeFlowLogsResultTypeDef:
        """
        Describes one or more flow logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_flow_logs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_flow_logs)
        """

    def describe_fpga_image_attribute(
        self, *, FpgaImageId: str, Attribute: FpgaImageAttributeNameType, DryRun: bool = None
    ) -> DescribeFpgaImageAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified Amazon FPGA Image (AFI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_fpga_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_fpga_image_attribute)
        """

    def describe_fpga_images(
        self,
        *,
        DryRun: bool = None,
        FpgaImageIds: List[str] = None,
        Owners: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeFpgaImagesResultTypeDef:
        """
        Describes the Amazon FPGA Images (AFIs) available to you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_fpga_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_fpga_images)
        """

    def describe_host_reservation_offerings(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxDuration: int = None,
        MaxResults: int = None,
        MinDuration: int = None,
        NextToken: str = None,
        OfferingId: str = None
    ) -> DescribeHostReservationOfferingsResultTypeDef:
        """
        Describes the Dedicated Host reservations that are available to purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_host_reservation_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_host_reservation_offerings)
        """

    def describe_host_reservations(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        HostReservationIdSet: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeHostReservationsResultTypeDef:
        """
        Describes reservations that are associated with Dedicated Hosts in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_host_reservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_host_reservations)
        """

    def describe_hosts(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        HostIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeHostsResultTypeDef:
        """
        Describes the specified Dedicated Hosts or all your Dedicated Hosts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_hosts)
        """

    def describe_iam_instance_profile_associations(
        self,
        *,
        AssociationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeIamInstanceProfileAssociationsResultTypeDef:
        """
        Describes your IAM instance profile associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_iam_instance_profile_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_iam_instance_profile_associations)
        """

    def describe_id_format(self, *, Resource: str = None) -> DescribeIdFormatResultTypeDef:
        """
        Describes the ID format settings for your resources on a per-Region basis, for
        example, to view which resource types are enabled for longer IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_id_format)
        """

    def describe_identity_id_format(
        self, *, PrincipalArn: str, Resource: str = None
    ) -> DescribeIdentityIdFormatResultTypeDef:
        """
        Describes the ID format settings for resources for the specified IAM user, IAM
        role, or root user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_identity_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_identity_id_format)
        """

    def describe_image_attribute(
        self, *, Attribute: ImageAttributeNameType, ImageId: str, DryRun: bool = None
    ) -> ImageAttributeTypeDef:
        """
        Describes the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_image_attribute)
        """

    def describe_images(
        self,
        *,
        ExecutableUsers: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        IncludeDeprecated: bool = None,
        IncludeDisabled: bool = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeImagesResultTypeDef:
        """
        Describes the specified images (AMIs, AKIs, and ARIs) available to you or all of
        the images available to you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_images)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_images)
        """

    def describe_import_image_tasks(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        ImportTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeImportImageTasksResultTypeDef:
        """
        Displays details about an import virtual machine or import snapshot tasks that
        are already created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_import_image_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_import_image_tasks)
        """

    def describe_import_snapshot_tasks(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        ImportTaskIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeImportSnapshotTasksResultTypeDef:
        """
        Describes your import snapshot tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_import_snapshot_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_import_snapshot_tasks)
        """

    def describe_instance_attribute(
        self, *, Attribute: InstanceAttributeNameType, InstanceId: str, DryRun: bool = None
    ) -> InstanceAttributeTypeDef:
        """
        Describes the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instance_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instance_attribute)
        """

    def describe_instance_connect_endpoints(
        self,
        *,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        InstanceConnectEndpointIds: List[str] = None
    ) -> DescribeInstanceConnectEndpointsResultTypeDef:
        """
        Describes the specified EC2 Instance Connect Endpoints or all EC2 Instance
        Connect Endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instance_connect_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instance_connect_endpoints)
        """

    def describe_instance_credit_specifications(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeInstanceCreditSpecificationsResultTypeDef:
        """
        Describes the credit option for CPU usage of the specified burstable performance
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instance_credit_specifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instance_credit_specifications)
        """

    def describe_instance_event_notification_attributes(
        self, *, DryRun: bool = None
    ) -> DescribeInstanceEventNotificationAttributesResultTypeDef:
        """
        Describes the tag keys that are registered to appear in scheduled event
        notifications for resources in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instance_event_notification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instance_event_notification_attributes)
        """

    def describe_instance_event_windows(
        self,
        *,
        DryRun: bool = None,
        InstanceEventWindowIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeInstanceEventWindowsResultTypeDef:
        """
        Describes the specified event windows or all event windows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instance_event_windows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instance_event_windows)
        """

    def describe_instance_status(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        InstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None
    ) -> DescribeInstanceStatusResultTypeDef:
        """
        Describes the status of the specified instances or all of your instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instance_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instance_status)
        """

    def describe_instance_topology(
        self,
        *,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None,
        InstanceIds: List[str] = None,
        GroupNames: List[str] = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribeInstanceTopologyResultTypeDef:
        """
        Describes a tree-based hierarchy that represents the physical host placement of
        your EC2 instances within an Availability Zone or Local Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instance_topology)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instance_topology)
        """

    def describe_instance_type_offerings(
        self,
        *,
        DryRun: bool = None,
        LocationType: LocationTypeType = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeInstanceTypeOfferingsResultTypeDef:
        """
        Lists the instance types that are offered for the specified location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instance_type_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instance_type_offerings)
        """

    def describe_instance_types(
        self,
        *,
        DryRun: bool = None,
        InstanceTypes: List[InstanceTypeType] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeInstanceTypesResultTypeDef:
        """
        Describes the specified instance types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instance_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instance_types)
        """

    def describe_instances(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeInstancesResultTypeDef:
        """
        Describes the specified instances or all instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_instances)
        """

    def describe_internet_gateways(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeInternetGatewaysResultTypeDef:
        """
        Describes your internet gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_internet_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_internet_gateways)
        """

    def describe_ipam_byoasn(
        self, *, DryRun: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeIpamByoasnResultTypeDef:
        """
        Describes your Autonomous System Numbers (ASNs), their provisioning statuses,
        and the BYOIP CIDRs with which they are associated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_ipam_byoasn)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_ipam_byoasn)
        """

    def describe_ipam_pools(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        IpamPoolIds: List[str] = None
    ) -> DescribeIpamPoolsResultTypeDef:
        """
        Get information about your IPAM pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_ipam_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_ipam_pools)
        """

    def describe_ipam_resource_discoveries(
        self,
        *,
        DryRun: bool = None,
        IpamResourceDiscoveryIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribeIpamResourceDiscoveriesResultTypeDef:
        """
        Describes IPAM resource discoveries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_ipam_resource_discoveries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_ipam_resource_discoveries)
        """

    def describe_ipam_resource_discovery_associations(
        self,
        *,
        DryRun: bool = None,
        IpamResourceDiscoveryAssociationIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribeIpamResourceDiscoveryAssociationsResultTypeDef:
        """
        Describes resource discovery association with an Amazon VPC IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_ipam_resource_discovery_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_ipam_resource_discovery_associations)
        """

    def describe_ipam_scopes(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        IpamScopeIds: List[str] = None
    ) -> DescribeIpamScopesResultTypeDef:
        """
        Get information about your IPAM scopes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_ipam_scopes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_ipam_scopes)
        """

    def describe_ipams(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        IpamIds: List[str] = None
    ) -> DescribeIpamsResultTypeDef:
        """
        Get information about your IPAM pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_ipams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_ipams)
        """

    def describe_ipv6_pools(
        self,
        *,
        PoolIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribeIpv6PoolsResultTypeDef:
        """
        Describes your IPv6 address pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_ipv6_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_ipv6_pools)
        """

    def describe_key_pairs(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        KeyNames: List[str] = None,
        KeyPairIds: List[str] = None,
        DryRun: bool = None,
        IncludePublicKey: bool = None
    ) -> DescribeKeyPairsResultTypeDef:
        """
        Describes the specified key pairs or all of your key pairs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_key_pairs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_key_pairs)
        """

    def describe_launch_template_versions(
        self,
        *,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[str] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        ResolveAlias: bool = None
    ) -> DescribeLaunchTemplateVersionsResultTypeDef:
        """
        Describes one or more versions of a specified launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_launch_template_versions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_launch_template_versions)
        """

    def describe_launch_templates(
        self,
        *,
        DryRun: bool = None,
        LaunchTemplateIds: List[str] = None,
        LaunchTemplateNames: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeLaunchTemplatesResultTypeDef:
        """
        Describes one or more launch templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_launch_templates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_launch_templates)
        """

    def describe_local_gateway_route_table_virtual_interface_group_associations(
        self,
        *,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef:
        """
        Describes the associations between virtual interface groups and local gateway
        route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_virtual_interface_group_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_local_gateway_route_table_virtual_interface_group_associations)
        """

    def describe_local_gateway_route_table_vpc_associations(
        self,
        *,
        LocalGatewayRouteTableVpcAssociationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef:
        """
        Describes the specified associations between VPCs and local gateway route
        tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_table_vpc_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_local_gateway_route_table_vpc_associations)
        """

    def describe_local_gateway_route_tables(
        self,
        *,
        LocalGatewayRouteTableIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeLocalGatewayRouteTablesResultTypeDef:
        """
        Describes one or more local gateway route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_local_gateway_route_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_local_gateway_route_tables)
        """

    def describe_local_gateway_virtual_interface_groups(
        self,
        *,
        LocalGatewayVirtualInterfaceGroupIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef:
        """
        Describes the specified local gateway virtual interface groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interface_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_local_gateway_virtual_interface_groups)
        """

    def describe_local_gateway_virtual_interfaces(
        self,
        *,
        LocalGatewayVirtualInterfaceIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeLocalGatewayVirtualInterfacesResultTypeDef:
        """
        Describes the specified local gateway virtual interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_local_gateway_virtual_interfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_local_gateway_virtual_interfaces)
        """

    def describe_local_gateways(
        self,
        *,
        LocalGatewayIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeLocalGatewaysResultTypeDef:
        """
        Describes one or more local gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_local_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_local_gateways)
        """

    def describe_locked_snapshots(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None
    ) -> DescribeLockedSnapshotsResultTypeDef:
        """
        Describes the lock status for a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_locked_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_locked_snapshots)
        """

    def describe_mac_hosts(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        HostIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeMacHostsResultTypeDef:
        """
        Describes the specified EC2 Mac Dedicated Host or all of your EC2 Mac Dedicated
        Hosts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_mac_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_mac_hosts)
        """

    def describe_managed_prefix_lists(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        PrefixListIds: List[str] = None
    ) -> DescribeManagedPrefixListsResultTypeDef:
        """
        Describes your managed prefix lists and any Amazon Web Services-managed prefix
        lists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_managed_prefix_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_managed_prefix_lists)
        """

    def describe_moving_addresses(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        PublicIps: List[str] = None
    ) -> DescribeMovingAddressesResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_moving_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_moving_addresses)
        """

    def describe_nat_gateways(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NatGatewayIds: List[str] = None,
        NextToken: str = None
    ) -> DescribeNatGatewaysResultTypeDef:
        """
        Describes your NAT gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_nat_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_nat_gateways)
        """

    def describe_network_acls(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeNetworkAclsResultTypeDef:
        """
        Describes your network ACLs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_network_acls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_network_acls)
        """

    def describe_network_insights_access_scope_analyses(
        self,
        *,
        NetworkInsightsAccessScopeAnalysisIds: List[str] = None,
        NetworkInsightsAccessScopeId: str = None,
        AnalysisStartTimeBegin: Union[datetime, str] = None,
        AnalysisStartTimeEnd: Union[datetime, str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        DryRun: bool = None,
        NextToken: str = None
    ) -> DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef:
        """
        Describes the specified Network Access Scope analyses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_network_insights_access_scope_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_network_insights_access_scope_analyses)
        """

    def describe_network_insights_access_scopes(
        self,
        *,
        NetworkInsightsAccessScopeIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        DryRun: bool = None,
        NextToken: str = None
    ) -> DescribeNetworkInsightsAccessScopesResultTypeDef:
        """
        Describes the specified Network Access Scopes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_network_insights_access_scopes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_network_insights_access_scopes)
        """

    def describe_network_insights_analyses(
        self,
        *,
        NetworkInsightsAnalysisIds: List[str] = None,
        NetworkInsightsPathId: str = None,
        AnalysisStartTime: Union[datetime, str] = None,
        AnalysisEndTime: Union[datetime, str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        DryRun: bool = None,
        NextToken: str = None
    ) -> DescribeNetworkInsightsAnalysesResultTypeDef:
        """
        Describes one or more of your network insights analyses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_network_insights_analyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_network_insights_analyses)
        """

    def describe_network_insights_paths(
        self,
        *,
        NetworkInsightsPathIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        DryRun: bool = None,
        NextToken: str = None
    ) -> DescribeNetworkInsightsPathsResultTypeDef:
        """
        Describes one or more of your paths.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_network_insights_paths)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_network_insights_paths)
        """

    def describe_network_interface_attribute(
        self,
        *,
        NetworkInterfaceId: str,
        Attribute: NetworkInterfaceAttributeType = None,
        DryRun: bool = None
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        Describes a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_network_interface_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_network_interface_attribute)
        """

    def describe_network_interface_permissions(
        self,
        *,
        NetworkInterfacePermissionIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeNetworkInterfacePermissionsResultTypeDef:
        """
        Describes the permissions for your network interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_network_interface_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_network_interface_permissions)
        """

    def describe_network_interfaces(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeNetworkInterfacesResultTypeDef:
        """
        Describes one or more of your network interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_network_interfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_network_interfaces)
        """

    def describe_placement_groups(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        GroupNames: List[str] = None,
        GroupIds: List[str] = None
    ) -> DescribePlacementGroupsResultTypeDef:
        """
        Describes the specified placement groups or all of your placement groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_placement_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_placement_groups)
        """

    def describe_prefix_lists(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        PrefixListIds: List[str] = None
    ) -> DescribePrefixListsResultTypeDef:
        """
        Describes available Amazon Web Services services in a prefix list format, which
        includes the prefix list name and prefix list ID of the service and the IP
        address range for the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_prefix_lists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_prefix_lists)
        """

    def describe_principal_id_format(
        self,
        *,
        DryRun: bool = None,
        Resources: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribePrincipalIdFormatResultTypeDef:
        """
        Describes the ID format settings for the root user and all IAM roles and IAM
        users that have explicitly specified a longer ID (17-character ID) preference.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_principal_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_principal_id_format)
        """

    def describe_public_ipv4_pools(
        self,
        *,
        PoolIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None
    ) -> DescribePublicIpv4PoolsResultTypeDef:
        """
        Describes the specified IPv4 address pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_public_ipv4_pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_public_ipv4_pools)
        """

    def describe_regions(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        RegionNames: List[str] = None,
        DryRun: bool = None,
        AllRegions: bool = None
    ) -> DescribeRegionsResultTypeDef:
        """
        Describes the Regions that are enabled for your account, or all Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_regions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_regions)
        """

    def describe_replace_root_volume_tasks(
        self,
        *,
        ReplaceRootVolumeTaskIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeReplaceRootVolumeTasksResultTypeDef:
        """
        Describes a root volume replacement task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_replace_root_volume_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_replace_root_volume_tasks)
        """

    def describe_reserved_instances(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        OfferingClass: OfferingClassTypeType = None,
        ReservedInstancesIds: List[str] = None,
        DryRun: bool = None,
        OfferingType: OfferingTypeValuesType = None
    ) -> DescribeReservedInstancesResultTypeDef:
        """
        Describes one or more of the Reserved Instances that you purchased.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_reserved_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_reserved_instances)
        """

    def describe_reserved_instances_listings(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        ReservedInstancesId: str = None,
        ReservedInstancesListingId: str = None
    ) -> DescribeReservedInstancesListingsResultTypeDef:
        """
        Describes your account's Reserved Instance listings in the Reserved Instance
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_reserved_instances_listings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_reserved_instances_listings)
        """

    def describe_reserved_instances_modifications(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        ReservedInstancesModificationIds: List[str] = None,
        NextToken: str = None
    ) -> DescribeReservedInstancesModificationsResultTypeDef:
        """
        Describes the modifications made to your Reserved Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_reserved_instances_modifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_reserved_instances_modifications)
        """

    def describe_reserved_instances_offerings(
        self,
        *,
        AvailabilityZone: str = None,
        Filters: List["FilterTypeDef"] = None,
        IncludeMarketplace: bool = None,
        InstanceType: InstanceTypeType = None,
        MaxDuration: int = None,
        MaxInstanceCount: int = None,
        MinDuration: int = None,
        OfferingClass: OfferingClassTypeType = None,
        ProductDescription: RIProductDescriptionType = None,
        ReservedInstancesOfferingIds: List[str] = None,
        DryRun: bool = None,
        InstanceTenancy: TenancyType = None,
        MaxResults: int = None,
        NextToken: str = None,
        OfferingType: OfferingTypeValuesType = None
    ) -> DescribeReservedInstancesOfferingsResultTypeDef:
        """
        Describes Reserved Instance offerings that are available for purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_reserved_instances_offerings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_reserved_instances_offerings)
        """

    def describe_route_tables(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeRouteTablesResultTypeDef:
        """
        Describes your route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_route_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_route_tables)
        """

    def describe_scheduled_instance_availability(
        self,
        *,
        FirstSlotStartTimeRange: "SlotDateTimeRangeRequestTypeDef",
        Recurrence: "ScheduledInstanceRecurrenceRequestTypeDef",
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        NextToken: str = None
    ) -> DescribeScheduledInstanceAvailabilityResultTypeDef:
        """
        Finds available schedules that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_scheduled_instance_availability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_scheduled_instance_availability)
        """

    def describe_scheduled_instances(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ScheduledInstanceIds: List[str] = None,
        SlotStartTimeRange: "SlotStartTimeRangeRequestTypeDef" = None
    ) -> DescribeScheduledInstancesResultTypeDef:
        """
        Describes the specified Scheduled Instances or all your Scheduled Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_scheduled_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_scheduled_instances)
        """

    def describe_security_group_references(
        self, *, GroupId: List[str], DryRun: bool = None
    ) -> DescribeSecurityGroupReferencesResultTypeDef:
        """
        Describes the VPCs on the other side of a VPC peering connection that are
        referencing the security groups you've specified in this request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_security_group_references)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_security_group_references)
        """

    def describe_security_group_rules(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        SecurityGroupRuleIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeSecurityGroupRulesResultTypeDef:
        """
        Describes one or more of your security group rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_security_group_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_security_group_rules)
        """

    def describe_security_groups(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeSecurityGroupsResultTypeDef:
        """
        Describes the specified security groups or all of your security groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_security_groups)
        """

    def describe_snapshot_attribute(
        self, *, Attribute: SnapshotAttributeNameType, SnapshotId: str, DryRun: bool = None
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_snapshot_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_snapshot_attribute)
        """

    def describe_snapshot_tier_status(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeSnapshotTierStatusResultTypeDef:
        """
        Describes the storage tier status of one or more Amazon EBS snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_snapshot_tier_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_snapshot_tier_status)
        """

    def describe_snapshots(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None
    ) -> DescribeSnapshotsResultTypeDef:
        """
        Describes the specified EBS snapshots available to you or all of the EBS
        snapshots available to you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_snapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_snapshots)
        """

    def describe_spot_datafeed_subscription(
        self, *, DryRun: bool = None
    ) -> DescribeSpotDatafeedSubscriptionResultTypeDef:
        """
        Describes the data feed for Spot Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_spot_datafeed_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_spot_datafeed_subscription)
        """

    def describe_spot_fleet_instances(
        self,
        *,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeSpotFleetInstancesResponseTypeDef:
        """
        Describes the running instances for the specified Spot Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_spot_fleet_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_spot_fleet_instances)
        """

    def describe_spot_fleet_request_history(
        self,
        *,
        SpotFleetRequestId: str,
        StartTime: Union[datetime, str],
        DryRun: bool = None,
        EventType: EventTypeType = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeSpotFleetRequestHistoryResponseTypeDef:
        """
        Describes the events for the specified Spot Fleet request during the specified
        time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_spot_fleet_request_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_spot_fleet_request_history)
        """

    def describe_spot_fleet_requests(
        self,
        *,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None,
        SpotFleetRequestIds: List[str] = None
    ) -> DescribeSpotFleetRequestsResponseTypeDef:
        """
        Describes your Spot Fleet requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_spot_fleet_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_spot_fleet_requests)
        """

    def describe_spot_instance_requests(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeSpotInstanceRequestsResultTypeDef:
        """
        Describes the specified Spot Instance requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_spot_instance_requests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_spot_instance_requests)
        """

    def describe_spot_price_history(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        AvailabilityZone: str = None,
        DryRun: bool = None,
        EndTime: Union[datetime, str] = None,
        InstanceTypes: List[InstanceTypeType] = None,
        MaxResults: int = None,
        NextToken: str = None,
        ProductDescriptions: List[str] = None,
        StartTime: Union[datetime, str] = None
    ) -> DescribeSpotPriceHistoryResultTypeDef:
        """
        Describes the Spot price history.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_spot_price_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_spot_price_history)
        """

    def describe_stale_security_groups(
        self, *, VpcId: str, DryRun: bool = None, MaxResults: int = None, NextToken: str = None
    ) -> DescribeStaleSecurityGroupsResultTypeDef:
        """
        Describes the stale security group rules for security groups in a specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_stale_security_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_stale_security_groups)
        """

    def describe_store_image_tasks(
        self,
        *,
        ImageIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeStoreImageTasksResultTypeDef:
        """
        Describes the progress of the AMI store tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_store_image_tasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_store_image_tasks)
        """

    def describe_subnets(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeSubnetsResultTypeDef:
        """
        Describes your subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_subnets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_subnets)
        """

    def describe_tags(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeTagsResultTypeDef:
        """
        Describes the specified tags for your EC2 resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_tags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_tags)
        """

    def describe_traffic_mirror_filter_rules(
        self,
        *,
        TrafficMirrorFilterRuleIds: List[str] = None,
        TrafficMirrorFilterId: str = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeTrafficMirrorFilterRulesResultTypeDef:
        """
        Describe traffic mirror filters that determine the traffic that is mirrored.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_filter_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_traffic_mirror_filter_rules)
        """

    def describe_traffic_mirror_filters(
        self,
        *,
        TrafficMirrorFilterIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeTrafficMirrorFiltersResultTypeDef:
        """
        Describes one or more Traffic Mirror filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_filters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_traffic_mirror_filters)
        """

    def describe_traffic_mirror_sessions(
        self,
        *,
        TrafficMirrorSessionIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeTrafficMirrorSessionsResultTypeDef:
        """
        Describes one or more Traffic Mirror sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_sessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_traffic_mirror_sessions)
        """

    def describe_traffic_mirror_targets(
        self,
        *,
        TrafficMirrorTargetIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeTrafficMirrorTargetsResultTypeDef:
        """
        Information about one or more Traffic Mirror targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_traffic_mirror_targets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_traffic_mirror_targets)
        """

    def describe_transit_gateway_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewayAttachmentsResultTypeDef:
        """
        Describes one or more attachments between resources and transit gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateway_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateway_attachments)
        """

    def describe_transit_gateway_connect_peers(
        self,
        *,
        TransitGatewayConnectPeerIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewayConnectPeersResultTypeDef:
        """
        Describes one or more Connect peers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateway_connect_peers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateway_connect_peers)
        """

    def describe_transit_gateway_connects(
        self,
        *,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewayConnectsResultTypeDef:
        """
        Describes one or more Connect attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateway_connects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateway_connects)
        """

    def describe_transit_gateway_multicast_domains(
        self,
        *,
        TransitGatewayMulticastDomainIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewayMulticastDomainsResultTypeDef:
        """
        Describes one or more transit gateway multicast domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateway_multicast_domains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateway_multicast_domains)
        """

    def describe_transit_gateway_peering_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewayPeeringAttachmentsResultTypeDef:
        """
        Describes your transit gateway peering attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateway_peering_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateway_peering_attachments)
        """

    def describe_transit_gateway_policy_tables(
        self,
        *,
        TransitGatewayPolicyTableIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewayPolicyTablesResultTypeDef:
        """
        Describes one or more transit gateway route policy tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateway_policy_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateway_policy_tables)
        """

    def describe_transit_gateway_route_table_announcements(
        self,
        *,
        TransitGatewayRouteTableAnnouncementIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef:
        """
        Describes one or more transit gateway route table advertisements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateway_route_table_announcements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateway_route_table_announcements)
        """

    def describe_transit_gateway_route_tables(
        self,
        *,
        TransitGatewayRouteTableIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewayRouteTablesResultTypeDef:
        """
        Describes one or more transit gateway route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateway_route_tables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateway_route_tables)
        """

    def describe_transit_gateway_vpc_attachments(
        self,
        *,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewayVpcAttachmentsResultTypeDef:
        """
        Describes one or more VPC attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateway_vpc_attachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateway_vpc_attachments)
        """

    def describe_transit_gateways(
        self,
        *,
        TransitGatewayIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> DescribeTransitGatewaysResultTypeDef:
        """
        Describes one or more transit gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_transit_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_transit_gateways)
        """

    def describe_trunk_interface_associations(
        self,
        *,
        AssociationIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeTrunkInterfaceAssociationsResultTypeDef:
        """
        Describes one or more network interface trunk associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_trunk_interface_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_trunk_interface_associations)
        """

    def describe_verified_access_endpoints(
        self,
        *,
        VerifiedAccessEndpointIds: List[str] = None,
        VerifiedAccessInstanceId: str = None,
        VerifiedAccessGroupId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeVerifiedAccessEndpointsResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_verified_access_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_verified_access_endpoints)
        """

    def describe_verified_access_groups(
        self,
        *,
        VerifiedAccessGroupIds: List[str] = None,
        VerifiedAccessInstanceId: str = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeVerifiedAccessGroupsResultTypeDef:
        """
        Describes the specified Verified Access groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_verified_access_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_verified_access_groups)
        """

    def describe_verified_access_instance_logging_configurations(
        self,
        *,
        VerifiedAccessInstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_verified_access_instance_logging_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_verified_access_instance_logging_configurations)
        """

    def describe_verified_access_instances(
        self,
        *,
        VerifiedAccessInstanceIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeVerifiedAccessInstancesResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_verified_access_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_verified_access_instances)
        """

    def describe_verified_access_trust_providers(
        self,
        *,
        VerifiedAccessTrustProviderIds: List[str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> DescribeVerifiedAccessTrustProvidersResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access trust providers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_verified_access_trust_providers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_verified_access_trust_providers)
        """

    def describe_volume_attribute(
        self, *, Attribute: VolumeAttributeNameType, VolumeId: str, DryRun: bool = None
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_volume_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_volume_attribute)
        """

    def describe_volume_status(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        Describes the status of the specified volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_volume_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_volume_status)
        """

    def describe_volumes(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeVolumesResultTypeDef:
        """
        Describes the specified EBS volumes or all of your EBS volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_volumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_volumes)
        """

    def describe_volumes_modifications(
        self,
        *,
        DryRun: bool = None,
        VolumeIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeVolumesModificationsResultTypeDef:
        """
        Describes the most recent volume modification request for the specified EBS
        volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_volumes_modifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_volumes_modifications)
        """

    def describe_vpc_attribute(
        self, *, Attribute: VpcAttributeNameType, VpcId: str, DryRun: bool = None
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_attribute)
        """

    def describe_vpc_classic_link(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        VpcIds: List[str] = None
    ) -> DescribeVpcClassicLinkResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_classic_link)
        """

    def describe_vpc_classic_link_dns_support(
        self, *, MaxResults: int = None, NextToken: str = None, VpcIds: List[str] = None
    ) -> DescribeVpcClassicLinkDnsSupportResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_classic_link_dns_support)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_classic_link_dns_support)
        """

    def describe_vpc_endpoint_connection_notifications(
        self,
        *,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeVpcEndpointConnectionNotificationsResultTypeDef:
        """
        Describes the connection notifications for VPC endpoints and VPC endpoint
        services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connection_notifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_endpoint_connection_notifications)
        """

    def describe_vpc_endpoint_connections(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeVpcEndpointConnectionsResultTypeDef:
        """
        Describes the VPC endpoint connections to your VPC endpoint services, including
        any endpoints that are pending your acceptance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_endpoint_connections)
        """

    def describe_vpc_endpoint_service_configurations(
        self,
        *,
        DryRun: bool = None,
        ServiceIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeVpcEndpointServiceConfigurationsResultTypeDef:
        """
        Describes the VPC endpoint service configurations in your account (your
        services).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_configurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_endpoint_service_configurations)
        """

    def describe_vpc_endpoint_service_permissions(
        self,
        *,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeVpcEndpointServicePermissionsResultTypeDef:
        """
        Describes the principals (service consumers) that are permitted to discover your
        VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_service_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_endpoint_service_permissions)
        """

    def describe_vpc_endpoint_services(
        self,
        *,
        DryRun: bool = None,
        ServiceNames: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeVpcEndpointServicesResultTypeDef:
        """
        Describes available services to which you can create a VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_endpoint_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_endpoint_services)
        """

    def describe_vpc_endpoints(
        self,
        *,
        DryRun: bool = None,
        VpcEndpointIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> DescribeVpcEndpointsResultTypeDef:
        """
        Describes your VPC endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_endpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_endpoints)
        """

    def describe_vpc_peering_connections(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeVpcPeeringConnectionsResultTypeDef:
        """
        Describes your VPC peering connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpc_peering_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpc_peering_connections)
        """

    def describe_vpcs(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> DescribeVpcsResultTypeDef:
        """
        Describes your VPCs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpcs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpcs)
        """

    def describe_vpn_connections(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        VpnConnectionIds: List[str] = None,
        DryRun: bool = None
    ) -> DescribeVpnConnectionsResultTypeDef:
        """
        Describes one or more of your VPN connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpn_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpn_connections)
        """

    def describe_vpn_gateways(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        VpnGatewayIds: List[str] = None,
        DryRun: bool = None
    ) -> DescribeVpnGatewaysResultTypeDef:
        """
        Describes one or more of your virtual private gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.describe_vpn_gateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#describe_vpn_gateways)
        """

    def detach_classic_link_vpc(
        self, *, InstanceId: str, VpcId: str, DryRun: bool = None
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.detach_classic_link_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach_classic_link_vpc)
        """

    def detach_internet_gateway(
        self, *, InternetGatewayId: str, VpcId: str, DryRun: bool = None
    ) -> None:
        """
        Detaches an internet gateway from a VPC, disabling connectivity between the
        internet and the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.detach_internet_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach_internet_gateway)
        """

    def detach_network_interface(
        self, *, AttachmentId: str, DryRun: bool = None, Force: bool = None
    ) -> None:
        """
        Detaches a network interface from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.detach_network_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach_network_interface)
        """

    def detach_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessInstanceId: str,
        VerifiedAccessTrustProviderId: str,
        ClientToken: str = None,
        DryRun: bool = None
    ) -> DetachVerifiedAccessTrustProviderResultTypeDef:
        """
        Detaches the specified Amazon Web Services Verified Access trust provider from
        the specified Amazon Web Services Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.detach_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach_verified_access_trust_provider)
        """

    def detach_volume(
        self,
        *,
        VolumeId: str,
        Device: str = None,
        Force: bool = None,
        InstanceId: str = None,
        DryRun: bool = None
    ) -> VolumeAttachmentResponseMetadataTypeDef:
        """
        Detaches an EBS volume from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.detach_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach_volume)
        """

    def detach_vpn_gateway(self, *, VpcId: str, VpnGatewayId: str, DryRun: bool = None) -> None:
        """
        Detaches a virtual private gateway from a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.detach_vpn_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#detach_vpn_gateway)
        """

    def disable_address_transfer(
        self, *, AllocationId: str, DryRun: bool = None
    ) -> DisableAddressTransferResultTypeDef:
        """
        Disables Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_address_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_address_transfer)
        """

    def disable_aws_network_performance_metric_subscription(
        self,
        *,
        Source: str = None,
        Destination: str = None,
        Metric: Literal["aggregate-latency"] = None,
        Statistic: Literal["p50"] = None,
        DryRun: bool = None
    ) -> DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef:
        """
        Disables Infrastructure Performance metric subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_aws_network_performance_metric_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_aws_network_performance_metric_subscription)
        """

    def disable_ebs_encryption_by_default(
        self, *, DryRun: bool = None
    ) -> DisableEbsEncryptionByDefaultResultTypeDef:
        """
        Disables EBS encryption by default for your account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_ebs_encryption_by_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_ebs_encryption_by_default)
        """

    def disable_fast_launch(
        self, *, ImageId: str, Force: bool = None, DryRun: bool = None
    ) -> DisableFastLaunchResultTypeDef:
        """
        Discontinue Windows fast launch for a Windows AMI, and clean up existing pre-
        provisioned snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_fast_launch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_fast_launch)
        """

    def disable_fast_snapshot_restores(
        self, *, AvailabilityZones: List[str], SourceSnapshotIds: List[str], DryRun: bool = None
    ) -> DisableFastSnapshotRestoresResultTypeDef:
        """
        Disables fast snapshot restores for the specified snapshots in the specified
        Availability Zones.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_fast_snapshot_restores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_fast_snapshot_restores)
        """

    def disable_image(self, *, ImageId: str, DryRun: bool = None) -> DisableImageResultTypeDef:
        """
        Sets the AMI state to `disabled` and removes all launch permissions from the
        AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_image)
        """

    def disable_image_block_public_access(
        self, *, DryRun: bool = None
    ) -> DisableImageBlockPublicAccessResultTypeDef:
        """
        Disables *block public access for AMIs* at the account level in the specified
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_image_block_public_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_image_block_public_access)
        """

    def disable_image_deprecation(
        self, *, ImageId: str, DryRun: bool = None
    ) -> DisableImageDeprecationResultTypeDef:
        """
        Cancels the deprecation of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_image_deprecation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_image_deprecation)
        """

    def disable_image_deregistration_protection(
        self, *, ImageId: str, DryRun: bool = None
    ) -> DisableImageDeregistrationProtectionResultTypeDef:
        """
        Disables deregistration protection for an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_image_deregistration_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_image_deregistration_protection)
        """

    def disable_ipam_organization_admin_account(
        self, *, DelegatedAdminAccountId: str, DryRun: bool = None
    ) -> DisableIpamOrganizationAdminAccountResultTypeDef:
        """
        Disable the IPAM account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_ipam_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_ipam_organization_admin_account)
        """

    def disable_serial_console_access(
        self, *, DryRun: bool = None
    ) -> DisableSerialConsoleAccessResultTypeDef:
        """
        Disables access to the EC2 serial console of all instances for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_serial_console_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_serial_console_access)
        """

    def disable_snapshot_block_public_access(
        self, *, DryRun: bool = None
    ) -> DisableSnapshotBlockPublicAccessResultTypeDef:
        """
        Disables the *block public access for snapshots* setting at the account level
        for the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_snapshot_block_public_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_snapshot_block_public_access)
        """

    def disable_transit_gateway_route_table_propagation(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        DryRun: bool = None,
        TransitGatewayRouteTableAnnouncementId: str = None
    ) -> DisableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        Disables the specified resource attachment from propagating routes to the
        specified propagation route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_transit_gateway_route_table_propagation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_transit_gateway_route_table_propagation)
        """

    def disable_vgw_route_propagation(
        self, *, GatewayId: str, RouteTableId: str, DryRun: bool = None
    ) -> None:
        """
        Disables a virtual private gateway (VGW) from propagating routes to a specified
        route table of a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_vgw_route_propagation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_vgw_route_propagation)
        """

    def disable_vpc_classic_link(
        self, *, VpcId: str, DryRun: bool = None
    ) -> DisableVpcClassicLinkResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_vpc_classic_link)
        """

    def disable_vpc_classic_link_dns_support(
        self, *, VpcId: str = None
    ) -> DisableVpcClassicLinkDnsSupportResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disable_vpc_classic_link_dns_support)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disable_vpc_classic_link_dns_support)
        """

    def disassociate_address(
        self, *, AssociationId: str = None, PublicIp: str = None, DryRun: bool = None
    ) -> None:
        """
        Disassociates an Elastic IP address from the instance or network interface it's
        associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_address)
        """

    def disassociate_client_vpn_target_network(
        self, *, ClientVpnEndpointId: str, AssociationId: str, DryRun: bool = None
    ) -> DisassociateClientVpnTargetNetworkResultTypeDef:
        """
        Disassociates a target network from the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_client_vpn_target_network)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_client_vpn_target_network)
        """

    def disassociate_enclave_certificate_iam_role(
        self, *, CertificateArn: str, RoleArn: str, DryRun: bool = None
    ) -> DisassociateEnclaveCertificateIamRoleResultTypeDef:
        """
        Disassociates an IAM role from an Certificate Manager (ACM) certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_enclave_certificate_iam_role)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_enclave_certificate_iam_role)
        """

    def disassociate_iam_instance_profile(
        self, *, AssociationId: str
    ) -> DisassociateIamInstanceProfileResultTypeDef:
        """
        Disassociates an IAM instance profile from a running or stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_iam_instance_profile)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_iam_instance_profile)
        """

    def disassociate_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        AssociationTarget: "InstanceEventWindowDisassociationRequestTypeDef",
        DryRun: bool = None
    ) -> DisassociateInstanceEventWindowResultTypeDef:
        """
        Disassociates one or more targets from an event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_instance_event_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_instance_event_window)
        """

    def disassociate_ipam_byoasn(
        self, *, Asn: str, Cidr: str, DryRun: bool = None
    ) -> DisassociateIpamByoasnResultTypeDef:
        """
        Remove the association between your Autonomous System Number (ASN) and your
        BYOIP CIDR.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_ipam_byoasn)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_ipam_byoasn)
        """

    def disassociate_ipam_resource_discovery(
        self, *, IpamResourceDiscoveryAssociationId: str, DryRun: bool = None
    ) -> DisassociateIpamResourceDiscoveryResultTypeDef:
        """
        Disassociates a resource discovery from an Amazon VPC IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_ipam_resource_discovery)
        """

    def disassociate_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        AssociationIds: List[str],
        MaxDrainDurationSeconds: int = None,
        DryRun: bool = None
    ) -> DisassociateNatGatewayAddressResultTypeDef:
        """
        Disassociates secondary Elastic IP addresses (EIPs) from a public NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_nat_gateway_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_nat_gateway_address)
        """

    def disassociate_route_table(self, *, AssociationId: str, DryRun: bool = None) -> None:
        """
        Disassociates a subnet or gateway from a route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_route_table)
        """

    def disassociate_subnet_cidr_block(
        self, *, AssociationId: str
    ) -> DisassociateSubnetCidrBlockResultTypeDef:
        """
        Disassociates a CIDR block from a subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_subnet_cidr_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_subnet_cidr_block)
        """

    def disassociate_transit_gateway_multicast_domain(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        TransitGatewayAttachmentId: str,
        SubnetIds: List[str],
        DryRun: bool = None
    ) -> DisassociateTransitGatewayMulticastDomainResultTypeDef:
        """
        Disassociates the specified subnets from the transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_multicast_domain)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_transit_gateway_multicast_domain)
        """

    def disassociate_transit_gateway_policy_table(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool = None
    ) -> DisassociateTransitGatewayPolicyTableResultTypeDef:
        """
        Removes the association between an an attachment and a policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_policy_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_transit_gateway_policy_table)
        """

    def disassociate_transit_gateway_route_table(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str,
        DryRun: bool = None
    ) -> DisassociateTransitGatewayRouteTableResultTypeDef:
        """
        Disassociates a resource attachment from a transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_transit_gateway_route_table)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_transit_gateway_route_table)
        """

    def disassociate_trunk_interface(
        self, *, AssociationId: str, ClientToken: str = None, DryRun: bool = None
    ) -> DisassociateTrunkInterfaceResultTypeDef:
        """
        Removes an association between a branch network interface with a trunk network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_trunk_interface)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_trunk_interface)
        """

    def disassociate_vpc_cidr_block(
        self, *, AssociationId: str
    ) -> DisassociateVpcCidrBlockResultTypeDef:
        """
        Disassociates a CIDR block from a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.disassociate_vpc_cidr_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#disassociate_vpc_cidr_block)
        """

    def enable_address_transfer(
        self, *, AllocationId: str, TransferAccountId: str, DryRun: bool = None
    ) -> EnableAddressTransferResultTypeDef:
        """
        Enables Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_address_transfer)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_address_transfer)
        """

    def enable_aws_network_performance_metric_subscription(
        self,
        *,
        Source: str = None,
        Destination: str = None,
        Metric: Literal["aggregate-latency"] = None,
        Statistic: Literal["p50"] = None,
        DryRun: bool = None
    ) -> EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef:
        """
        Enables Infrastructure Performance subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_aws_network_performance_metric_subscription)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_aws_network_performance_metric_subscription)
        """

    def enable_ebs_encryption_by_default(
        self, *, DryRun: bool = None
    ) -> EnableEbsEncryptionByDefaultResultTypeDef:
        """
        Enables EBS encryption by default for your account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_ebs_encryption_by_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_ebs_encryption_by_default)
        """

    def enable_fast_launch(
        self,
        *,
        ImageId: str,
        ResourceType: str = None,
        SnapshotConfiguration: "FastLaunchSnapshotConfigurationRequestTypeDef" = None,
        LaunchTemplate: "FastLaunchLaunchTemplateSpecificationRequestTypeDef" = None,
        MaxParallelLaunches: int = None,
        DryRun: bool = None
    ) -> EnableFastLaunchResultTypeDef:
        """
        When you enable Windows fast launch for a Windows AMI, images are pre-
        provisioned, using snapshots to launch instances up to 65% faster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_fast_launch)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_fast_launch)
        """

    def enable_fast_snapshot_restores(
        self, *, AvailabilityZones: List[str], SourceSnapshotIds: List[str], DryRun: bool = None
    ) -> EnableFastSnapshotRestoresResultTypeDef:
        """
        Enables fast snapshot restores for the specified snapshots in the specified
        Availability Zones.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_fast_snapshot_restores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_fast_snapshot_restores)
        """

    def enable_image(self, *, ImageId: str, DryRun: bool = None) -> EnableImageResultTypeDef:
        """
        Re-enables a disabled AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_image)
        """

    def enable_image_block_public_access(
        self, *, ImageBlockPublicAccessState: Literal["block-new-sharing"], DryRun: bool = None
    ) -> EnableImageBlockPublicAccessResultTypeDef:
        """
        Enables *block public access for AMIs* at the account level in the specified
        Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_image_block_public_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_image_block_public_access)
        """

    def enable_image_deprecation(
        self, *, ImageId: str, DeprecateAt: Union[datetime, str], DryRun: bool = None
    ) -> EnableImageDeprecationResultTypeDef:
        """
        Enables deprecation of the specified AMI at the specified date and time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_image_deprecation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_image_deprecation)
        """

    def enable_image_deregistration_protection(
        self, *, ImageId: str, WithCooldown: bool = None, DryRun: bool = None
    ) -> EnableImageDeregistrationProtectionResultTypeDef:
        """
        Enables deregistration protection for an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_image_deregistration_protection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_image_deregistration_protection)
        """

    def enable_ipam_organization_admin_account(
        self, *, DelegatedAdminAccountId: str, DryRun: bool = None
    ) -> EnableIpamOrganizationAdminAccountResultTypeDef:
        """
        Enable an Organizations member account as the IPAM admin account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_ipam_organization_admin_account)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_ipam_organization_admin_account)
        """

    def enable_reachability_analyzer_organization_sharing(
        self, *, DryRun: bool = None
    ) -> EnableReachabilityAnalyzerOrganizationSharingResultTypeDef:
        """
        Establishes a trust relationship between Reachability Analyzer and
        Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_reachability_analyzer_organization_sharing)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_reachability_analyzer_organization_sharing)
        """

    def enable_serial_console_access(
        self, *, DryRun: bool = None
    ) -> EnableSerialConsoleAccessResultTypeDef:
        """
        Enables access to the EC2 serial console of all instances for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_serial_console_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_serial_console_access)
        """

    def enable_snapshot_block_public_access(
        self, *, State: SnapshotBlockPublicAccessStateType, DryRun: bool = None
    ) -> EnableSnapshotBlockPublicAccessResultTypeDef:
        """
        Enables or modifies the *block public access for snapshots* setting at the
        account level for the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_snapshot_block_public_access)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_snapshot_block_public_access)
        """

    def enable_transit_gateway_route_table_propagation(
        self,
        *,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        DryRun: bool = None,
        TransitGatewayRouteTableAnnouncementId: str = None
    ) -> EnableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        Enables the specified attachment to propagate routes to the specified
        propagation route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_transit_gateway_route_table_propagation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_transit_gateway_route_table_propagation)
        """

    def enable_vgw_route_propagation(
        self, *, GatewayId: str, RouteTableId: str, DryRun: bool = None
    ) -> None:
        """
        Enables a virtual private gateway (VGW) to propagate routes to the specified
        route table of a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_vgw_route_propagation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_vgw_route_propagation)
        """

    def enable_volume_io(self, *, VolumeId: str, DryRun: bool = None) -> None:
        """
        Enables I/O operations for a volume that had I/O operations disabled because the
        data on the volume was potentially inconsistent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_volume_io)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_volume_io)
        """

    def enable_vpc_classic_link(
        self, *, VpcId: str, DryRun: bool = None
    ) -> EnableVpcClassicLinkResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_vpc_classic_link)
        """

    def enable_vpc_classic_link_dns_support(
        self, *, VpcId: str = None
    ) -> EnableVpcClassicLinkDnsSupportResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.enable_vpc_classic_link_dns_support)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#enable_vpc_classic_link_dns_support)
        """

    def export_client_vpn_client_certificate_revocation_list(
        self, *, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> ExportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        Downloads the client certificate revocation list for the specified Client VPN
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.export_client_vpn_client_certificate_revocation_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#export_client_vpn_client_certificate_revocation_list)
        """

    def export_client_vpn_client_configuration(
        self, *, ClientVpnEndpointId: str, DryRun: bool = None
    ) -> ExportClientVpnClientConfigurationResultTypeDef:
        """
        Downloads the contents of the Client VPN endpoint configuration file for the
        specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.export_client_vpn_client_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#export_client_vpn_client_configuration)
        """

    def export_image(
        self,
        *,
        DiskImageFormat: DiskImageFormatType,
        ImageId: str,
        S3ExportLocation: "ExportTaskS3LocationRequestTypeDef",
        ClientToken: str = None,
        Description: str = None,
        DryRun: bool = None,
        RoleName: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> ExportImageResultTypeDef:
        """
        Exports an Amazon Machine Image (AMI) to a VM file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.export_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#export_image)
        """

    def export_transit_gateway_routes(
        self,
        *,
        TransitGatewayRouteTableId: str,
        S3Bucket: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> ExportTransitGatewayRoutesResultTypeDef:
        """
        Exports routes from the specified transit gateway route table to the specified
        S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.export_transit_gateway_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#export_transit_gateway_routes)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Dict[str, Any] = None,
        ExpiresIn: int = 3600,
        HttpMethod: str = None,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.generate_presigned_url)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#generate_presigned_url)
        """

    def get_associated_enclave_certificate_iam_roles(
        self, *, CertificateArn: str, DryRun: bool = None
    ) -> GetAssociatedEnclaveCertificateIamRolesResultTypeDef:
        """
        Returns the IAM roles that are associated with the specified ACM (ACM)
        certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_associated_enclave_certificate_iam_roles)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_associated_enclave_certificate_iam_roles)
        """

    def get_associated_ipv6_pool_cidrs(
        self, *, PoolId: str, NextToken: str = None, MaxResults: int = None, DryRun: bool = None
    ) -> GetAssociatedIpv6PoolCidrsResultTypeDef:
        """
        Gets information about the IPv6 CIDR block associations for a specified IPv6
        address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_associated_ipv6_pool_cidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_associated_ipv6_pool_cidrs)
        """

    def get_aws_network_performance_data(
        self,
        *,
        DataQueries: List["DataQueryTypeDef"] = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetAwsNetworkPerformanceDataResultTypeDef:
        """
        Gets network performance data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_aws_network_performance_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_aws_network_performance_data)
        """

    def get_capacity_reservation_usage(
        self,
        *,
        CapacityReservationId: str,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None
    ) -> GetCapacityReservationUsageResultTypeDef:
        """
        Gets usage information about a Capacity Reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_capacity_reservation_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_capacity_reservation_usage)
        """

    def get_coip_pool_usage(
        self,
        *,
        PoolId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetCoipPoolUsageResultTypeDef:
        """
        Describes the allocations from the specified customer-owned address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_coip_pool_usage)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_coip_pool_usage)
        """

    def get_console_output(
        self, *, InstanceId: str, DryRun: bool = None, Latest: bool = None
    ) -> GetConsoleOutputResultTypeDef:
        """
        Gets the console output for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_console_output)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_console_output)
        """

    def get_console_screenshot(
        self, *, InstanceId: str, DryRun: bool = None, WakeUp: bool = None
    ) -> GetConsoleScreenshotResultTypeDef:
        """
        Retrieve a JPG-format screenshot of a running instance to help with
        troubleshooting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_console_screenshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_console_screenshot)
        """

    def get_default_credit_specification(
        self, *, InstanceFamily: UnlimitedSupportedInstanceFamilyType, DryRun: bool = None
    ) -> GetDefaultCreditSpecificationResultTypeDef:
        """
        Describes the default credit option for CPU usage of a burstable performance
        instance family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_default_credit_specification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_default_credit_specification)
        """

    def get_ebs_default_kms_key_id(
        self, *, DryRun: bool = None
    ) -> GetEbsDefaultKmsKeyIdResultTypeDef:
        """
        Describes the default KMS key for EBS encryption by default for your account in
        this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_ebs_default_kms_key_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_ebs_default_kms_key_id)
        """

    def get_ebs_encryption_by_default(
        self, *, DryRun: bool = None
    ) -> GetEbsEncryptionByDefaultResultTypeDef:
        """
        Describes whether EBS encryption by default is enabled for your account in the
        current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_ebs_encryption_by_default)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_ebs_encryption_by_default)
        """

    def get_flow_logs_integration_template(
        self,
        *,
        FlowLogId: str,
        ConfigDeliveryS3DestinationArn: str,
        IntegrateServices: "IntegrateServicesTypeDef",
        DryRun: bool = None
    ) -> GetFlowLogsIntegrationTemplateResultTypeDef:
        """
        Generates a CloudFormation template that streamlines and automates the
        integration of VPC flow logs with Amazon Athena.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_flow_logs_integration_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_flow_logs_integration_template)
        """

    def get_groups_for_capacity_reservation(
        self,
        *,
        CapacityReservationId: str,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None
    ) -> GetGroupsForCapacityReservationResultTypeDef:
        """
        Lists the resource groups to which a Capacity Reservation has been added.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_groups_for_capacity_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_groups_for_capacity_reservation)
        """

    def get_host_reservation_purchase_preview(
        self, *, HostIdSet: List[str], OfferingId: str
    ) -> GetHostReservationPurchasePreviewResultTypeDef:
        """
        Preview a reservation purchase with configurations that match those of your
        Dedicated Host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_host_reservation_purchase_preview)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_host_reservation_purchase_preview)
        """

    def get_image_block_public_access_state(
        self, *, DryRun: bool = None
    ) -> GetImageBlockPublicAccessStateResultTypeDef:
        """
        Gets the current state of *block public access for AMIs* at the account level in
        the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_image_block_public_access_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_image_block_public_access_state)
        """

    def get_instance_metadata_defaults(
        self, *, DryRun: bool = None
    ) -> GetInstanceMetadataDefaultsResultTypeDef:
        """
        Gets the default instance metadata service (IMDS) settings that are set at the
        account level in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_instance_metadata_defaults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_instance_metadata_defaults)
        """

    def get_instance_tpm_ek_pub(
        self,
        *,
        InstanceId: str,
        KeyType: EkPubKeyTypeType,
        KeyFormat: EkPubKeyFormatType,
        DryRun: bool = None
    ) -> GetInstanceTpmEkPubResultTypeDef:
        """
        Gets the public endorsement key associated with the Nitro Trusted Platform
        Module (NitroTPM) for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_instance_tpm_ek_pub)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_instance_tpm_ek_pub)
        """

    def get_instance_types_from_instance_requirements(
        self,
        *,
        ArchitectureTypes: List[ArchitectureTypeType],
        VirtualizationTypes: List[VirtualizationTypeType],
        InstanceRequirements: "InstanceRequirementsRequestTypeDef",
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetInstanceTypesFromInstanceRequirementsResultTypeDef:
        """
        Returns a list of instance types with the specified instance attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_instance_types_from_instance_requirements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_instance_types_from_instance_requirements)
        """

    def get_instance_uefi_data(
        self, *, InstanceId: str, DryRun: bool = None
    ) -> GetInstanceUefiDataResultTypeDef:
        """
        A binary representation of the UEFI variable store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_instance_uefi_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_instance_uefi_data)
        """

    def get_ipam_address_history(
        self,
        *,
        Cidr: str,
        IpamScopeId: str,
        DryRun: bool = None,
        VpcId: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetIpamAddressHistoryResultTypeDef:
        """
        Retrieve historical information about a CIDR within an IPAM scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_ipam_address_history)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_ipam_address_history)
        """

    def get_ipam_discovered_accounts(
        self,
        *,
        IpamResourceDiscoveryId: str,
        DiscoveryRegion: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetIpamDiscoveredAccountsResultTypeDef:
        """
        Gets IPAM discovered accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_ipam_discovered_accounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_ipam_discovered_accounts)
        """

    def get_ipam_discovered_public_addresses(
        self,
        *,
        IpamResourceDiscoveryId: str,
        AddressRegion: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetIpamDiscoveredPublicAddressesResultTypeDef:
        """
        Gets the public IP addresses that have been discovered by IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_ipam_discovered_public_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_ipam_discovered_public_addresses)
        """

    def get_ipam_discovered_resource_cidrs(
        self,
        *,
        IpamResourceDiscoveryId: str,
        ResourceRegion: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetIpamDiscoveredResourceCidrsResultTypeDef:
        """
        Returns the resource CIDRs that are monitored as part of a resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_ipam_discovered_resource_cidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_ipam_discovered_resource_cidrs)
        """

    def get_ipam_pool_allocations(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = None,
        IpamPoolAllocationId: str = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetIpamPoolAllocationsResultTypeDef:
        """
        Get a list of all the CIDR allocations in an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_ipam_pool_allocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_ipam_pool_allocations)
        """

    def get_ipam_pool_cidrs(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetIpamPoolCidrsResultTypeDef:
        """
        Get the CIDRs provisioned to an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_ipam_pool_cidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_ipam_pool_cidrs)
        """

    def get_ipam_resource_cidrs(
        self,
        *,
        IpamScopeId: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        IpamPoolId: str = None,
        ResourceId: str = None,
        ResourceType: IpamResourceTypeType = None,
        ResourceTag: "RequestIpamResourceTagTypeDef" = None,
        ResourceOwner: str = None
    ) -> GetIpamResourceCidrsResultTypeDef:
        """
        Returns resource CIDRs managed by IPAM in a given scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_ipam_resource_cidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_ipam_resource_cidrs)
        """

    def get_launch_template_data(
        self, *, InstanceId: str, DryRun: bool = None
    ) -> GetLaunchTemplateDataResultTypeDef:
        """
        Retrieves the configuration data of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_launch_template_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_launch_template_data)
        """

    def get_managed_prefix_list_associations(
        self,
        *,
        PrefixListId: str,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetManagedPrefixListAssociationsResultTypeDef:
        """
        Gets information about the resources that are associated with the specified
        managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_managed_prefix_list_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_managed_prefix_list_associations)
        """

    def get_managed_prefix_list_entries(
        self,
        *,
        PrefixListId: str,
        DryRun: bool = None,
        TargetVersion: int = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetManagedPrefixListEntriesResultTypeDef:
        """
        Gets information about the entries for a specified managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_managed_prefix_list_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_managed_prefix_list_entries)
        """

    def get_network_insights_access_scope_analysis_findings(
        self,
        *,
        NetworkInsightsAccessScopeAnalysisId: str,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef:
        """
        Gets the findings for the specified Network Access Scope analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_network_insights_access_scope_analysis_findings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_network_insights_access_scope_analysis_findings)
        """

    def get_network_insights_access_scope_content(
        self, *, NetworkInsightsAccessScopeId: str, DryRun: bool = None
    ) -> GetNetworkInsightsAccessScopeContentResultTypeDef:
        """
        Gets the content for the specified Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_network_insights_access_scope_content)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_network_insights_access_scope_content)
        """

    def get_password_data(
        self, *, InstanceId: str, DryRun: bool = None
    ) -> GetPasswordDataResultTypeDef:
        """
        Retrieves the encrypted administrator password for a running Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_password_data)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_password_data)
        """

    def get_reserved_instances_exchange_quote(
        self,
        *,
        ReservedInstanceIds: List[str],
        DryRun: bool = None,
        TargetConfigurations: List["TargetConfigurationRequestTypeDef"] = None
    ) -> GetReservedInstancesExchangeQuoteResultTypeDef:
        """
        Returns a quote and exchange information for exchanging one or more specified
        Convertible Reserved Instances for a new Convertible Reserved Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_reserved_instances_exchange_quote)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_reserved_instances_exchange_quote)
        """

    def get_security_groups_for_vpc(
        self,
        *,
        VpcId: str,
        NextToken: str = None,
        MaxResults: int = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None
    ) -> GetSecurityGroupsForVpcResultTypeDef:
        """
        Gets security groups that can be associated by the Amazon Web Services account
        making the request with network interfaces in the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_security_groups_for_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_security_groups_for_vpc)
        """

    def get_serial_console_access_status(
        self, *, DryRun: bool = None
    ) -> GetSerialConsoleAccessStatusResultTypeDef:
        """
        Retrieves the access status of your account to the EC2 serial console of all
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_serial_console_access_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_serial_console_access_status)
        """

    def get_snapshot_block_public_access_state(
        self, *, DryRun: bool = None
    ) -> GetSnapshotBlockPublicAccessStateResultTypeDef:
        """
        Gets the current state of *block public access for snapshots* setting for the
        account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_snapshot_block_public_access_state)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_snapshot_block_public_access_state)
        """

    def get_spot_placement_scores(
        self,
        *,
        TargetCapacity: int,
        InstanceTypes: List[str] = None,
        TargetCapacityUnitType: TargetCapacityUnitTypeType = None,
        SingleAvailabilityZone: bool = None,
        RegionNames: List[str] = None,
        InstanceRequirementsWithMetadata: "InstanceRequirementsWithMetadataRequestTypeDef" = None,
        DryRun: bool = None,
        MaxResults: int = None,
        NextToken: str = None
    ) -> GetSpotPlacementScoresResultTypeDef:
        """
        Calculates the Spot placement score for a Region or Availability Zone based on
        the specified target capacity and compute requirements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_spot_placement_scores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_spot_placement_scores)
        """

    def get_subnet_cidr_reservations(
        self,
        *,
        SubnetId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        NextToken: str = None,
        MaxResults: int = None
    ) -> GetSubnetCidrReservationsResultTypeDef:
        """
        Gets information about the subnet CIDR reservations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_subnet_cidr_reservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_subnet_cidr_reservations)
        """

    def get_transit_gateway_attachment_propagations(
        self,
        *,
        TransitGatewayAttachmentId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetTransitGatewayAttachmentPropagationsResultTypeDef:
        """
        Lists the route tables to which the specified resource attachment propagates
        routes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_transit_gateway_attachment_propagations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_transit_gateway_attachment_propagations)
        """

    def get_transit_gateway_multicast_domain_associations(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        Gets information about the associations for the transit gateway multicast
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_transit_gateway_multicast_domain_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_transit_gateway_multicast_domain_associations)
        """

    def get_transit_gateway_policy_table_associations(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetTransitGatewayPolicyTableAssociationsResultTypeDef:
        """
        Gets a list of the transit gateway policy table associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_transit_gateway_policy_table_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_transit_gateway_policy_table_associations)
        """

    def get_transit_gateway_policy_table_entries(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetTransitGatewayPolicyTableEntriesResultTypeDef:
        """
        Returns a list of transit gateway policy table entries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_transit_gateway_policy_table_entries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_transit_gateway_policy_table_entries)
        """

    def get_transit_gateway_prefix_list_references(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetTransitGatewayPrefixListReferencesResultTypeDef:
        """
        Gets information about the prefix list references in a specified transit gateway
        route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_transit_gateway_prefix_list_references)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_transit_gateway_prefix_list_references)
        """

    def get_transit_gateway_route_table_associations(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetTransitGatewayRouteTableAssociationsResultTypeDef:
        """
        Gets information about the associations for the specified transit gateway route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_transit_gateway_route_table_associations)
        """

    def get_transit_gateway_route_table_propagations(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> GetTransitGatewayRouteTablePropagationsResultTypeDef:
        """
        Gets information about the route table propagations for the specified transit
        gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_transit_gateway_route_table_propagations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_transit_gateway_route_table_propagations)
        """

    def get_verified_access_endpoint_policy(
        self, *, VerifiedAccessEndpointId: str, DryRun: bool = None
    ) -> GetVerifiedAccessEndpointPolicyResultTypeDef:
        """
        Get the Verified Access policy associated with the endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_verified_access_endpoint_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_verified_access_endpoint_policy)
        """

    def get_verified_access_group_policy(
        self, *, VerifiedAccessGroupId: str, DryRun: bool = None
    ) -> GetVerifiedAccessGroupPolicyResultTypeDef:
        """
        Shows the contents of the Verified Access policy associated with the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_verified_access_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_verified_access_group_policy)
        """

    def get_vpn_connection_device_sample_configuration(
        self,
        *,
        VpnConnectionId: str,
        VpnConnectionDeviceTypeId: str,
        InternetKeyExchangeVersion: str = None,
        DryRun: bool = None
    ) -> GetVpnConnectionDeviceSampleConfigurationResultTypeDef:
        """
        Download an Amazon Web Services-provided sample configuration file to be used
        with the customer gateway device specified for your Site-to-Site VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_vpn_connection_device_sample_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_vpn_connection_device_sample_configuration)
        """

    def get_vpn_connection_device_types(
        self, *, MaxResults: int = None, NextToken: str = None, DryRun: bool = None
    ) -> GetVpnConnectionDeviceTypesResultTypeDef:
        """
        Obtain a list of customer gateway devices for which sample configuration files
        can be provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_vpn_connection_device_types)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_vpn_connection_device_types)
        """

    def get_vpn_tunnel_replacement_status(
        self, *, VpnConnectionId: str, VpnTunnelOutsideIpAddress: str, DryRun: bool = None
    ) -> GetVpnTunnelReplacementStatusResultTypeDef:
        """
        Get details of available tunnel endpoint maintenance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.get_vpn_tunnel_replacement_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#get_vpn_tunnel_replacement_status)
        """

    def import_client_vpn_client_certificate_revocation_list(
        self, *, ClientVpnEndpointId: str, CertificateRevocationList: str, DryRun: bool = None
    ) -> ImportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        Uploads a client certificate revocation list to the specified Client VPN
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.import_client_vpn_client_certificate_revocation_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import_client_vpn_client_certificate_revocation_list)
        """

    def import_image(
        self,
        *,
        Architecture: str = None,
        ClientData: "ClientDataTypeDef" = None,
        ClientToken: str = None,
        Description: str = None,
        DiskContainers: List["ImageDiskContainerTypeDef"] = None,
        DryRun: bool = None,
        Encrypted: bool = None,
        Hypervisor: str = None,
        KmsKeyId: str = None,
        LicenseType: str = None,
        Platform: str = None,
        RoleName: str = None,
        LicenseSpecifications: List["ImportImageLicenseConfigurationRequestTypeDef"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        UsageOperation: str = None,
        BootMode: BootModeValuesType = None
    ) -> ImportImageResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.import_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import_image)
        """

    def import_instance(
        self,
        *,
        Platform: Literal["Windows"],
        Description: str = None,
        DiskImages: List["DiskImageTypeDef"] = None,
        DryRun: bool = None,
        LaunchSpecification: "ImportInstanceLaunchSpecificationTypeDef" = None
    ) -> ImportInstanceResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.import_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import_instance)
        """

    def import_key_pair(
        self,
        *,
        KeyName: str,
        PublicKeyMaterial: Union[bytes, IO[bytes], StreamingBody],
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> ImportKeyPairResultTypeDef:
        """
        Imports the public key from an RSA or ED25519 key pair that you created with a
        third-party tool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.import_key_pair)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import_key_pair)
        """

    def import_snapshot(
        self,
        *,
        ClientData: "ClientDataTypeDef" = None,
        ClientToken: str = None,
        Description: str = None,
        DiskContainer: "SnapshotDiskContainerTypeDef" = None,
        DryRun: bool = None,
        Encrypted: bool = None,
        KmsKeyId: str = None,
        RoleName: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> ImportSnapshotResultTypeDef:
        """
        Imports a disk into an EBS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.import_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import_snapshot)
        """

    def import_volume(
        self,
        *,
        AvailabilityZone: str,
        Image: "DiskImageDetailTypeDef",
        Volume: "VolumeDetailTypeDef",
        Description: str = None,
        DryRun: bool = None
    ) -> ImportVolumeResultTypeDef:
        """
        Creates an import volume task using metadata from the specified disk image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.import_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#import_volume)
        """

    def list_images_in_recycle_bin(
        self,
        *,
        ImageIds: List[str] = None,
        NextToken: str = None,
        MaxResults: int = None,
        DryRun: bool = None
    ) -> ListImagesInRecycleBinResultTypeDef:
        """
        Lists one or more AMIs that are currently in the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.list_images_in_recycle_bin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#list_images_in_recycle_bin)
        """

    def list_snapshots_in_recycle_bin(
        self,
        *,
        MaxResults: int = None,
        NextToken: str = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None
    ) -> ListSnapshotsInRecycleBinResultTypeDef:
        """
        Lists one or more snapshots that are currently in the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.list_snapshots_in_recycle_bin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#list_snapshots_in_recycle_bin)
        """

    def lock_snapshot(
        self,
        *,
        SnapshotId: str,
        LockMode: LockModeType,
        DryRun: bool = None,
        CoolOffPeriod: int = None,
        LockDuration: int = None,
        ExpirationDate: Union[datetime, str] = None
    ) -> LockSnapshotResultTypeDef:
        """
        Locks an Amazon EBS snapshot in either *governance* or *compliance* mode to
        protect it against accidental or malicious deletions for a specific duration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.lock_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#lock_snapshot)
        """

    def modify_address_attribute(
        self, *, AllocationId: str, DomainName: str = None, DryRun: bool = None
    ) -> ModifyAddressAttributeResultTypeDef:
        """
        Modifies an attribute of the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_address_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_address_attribute)
        """

    def modify_availability_zone_group(
        self,
        *,
        GroupName: str,
        OptInStatus: ModifyAvailabilityZoneOptInStatusType,
        DryRun: bool = None
    ) -> ModifyAvailabilityZoneGroupResultTypeDef:
        """
        Changes the opt-in status of the specified zone group for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_availability_zone_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_availability_zone_group)
        """

    def modify_capacity_reservation(
        self,
        *,
        CapacityReservationId: str,
        InstanceCount: int = None,
        EndDate: Union[datetime, str] = None,
        EndDateType: EndDateTypeType = None,
        Accept: bool = None,
        DryRun: bool = None,
        AdditionalInfo: str = None
    ) -> ModifyCapacityReservationResultTypeDef:
        """
        Modifies a Capacity Reservation's capacity and the conditions under which it is
        to be released.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_capacity_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_capacity_reservation)
        """

    def modify_capacity_reservation_fleet(
        self,
        *,
        CapacityReservationFleetId: str,
        TotalTargetCapacity: int = None,
        EndDate: Union[datetime, str] = None,
        DryRun: bool = None,
        RemoveEndDate: bool = None
    ) -> ModifyCapacityReservationFleetResultTypeDef:
        """
        Modifies a Capacity Reservation Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_capacity_reservation_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_capacity_reservation_fleet)
        """

    def modify_client_vpn_endpoint(
        self,
        *,
        ClientVpnEndpointId: str,
        ServerCertificateArn: str = None,
        ConnectionLogOptions: "ConnectionLogOptionsTypeDef" = None,
        DnsServers: "DnsServersOptionsModifyStructureTypeDef" = None,
        VpnPort: int = None,
        Description: str = None,
        SplitTunnel: bool = None,
        DryRun: bool = None,
        SecurityGroupIds: List[str] = None,
        VpcId: str = None,
        SelfServicePortal: SelfServicePortalType = None,
        ClientConnectOptions: "ClientConnectOptionsTypeDef" = None,
        SessionTimeoutHours: int = None,
        ClientLoginBannerOptions: "ClientLoginBannerOptionsTypeDef" = None
    ) -> ModifyClientVpnEndpointResultTypeDef:
        """
        Modifies the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_client_vpn_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_client_vpn_endpoint)
        """

    def modify_default_credit_specification(
        self,
        *,
        InstanceFamily: UnlimitedSupportedInstanceFamilyType,
        CpuCredits: str,
        DryRun: bool = None
    ) -> ModifyDefaultCreditSpecificationResultTypeDef:
        """
        Modifies the default credit option for CPU usage of burstable performance
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_default_credit_specification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_default_credit_specification)
        """

    def modify_ebs_default_kms_key_id(
        self, *, KmsKeyId: str, DryRun: bool = None
    ) -> ModifyEbsDefaultKmsKeyIdResultTypeDef:
        """
        Changes the default KMS key for EBS encryption by default for your account in
        this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_ebs_default_kms_key_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_ebs_default_kms_key_id)
        """

    def modify_fleet(
        self,
        *,
        FleetId: str,
        DryRun: bool = None,
        ExcessCapacityTerminationPolicy: FleetExcessCapacityTerminationPolicyType = None,
        LaunchTemplateConfigs: List["FleetLaunchTemplateConfigRequestTypeDef"] = None,
        TargetCapacitySpecification: "TargetCapacitySpecificationRequestTypeDef" = None,
        Context: str = None
    ) -> ModifyFleetResultTypeDef:
        """
        Modifies the specified EC2 Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_fleet)
        """

    def modify_fpga_image_attribute(
        self,
        *,
        FpgaImageId: str,
        DryRun: bool = None,
        Attribute: FpgaImageAttributeNameType = None,
        OperationType: OperationTypeType = None,
        UserIds: List[str] = None,
        UserGroups: List[str] = None,
        ProductCodes: List[str] = None,
        LoadPermission: "LoadPermissionModificationsTypeDef" = None,
        Description: str = None,
        Name: str = None
    ) -> ModifyFpgaImageAttributeResultTypeDef:
        """
        Modifies the specified attribute of the specified Amazon FPGA Image (AFI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_fpga_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_fpga_image_attribute)
        """

    def modify_hosts(
        self,
        *,
        HostIds: List[str],
        AutoPlacement: AutoPlacementType = None,
        HostRecovery: HostRecoveryType = None,
        InstanceType: str = None,
        InstanceFamily: str = None,
        HostMaintenance: HostMaintenanceType = None
    ) -> ModifyHostsResultTypeDef:
        """
        Modify the auto-placement setting of a Dedicated Host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_hosts)
        """

    def modify_id_format(self, *, Resource: str, UseLongIds: bool) -> None:
        """
        Modifies the ID format for the specified resource on a per-Region basis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_id_format)
        """

    def modify_identity_id_format(
        self, *, PrincipalArn: str, Resource: str, UseLongIds: bool
    ) -> None:
        """
        Modifies the ID format of a resource for a specified IAM user, IAM role, or the
        root user for an account; or all IAM users, IAM roles, and the root user for an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_identity_id_format)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_identity_id_format)
        """

    def modify_image_attribute(
        self,
        *,
        ImageId: str,
        Attribute: str = None,
        Description: "AttributeValueTypeDef" = None,
        LaunchPermission: "LaunchPermissionModificationsTypeDef" = None,
        OperationType: OperationTypeType = None,
        ProductCodes: List[str] = None,
        UserGroups: List[str] = None,
        UserIds: List[str] = None,
        Value: str = None,
        DryRun: bool = None,
        OrganizationArns: List[str] = None,
        OrganizationalUnitArns: List[str] = None,
        ImdsSupport: "AttributeValueTypeDef" = None
    ) -> None:
        """
        Modifies the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_image_attribute)
        """

    def modify_instance_attribute(
        self,
        *,
        InstanceId: str,
        SourceDestCheck: "AttributeBooleanValueTypeDef" = None,
        Attribute: InstanceAttributeNameType = None,
        BlockDeviceMappings: List["InstanceBlockDeviceMappingSpecificationTypeDef"] = None,
        DisableApiTermination: "AttributeBooleanValueTypeDef" = None,
        DryRun: bool = None,
        EbsOptimized: "AttributeBooleanValueTypeDef" = None,
        EnaSupport: "AttributeBooleanValueTypeDef" = None,
        Groups: List[str] = None,
        InstanceInitiatedShutdownBehavior: "AttributeValueTypeDef" = None,
        InstanceType: "AttributeValueTypeDef" = None,
        Kernel: "AttributeValueTypeDef" = None,
        Ramdisk: "AttributeValueTypeDef" = None,
        SriovNetSupport: "AttributeValueTypeDef" = None,
        UserData: "BlobAttributeValueTypeDef" = None,
        Value: str = None,
        DisableApiStop: "AttributeBooleanValueTypeDef" = None
    ) -> None:
        """
        Modifies the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_instance_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_instance_attribute)
        """

    def modify_instance_capacity_reservation_attributes(
        self,
        *,
        InstanceId: str,
        CapacityReservationSpecification: "CapacityReservationSpecificationTypeDef",
        DryRun: bool = None
    ) -> ModifyInstanceCapacityReservationAttributesResultTypeDef:
        """
        Modifies the Capacity Reservation settings for a stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_instance_capacity_reservation_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_instance_capacity_reservation_attributes)
        """

    def modify_instance_credit_specification(
        self,
        *,
        InstanceCreditSpecifications: List["InstanceCreditSpecificationRequestTypeDef"],
        DryRun: bool = None,
        ClientToken: str = None
    ) -> ModifyInstanceCreditSpecificationResultTypeDef:
        """
        Modifies the credit option for CPU usage on a running or stopped burstable
        performance instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_instance_credit_specification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_instance_credit_specification)
        """

    def modify_instance_event_start_time(
        self,
        *,
        InstanceId: str,
        InstanceEventId: str,
        NotBefore: Union[datetime, str],
        DryRun: bool = None
    ) -> ModifyInstanceEventStartTimeResultTypeDef:
        """
        Modifies the start time for a scheduled Amazon EC2 instance event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_instance_event_start_time)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_instance_event_start_time)
        """

    def modify_instance_event_window(
        self,
        *,
        InstanceEventWindowId: str,
        DryRun: bool = None,
        Name: str = None,
        TimeRanges: List["InstanceEventWindowTimeRangeRequestTypeDef"] = None,
        CronExpression: str = None
    ) -> ModifyInstanceEventWindowResultTypeDef:
        """
        Modifies the specified event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_instance_event_window)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_instance_event_window)
        """

    def modify_instance_maintenance_options(
        self,
        *,
        InstanceId: str,
        AutoRecovery: InstanceAutoRecoveryStateType = None,
        DryRun: bool = None
    ) -> ModifyInstanceMaintenanceOptionsResultTypeDef:
        """
        Modifies the recovery behavior of your instance to disable simplified automatic
        recovery or set the recovery behavior to default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_instance_maintenance_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_instance_maintenance_options)
        """

    def modify_instance_metadata_defaults(
        self,
        *,
        HttpTokens: MetadataDefaultHttpTokensStateType = None,
        HttpPutResponseHopLimit: int = None,
        HttpEndpoint: DefaultInstanceMetadataEndpointStateType = None,
        InstanceMetadataTags: DefaultInstanceMetadataTagsStateType = None,
        DryRun: bool = None
    ) -> ModifyInstanceMetadataDefaultsResultTypeDef:
        """
        Modifies the default instance metadata service (IMDS) settings at the account
        level in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_instance_metadata_defaults)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_instance_metadata_defaults)
        """

    def modify_instance_metadata_options(
        self,
        *,
        InstanceId: str,
        HttpTokens: HttpTokensStateType = None,
        HttpPutResponseHopLimit: int = None,
        HttpEndpoint: InstanceMetadataEndpointStateType = None,
        DryRun: bool = None,
        HttpProtocolIpv6: InstanceMetadataProtocolStateType = None,
        InstanceMetadataTags: InstanceMetadataTagsStateType = None
    ) -> ModifyInstanceMetadataOptionsResultTypeDef:
        """
        Modify the instance metadata parameters on a running or stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_instance_metadata_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_instance_metadata_options)
        """

    def modify_instance_placement(
        self,
        *,
        InstanceId: str,
        Affinity: AffinityType = None,
        GroupName: str = None,
        HostId: str = None,
        Tenancy: HostTenancyType = None,
        PartitionNumber: int = None,
        HostResourceGroupArn: str = None,
        GroupId: str = None
    ) -> ModifyInstancePlacementResultTypeDef:
        """
        Modifies the placement attributes for a specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_instance_placement)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_instance_placement)
        """

    def modify_ipam(
        self,
        *,
        IpamId: str,
        DryRun: bool = None,
        Description: str = None,
        AddOperatingRegions: List["AddIpamOperatingRegionTypeDef"] = None,
        RemoveOperatingRegions: List["RemoveIpamOperatingRegionTypeDef"] = None,
        Tier: IpamTierType = None
    ) -> ModifyIpamResultTypeDef:
        """
        Modify the configurations of an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_ipam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_ipam)
        """

    def modify_ipam_pool(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = None,
        Description: str = None,
        AutoImport: bool = None,
        AllocationMinNetmaskLength: int = None,
        AllocationMaxNetmaskLength: int = None,
        AllocationDefaultNetmaskLength: int = None,
        ClearAllocationDefaultNetmaskLength: bool = None,
        AddAllocationResourceTags: List["RequestIpamResourceTagTypeDef"] = None,
        RemoveAllocationResourceTags: List["RequestIpamResourceTagTypeDef"] = None
    ) -> ModifyIpamPoolResultTypeDef:
        """
        Modify the configurations of an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_ipam_pool)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_ipam_pool)
        """

    def modify_ipam_resource_cidr(
        self,
        *,
        ResourceId: str,
        ResourceCidr: str,
        ResourceRegion: str,
        CurrentIpamScopeId: str,
        Monitored: bool,
        DryRun: bool = None,
        DestinationIpamScopeId: str = None
    ) -> ModifyIpamResourceCidrResultTypeDef:
        """
        Modify a resource CIDR.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_ipam_resource_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_ipam_resource_cidr)
        """

    def modify_ipam_resource_discovery(
        self,
        *,
        IpamResourceDiscoveryId: str,
        DryRun: bool = None,
        Description: str = None,
        AddOperatingRegions: List["AddIpamOperatingRegionTypeDef"] = None,
        RemoveOperatingRegions: List["RemoveIpamOperatingRegionTypeDef"] = None
    ) -> ModifyIpamResourceDiscoveryResultTypeDef:
        """
        Modifies a resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_ipam_resource_discovery)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_ipam_resource_discovery)
        """

    def modify_ipam_scope(
        self, *, IpamScopeId: str, DryRun: bool = None, Description: str = None
    ) -> ModifyIpamScopeResultTypeDef:
        """
        Modify an IPAM scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_ipam_scope)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_ipam_scope)
        """

    def modify_launch_template(
        self,
        *,
        DryRun: bool = None,
        ClientToken: str = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        DefaultVersion: str = None
    ) -> ModifyLaunchTemplateResultTypeDef:
        """
        Modifies a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_launch_template)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_launch_template)
        """

    def modify_local_gateway_route(
        self,
        *,
        LocalGatewayRouteTableId: str,
        DestinationCidrBlock: str = None,
        LocalGatewayVirtualInterfaceGroupId: str = None,
        NetworkInterfaceId: str = None,
        DryRun: bool = None,
        DestinationPrefixListId: str = None
    ) -> ModifyLocalGatewayRouteResultTypeDef:
        """
        Modifies the specified local gateway route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_local_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_local_gateway_route)
        """

    def modify_managed_prefix_list(
        self,
        *,
        PrefixListId: str,
        DryRun: bool = None,
        CurrentVersion: int = None,
        PrefixListName: str = None,
        AddEntries: List["AddPrefixListEntryTypeDef"] = None,
        RemoveEntries: List["RemovePrefixListEntryTypeDef"] = None,
        MaxEntries: int = None
    ) -> ModifyManagedPrefixListResultTypeDef:
        """
        Modifies the specified managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_managed_prefix_list)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_managed_prefix_list)
        """

    def modify_network_interface_attribute(
        self,
        *,
        NetworkInterfaceId: str,
        Attachment: "NetworkInterfaceAttachmentChangesTypeDef" = None,
        Description: "AttributeValueTypeDef" = None,
        DryRun: bool = None,
        Groups: List[str] = None,
        SourceDestCheck: "AttributeBooleanValueTypeDef" = None,
        EnaSrdSpecification: "EnaSrdSpecificationTypeDef" = None,
        EnablePrimaryIpv6: bool = None,
        ConnectionTrackingSpecification: "ConnectionTrackingSpecificationRequestTypeDef" = None,
        AssociatePublicIpAddress: bool = None
    ) -> None:
        """
        Modifies the specified network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_network_interface_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_network_interface_attribute)
        """

    def modify_private_dns_name_options(
        self,
        *,
        InstanceId: str,
        DryRun: bool = None,
        PrivateDnsHostnameType: HostnameTypeType = None,
        EnableResourceNameDnsARecord: bool = None,
        EnableResourceNameDnsAAAARecord: bool = None
    ) -> ModifyPrivateDnsNameOptionsResultTypeDef:
        """
        Modifies the options for instance hostnames for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_private_dns_name_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_private_dns_name_options)
        """

    def modify_reserved_instances(
        self,
        *,
        ReservedInstancesIds: List[str],
        TargetConfigurations: List["ReservedInstancesConfigurationTypeDef"],
        ClientToken: str = None
    ) -> ModifyReservedInstancesResultTypeDef:
        """
        Modifies the configuration of your Reserved Instances, such as the Availability
        Zone, instance count, or instance type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_reserved_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_reserved_instances)
        """

    def modify_security_group_rules(
        self,
        *,
        GroupId: str,
        SecurityGroupRules: List["SecurityGroupRuleUpdateTypeDef"],
        DryRun: bool = None
    ) -> ModifySecurityGroupRulesResultTypeDef:
        """
        Modifies the rules of a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_security_group_rules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_security_group_rules)
        """

    def modify_snapshot_attribute(
        self,
        *,
        SnapshotId: str,
        Attribute: SnapshotAttributeNameType = None,
        CreateVolumePermission: "CreateVolumePermissionModificationsTypeDef" = None,
        GroupNames: List[str] = None,
        OperationType: OperationTypeType = None,
        UserIds: List[str] = None,
        DryRun: bool = None
    ) -> None:
        """
        Adds or removes permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_snapshot_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_snapshot_attribute)
        """

    def modify_snapshot_tier(
        self, *, SnapshotId: str, StorageTier: Literal["archive"] = None, DryRun: bool = None
    ) -> ModifySnapshotTierResultTypeDef:
        """
        Archives an Amazon EBS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_snapshot_tier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_snapshot_tier)
        """

    def modify_spot_fleet_request(
        self,
        *,
        SpotFleetRequestId: str,
        ExcessCapacityTerminationPolicy: ExcessCapacityTerminationPolicyType = None,
        LaunchTemplateConfigs: List["LaunchTemplateConfigTypeDef"] = None,
        TargetCapacity: int = None,
        OnDemandTargetCapacity: int = None,
        Context: str = None
    ) -> ModifySpotFleetRequestResponseTypeDef:
        """
        Modifies the specified Spot Fleet request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_spot_fleet_request)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_spot_fleet_request)
        """

    def modify_subnet_attribute(
        self,
        *,
        SubnetId: str,
        AssignIpv6AddressOnCreation: "AttributeBooleanValueTypeDef" = None,
        MapPublicIpOnLaunch: "AttributeBooleanValueTypeDef" = None,
        MapCustomerOwnedIpOnLaunch: "AttributeBooleanValueTypeDef" = None,
        CustomerOwnedIpv4Pool: str = None,
        EnableDns64: "AttributeBooleanValueTypeDef" = None,
        PrivateDnsHostnameTypeOnLaunch: HostnameTypeType = None,
        EnableResourceNameDnsARecordOnLaunch: "AttributeBooleanValueTypeDef" = None,
        EnableResourceNameDnsAAAARecordOnLaunch: "AttributeBooleanValueTypeDef" = None,
        EnableLniAtDeviceIndex: int = None,
        DisableLniAtDeviceIndex: "AttributeBooleanValueTypeDef" = None
    ) -> None:
        """
        Modifies a subnet attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_subnet_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_subnet_attribute)
        """

    def modify_traffic_mirror_filter_network_services(
        self,
        *,
        TrafficMirrorFilterId: str,
        AddNetworkServices: List[Literal["amazon-dns"]] = None,
        RemoveNetworkServices: List[Literal["amazon-dns"]] = None,
        DryRun: bool = None
    ) -> ModifyTrafficMirrorFilterNetworkServicesResultTypeDef:
        """
        Allows or restricts mirroring network services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_network_services)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_traffic_mirror_filter_network_services)
        """

    def modify_traffic_mirror_filter_rule(
        self,
        *,
        TrafficMirrorFilterRuleId: str,
        TrafficDirection: TrafficDirectionType = None,
        RuleNumber: int = None,
        RuleAction: TrafficMirrorRuleActionType = None,
        DestinationPortRange: "TrafficMirrorPortRangeRequestTypeDef" = None,
        SourcePortRange: "TrafficMirrorPortRangeRequestTypeDef" = None,
        Protocol: int = None,
        DestinationCidrBlock: str = None,
        SourceCidrBlock: str = None,
        Description: str = None,
        RemoveFields: List[TrafficMirrorFilterRuleFieldType] = None,
        DryRun: bool = None
    ) -> ModifyTrafficMirrorFilterRuleResultTypeDef:
        """
        Modifies the specified Traffic Mirror rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_filter_rule)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_traffic_mirror_filter_rule)
        """

    def modify_traffic_mirror_session(
        self,
        *,
        TrafficMirrorSessionId: str,
        TrafficMirrorTargetId: str = None,
        TrafficMirrorFilterId: str = None,
        PacketLength: int = None,
        SessionNumber: int = None,
        VirtualNetworkId: int = None,
        Description: str = None,
        RemoveFields: List[TrafficMirrorSessionFieldType] = None,
        DryRun: bool = None
    ) -> ModifyTrafficMirrorSessionResultTypeDef:
        """
        Modifies a Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_traffic_mirror_session)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_traffic_mirror_session)
        """

    def modify_transit_gateway(
        self,
        *,
        TransitGatewayId: str,
        Description: str = None,
        Options: "ModifyTransitGatewayOptionsTypeDef" = None,
        DryRun: bool = None
    ) -> ModifyTransitGatewayResultTypeDef:
        """
        Modifies the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_transit_gateway)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_transit_gateway)
        """

    def modify_transit_gateway_prefix_list_reference(
        self,
        *,
        TransitGatewayRouteTableId: str,
        PrefixListId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None
    ) -> ModifyTransitGatewayPrefixListReferenceResultTypeDef:
        """
        Modifies a reference (route) to a prefix list in a specified transit gateway
        route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_transit_gateway_prefix_list_reference)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_transit_gateway_prefix_list_reference)
        """

    def modify_transit_gateway_vpc_attachment(
        self,
        *,
        TransitGatewayAttachmentId: str,
        AddSubnetIds: List[str] = None,
        RemoveSubnetIds: List[str] = None,
        Options: "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef" = None,
        DryRun: bool = None
    ) -> ModifyTransitGatewayVpcAttachmentResultTypeDef:
        """
        Modifies the specified VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_transit_gateway_vpc_attachment)
        """

    def modify_verified_access_endpoint(
        self,
        *,
        VerifiedAccessEndpointId: str,
        VerifiedAccessGroupId: str = None,
        LoadBalancerOptions: "ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef" = None,
        NetworkInterfaceOptions: "ModifyVerifiedAccessEndpointEniOptionsTypeDef" = None,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None
    ) -> ModifyVerifiedAccessEndpointResultTypeDef:
        """
        Modifies the configuration of the specified Amazon Web Services Verified Access
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_verified_access_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_verified_access_endpoint)
        """

    def modify_verified_access_endpoint_policy(
        self,
        *,
        VerifiedAccessEndpointId: str,
        PolicyEnabled: bool = None,
        PolicyDocument: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
        SseSpecification: "VerifiedAccessSseSpecificationRequestTypeDef" = None
    ) -> ModifyVerifiedAccessEndpointPolicyResultTypeDef:
        """
        Modifies the specified Amazon Web Services Verified Access endpoint policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_verified_access_endpoint_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_verified_access_endpoint_policy)
        """

    def modify_verified_access_group(
        self,
        *,
        VerifiedAccessGroupId: str,
        VerifiedAccessInstanceId: str = None,
        Description: str = None,
        ClientToken: str = None,
        DryRun: bool = None
    ) -> ModifyVerifiedAccessGroupResultTypeDef:
        """
        Modifies the specified Amazon Web Services Verified Access group configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_verified_access_group)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_verified_access_group)
        """

    def modify_verified_access_group_policy(
        self,
        *,
        VerifiedAccessGroupId: str,
        PolicyEnabled: bool = None,
        PolicyDocument: str = None,
        ClientToken: str = None,
        DryRun: bool = None,
        SseSpecification: "VerifiedAccessSseSpecificationRequestTypeDef" = None
    ) -> ModifyVerifiedAccessGroupPolicyResultTypeDef:
        """
        Modifies the specified Amazon Web Services Verified Access group policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_verified_access_group_policy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_verified_access_group_policy)
        """

    def modify_verified_access_instance(
        self,
        *,
        VerifiedAccessInstanceId: str,
        Description: str = None,
        DryRun: bool = None,
        ClientToken: str = None
    ) -> ModifyVerifiedAccessInstanceResultTypeDef:
        """
        Modifies the configuration of the specified Amazon Web Services Verified Access
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_verified_access_instance)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_verified_access_instance)
        """

    def modify_verified_access_instance_logging_configuration(
        self,
        *,
        VerifiedAccessInstanceId: str,
        AccessLogs: "VerifiedAccessLogOptionsTypeDef",
        DryRun: bool = None,
        ClientToken: str = None
    ) -> ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef:
        """
        Modifies the logging configuration for the specified Amazon Web Services
        Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_verified_access_instance_logging_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_verified_access_instance_logging_configuration)
        """

    def modify_verified_access_trust_provider(
        self,
        *,
        VerifiedAccessTrustProviderId: str,
        OidcOptions: "ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef" = None,
        DeviceOptions: "ModifyVerifiedAccessTrustProviderDeviceOptionsTypeDef" = None,
        Description: str = None,
        DryRun: bool = None,
        ClientToken: str = None,
        SseSpecification: "VerifiedAccessSseSpecificationRequestTypeDef" = None
    ) -> ModifyVerifiedAccessTrustProviderResultTypeDef:
        """
        Modifies the configuration of the specified Amazon Web Services Verified Access
        trust provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_verified_access_trust_provider)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_verified_access_trust_provider)
        """

    def modify_volume(
        self,
        *,
        VolumeId: str,
        DryRun: bool = None,
        Size: int = None,
        VolumeType: VolumeTypeType = None,
        Iops: int = None,
        Throughput: int = None,
        MultiAttachEnabled: bool = None
    ) -> ModifyVolumeResultTypeDef:
        """
        You can modify several parameters of an existing EBS volume, including volume
        size, volume type, and IOPS capacity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_volume)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_volume)
        """

    def modify_volume_attribute(
        self,
        *,
        VolumeId: str,
        AutoEnableIO: "AttributeBooleanValueTypeDef" = None,
        DryRun: bool = None
    ) -> None:
        """
        Modifies a volume attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_volume_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_volume_attribute)
        """

    def modify_vpc_attribute(
        self,
        *,
        VpcId: str,
        EnableDnsHostnames: "AttributeBooleanValueTypeDef" = None,
        EnableDnsSupport: "AttributeBooleanValueTypeDef" = None,
        EnableNetworkAddressUsageMetrics: "AttributeBooleanValueTypeDef" = None
    ) -> None:
        """
        Modifies the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpc_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpc_attribute)
        """

    def modify_vpc_endpoint(
        self,
        *,
        VpcEndpointId: str,
        DryRun: bool = None,
        ResetPolicy: bool = None,
        PolicyDocument: str = None,
        AddRouteTableIds: List[str] = None,
        RemoveRouteTableIds: List[str] = None,
        AddSubnetIds: List[str] = None,
        RemoveSubnetIds: List[str] = None,
        AddSecurityGroupIds: List[str] = None,
        RemoveSecurityGroupIds: List[str] = None,
        IpAddressType: IpAddressTypeType = None,
        DnsOptions: "DnsOptionsSpecificationTypeDef" = None,
        PrivateDnsEnabled: bool = None,
        SubnetConfigurations: List["SubnetConfigurationTypeDef"] = None
    ) -> ModifyVpcEndpointResultTypeDef:
        """
        Modifies attributes of a specified VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpc_endpoint)
        """

    def modify_vpc_endpoint_connection_notification(
        self,
        *,
        ConnectionNotificationId: str,
        DryRun: bool = None,
        ConnectionNotificationArn: str = None,
        ConnectionEvents: List[str] = None
    ) -> ModifyVpcEndpointConnectionNotificationResultTypeDef:
        """
        Modifies a connection notification for VPC endpoint or VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_connection_notification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpc_endpoint_connection_notification)
        """

    def modify_vpc_endpoint_service_configuration(
        self,
        *,
        ServiceId: str,
        DryRun: bool = None,
        PrivateDnsName: str = None,
        RemovePrivateDnsName: bool = None,
        AcceptanceRequired: bool = None,
        AddNetworkLoadBalancerArns: List[str] = None,
        RemoveNetworkLoadBalancerArns: List[str] = None,
        AddGatewayLoadBalancerArns: List[str] = None,
        RemoveGatewayLoadBalancerArns: List[str] = None,
        AddSupportedIpAddressTypes: List[str] = None,
        RemoveSupportedIpAddressTypes: List[str] = None
    ) -> ModifyVpcEndpointServiceConfigurationResultTypeDef:
        """
        Modifies the attributes of your VPC endpoint service configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_configuration)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpc_endpoint_service_configuration)
        """

    def modify_vpc_endpoint_service_payer_responsibility(
        self, *, ServiceId: str, PayerResponsibility: Literal["ServiceOwner"], DryRun: bool = None
    ) -> ModifyVpcEndpointServicePayerResponsibilityResultTypeDef:
        """
        Modifies the payer responsibility for your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_payer_responsibility)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpc_endpoint_service_payer_responsibility)
        """

    def modify_vpc_endpoint_service_permissions(
        self,
        *,
        ServiceId: str,
        DryRun: bool = None,
        AddAllowedPrincipals: List[str] = None,
        RemoveAllowedPrincipals: List[str] = None
    ) -> ModifyVpcEndpointServicePermissionsResultTypeDef:
        """
        Modifies the permissions for your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpc_endpoint_service_permissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpc_endpoint_service_permissions)
        """

    def modify_vpc_peering_connection_options(
        self,
        *,
        VpcPeeringConnectionId: str,
        AccepterPeeringConnectionOptions: "PeeringConnectionOptionsRequestTypeDef" = None,
        DryRun: bool = None,
        RequesterPeeringConnectionOptions: "PeeringConnectionOptionsRequestTypeDef" = None
    ) -> ModifyVpcPeeringConnectionOptionsResultTypeDef:
        """
        Modifies the VPC peering connection options on one side of a VPC peering
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpc_peering_connection_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpc_peering_connection_options)
        """

    def modify_vpc_tenancy(
        self, *, VpcId: str, InstanceTenancy: Literal["default"], DryRun: bool = None
    ) -> ModifyVpcTenancyResultTypeDef:
        """
        Modifies the instance tenancy attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpc_tenancy)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpc_tenancy)
        """

    def modify_vpn_connection(
        self,
        *,
        VpnConnectionId: str,
        TransitGatewayId: str = None,
        CustomerGatewayId: str = None,
        VpnGatewayId: str = None,
        DryRun: bool = None
    ) -> ModifyVpnConnectionResultTypeDef:
        """
        Modifies the customer gateway or the target gateway of an Amazon Web Services
        Site-to-Site VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpn_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpn_connection)
        """

    def modify_vpn_connection_options(
        self,
        *,
        VpnConnectionId: str,
        LocalIpv4NetworkCidr: str = None,
        RemoteIpv4NetworkCidr: str = None,
        LocalIpv6NetworkCidr: str = None,
        RemoteIpv6NetworkCidr: str = None,
        DryRun: bool = None
    ) -> ModifyVpnConnectionOptionsResultTypeDef:
        """
        Modifies the connection options for your Site-to-Site VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpn_connection_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpn_connection_options)
        """

    def modify_vpn_tunnel_certificate(
        self, *, VpnConnectionId: str, VpnTunnelOutsideIpAddress: str, DryRun: bool = None
    ) -> ModifyVpnTunnelCertificateResultTypeDef:
        """
        Modifies the VPN tunnel endpoint certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_certificate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpn_tunnel_certificate)
        """

    def modify_vpn_tunnel_options(
        self,
        *,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        TunnelOptions: "ModifyVpnTunnelOptionsSpecificationTypeDef",
        DryRun: bool = None,
        SkipTunnelReplacement: bool = None
    ) -> ModifyVpnTunnelOptionsResultTypeDef:
        """
        Modifies the options for a VPN tunnel in an Amazon Web Services Site-to-Site VPN
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.modify_vpn_tunnel_options)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#modify_vpn_tunnel_options)
        """

    def monitor_instances(
        self, *, InstanceIds: List[str], DryRun: bool = None
    ) -> MonitorInstancesResultTypeDef:
        """
        Enables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.monitor_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#monitor_instances)
        """

    def move_address_to_vpc(
        self, *, PublicIp: str, DryRun: bool = None
    ) -> MoveAddressToVpcResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.move_address_to_vpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#move_address_to_vpc)
        """

    def move_byoip_cidr_to_ipam(
        self, *, Cidr: str, IpamPoolId: str, IpamPoolOwner: str, DryRun: bool = None
    ) -> MoveByoipCidrToIpamResultTypeDef:
        """
        Move a BYOIPv4 CIDR to IPAM from a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.move_byoip_cidr_to_ipam)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#move_byoip_cidr_to_ipam)
        """

    def provision_byoip_cidr(
        self,
        *,
        Cidr: str,
        CidrAuthorizationContext: "CidrAuthorizationContextTypeDef" = None,
        PubliclyAdvertisable: bool = None,
        Description: str = None,
        DryRun: bool = None,
        PoolTagSpecifications: List["TagSpecificationTypeDef"] = None,
        MultiRegion: bool = None,
        NetworkBorderGroup: str = None
    ) -> ProvisionByoipCidrResultTypeDef:
        """
        Provisions an IPv4 or IPv6 address range for use with your Amazon Web Services
        resources through bring your own IP addresses (BYOIP) and creates a
        corresponding address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.provision_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#provision_byoip_cidr)
        """

    def provision_ipam_byoasn(
        self,
        *,
        IpamId: str,
        Asn: str,
        AsnAuthorizationContext: "AsnAuthorizationContextTypeDef",
        DryRun: bool = None
    ) -> ProvisionIpamByoasnResultTypeDef:
        """
        Provisions your Autonomous System Number (ASN) for use in your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.provision_ipam_byoasn)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#provision_ipam_byoasn)
        """

    def provision_ipam_pool_cidr(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = None,
        Cidr: str = None,
        CidrAuthorizationContext: "IpamCidrAuthorizationContextTypeDef" = None,
        NetmaskLength: int = None,
        ClientToken: str = None
    ) -> ProvisionIpamPoolCidrResultTypeDef:
        """
        Provision a CIDR to an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.provision_ipam_pool_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#provision_ipam_pool_cidr)
        """

    def provision_public_ipv4_pool_cidr(
        self, *, IpamPoolId: str, PoolId: str, NetmaskLength: int, DryRun: bool = None
    ) -> ProvisionPublicIpv4PoolCidrResultTypeDef:
        """
        Provision a CIDR to a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.provision_public_ipv4_pool_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#provision_public_ipv4_pool_cidr)
        """

    def purchase_capacity_block(
        self,
        *,
        CapacityBlockOfferingId: str,
        InstancePlatform: CapacityReservationInstancePlatformType,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> PurchaseCapacityBlockResultTypeDef:
        """
        Purchase the Capacity Block for use with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.purchase_capacity_block)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#purchase_capacity_block)
        """

    def purchase_host_reservation(
        self,
        *,
        HostIdSet: List[str],
        OfferingId: str,
        ClientToken: str = None,
        CurrencyCode: Literal["USD"] = None,
        LimitPrice: str = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> PurchaseHostReservationResultTypeDef:
        """
        Purchase a reservation with configurations that match those of your Dedicated
        Host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.purchase_host_reservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#purchase_host_reservation)
        """

    def purchase_reserved_instances_offering(
        self,
        *,
        InstanceCount: int,
        ReservedInstancesOfferingId: str,
        DryRun: bool = None,
        LimitPrice: "ReservedInstanceLimitPriceTypeDef" = None,
        PurchaseTime: Union[datetime, str] = None
    ) -> PurchaseReservedInstancesOfferingResultTypeDef:
        """
        Purchases a Reserved Instance for use with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.purchase_reserved_instances_offering)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#purchase_reserved_instances_offering)
        """

    def purchase_scheduled_instances(
        self,
        *,
        PurchaseRequests: List["PurchaseRequestTypeDef"],
        ClientToken: str = None,
        DryRun: bool = None
    ) -> PurchaseScheduledInstancesResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.purchase_scheduled_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#purchase_scheduled_instances)
        """

    def reboot_instances(self, *, InstanceIds: List[str], DryRun: bool = None) -> None:
        """
        Requests a reboot of the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reboot_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reboot_instances)
        """

    def register_image(
        self,
        *,
        Name: str,
        ImageLocation: str = None,
        Architecture: ArchitectureValuesType = None,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        Description: str = None,
        DryRun: bool = None,
        EnaSupport: bool = None,
        KernelId: str = None,
        BillingProducts: List[str] = None,
        RamdiskId: str = None,
        RootDeviceName: str = None,
        SriovNetSupport: str = None,
        VirtualizationType: str = None,
        BootMode: BootModeValuesType = None,
        TpmSupport: Literal["v2.0"] = None,
        UefiData: str = None,
        ImdsSupport: Literal["v2.0"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> RegisterImageResultTypeDef:
        """
        Registers an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.register_image)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#register_image)
        """

    def register_instance_event_notification_attributes(
        self,
        *,
        InstanceTagAttribute: "RegisterInstanceTagAttributeRequestTypeDef",
        DryRun: bool = None
    ) -> RegisterInstanceEventNotificationAttributesResultTypeDef:
        """
        Registers a set of tag keys to include in scheduled event notifications for your
        resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.register_instance_event_notification_attributes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#register_instance_event_notification_attributes)
        """

    def register_transit_gateway_multicast_group_members(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        NetworkInterfaceIds: List[str],
        GroupIpAddress: str = None,
        DryRun: bool = None
    ) -> RegisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        Registers members (network interfaces) with the transit gateway multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_members)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#register_transit_gateway_multicast_group_members)
        """

    def register_transit_gateway_multicast_group_sources(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        NetworkInterfaceIds: List[str],
        GroupIpAddress: str = None,
        DryRun: bool = None
    ) -> RegisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        Registers sources (network interfaces) with the specified transit gateway
        multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.register_transit_gateway_multicast_group_sources)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#register_transit_gateway_multicast_group_sources)
        """

    def reject_transit_gateway_multicast_domain_associations(
        self,
        *,
        TransitGatewayMulticastDomainId: str = None,
        TransitGatewayAttachmentId: str = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None
    ) -> RejectTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        Rejects a request to associate cross-account subnets with a transit gateway
        multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reject_transit_gateway_multicast_domain_associations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject_transit_gateway_multicast_domain_associations)
        """

    def reject_transit_gateway_peering_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> RejectTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Rejects a transit gateway peering attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reject_transit_gateway_peering_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject_transit_gateway_peering_attachment)
        """

    def reject_transit_gateway_vpc_attachment(
        self, *, TransitGatewayAttachmentId: str, DryRun: bool = None
    ) -> RejectTransitGatewayVpcAttachmentResultTypeDef:
        """
        Rejects a request to attach a VPC to a transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reject_transit_gateway_vpc_attachment)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject_transit_gateway_vpc_attachment)
        """

    def reject_vpc_endpoint_connections(
        self, *, ServiceId: str, VpcEndpointIds: List[str], DryRun: bool = None
    ) -> RejectVpcEndpointConnectionsResultTypeDef:
        """
        Rejects VPC endpoint connection requests to your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reject_vpc_endpoint_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject_vpc_endpoint_connections)
        """

    def reject_vpc_peering_connection(
        self, *, VpcPeeringConnectionId: str, DryRun: bool = None
    ) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        Rejects a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reject_vpc_peering_connection)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reject_vpc_peering_connection)
        """

    def release_address(
        self,
        *,
        AllocationId: str = None,
        PublicIp: str = None,
        NetworkBorderGroup: str = None,
        DryRun: bool = None
    ) -> None:
        """
        Releases the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.release_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#release_address)
        """

    def release_hosts(self, *, HostIds: List[str]) -> ReleaseHostsResultTypeDef:
        """
        When you no longer want to use an On-Demand Dedicated Host it can be released.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.release_hosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#release_hosts)
        """

    def release_ipam_pool_allocation(
        self, *, IpamPoolId: str, Cidr: str, IpamPoolAllocationId: str, DryRun: bool = None
    ) -> ReleaseIpamPoolAllocationResultTypeDef:
        """
        Release an allocation within an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.release_ipam_pool_allocation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#release_ipam_pool_allocation)
        """

    def replace_iam_instance_profile_association(
        self, *, IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef", AssociationId: str
    ) -> ReplaceIamInstanceProfileAssociationResultTypeDef:
        """
        Replaces an IAM instance profile for the specified running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.replace_iam_instance_profile_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace_iam_instance_profile_association)
        """

    def replace_network_acl_association(
        self, *, AssociationId: str, NetworkAclId: str, DryRun: bool = None
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        Changes which network ACL a subnet is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.replace_network_acl_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace_network_acl_association)
        """

    def replace_network_acl_entry(
        self,
        *,
        Egress: bool,
        NetworkAclId: str,
        Protocol: str,
        RuleAction: RuleActionType,
        RuleNumber: int,
        CidrBlock: str = None,
        DryRun: bool = None,
        IcmpTypeCode: "IcmpTypeCodeTypeDef" = None,
        Ipv6CidrBlock: str = None,
        PortRange: "PortRangeTypeDef" = None
    ) -> None:
        """
        Replaces an entry (rule) in a network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.replace_network_acl_entry)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace_network_acl_entry)
        """

    def replace_route(
        self,
        *,
        RouteTableId: str,
        DestinationCidrBlock: str = None,
        DestinationIpv6CidrBlock: str = None,
        DestinationPrefixListId: str = None,
        DryRun: bool = None,
        VpcEndpointId: str = None,
        EgressOnlyInternetGatewayId: str = None,
        GatewayId: str = None,
        InstanceId: str = None,
        LocalTarget: bool = None,
        NatGatewayId: str = None,
        TransitGatewayId: str = None,
        LocalGatewayId: str = None,
        CarrierGatewayId: str = None,
        NetworkInterfaceId: str = None,
        VpcPeeringConnectionId: str = None,
        CoreNetworkArn: str = None
    ) -> None:
        """
        Replaces an existing route within a route table in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.replace_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace_route)
        """

    def replace_route_table_association(
        self, *, AssociationId: str, RouteTableId: str, DryRun: bool = None
    ) -> ReplaceRouteTableAssociationResultTypeDef:
        """
        Changes the route table associated with a given subnet, internet gateway, or
        virtual private gateway in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.replace_route_table_association)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace_route_table_association)
        """

    def replace_transit_gateway_route(
        self,
        *,
        DestinationCidrBlock: str,
        TransitGatewayRouteTableId: str,
        TransitGatewayAttachmentId: str = None,
        Blackhole: bool = None,
        DryRun: bool = None
    ) -> ReplaceTransitGatewayRouteResultTypeDef:
        """
        Replaces the specified route in the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.replace_transit_gateway_route)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace_transit_gateway_route)
        """

    def replace_vpn_tunnel(
        self,
        *,
        VpnConnectionId: str,
        VpnTunnelOutsideIpAddress: str,
        ApplyPendingMaintenance: bool = None,
        DryRun: bool = None
    ) -> ReplaceVpnTunnelResultTypeDef:
        """
        Trigger replacement of specified VPN tunnel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.replace_vpn_tunnel)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#replace_vpn_tunnel)
        """

    def report_instance_status(
        self,
        *,
        Instances: List[str],
        ReasonCodes: List[ReportInstanceReasonCodesType],
        Status: ReportStatusTypeType,
        Description: str = None,
        DryRun: bool = None,
        EndTime: Union[datetime, str] = None,
        StartTime: Union[datetime, str] = None
    ) -> None:
        """
        Submits feedback about the status of an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.report_instance_status)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#report_instance_status)
        """

    def request_spot_fleet(
        self, *, SpotFleetRequestConfig: "SpotFleetRequestConfigDataTypeDef", DryRun: bool = None
    ) -> RequestSpotFleetResponseTypeDef:
        """
        Creates a Spot Fleet request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.request_spot_fleet)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#request_spot_fleet)
        """

    def request_spot_instances(
        self,
        *,
        AvailabilityZoneGroup: str = None,
        BlockDurationMinutes: int = None,
        ClientToken: str = None,
        DryRun: bool = None,
        InstanceCount: int = None,
        LaunchGroup: str = None,
        LaunchSpecification: "RequestSpotLaunchSpecificationTypeDef" = None,
        SpotPrice: str = None,
        Type: SpotInstanceTypeType = None,
        ValidFrom: Union[datetime, str] = None,
        ValidUntil: Union[datetime, str] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        InstanceInterruptionBehavior: InstanceInterruptionBehaviorType = None
    ) -> RequestSpotInstancesResultTypeDef:
        """
        Creates a Spot Instance request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.request_spot_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#request_spot_instances)
        """

    def reset_address_attribute(
        self, *, AllocationId: str, Attribute: Literal["domain-name"], DryRun: bool = None
    ) -> ResetAddressAttributeResultTypeDef:
        """
        Resets the attribute of the specified IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reset_address_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset_address_attribute)
        """

    def reset_ebs_default_kms_key_id(
        self, *, DryRun: bool = None
    ) -> ResetEbsDefaultKmsKeyIdResultTypeDef:
        """
        Resets the default KMS key for EBS encryption for your account in this Region to
        the Amazon Web Services managed KMS key for EBS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reset_ebs_default_kms_key_id)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset_ebs_default_kms_key_id)
        """

    def reset_fpga_image_attribute(
        self, *, FpgaImageId: str, DryRun: bool = None, Attribute: Literal["loadPermission"] = None
    ) -> ResetFpgaImageAttributeResultTypeDef:
        """
        Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its
        default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reset_fpga_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset_fpga_image_attribute)
        """

    def reset_image_attribute(
        self, *, Attribute: Literal["launchPermission"], ImageId: str, DryRun: bool = None
    ) -> None:
        """
        Resets an attribute of an AMI to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reset_image_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset_image_attribute)
        """

    def reset_instance_attribute(
        self, *, Attribute: InstanceAttributeNameType, InstanceId: str, DryRun: bool = None
    ) -> None:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reset_instance_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset_instance_attribute)
        """

    def reset_network_interface_attribute(
        self, *, NetworkInterfaceId: str, DryRun: bool = None, SourceDestCheck: str = None
    ) -> None:
        """
        Resets a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reset_network_interface_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset_network_interface_attribute)
        """

    def reset_snapshot_attribute(
        self, *, Attribute: SnapshotAttributeNameType, SnapshotId: str, DryRun: bool = None
    ) -> None:
        """
        Resets permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.reset_snapshot_attribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#reset_snapshot_attribute)
        """

    def restore_address_to_classic(
        self, *, PublicIp: str, DryRun: bool = None
    ) -> RestoreAddressToClassicResultTypeDef:
        """
        .

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.restore_address_to_classic)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#restore_address_to_classic)
        """

    def restore_image_from_recycle_bin(
        self, *, ImageId: str, DryRun: bool = None
    ) -> RestoreImageFromRecycleBinResultTypeDef:
        """
        Restores an AMI from the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.restore_image_from_recycle_bin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#restore_image_from_recycle_bin)
        """

    def restore_managed_prefix_list_version(
        self, *, PrefixListId: str, PreviousVersion: int, CurrentVersion: int, DryRun: bool = None
    ) -> RestoreManagedPrefixListVersionResultTypeDef:
        """
        Restores the entries from a previous version of a managed prefix list to a new
        version of the prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.restore_managed_prefix_list_version)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#restore_managed_prefix_list_version)
        """

    def restore_snapshot_from_recycle_bin(
        self, *, SnapshotId: str, DryRun: bool = None
    ) -> RestoreSnapshotFromRecycleBinResultTypeDef:
        """
        Restores a snapshot from the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.restore_snapshot_from_recycle_bin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#restore_snapshot_from_recycle_bin)
        """

    def restore_snapshot_tier(
        self,
        *,
        SnapshotId: str,
        TemporaryRestoreDays: int = None,
        PermanentRestore: bool = None,
        DryRun: bool = None
    ) -> RestoreSnapshotTierResultTypeDef:
        """
        Restores an archived Amazon EBS snapshot for use temporarily or permanently, or
        modifies the restore period or restore type for a snapshot that was previously
        temporarily restored.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.restore_snapshot_tier)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#restore_snapshot_tier)
        """

    def revoke_client_vpn_ingress(
        self,
        *,
        ClientVpnEndpointId: str,
        TargetNetworkCidr: str,
        AccessGroupId: str = None,
        RevokeAllGroups: bool = None,
        DryRun: bool = None
    ) -> RevokeClientVpnIngressResultTypeDef:
        """
        Removes an ingress authorization rule from a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.revoke_client_vpn_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#revoke_client_vpn_ingress)
        """

    def revoke_security_group_egress(
        self,
        *,
        GroupId: str,
        DryRun: bool = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        SecurityGroupRuleIds: List[str] = None,
        CidrIp: str = None,
        FromPort: int = None,
        IpProtocol: str = None,
        ToPort: int = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None
    ) -> RevokeSecurityGroupEgressResultTypeDef:
        """
        Removes the specified outbound (egress) rules from the specified security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.revoke_security_group_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#revoke_security_group_egress)
        """

    def revoke_security_group_ingress(
        self,
        *,
        CidrIp: str = None,
        FromPort: int = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        IpProtocol: str = None,
        SourceSecurityGroupName: str = None,
        SourceSecurityGroupOwnerId: str = None,
        ToPort: int = None,
        DryRun: bool = None,
        SecurityGroupRuleIds: List[str] = None
    ) -> RevokeSecurityGroupIngressResultTypeDef:
        """
        Removes the specified inbound (ingress) rules from a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.revoke_security_group_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#revoke_security_group_ingress)
        """

    def run_instances(
        self,
        *,
        MaxCount: int,
        MinCount: int,
        BlockDeviceMappings: List["BlockDeviceMappingTypeDef"] = None,
        ImageId: str = None,
        InstanceType: InstanceTypeType = None,
        Ipv6AddressCount: int = None,
        Ipv6Addresses: List["InstanceIpv6AddressTypeDef"] = None,
        KernelId: str = None,
        KeyName: str = None,
        Monitoring: "RunInstancesMonitoringEnabledTypeDef" = None,
        Placement: "PlacementTypeDef" = None,
        RamdiskId: str = None,
        SecurityGroupIds: List[str] = None,
        SecurityGroups: List[str] = None,
        SubnetId: str = None,
        UserData: str = None,
        AdditionalInfo: str = None,
        ClientToken: str = None,
        DisableApiTermination: bool = None,
        DryRun: bool = None,
        EbsOptimized: bool = None,
        IamInstanceProfile: "IamInstanceProfileSpecificationTypeDef" = None,
        InstanceInitiatedShutdownBehavior: ShutdownBehaviorType = None,
        NetworkInterfaces: List["InstanceNetworkInterfaceSpecificationTypeDef"] = None,
        PrivateIpAddress: str = None,
        ElasticGpuSpecification: List["ElasticGpuSpecificationTypeDef"] = None,
        ElasticInferenceAccelerators: List["ElasticInferenceAcceleratorTypeDef"] = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None,
        LaunchTemplate: "LaunchTemplateSpecificationTypeDef" = None,
        InstanceMarketOptions: "InstanceMarketOptionsRequestTypeDef" = None,
        CreditSpecification: "CreditSpecificationRequestTypeDef" = None,
        CpuOptions: "CpuOptionsRequestTypeDef" = None,
        CapacityReservationSpecification: "CapacityReservationSpecificationTypeDef" = None,
        HibernationOptions: "HibernationOptionsRequestTypeDef" = None,
        LicenseSpecifications: List["LicenseConfigurationRequestTypeDef"] = None,
        MetadataOptions: "InstanceMetadataOptionsRequestTypeDef" = None,
        EnclaveOptions: "EnclaveOptionsRequestTypeDef" = None,
        PrivateDnsNameOptions: "PrivateDnsNameOptionsRequestTypeDef" = None,
        MaintenanceOptions: "InstanceMaintenanceOptionsRequestTypeDef" = None,
        DisableApiStop: bool = None,
        EnablePrimaryIpv6: bool = None
    ) -> ReservationResponseMetadataTypeDef:
        """
        Launches the specified number of instances using an AMI for which you have
        permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.run_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#run_instances)
        """

    def run_scheduled_instances(
        self,
        *,
        LaunchSpecification: "ScheduledInstancesLaunchSpecificationTypeDef",
        ScheduledInstanceId: str,
        ClientToken: str = None,
        DryRun: bool = None,
        InstanceCount: int = None
    ) -> RunScheduledInstancesResultTypeDef:
        """
        Launches the specified Scheduled Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.run_scheduled_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#run_scheduled_instances)
        """

    def search_local_gateway_routes(
        self,
        *,
        LocalGatewayRouteTableId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> SearchLocalGatewayRoutesResultTypeDef:
        """
        Searches for routes in the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.search_local_gateway_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#search_local_gateway_routes)
        """

    def search_transit_gateway_multicast_groups(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        Filters: List["FilterTypeDef"] = None,
        MaxResults: int = None,
        NextToken: str = None,
        DryRun: bool = None
    ) -> SearchTransitGatewayMulticastGroupsResultTypeDef:
        """
        Searches one or more transit gateway multicast groups and returns the group
        membership information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.search_transit_gateway_multicast_groups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#search_transit_gateway_multicast_groups)
        """

    def search_transit_gateway_routes(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: List["FilterTypeDef"],
        MaxResults: int = None,
        DryRun: bool = None
    ) -> SearchTransitGatewayRoutesResultTypeDef:
        """
        Searches for routes in the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.search_transit_gateway_routes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#search_transit_gateway_routes)
        """

    def send_diagnostic_interrupt(self, *, InstanceId: str, DryRun: bool = None) -> None:
        """
        Sends a diagnostic interrupt to the specified Amazon EC2 instance to trigger a
        *kernel panic* (on Linux instances), or a *blue screen*/*stop error* (on Windows
        instances).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.send_diagnostic_interrupt)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#send_diagnostic_interrupt)
        """

    def start_instances(
        self, *, InstanceIds: List[str], AdditionalInfo: str = None, DryRun: bool = None
    ) -> StartInstancesResultTypeDef:
        """
        Starts an Amazon EBS-backed instance that you've previously stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.start_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#start_instances)
        """

    def start_network_insights_access_scope_analysis(
        self,
        *,
        NetworkInsightsAccessScopeId: str,
        ClientToken: str,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> StartNetworkInsightsAccessScopeAnalysisResultTypeDef:
        """
        Starts analyzing the specified Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.start_network_insights_access_scope_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#start_network_insights_access_scope_analysis)
        """

    def start_network_insights_analysis(
        self,
        *,
        NetworkInsightsPathId: str,
        ClientToken: str,
        AdditionalAccounts: List[str] = None,
        FilterInArns: List[str] = None,
        DryRun: bool = None,
        TagSpecifications: List["TagSpecificationTypeDef"] = None
    ) -> StartNetworkInsightsAnalysisResultTypeDef:
        """
        Starts analyzing the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.start_network_insights_analysis)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#start_network_insights_analysis)
        """

    def start_vpc_endpoint_service_private_dns_verification(
        self, *, ServiceId: str, DryRun: bool = None
    ) -> StartVpcEndpointServicePrivateDnsVerificationResultTypeDef:
        """
        Initiates the verification process to prove that the service provider owns the
        private DNS name domain for the endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.start_vpc_endpoint_service_private_dns_verification)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#start_vpc_endpoint_service_private_dns_verification)
        """

    def stop_instances(
        self,
        *,
        InstanceIds: List[str],
        Hibernate: bool = None,
        DryRun: bool = None,
        Force: bool = None
    ) -> StopInstancesResultTypeDef:
        """
        Stops an Amazon EBS-backed instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.stop_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#stop_instances)
        """

    def terminate_client_vpn_connections(
        self,
        *,
        ClientVpnEndpointId: str,
        ConnectionId: str = None,
        Username: str = None,
        DryRun: bool = None
    ) -> TerminateClientVpnConnectionsResultTypeDef:
        """
        Terminates active Client VPN endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.terminate_client_vpn_connections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#terminate_client_vpn_connections)
        """

    def terminate_instances(
        self, *, InstanceIds: List[str], DryRun: bool = None
    ) -> TerminateInstancesResultTypeDef:
        """
        Shuts down the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.terminate_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#terminate_instances)
        """

    def unassign_ipv6_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        Ipv6Addresses: List[str] = None,
        Ipv6Prefixes: List[str] = None
    ) -> UnassignIpv6AddressesResultTypeDef:
        """
        Unassigns one or more IPv6 addresses IPv4 Prefix Delegation prefixes from a
        network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.unassign_ipv6_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#unassign_ipv6_addresses)
        """

    def unassign_private_ip_addresses(
        self,
        *,
        NetworkInterfaceId: str,
        PrivateIpAddresses: List[str] = None,
        Ipv4Prefixes: List[str] = None
    ) -> None:
        """
        Unassigns one or more secondary private IP addresses, or IPv4 Prefix Delegation
        prefixes from a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.unassign_private_ip_addresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#unassign_private_ip_addresses)
        """

    def unassign_private_nat_gateway_address(
        self,
        *,
        NatGatewayId: str,
        PrivateIpAddresses: List[str],
        MaxDrainDurationSeconds: int = None,
        DryRun: bool = None
    ) -> UnassignPrivateNatGatewayAddressResultTypeDef:
        """
        Unassigns secondary private IPv4 addresses from a private NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.unassign_private_nat_gateway_address)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#unassign_private_nat_gateway_address)
        """

    def unlock_snapshot(
        self, *, SnapshotId: str, DryRun: bool = None
    ) -> UnlockSnapshotResultTypeDef:
        """
        Unlocks a snapshot that is locked in governance mode or that is locked in
        compliance mode but still in the cooling-off period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.unlock_snapshot)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#unlock_snapshot)
        """

    def unmonitor_instances(
        self, *, InstanceIds: List[str], DryRun: bool = None
    ) -> UnmonitorInstancesResultTypeDef:
        """
        Disables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.unmonitor_instances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#unmonitor_instances)
        """

    def update_security_group_rule_descriptions_egress(
        self,
        *,
        DryRun: bool = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        SecurityGroupRuleDescriptions: List["SecurityGroupRuleDescriptionTypeDef"] = None
    ) -> UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef:
        """
        Updates the description of an egress (outbound) security group rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_egress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#update_security_group_rule_descriptions_egress)
        """

    def update_security_group_rule_descriptions_ingress(
        self,
        *,
        DryRun: bool = None,
        GroupId: str = None,
        GroupName: str = None,
        IpPermissions: List["IpPermissionTypeDef"] = None,
        SecurityGroupRuleDescriptions: List["SecurityGroupRuleDescriptionTypeDef"] = None
    ) -> UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef:
        """
        Updates the description of an ingress (inbound) security group rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.update_security_group_rule_descriptions_ingress)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#update_security_group_rule_descriptions_ingress)
        """

    def withdraw_byoip_cidr(
        self, *, Cidr: str, DryRun: bool = None
    ) -> WithdrawByoipCidrResultTypeDef:
        """
        Stops advertising an address range that is provisioned as an address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Client.withdraw_byoip_cidr)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/client.html#withdraw_byoip_cidr)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_address_transfers"]
    ) -> DescribeAddressTransfersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeAddressTransfers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeaddresstransferspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_addresses_attribute"]
    ) -> DescribeAddressesAttributePaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeAddressesAttribute)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeaddressesattributepaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_aws_network_performance_metric_subscriptions"]
    ) -> DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeAwsNetworkPerformanceMetricSubscriptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeawsnetworkperformancemetricsubscriptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_byoip_cidrs"]
    ) -> DescribeByoipCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describebyoipcidrspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_capacity_block_offerings"]
    ) -> DescribeCapacityBlockOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeCapacityBlockOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityblockofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_capacity_reservation_fleets"]
    ) -> DescribeCapacityReservationFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservationFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityreservationfleetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_capacity_reservations"]
    ) -> DescribeCapacityReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityreservationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_carrier_gateways"]
    ) -> DescribeCarrierGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeCarrierGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecarriergatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_classic_link_instances"]
    ) -> DescribeClassicLinkInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclassiclinkinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_authorization_rules"]
    ) -> DescribeClientVpnAuthorizationRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnauthorizationrulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_connections"]
    ) -> DescribeClientVpnConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnconnectionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_endpoints"]
    ) -> DescribeClientVpnEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_routes"]
    ) -> DescribeClientVpnRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnroutespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_client_vpn_target_networks"]
    ) -> DescribeClientVpnTargetNetworksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpntargetnetworkspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_coip_pools"]
    ) -> DescribeCoipPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeCoipPools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecoippoolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_dhcp_options"]
    ) -> DescribeDhcpOptionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describedhcpoptionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_egress_only_internet_gateways"]
    ) -> DescribeEgressOnlyInternetGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeegressonlyinternetgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_export_image_tasks"]
    ) -> DescribeExportImageTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeexportimagetaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fast_launch_images"]
    ) -> DescribeFastLaunchImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeFastLaunchImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefastlaunchimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fast_snapshot_restores"]
    ) -> DescribeFastSnapshotRestoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefastsnapshotrestorespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_fleets"]) -> DescribeFleetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeFleets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefleetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_flow_logs"]
    ) -> DescribeFlowLogsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeflowlogspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_fpga_images"]
    ) -> DescribeFpgaImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefpgaimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_host_reservation_offerings"]
    ) -> DescribeHostReservationOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostreservationofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_host_reservations"]
    ) -> DescribeHostReservationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostreservationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_hosts"]) -> DescribeHostsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeHosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_iam_instance_profile_associations"]
    ) -> DescribeIamInstanceProfileAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeiaminstanceprofileassociationspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_images"]) -> DescribeImagesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeImages)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimagespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_import_image_tasks"]
    ) -> DescribeImportImageTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimportimagetaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_import_snapshot_tasks"]
    ) -> DescribeImportSnapshotTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimportsnapshottaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_connect_endpoints"]
    ) -> DescribeInstanceConnectEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeInstanceConnectEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstanceconnectendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_credit_specifications"]
    ) -> DescribeInstanceCreditSpecificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancecreditspecificationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_event_windows"]
    ) -> DescribeInstanceEventWindowsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeInstanceEventWindows)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstanceeventwindowspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_status"]
    ) -> DescribeInstanceStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancestatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_topology"]
    ) -> DescribeInstanceTopologyPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTopology)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetopologypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_type_offerings"]
    ) -> DescribeInstanceTypeOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypeOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetypeofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instance_types"]
    ) -> DescribeInstanceTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_instances"]
    ) -> DescribeInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_internet_gateways"]
    ) -> DescribeInternetGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinternetgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipam_pools"]
    ) -> DescribeIpamPoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeIpamPools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipampoolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipam_resource_discoveries"]
    ) -> DescribeIpamResourceDiscoveriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeIpamResourceDiscoveries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamresourcediscoveriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipam_resource_discovery_associations"]
    ) -> DescribeIpamResourceDiscoveryAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeIpamResourceDiscoveryAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamresourcediscoveryassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipam_scopes"]
    ) -> DescribeIpamScopesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeIpamScopes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamscopespaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_ipams"]) -> DescribeIpamsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeIpams)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_ipv6_pools"]
    ) -> DescribeIpv6PoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeIpv6Pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipv6poolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_template_versions"]
    ) -> DescribeLaunchTemplateVersionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelaunchtemplateversionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_launch_templates"]
    ) -> DescribeLaunchTemplatesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelaunchtemplatespaginator)
        """

    @overload
    def get_paginator(
        self,
        operation_name: Literal[
            "describe_local_gateway_route_table_virtual_interface_group_associations"
        ],
    ) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablevirtualinterfacegroupassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_route_table_vpc_associations"]
    ) -> DescribeLocalGatewayRouteTableVpcAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablevpcassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_route_tables"]
    ) -> DescribeLocalGatewayRouteTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_virtual_interface_groups"]
    ) -> DescribeLocalGatewayVirtualInterfaceGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayvirtualinterfacegroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateway_virtual_interfaces"]
    ) -> DescribeLocalGatewayVirtualInterfacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayvirtualinterfacespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_local_gateways"]
    ) -> DescribeLocalGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeLocalGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_mac_hosts"]
    ) -> DescribeMacHostsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeMacHosts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describemachostspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_managed_prefix_lists"]
    ) -> DescribeManagedPrefixListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeManagedPrefixLists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describemanagedprefixlistspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_moving_addresses"]
    ) -> DescribeMovingAddressesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describemovingaddressespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_nat_gateways"]
    ) -> DescribeNatGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenatgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_acls"]
    ) -> DescribeNetworkAclsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkaclspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_access_scope_analyses"]
    ) -> DescribeNetworkInsightsAccessScopeAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAccessScopeAnalyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsaccessscopeanalysespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_access_scopes"]
    ) -> DescribeNetworkInsightsAccessScopesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAccessScopes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsaccessscopespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_analyses"]
    ) -> DescribeNetworkInsightsAnalysesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAnalyses)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsanalysespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_insights_paths"]
    ) -> DescribeNetworkInsightsPathsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsPaths)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightspathspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_interface_permissions"]
    ) -> DescribeNetworkInterfacePermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinterfacepermissionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_network_interfaces"]
    ) -> DescribeNetworkInterfacesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinterfacespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_prefix_lists"]
    ) -> DescribePrefixListsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeprefixlistspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_principal_id_format"]
    ) -> DescribePrincipalIdFormatPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeprincipalidformatpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_public_ipv4_pools"]
    ) -> DescribePublicIpv4PoolsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describepublicipv4poolspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_replace_root_volume_tasks"]
    ) -> DescribeReplaceRootVolumeTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeReplaceRootVolumeTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereplacerootvolumetaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_modifications"]
    ) -> DescribeReservedInstancesModificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereservedinstancesmodificationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_reserved_instances_offerings"]
    ) -> DescribeReservedInstancesOfferingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereservedinstancesofferingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_route_tables"]
    ) -> DescribeRouteTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeroutetablespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instance_availability"]
    ) -> DescribeScheduledInstanceAvailabilityPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describescheduledinstanceavailabilitypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_scheduled_instances"]
    ) -> DescribeScheduledInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describescheduledinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_security_group_rules"]
    ) -> DescribeSecurityGroupRulesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroupRules)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesecuritygrouprulespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_security_groups"]
    ) -> DescribeSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesecuritygroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshot_tier_status"]
    ) -> DescribeSnapshotTierStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeSnapshotTierStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesnapshottierstatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesnapshotspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_instances"]
    ) -> DescribeSpotFleetInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotfleetinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_fleet_requests"]
    ) -> DescribeSpotFleetRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotfleetrequestspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_instance_requests"]
    ) -> DescribeSpotInstanceRequestsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotinstancerequestspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_spot_price_history"]
    ) -> DescribeSpotPriceHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotpricehistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_stale_security_groups"]
    ) -> DescribeStaleSecurityGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describestalesecuritygroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_store_image_tasks"]
    ) -> DescribeStoreImageTasksPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeStoreImageTasks)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describestoreimagetaskspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_subnets"]
    ) -> DescribeSubnetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeSubnets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesubnetspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_tags"]) -> DescribeTagsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTags)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetagspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_filters"]
    ) -> DescribeTrafficMirrorFiltersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrorfilterspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_sessions"]
    ) -> DescribeTrafficMirrorSessionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrorsessionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_traffic_mirror_targets"]
    ) -> DescribeTrafficMirrorTargetsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrortargetspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_attachments"]
    ) -> DescribeTransitGatewayAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_connect_peers"]
    ) -> DescribeTransitGatewayConnectPeersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnectPeers)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayconnectpeerspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_connects"]
    ) -> DescribeTransitGatewayConnectsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnects)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayconnectspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_multicast_domains"]
    ) -> DescribeTransitGatewayMulticastDomainsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayMulticastDomains)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaymulticastdomainspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_peering_attachments"]
    ) -> DescribeTransitGatewayPeeringAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPeeringAttachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaypeeringattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_policy_tables"]
    ) -> DescribeTransitGatewayPolicyTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPolicyTables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaypolicytablespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_route_table_announcements"]
    ) -> DescribeTransitGatewayRouteTableAnnouncementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTableAnnouncements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayroutetableannouncementspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_route_tables"]
    ) -> DescribeTransitGatewayRouteTablesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayroutetablespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateway_vpc_attachments"]
    ) -> DescribeTransitGatewayVpcAttachmentsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayvpcattachmentspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_transit_gateways"]
    ) -> DescribeTransitGatewaysPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_trunk_interface_associations"]
    ) -> DescribeTrunkInterfaceAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeTrunkInterfaceAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrunkinterfaceassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_endpoints"]
    ) -> DescribeVerifiedAccessEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_groups"]
    ) -> DescribeVerifiedAccessGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessgroupspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_instance_logging_configurations"]
    ) -> DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessInstanceLoggingConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessinstanceloggingconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_instances"]
    ) -> DescribeVerifiedAccessInstancesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessInstances)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessinstancespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_verified_access_trust_providers"]
    ) -> DescribeVerifiedAccessTrustProvidersPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessTrustProviders)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccesstrustproviderspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volume_status"]
    ) -> DescribeVolumeStatusPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumestatuspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volumes"]
    ) -> DescribeVolumesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVolumes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_volumes_modifications"]
    ) -> DescribeVolumesModificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumesmodificationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_classic_link_dns_support"]
    ) -> DescribeVpcClassicLinkDnsSupportPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcclassiclinkdnssupportpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connection_notifications"]
    ) -> DescribeVpcEndpointConnectionNotificationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointconnectionnotificationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_connections"]
    ) -> DescribeVpcEndpointConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointconnectionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_configurations"]
    ) -> DescribeVpcEndpointServiceConfigurationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointserviceconfigurationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_service_permissions"]
    ) -> DescribeVpcEndpointServicePermissionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointservicepermissionspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoint_services"]
    ) -> DescribeVpcEndpointServicesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointservicespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_endpoints"]
    ) -> DescribeVpcEndpointsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["describe_vpc_peering_connections"]
    ) -> DescribeVpcPeeringConnectionsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcpeeringconnectionspaginator)
        """

    @overload
    def get_paginator(self, operation_name: Literal["describe_vpcs"]) -> DescribeVpcsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.DescribeVpcs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_associated_ipv6_pool_cidrs"]
    ) -> GetAssociatedIpv6PoolCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getassociatedipv6poolcidrspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_aws_network_performance_data"]
    ) -> GetAwsNetworkPerformanceDataPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetAwsNetworkPerformanceData)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getawsnetworkperformancedatapaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_groups_for_capacity_reservation"]
    ) -> GetGroupsForCapacityReservationPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetGroupsForCapacityReservation)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getgroupsforcapacityreservationpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_instance_types_from_instance_requirements"]
    ) -> GetInstanceTypesFromInstanceRequirementsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetInstanceTypesFromInstanceRequirements)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getinstancetypesfrominstancerequirementspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_address_history"]
    ) -> GetIpamAddressHistoryPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetIpamAddressHistory)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamaddresshistorypaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_discovered_accounts"]
    ) -> GetIpamDiscoveredAccountsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetIpamDiscoveredAccounts)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamdiscoveredaccountspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_discovered_resource_cidrs"]
    ) -> GetIpamDiscoveredResourceCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetIpamDiscoveredResourceCidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamdiscoveredresourcecidrspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_pool_allocations"]
    ) -> GetIpamPoolAllocationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetIpamPoolAllocations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipampoolallocationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_pool_cidrs"]
    ) -> GetIpamPoolCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetIpamPoolCidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipampoolcidrspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_ipam_resource_cidrs"]
    ) -> GetIpamResourceCidrsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetIpamResourceCidrs)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamresourcecidrspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_managed_prefix_list_associations"]
    ) -> GetManagedPrefixListAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getmanagedprefixlistassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_managed_prefix_list_entries"]
    ) -> GetManagedPrefixListEntriesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListEntries)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getmanagedprefixlistentriespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_network_insights_access_scope_analysis_findings"]
    ) -> GetNetworkInsightsAccessScopeAnalysisFindingsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetNetworkInsightsAccessScopeAnalysisFindings)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getnetworkinsightsaccessscopeanalysisfindingspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_security_groups_for_vpc"]
    ) -> GetSecurityGroupsForVpcPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetSecurityGroupsForVpc)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getsecuritygroupsforvpcpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_spot_placement_scores"]
    ) -> GetSpotPlacementScoresPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetSpotPlacementScores)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getspotplacementscorespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_attachment_propagations"]
    ) -> GetTransitGatewayAttachmentPropagationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayattachmentpropagationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_multicast_domain_associations"]
    ) -> GetTransitGatewayMulticastDomainAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayMulticastDomainAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewaymulticastdomainassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_policy_table_associations"]
    ) -> GetTransitGatewayPolicyTableAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayPolicyTableAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewaypolicytableassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_prefix_list_references"]
    ) -> GetTransitGatewayPrefixListReferencesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayPrefixListReferences)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayprefixlistreferencespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_associations"]
    ) -> GetTransitGatewayRouteTableAssociationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayroutetableassociationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_transit_gateway_route_table_propagations"]
    ) -> GetTransitGatewayRouteTablePropagationsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayroutetablepropagationspaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["get_vpn_connection_device_types"]
    ) -> GetVpnConnectionDeviceTypesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.GetVpnConnectionDeviceTypes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getvpnconnectiondevicetypespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_images_in_recycle_bin"]
    ) -> ListImagesInRecycleBinPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.ListImagesInRecycleBin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#listimagesinrecyclebinpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["list_snapshots_in_recycle_bin"]
    ) -> ListSnapshotsInRecycleBinPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.ListSnapshotsInRecycleBin)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#listsnapshotsinrecyclebinpaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_local_gateway_routes"]
    ) -> SearchLocalGatewayRoutesPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.SearchLocalGatewayRoutes)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#searchlocalgatewayroutespaginator)
        """

    @overload
    def get_paginator(
        self, operation_name: Literal["search_transit_gateway_multicast_groups"]
    ) -> SearchTransitGatewayMulticastGroupsPaginator:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Paginator.SearchTransitGatewayMulticastGroups)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#searchtransitgatewaymulticastgroupspaginator)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["bundle_task_complete"]) -> BundleTaskCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.BundleTaskComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#bundletaskcompletewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_cancelled"]
    ) -> ConversionTaskCancelledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.ConversionTaskCancelled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#conversiontaskcancelledwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_completed"]
    ) -> ConversionTaskCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.ConversionTaskCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#conversiontaskcompletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["conversion_task_deleted"]
    ) -> ConversionTaskDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.ConversionTaskDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#conversiontaskdeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["customer_gateway_available"]
    ) -> CustomerGatewayAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.CustomerGatewayAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#customergatewayavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["export_task_cancelled"]
    ) -> ExportTaskCancelledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.ExportTaskCancelled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#exporttaskcancelledwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["export_task_completed"]
    ) -> ExportTaskCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.ExportTaskCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#exporttaskcompletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_available"]) -> ImageAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.ImageAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#imageavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["image_exists"]) -> ImageExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.ImageExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#imageexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_exists"]) -> InstanceExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.InstanceExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instanceexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_running"]) -> InstanceRunningWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.InstanceRunning)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instancerunningwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_status_ok"]) -> InstanceStatusOkWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.InstanceStatusOk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instancestatusokwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_stopped"]) -> InstanceStoppedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.InstanceStopped)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instancestoppedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["instance_terminated"]) -> InstanceTerminatedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.InstanceTerminated)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#instanceterminatedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["internet_gateway_exists"]
    ) -> InternetGatewayExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.InternetGatewayExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#internetgatewayexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["key_pair_exists"]) -> KeyPairExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.KeyPairExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#keypairexistswaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["nat_gateway_available"]
    ) -> NatGatewayAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.NatGatewayAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#natgatewayavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["nat_gateway_deleted"]) -> NatGatewayDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.NatGatewayDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#natgatewaydeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["network_interface_available"]
    ) -> NetworkInterfaceAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.NetworkInterfaceAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#networkinterfaceavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["password_data_available"]
    ) -> PasswordDataAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.PasswordDataAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#passworddataavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["security_group_exists"]
    ) -> SecurityGroupExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.SecurityGroupExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#securitygroupexistswaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["snapshot_completed"]) -> SnapshotCompletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.SnapshotCompleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#snapshotcompletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["snapshot_imported"]) -> SnapshotImportedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.SnapshotImported)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#snapshotimportedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["spot_instance_request_fulfilled"]
    ) -> SpotInstanceRequestFulfilledWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.SpotInstanceRequestFulfilled)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#spotinstancerequestfulfilledwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["store_image_task_complete"]
    ) -> StoreImageTaskCompleteWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.StoreImageTaskComplete)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#storeimagetaskcompletewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["subnet_available"]) -> SubnetAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.SubnetAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#subnetavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["system_status_ok"]) -> SystemStatusOkWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.SystemStatusOk)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#systemstatusokwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_available"]) -> VolumeAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.VolumeAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#volumeavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_deleted"]) -> VolumeDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.VolumeDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#volumedeletedwaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["volume_in_use"]) -> VolumeInUseWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.VolumeInUse)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#volumeinusewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vpc_available"]) -> VpcAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.VpcAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpcavailablewaiter)
        """

    @overload
    def get_waiter(self, waiter_name: Literal["vpc_exists"]) -> VpcExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.VpcExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpcexistswaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_deleted"]
    ) -> VpcPeeringConnectionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpcpeeringconnectiondeletedwaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpc_peering_connection_exists"]
    ) -> VpcPeeringConnectionExistsWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.VpcPeeringConnectionExists)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpcpeeringconnectionexistswaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_available"]
    ) -> VpnConnectionAvailableWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.VpnConnectionAvailable)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpnconnectionavailablewaiter)
        """

    @overload
    def get_waiter(
        self, waiter_name: Literal["vpn_connection_deleted"]
    ) -> VpnConnectionDeletedWaiter:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.34.138/reference/services/ec2.html#EC2.Waiter.VpnConnectionDeleted)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/waiters.html#vpnconnectiondeletedwaiter)
        """
