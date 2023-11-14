"""
Type annotations for ec2 service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/type_defs.html)

Usage::

    ```python
    from mypy_boto3_ec2.type_defs import AcceleratorCountRequestTypeDef

    data: AcceleratorCountRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import IO, Any, Dict, List, Optional, Union

from botocore.response import StreamingBody

from .literals import (
    AcceleratorManufacturerType,
    AcceleratorNameType,
    AcceleratorTypeType,
    AccountAttributeNameType,
    ActivityStatusType,
    AddressFamilyType,
    AddressTransferStatusType,
    AffinityType,
    AllocationStateType,
    AllocationStrategyType,
    AllowsMultipleInstanceTypesType,
    AmdSevSnpSpecificationType,
    AnalysisStatusType,
    ApplianceModeSupportValueType,
    ArchitectureTypeType,
    ArchitectureValuesType,
    AssociationStatusCodeType,
    AttachmentStatusType,
    AutoAcceptSharedAssociationsValueType,
    AutoAcceptSharedAttachmentsValueType,
    AutoPlacementType,
    AvailabilityZoneOptInStatusType,
    AvailabilityZoneStateType,
    BareMetalType,
    BatchStateType,
    BgpStatusType,
    BootModeTypeType,
    BootModeValuesType,
    BundleTaskStateType,
    BurstablePerformanceType,
    ByoipCidrStateType,
    CancelBatchErrorCodeType,
    CancelSpotInstanceRequestStateType,
    CapacityReservationFleetStateType,
    CapacityReservationInstancePlatformType,
    CapacityReservationPreferenceType,
    CapacityReservationStateType,
    CapacityReservationTenancyType,
    CapacityReservationTypeType,
    CarrierGatewayStateType,
    ClientCertificateRevocationListStatusCodeType,
    ClientVpnAuthenticationTypeType,
    ClientVpnAuthorizationRuleStatusCodeType,
    ClientVpnConnectionStatusCodeType,
    ClientVpnEndpointAttributeStatusCodeType,
    ClientVpnEndpointStatusCodeType,
    ClientVpnRouteStatusCodeType,
    ConnectionNotificationStateType,
    ConnectivityTypeType,
    ConversionTaskStateType,
    CpuManufacturerType,
    DatafeedSubscriptionStateType,
    DefaultRouteTableAssociationValueType,
    DefaultRouteTablePropagationValueType,
    DefaultTargetCapacityTypeType,
    DeleteFleetErrorCodeType,
    DeleteQueuedReservedInstancesErrorCodeType,
    DestinationFileFormatType,
    DeviceTrustProviderTypeType,
    DeviceTypeType,
    DiskImageFormatType,
    DiskTypeType,
    DnsNameStateType,
    DnsRecordIpTypeType,
    DnsSupportValueType,
    DomainTypeType,
    DynamicRoutingValueType,
    EbsEncryptionSupportType,
    EbsNvmeSupportType,
    EbsOptimizedSupportType,
    Ec2InstanceConnectEndpointStateType,
    ElasticGpuStatusType,
    EnaSupportType,
    EndDateTypeType,
    EphemeralNvmeSupportType,
    EventCodeType,
    EventTypeType,
    ExcessCapacityTerminationPolicyType,
    ExportEnvironmentType,
    ExportTaskStateType,
    FastLaunchStateCodeType,
    FastSnapshotRestoreStateCodeType,
    FindingsFoundType,
    FleetActivityStatusType,
    FleetEventTypeType,
    FleetExcessCapacityTerminationPolicyType,
    FleetOnDemandAllocationStrategyType,
    FleetReplacementStrategyType,
    FleetStateCodeType,
    FleetTypeType,
    FlowLogsResourceTypeType,
    FpgaImageAttributeNameType,
    FpgaImageStateCodeType,
    GatewayAssociationStateType,
    HostMaintenanceType,
    HostnameTypeType,
    HostRecoveryType,
    HostTenancyType,
    HttpTokensStateType,
    HypervisorTypeType,
    IamInstanceProfileAssociationStateType,
    Igmpv2SupportValueType,
    ImageAttributeNameType,
    ImageStateType,
    ImageTypeValuesType,
    InstanceAttributeNameType,
    InstanceAutoRecoveryStateType,
    InstanceBootModeValuesType,
    InstanceEventWindowStateType,
    InstanceGenerationType,
    InstanceHealthStatusType,
    InstanceInterruptionBehaviorType,
    InstanceLifecycleType,
    InstanceLifecycleTypeType,
    InstanceMatchCriteriaType,
    InstanceMetadataEndpointStateType,
    InstanceMetadataOptionsStateType,
    InstanceMetadataProtocolStateType,
    InstanceMetadataTagsStateType,
    InstanceStateNameType,
    InstanceStorageEncryptionSupportType,
    InstanceTypeHypervisorType,
    InstanceTypeType,
    InterfacePermissionTypeType,
    InterfaceProtocolTypeType,
    IpAddressTypeType,
    IpamAddressHistoryResourceTypeType,
    IpamAssociatedResourceDiscoveryStatusType,
    IpamComplianceStatusType,
    IpamDiscoveryFailureCodeType,
    IpamManagementStateType,
    IpamOverlapStatusType,
    IpamPoolAllocationResourceTypeType,
    IpamPoolCidrFailureCodeType,
    IpamPoolCidrStateType,
    IpamPoolPublicIpSourceType,
    IpamPoolStateType,
    IpamResourceDiscoveryAssociationStateType,
    IpamResourceDiscoveryStateType,
    IpamResourceTypeType,
    IpamScopeStateType,
    IpamScopeTypeType,
    IpamStateType,
    Ipv6SupportValueType,
    KeyFormatType,
    KeyTypeType,
    LaunchTemplateAutoRecoveryStateType,
    LaunchTemplateErrorCodeType,
    LaunchTemplateHttpTokensStateType,
    LaunchTemplateInstanceMetadataEndpointStateType,
    LaunchTemplateInstanceMetadataOptionsStateType,
    LaunchTemplateInstanceMetadataProtocolIpv6Type,
    LaunchTemplateInstanceMetadataTagsStateType,
    ListingStateType,
    ListingStatusType,
    LocalGatewayRouteStateType,
    LocalGatewayRouteTableModeType,
    LocalGatewayRouteTypeType,
    LocalStorageType,
    LocalStorageTypeType,
    LocationTypeType,
    LogDestinationTypeType,
    MarketTypeType,
    MembershipTypeType,
    ModifyAvailabilityZoneOptInStatusType,
    MonitoringStateType,
    MoveStatusType,
    MulticastSupportValueType,
    NatGatewayAddressStatusType,
    NatGatewayStateType,
    NetworkInterfaceAttributeType,
    NetworkInterfaceCreationTypeType,
    NetworkInterfacePermissionStateCodeType,
    NetworkInterfaceStatusType,
    NetworkInterfaceTypeType,
    NitroEnclavesSupportType,
    NitroTpmSupportType,
    OfferingClassTypeType,
    OfferingTypeValuesType,
    OnDemandAllocationStrategyType,
    OperationTypeType,
    PartitionLoadFrequencyType,
    PaymentOptionType,
    PeriodTypeType,
    PlacementGroupStateType,
    PlacementGroupStrategyType,
    PlacementStrategyType,
    PrefixListStateType,
    PrincipalTypeType,
    ProductCodeValuesType,
    ProtocolType,
    ReplacementStrategyType,
    ReplaceRootVolumeTaskStateType,
    ReportInstanceReasonCodesType,
    ReportStatusTypeType,
    ReservationStateType,
    ReservedInstanceStateType,
    ResourceTypeType,
    RIProductDescriptionType,
    RootDeviceTypeType,
    RouteOriginType,
    RouteStateType,
    RouteTableAssociationStateCodeType,
    RuleActionType,
    SelfServicePortalType,
    ServiceConnectivityTypeType,
    ServiceStateType,
    ServiceTypeType,
    ShutdownBehaviorType,
    SnapshotAttributeNameType,
    SnapshotBlockPublicAccessStateType,
    SnapshotStateType,
    SpotAllocationStrategyType,
    SpotInstanceInterruptionBehaviorType,
    SpotInstanceStateType,
    SpotInstanceTypeType,
    SpreadLevelType,
    SSETypeType,
    StateType,
    StaticSourcesSupportValueType,
    StatusType,
    StatusTypeType,
    StorageTierType,
    SubnetCidrBlockStateCodeType,
    SubnetCidrReservationTypeType,
    SubnetStateType,
    SummaryStatusType,
    TargetCapacityUnitTypeType,
    TelemetryStatusType,
    TenancyType,
    TieringOperationStatusType,
    TrafficDirectionType,
    TrafficMirrorFilterRuleFieldType,
    TrafficMirrorRuleActionType,
    TrafficMirrorSessionFieldType,
    TrafficMirrorTargetTypeType,
    TrafficTypeType,
    TransitGatewayAssociationStateType,
    TransitGatewayAttachmentResourceTypeType,
    TransitGatewayAttachmentStateType,
    TransitGatewayConnectPeerStateType,
    TransitGatewayMulitcastDomainAssociationStateType,
    TransitGatewayMulticastDomainStateType,
    TransitGatewayPolicyTableStateType,
    TransitGatewayPrefixListReferenceStateType,
    TransitGatewayPropagationStateType,
    TransitGatewayRouteStateType,
    TransitGatewayRouteTableAnnouncementDirectionType,
    TransitGatewayRouteTableAnnouncementStateType,
    TransitGatewayRouteTableStateType,
    TransitGatewayRouteTypeType,
    TransitGatewayStateType,
    TransportProtocolType,
    TrustProviderTypeType,
    TunnelInsideIpVersionType,
    UnlimitedSupportedInstanceFamilyType,
    UnsuccessfulInstanceCreditSpecificationErrorCodeType,
    UsageClassTypeType,
    UserTrustProviderTypeType,
    VerifiedAccessEndpointProtocolType,
    VerifiedAccessEndpointStatusCodeType,
    VerifiedAccessEndpointTypeType,
    VerifiedAccessLogDeliveryStatusCodeType,
    VirtualizationTypeType,
    VolumeAttachmentStateType,
    VolumeAttributeNameType,
    VolumeModificationStateType,
    VolumeStateType,
    VolumeStatusInfoStatusType,
    VolumeStatusNameType,
    VolumeTypeType,
    VpcAttributeNameType,
    VpcCidrBlockStateCodeType,
    VpcEndpointTypeType,
    VpcPeeringConnectionStateReasonCodeType,
    VpcStateType,
    VpnEcmpSupportValueType,
    VpnStateType,
    WeekDayType,
    scopeType,
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
    "AcceleratorCountRequestTypeDef",
    "AcceleratorCountTypeDef",
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    "AcceleratorTotalMemoryMiBTypeDef",
    "AcceptAddressTransferRequestRequestTypeDef",
    "AcceptAddressTransferResultTypeDef",
    "AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef",
    "AcceptReservedInstancesExchangeQuoteResultTypeDef",
    "AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    "AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    "AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "AcceptTransitGatewayVpcAttachmentResultTypeDef",
    "AcceptVpcEndpointConnectionsRequestRequestTypeDef",
    "AcceptVpcEndpointConnectionsResultTypeDef",
    "AcceptVpcPeeringConnectionRequestRequestTypeDef",
    "AcceptVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    "AcceptVpcPeeringConnectionResultTypeDef",
    "AccessScopeAnalysisFindingTypeDef",
    "AccessScopePathRequestTypeDef",
    "AccessScopePathTypeDef",
    "AccountAttributeTypeDef",
    "AccountAttributeValueTypeDef",
    "ActiveInstanceTypeDef",
    "AddIpamOperatingRegionTypeDef",
    "AddPrefixListEntryTypeDef",
    "AddedPrincipalTypeDef",
    "AdditionalDetailTypeDef",
    "AddressAttributeTypeDef",
    "AddressTransferTypeDef",
    "AddressTypeDef",
    "AdvertiseByoipCidrRequestRequestTypeDef",
    "AdvertiseByoipCidrResultTypeDef",
    "AllocateAddressRequestRequestTypeDef",
    "AllocateAddressResultTypeDef",
    "AllocateHostsRequestRequestTypeDef",
    "AllocateHostsResultTypeDef",
    "AllocateIpamPoolCidrRequestRequestTypeDef",
    "AllocateIpamPoolCidrResultTypeDef",
    "AllowedPrincipalTypeDef",
    "AlternatePathHintTypeDef",
    "AnalysisAclRuleTypeDef",
    "AnalysisComponentTypeDef",
    "AnalysisLoadBalancerListenerTypeDef",
    "AnalysisLoadBalancerTargetTypeDef",
    "AnalysisPacketHeaderTypeDef",
    "AnalysisRouteTableRouteTypeDef",
    "AnalysisSecurityGroupRuleTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef",
    "ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    "AssignIpv6AddressesRequestRequestTypeDef",
    "AssignIpv6AddressesResultTypeDef",
    "AssignPrivateIpAddressesRequestNetworkInterfaceTypeDef",
    "AssignPrivateIpAddressesRequestRequestTypeDef",
    "AssignPrivateIpAddressesResultTypeDef",
    "AssignPrivateNatGatewayAddressRequestRequestTypeDef",
    "AssignPrivateNatGatewayAddressResultTypeDef",
    "AssignedPrivateIpAddressTypeDef",
    "AssociateAddressRequestClassicAddressTypeDef",
    "AssociateAddressRequestRequestTypeDef",
    "AssociateAddressRequestVpcAddressTypeDef",
    "AssociateAddressResultTypeDef",
    "AssociateClientVpnTargetNetworkRequestRequestTypeDef",
    "AssociateClientVpnTargetNetworkResultTypeDef",
    "AssociateDhcpOptionsRequestDhcpOptionsTypeDef",
    "AssociateDhcpOptionsRequestRequestTypeDef",
    "AssociateDhcpOptionsRequestVpcTypeDef",
    "AssociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    "AssociateEnclaveCertificateIamRoleResultTypeDef",
    "AssociateIamInstanceProfileRequestRequestTypeDef",
    "AssociateIamInstanceProfileResultTypeDef",
    "AssociateInstanceEventWindowRequestRequestTypeDef",
    "AssociateInstanceEventWindowResultTypeDef",
    "AssociateIpamResourceDiscoveryRequestRequestTypeDef",
    "AssociateIpamResourceDiscoveryResultTypeDef",
    "AssociateNatGatewayAddressRequestRequestTypeDef",
    "AssociateNatGatewayAddressResultTypeDef",
    "AssociateRouteTableRequestRequestTypeDef",
    "AssociateRouteTableRequestRouteTableTypeDef",
    "AssociateRouteTableResultTypeDef",
    "AssociateSubnetCidrBlockRequestRequestTypeDef",
    "AssociateSubnetCidrBlockResultTypeDef",
    "AssociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    "AssociateTransitGatewayMulticastDomainResultTypeDef",
    "AssociateTransitGatewayPolicyTableRequestRequestTypeDef",
    "AssociateTransitGatewayPolicyTableResultTypeDef",
    "AssociateTransitGatewayRouteTableRequestRequestTypeDef",
    "AssociateTransitGatewayRouteTableResultTypeDef",
    "AssociateTrunkInterfaceRequestRequestTypeDef",
    "AssociateTrunkInterfaceResultTypeDef",
    "AssociateVpcCidrBlockRequestRequestTypeDef",
    "AssociateVpcCidrBlockResultTypeDef",
    "AssociatedRoleTypeDef",
    "AssociatedTargetNetworkTypeDef",
    "AssociationStatusTypeDef",
    "AthenaIntegrationTypeDef",
    "AttachClassicLinkVpcRequestInstanceTypeDef",
    "AttachClassicLinkVpcRequestRequestTypeDef",
    "AttachClassicLinkVpcRequestVpcTypeDef",
    "AttachClassicLinkVpcResultTypeDef",
    "AttachInternetGatewayRequestInternetGatewayTypeDef",
    "AttachInternetGatewayRequestRequestTypeDef",
    "AttachInternetGatewayRequestVpcTypeDef",
    "AttachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    "AttachNetworkInterfaceRequestRequestTypeDef",
    "AttachNetworkInterfaceResultTypeDef",
    "AttachVerifiedAccessTrustProviderRequestRequestTypeDef",
    "AttachVerifiedAccessTrustProviderResultTypeDef",
    "AttachVolumeRequestInstanceTypeDef",
    "AttachVolumeRequestRequestTypeDef",
    "AttachVolumeRequestVolumeTypeDef",
    "AttachVpnGatewayRequestRequestTypeDef",
    "AttachVpnGatewayResultTypeDef",
    "AttachmentEnaSrdSpecificationTypeDef",
    "AttachmentEnaSrdUdpSpecificationTypeDef",
    "AttributeBooleanValueTypeDef",
    "AttributeValueTypeDef",
    "AuthorizationRuleTypeDef",
    "AuthorizeClientVpnIngressRequestRequestTypeDef",
    "AuthorizeClientVpnIngressResultTypeDef",
    "AuthorizeSecurityGroupEgressRequestRequestTypeDef",
    "AuthorizeSecurityGroupEgressRequestSecurityGroupTypeDef",
    "AuthorizeSecurityGroupEgressResultTypeDef",
    "AuthorizeSecurityGroupIngressRequestRequestTypeDef",
    "AuthorizeSecurityGroupIngressRequestSecurityGroupTypeDef",
    "AuthorizeSecurityGroupIngressResultTypeDef",
    "AvailabilityZoneMessageTypeDef",
    "AvailabilityZoneTypeDef",
    "AvailableCapacityTypeDef",
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    "BaselineEbsBandwidthMbpsTypeDef",
    "BlobAttributeValueTypeDef",
    "BlockDeviceMappingTypeDef",
    "BundleInstanceRequestRequestTypeDef",
    "BundleInstanceResultTypeDef",
    "BundleTaskErrorTypeDef",
    "BundleTaskTypeDef",
    "ByoipCidrTypeDef",
    "CancelBundleTaskRequestRequestTypeDef",
    "CancelBundleTaskResultTypeDef",
    "CancelCapacityReservationFleetErrorTypeDef",
    "CancelCapacityReservationFleetsRequestRequestTypeDef",
    "CancelCapacityReservationFleetsResultTypeDef",
    "CancelCapacityReservationRequestRequestTypeDef",
    "CancelCapacityReservationResultTypeDef",
    "CancelConversionRequestRequestTypeDef",
    "CancelExportTaskRequestRequestTypeDef",
    "CancelImageLaunchPermissionRequestRequestTypeDef",
    "CancelImageLaunchPermissionResultTypeDef",
    "CancelImportTaskRequestRequestTypeDef",
    "CancelImportTaskResultTypeDef",
    "CancelReservedInstancesListingRequestRequestTypeDef",
    "CancelReservedInstancesListingResultTypeDef",
    "CancelSpotFleetRequestsErrorItemTypeDef",
    "CancelSpotFleetRequestsErrorTypeDef",
    "CancelSpotFleetRequestsRequestRequestTypeDef",
    "CancelSpotFleetRequestsResponseTypeDef",
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    "CancelSpotInstanceRequestsRequestRequestTypeDef",
    "CancelSpotInstanceRequestsResultTypeDef",
    "CancelledSpotInstanceRequestTypeDef",
    "CapacityAllocationTypeDef",
    "CapacityBlockOfferingTypeDef",
    "CapacityReservationFleetCancellationStateTypeDef",
    "CapacityReservationFleetTypeDef",
    "CapacityReservationGroupTypeDef",
    "CapacityReservationOptionsRequestTypeDef",
    "CapacityReservationOptionsTypeDef",
    "CapacityReservationSpecificationResponseTypeDef",
    "CapacityReservationSpecificationTypeDef",
    "CapacityReservationTargetResponseTypeDef",
    "CapacityReservationTargetTypeDef",
    "CapacityReservationTypeDef",
    "CarrierGatewayTypeDef",
    "CertificateAuthenticationRequestTypeDef",
    "CertificateAuthenticationTypeDef",
    "CidrAuthorizationContextTypeDef",
    "CidrBlockTypeDef",
    "ClassicLinkDnsSupportTypeDef",
    "ClassicLinkInstanceTypeDef",
    "ClassicLoadBalancerTypeDef",
    "ClassicLoadBalancersConfigTypeDef",
    "ClientCertificateRevocationListStatusTypeDef",
    "ClientConnectOptionsTypeDef",
    "ClientConnectResponseOptionsTypeDef",
    "ClientDataTypeDef",
    "ClientLoginBannerOptionsTypeDef",
    "ClientLoginBannerResponseOptionsTypeDef",
    "ClientVpnAuthenticationRequestTypeDef",
    "ClientVpnAuthenticationTypeDef",
    "ClientVpnAuthorizationRuleStatusTypeDef",
    "ClientVpnConnectionStatusTypeDef",
    "ClientVpnConnectionTypeDef",
    "ClientVpnEndpointAttributeStatusTypeDef",
    "ClientVpnEndpointStatusTypeDef",
    "ClientVpnEndpointTypeDef",
    "ClientVpnRouteStatusTypeDef",
    "ClientVpnRouteTypeDef",
    "CloudWatchLogOptionsSpecificationTypeDef",
    "CloudWatchLogOptionsTypeDef",
    "CoipAddressUsageTypeDef",
    "CoipCidrTypeDef",
    "CoipPoolTypeDef",
    "ConfirmProductInstanceRequestRequestTypeDef",
    "ConfirmProductInstanceResultTypeDef",
    "ConnectionLogOptionsTypeDef",
    "ConnectionLogResponseOptionsTypeDef",
    "ConnectionNotificationTypeDef",
    "ConversionTaskTypeDef",
    "CopyFpgaImageRequestRequestTypeDef",
    "CopyFpgaImageResultTypeDef",
    "CopyImageRequestRequestTypeDef",
    "CopyImageResultTypeDef",
    "CopySnapshotRequestRequestTypeDef",
    "CopySnapshotRequestSnapshotTypeDef",
    "CopySnapshotResultTypeDef",
    "CpuOptionsRequestTypeDef",
    "CpuOptionsTypeDef",
    "CreateCapacityReservationFleetRequestRequestTypeDef",
    "CreateCapacityReservationFleetResultTypeDef",
    "CreateCapacityReservationRequestRequestTypeDef",
    "CreateCapacityReservationResultTypeDef",
    "CreateCarrierGatewayRequestRequestTypeDef",
    "CreateCarrierGatewayResultTypeDef",
    "CreateClientVpnEndpointRequestRequestTypeDef",
    "CreateClientVpnEndpointResultTypeDef",
    "CreateClientVpnRouteRequestRequestTypeDef",
    "CreateClientVpnRouteResultTypeDef",
    "CreateCoipCidrRequestRequestTypeDef",
    "CreateCoipCidrResultTypeDef",
    "CreateCoipPoolRequestRequestTypeDef",
    "CreateCoipPoolResultTypeDef",
    "CreateCustomerGatewayRequestRequestTypeDef",
    "CreateCustomerGatewayResultTypeDef",
    "CreateDefaultSubnetRequestRequestTypeDef",
    "CreateDefaultSubnetResultTypeDef",
    "CreateDefaultVpcRequestRequestTypeDef",
    "CreateDefaultVpcResultTypeDef",
    "CreateDhcpOptionsRequestRequestTypeDef",
    "CreateDhcpOptionsRequestServiceResourceTypeDef",
    "CreateDhcpOptionsResultTypeDef",
    "CreateEgressOnlyInternetGatewayRequestRequestTypeDef",
    "CreateEgressOnlyInternetGatewayResultTypeDef",
    "CreateFleetErrorTypeDef",
    "CreateFleetInstanceTypeDef",
    "CreateFleetRequestRequestTypeDef",
    "CreateFleetResultTypeDef",
    "CreateFlowLogsRequestRequestTypeDef",
    "CreateFlowLogsResultTypeDef",
    "CreateFpgaImageRequestRequestTypeDef",
    "CreateFpgaImageResultTypeDef",
    "CreateImageRequestInstanceTypeDef",
    "CreateImageRequestRequestTypeDef",
    "CreateImageResultTypeDef",
    "CreateInstanceConnectEndpointRequestRequestTypeDef",
    "CreateInstanceConnectEndpointResultTypeDef",
    "CreateInstanceEventWindowRequestRequestTypeDef",
    "CreateInstanceEventWindowResultTypeDef",
    "CreateInstanceExportTaskRequestRequestTypeDef",
    "CreateInstanceExportTaskResultTypeDef",
    "CreateInternetGatewayRequestRequestTypeDef",
    "CreateInternetGatewayRequestServiceResourceTypeDef",
    "CreateInternetGatewayResultTypeDef",
    "CreateIpamPoolRequestRequestTypeDef",
    "CreateIpamPoolResultTypeDef",
    "CreateIpamRequestRequestTypeDef",
    "CreateIpamResourceDiscoveryRequestRequestTypeDef",
    "CreateIpamResourceDiscoveryResultTypeDef",
    "CreateIpamResultTypeDef",
    "CreateIpamScopeRequestRequestTypeDef",
    "CreateIpamScopeResultTypeDef",
    "CreateKeyPairRequestRequestTypeDef",
    "CreateKeyPairRequestServiceResourceTypeDef",
    "CreateLaunchTemplateRequestRequestTypeDef",
    "CreateLaunchTemplateResultTypeDef",
    "CreateLaunchTemplateVersionRequestRequestTypeDef",
    "CreateLaunchTemplateVersionResultTypeDef",
    "CreateLocalGatewayRouteRequestRequestTypeDef",
    "CreateLocalGatewayRouteResultTypeDef",
    "CreateLocalGatewayRouteTableRequestRequestTypeDef",
    "CreateLocalGatewayRouteTableResultTypeDef",
    "CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    "CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    "CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "CreateManagedPrefixListRequestRequestTypeDef",
    "CreateManagedPrefixListResultTypeDef",
    "CreateNatGatewayRequestRequestTypeDef",
    "CreateNatGatewayResultTypeDef",
    "CreateNetworkAclEntryRequestNetworkAclTypeDef",
    "CreateNetworkAclEntryRequestRequestTypeDef",
    "CreateNetworkAclRequestRequestTypeDef",
    "CreateNetworkAclRequestServiceResourceTypeDef",
    "CreateNetworkAclRequestVpcTypeDef",
    "CreateNetworkAclResultTypeDef",
    "CreateNetworkInsightsAccessScopeRequestRequestTypeDef",
    "CreateNetworkInsightsAccessScopeResultTypeDef",
    "CreateNetworkInsightsPathRequestRequestTypeDef",
    "CreateNetworkInsightsPathResultTypeDef",
    "CreateNetworkInterfacePermissionRequestRequestTypeDef",
    "CreateNetworkInterfacePermissionResultTypeDef",
    "CreateNetworkInterfaceRequestRequestTypeDef",
    "CreateNetworkInterfaceRequestServiceResourceTypeDef",
    "CreateNetworkInterfaceRequestSubnetTypeDef",
    "CreateNetworkInterfaceResultTypeDef",
    "CreatePlacementGroupRequestRequestTypeDef",
    "CreatePlacementGroupRequestServiceResourceTypeDef",
    "CreatePlacementGroupResultTypeDef",
    "CreatePublicIpv4PoolRequestRequestTypeDef",
    "CreatePublicIpv4PoolResultTypeDef",
    "CreateReplaceRootVolumeTaskRequestRequestTypeDef",
    "CreateReplaceRootVolumeTaskResultTypeDef",
    "CreateReservedInstancesListingRequestRequestTypeDef",
    "CreateReservedInstancesListingResultTypeDef",
    "CreateRestoreImageTaskRequestRequestTypeDef",
    "CreateRestoreImageTaskResultTypeDef",
    "CreateRouteRequestRequestTypeDef",
    "CreateRouteRequestRouteTableTypeDef",
    "CreateRouteResultTypeDef",
    "CreateRouteTableRequestRequestTypeDef",
    "CreateRouteTableRequestServiceResourceTypeDef",
    "CreateRouteTableRequestVpcTypeDef",
    "CreateRouteTableResultTypeDef",
    "CreateSecurityGroupRequestRequestTypeDef",
    "CreateSecurityGroupRequestServiceResourceTypeDef",
    "CreateSecurityGroupRequestVpcTypeDef",
    "CreateSecurityGroupResultTypeDef",
    "CreateSnapshotRequestRequestTypeDef",
    "CreateSnapshotRequestServiceResourceTypeDef",
    "CreateSnapshotRequestVolumeTypeDef",
    "CreateSnapshotsRequestRequestTypeDef",
    "CreateSnapshotsResultTypeDef",
    "CreateSpotDatafeedSubscriptionRequestRequestTypeDef",
    "CreateSpotDatafeedSubscriptionResultTypeDef",
    "CreateStoreImageTaskRequestRequestTypeDef",
    "CreateStoreImageTaskResultTypeDef",
    "CreateSubnetCidrReservationRequestRequestTypeDef",
    "CreateSubnetCidrReservationResultTypeDef",
    "CreateSubnetRequestRequestTypeDef",
    "CreateSubnetRequestServiceResourceTypeDef",
    "CreateSubnetRequestVpcTypeDef",
    "CreateSubnetResultTypeDef",
    "CreateTagsRequestDhcpOptionsTypeDef",
    "CreateTagsRequestImageTypeDef",
    "CreateTagsRequestInstanceTypeDef",
    "CreateTagsRequestInternetGatewayTypeDef",
    "CreateTagsRequestNetworkAclTypeDef",
    "CreateTagsRequestNetworkInterfaceTypeDef",
    "CreateTagsRequestRequestTypeDef",
    "CreateTagsRequestRouteTableTypeDef",
    "CreateTagsRequestSecurityGroupTypeDef",
    "CreateTagsRequestServiceResourceTypeDef",
    "CreateTagsRequestSnapshotTypeDef",
    "CreateTagsRequestSubnetTypeDef",
    "CreateTagsRequestVolumeTypeDef",
    "CreateTagsRequestVpcTypeDef",
    "CreateTrafficMirrorFilterRequestRequestTypeDef",
    "CreateTrafficMirrorFilterResultTypeDef",
    "CreateTrafficMirrorFilterRuleRequestRequestTypeDef",
    "CreateTrafficMirrorFilterRuleResultTypeDef",
    "CreateTrafficMirrorSessionRequestRequestTypeDef",
    "CreateTrafficMirrorSessionResultTypeDef",
    "CreateTrafficMirrorTargetRequestRequestTypeDef",
    "CreateTrafficMirrorTargetResultTypeDef",
    "CreateTransitGatewayConnectPeerRequestRequestTypeDef",
    "CreateTransitGatewayConnectPeerResultTypeDef",
    "CreateTransitGatewayConnectRequestOptionsTypeDef",
    "CreateTransitGatewayConnectRequestRequestTypeDef",
    "CreateTransitGatewayConnectResultTypeDef",
    "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
    "CreateTransitGatewayMulticastDomainRequestRequestTypeDef",
    "CreateTransitGatewayMulticastDomainResultTypeDef",
    "CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef",
    "CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "CreateTransitGatewayPeeringAttachmentResultTypeDef",
    "CreateTransitGatewayPolicyTableRequestRequestTypeDef",
    "CreateTransitGatewayPolicyTableResultTypeDef",
    "CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    "CreateTransitGatewayPrefixListReferenceResultTypeDef",
    "CreateTransitGatewayRequestRequestTypeDef",
    "CreateTransitGatewayResultTypeDef",
    "CreateTransitGatewayRouteRequestRequestTypeDef",
    "CreateTransitGatewayRouteResultTypeDef",
    "CreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    "CreateTransitGatewayRouteTableAnnouncementResultTypeDef",
    "CreateTransitGatewayRouteTableRequestRequestTypeDef",
    "CreateTransitGatewayRouteTableResultTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "CreateTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "CreateTransitGatewayVpcAttachmentResultTypeDef",
    "CreateVerifiedAccessEndpointEniOptionsTypeDef",
    "CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    "CreateVerifiedAccessEndpointRequestRequestTypeDef",
    "CreateVerifiedAccessEndpointResultTypeDef",
    "CreateVerifiedAccessGroupRequestRequestTypeDef",
    "CreateVerifiedAccessGroupResultTypeDef",
    "CreateVerifiedAccessInstanceRequestRequestTypeDef",
    "CreateVerifiedAccessInstanceResultTypeDef",
    "CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef",
    "CreateVerifiedAccessTrustProviderOidcOptionsTypeDef",
    "CreateVerifiedAccessTrustProviderRequestRequestTypeDef",
    "CreateVerifiedAccessTrustProviderResultTypeDef",
    "CreateVolumePermissionModificationsTypeDef",
    "CreateVolumePermissionTypeDef",
    "CreateVolumeRequestRequestTypeDef",
    "CreateVolumeRequestServiceResourceTypeDef",
    "CreateVpcEndpointConnectionNotificationRequestRequestTypeDef",
    "CreateVpcEndpointConnectionNotificationResultTypeDef",
    "CreateVpcEndpointRequestRequestTypeDef",
    "CreateVpcEndpointResultTypeDef",
    "CreateVpcEndpointServiceConfigurationRequestRequestTypeDef",
    "CreateVpcEndpointServiceConfigurationResultTypeDef",
    "CreateVpcPeeringConnectionRequestRequestTypeDef",
    "CreateVpcPeeringConnectionRequestServiceResourceTypeDef",
    "CreateVpcPeeringConnectionRequestVpcTypeDef",
    "CreateVpcPeeringConnectionResultTypeDef",
    "CreateVpcRequestRequestTypeDef",
    "CreateVpcRequestServiceResourceTypeDef",
    "CreateVpcResultTypeDef",
    "CreateVpnConnectionRequestRequestTypeDef",
    "CreateVpnConnectionResultTypeDef",
    "CreateVpnConnectionRouteRequestRequestTypeDef",
    "CreateVpnGatewayRequestRequestTypeDef",
    "CreateVpnGatewayResultTypeDef",
    "CreditSpecificationRequestTypeDef",
    "CreditSpecificationTypeDef",
    "CustomerGatewayTypeDef",
    "DataQueryTypeDef",
    "DataResponseTypeDef",
    "DeleteCarrierGatewayRequestRequestTypeDef",
    "DeleteCarrierGatewayResultTypeDef",
    "DeleteClientVpnEndpointRequestRequestTypeDef",
    "DeleteClientVpnEndpointResultTypeDef",
    "DeleteClientVpnRouteRequestRequestTypeDef",
    "DeleteClientVpnRouteResultTypeDef",
    "DeleteCoipCidrRequestRequestTypeDef",
    "DeleteCoipCidrResultTypeDef",
    "DeleteCoipPoolRequestRequestTypeDef",
    "DeleteCoipPoolResultTypeDef",
    "DeleteCustomerGatewayRequestRequestTypeDef",
    "DeleteDhcpOptionsRequestDhcpOptionsTypeDef",
    "DeleteDhcpOptionsRequestRequestTypeDef",
    "DeleteEgressOnlyInternetGatewayRequestRequestTypeDef",
    "DeleteEgressOnlyInternetGatewayResultTypeDef",
    "DeleteFleetErrorItemTypeDef",
    "DeleteFleetErrorTypeDef",
    "DeleteFleetSuccessItemTypeDef",
    "DeleteFleetsRequestRequestTypeDef",
    "DeleteFleetsResultTypeDef",
    "DeleteFlowLogsRequestRequestTypeDef",
    "DeleteFlowLogsResultTypeDef",
    "DeleteFpgaImageRequestRequestTypeDef",
    "DeleteFpgaImageResultTypeDef",
    "DeleteInstanceConnectEndpointRequestRequestTypeDef",
    "DeleteInstanceConnectEndpointResultTypeDef",
    "DeleteInstanceEventWindowRequestRequestTypeDef",
    "DeleteInstanceEventWindowResultTypeDef",
    "DeleteInternetGatewayRequestInternetGatewayTypeDef",
    "DeleteInternetGatewayRequestRequestTypeDef",
    "DeleteIpamPoolRequestRequestTypeDef",
    "DeleteIpamPoolResultTypeDef",
    "DeleteIpamRequestRequestTypeDef",
    "DeleteIpamResourceDiscoveryRequestRequestTypeDef",
    "DeleteIpamResourceDiscoveryResultTypeDef",
    "DeleteIpamResultTypeDef",
    "DeleteIpamScopeRequestRequestTypeDef",
    "DeleteIpamScopeResultTypeDef",
    "DeleteKeyPairRequestKeyPairInfoTypeDef",
    "DeleteKeyPairRequestKeyPairTypeDef",
    "DeleteKeyPairRequestRequestTypeDef",
    "DeleteKeyPairResultTypeDef",
    "DeleteLaunchTemplateRequestRequestTypeDef",
    "DeleteLaunchTemplateResultTypeDef",
    "DeleteLaunchTemplateVersionsRequestRequestTypeDef",
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    "DeleteLaunchTemplateVersionsResultTypeDef",
    "DeleteLocalGatewayRouteRequestRequestTypeDef",
    "DeleteLocalGatewayRouteResultTypeDef",
    "DeleteLocalGatewayRouteTableRequestRequestTypeDef",
    "DeleteLocalGatewayRouteTableResultTypeDef",
    "DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    "DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    "DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    "DeleteManagedPrefixListRequestRequestTypeDef",
    "DeleteManagedPrefixListResultTypeDef",
    "DeleteNatGatewayRequestRequestTypeDef",
    "DeleteNatGatewayResultTypeDef",
    "DeleteNetworkAclEntryRequestNetworkAclTypeDef",
    "DeleteNetworkAclEntryRequestRequestTypeDef",
    "DeleteNetworkAclRequestNetworkAclTypeDef",
    "DeleteNetworkAclRequestRequestTypeDef",
    "DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    "DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef",
    "DeleteNetworkInsightsAccessScopeRequestRequestTypeDef",
    "DeleteNetworkInsightsAccessScopeResultTypeDef",
    "DeleteNetworkInsightsAnalysisRequestRequestTypeDef",
    "DeleteNetworkInsightsAnalysisResultTypeDef",
    "DeleteNetworkInsightsPathRequestRequestTypeDef",
    "DeleteNetworkInsightsPathResultTypeDef",
    "DeleteNetworkInterfacePermissionRequestRequestTypeDef",
    "DeleteNetworkInterfacePermissionResultTypeDef",
    "DeleteNetworkInterfaceRequestNetworkInterfaceTypeDef",
    "DeleteNetworkInterfaceRequestRequestTypeDef",
    "DeletePlacementGroupRequestPlacementGroupTypeDef",
    "DeletePlacementGroupRequestRequestTypeDef",
    "DeletePublicIpv4PoolRequestRequestTypeDef",
    "DeletePublicIpv4PoolResultTypeDef",
    "DeleteQueuedReservedInstancesErrorTypeDef",
    "DeleteQueuedReservedInstancesRequestRequestTypeDef",
    "DeleteQueuedReservedInstancesResultTypeDef",
    "DeleteRouteRequestRequestTypeDef",
    "DeleteRouteRequestRouteTypeDef",
    "DeleteRouteTableRequestRequestTypeDef",
    "DeleteRouteTableRequestRouteTableTypeDef",
    "DeleteSecurityGroupRequestRequestTypeDef",
    "DeleteSecurityGroupRequestSecurityGroupTypeDef",
    "DeleteSnapshotRequestRequestTypeDef",
    "DeleteSnapshotRequestSnapshotTypeDef",
    "DeleteSpotDatafeedSubscriptionRequestRequestTypeDef",
    "DeleteSubnetCidrReservationRequestRequestTypeDef",
    "DeleteSubnetCidrReservationResultTypeDef",
    "DeleteSubnetRequestRequestTypeDef",
    "DeleteSubnetRequestSubnetTypeDef",
    "DeleteTagsRequestRequestTypeDef",
    "DeleteTagsRequestTagTypeDef",
    "DeleteTrafficMirrorFilterRequestRequestTypeDef",
    "DeleteTrafficMirrorFilterResultTypeDef",
    "DeleteTrafficMirrorFilterRuleRequestRequestTypeDef",
    "DeleteTrafficMirrorFilterRuleResultTypeDef",
    "DeleteTrafficMirrorSessionRequestRequestTypeDef",
    "DeleteTrafficMirrorSessionResultTypeDef",
    "DeleteTrafficMirrorTargetRequestRequestTypeDef",
    "DeleteTrafficMirrorTargetResultTypeDef",
    "DeleteTransitGatewayConnectPeerRequestRequestTypeDef",
    "DeleteTransitGatewayConnectPeerResultTypeDef",
    "DeleteTransitGatewayConnectRequestRequestTypeDef",
    "DeleteTransitGatewayConnectResultTypeDef",
    "DeleteTransitGatewayMulticastDomainRequestRequestTypeDef",
    "DeleteTransitGatewayMulticastDomainResultTypeDef",
    "DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    "DeleteTransitGatewayPolicyTableRequestRequestTypeDef",
    "DeleteTransitGatewayPolicyTableResultTypeDef",
    "DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    "DeleteTransitGatewayPrefixListReferenceResultTypeDef",
    "DeleteTransitGatewayRequestRequestTypeDef",
    "DeleteTransitGatewayResultTypeDef",
    "DeleteTransitGatewayRouteRequestRequestTypeDef",
    "DeleteTransitGatewayRouteResultTypeDef",
    "DeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    "DeleteTransitGatewayRouteTableAnnouncementResultTypeDef",
    "DeleteTransitGatewayRouteTableRequestRequestTypeDef",
    "DeleteTransitGatewayRouteTableResultTypeDef",
    "DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "DeleteTransitGatewayVpcAttachmentResultTypeDef",
    "DeleteVerifiedAccessEndpointRequestRequestTypeDef",
    "DeleteVerifiedAccessEndpointResultTypeDef",
    "DeleteVerifiedAccessGroupRequestRequestTypeDef",
    "DeleteVerifiedAccessGroupResultTypeDef",
    "DeleteVerifiedAccessInstanceRequestRequestTypeDef",
    "DeleteVerifiedAccessInstanceResultTypeDef",
    "DeleteVerifiedAccessTrustProviderRequestRequestTypeDef",
    "DeleteVerifiedAccessTrustProviderResultTypeDef",
    "DeleteVolumeRequestRequestTypeDef",
    "DeleteVolumeRequestVolumeTypeDef",
    "DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    "DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    "DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    "DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    "DeleteVpcEndpointsRequestRequestTypeDef",
    "DeleteVpcEndpointsResultTypeDef",
    "DeleteVpcPeeringConnectionRequestRequestTypeDef",
    "DeleteVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    "DeleteVpcPeeringConnectionResultTypeDef",
    "DeleteVpcRequestRequestTypeDef",
    "DeleteVpcRequestVpcTypeDef",
    "DeleteVpnConnectionRequestRequestTypeDef",
    "DeleteVpnConnectionRouteRequestRequestTypeDef",
    "DeleteVpnGatewayRequestRequestTypeDef",
    "DeprovisionByoipCidrRequestRequestTypeDef",
    "DeprovisionByoipCidrResultTypeDef",
    "DeprovisionIpamPoolCidrRequestRequestTypeDef",
    "DeprovisionIpamPoolCidrResultTypeDef",
    "DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef",
    "DeprovisionPublicIpv4PoolCidrResultTypeDef",
    "DeregisterImageRequestImageTypeDef",
    "DeregisterImageRequestRequestTypeDef",
    "DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    "DeregisterInstanceEventNotificationAttributesResultTypeDef",
    "DeregisterInstanceTagAttributeRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    "DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "DescribeAccountAttributesRequestRequestTypeDef",
    "DescribeAccountAttributesResultTypeDef",
    "DescribeAddressTransfersRequestRequestTypeDef",
    "DescribeAddressTransfersResultTypeDef",
    "DescribeAddressesAttributeRequestRequestTypeDef",
    "DescribeAddressesAttributeResultTypeDef",
    "DescribeAddressesRequestRequestTypeDef",
    "DescribeAddressesResultTypeDef",
    "DescribeAggregateIdFormatRequestRequestTypeDef",
    "DescribeAggregateIdFormatResultTypeDef",
    "DescribeAvailabilityZonesRequestRequestTypeDef",
    "DescribeAvailabilityZonesResultTypeDef",
    "DescribeAwsNetworkPerformanceMetricSubscriptionsRequestRequestTypeDef",
    "DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef",
    "DescribeBundleTasksRequestRequestTypeDef",
    "DescribeBundleTasksResultTypeDef",
    "DescribeByoipCidrsRequestRequestTypeDef",
    "DescribeByoipCidrsResultTypeDef",
    "DescribeCapacityBlockOfferingsRequestRequestTypeDef",
    "DescribeCapacityBlockOfferingsResultTypeDef",
    "DescribeCapacityReservationFleetsRequestRequestTypeDef",
    "DescribeCapacityReservationFleetsResultTypeDef",
    "DescribeCapacityReservationsRequestRequestTypeDef",
    "DescribeCapacityReservationsResultTypeDef",
    "DescribeCarrierGatewaysRequestRequestTypeDef",
    "DescribeCarrierGatewaysResultTypeDef",
    "DescribeClassicLinkInstancesRequestRequestTypeDef",
    "DescribeClassicLinkInstancesResultTypeDef",
    "DescribeClientVpnAuthorizationRulesRequestRequestTypeDef",
    "DescribeClientVpnAuthorizationRulesResultTypeDef",
    "DescribeClientVpnConnectionsRequestRequestTypeDef",
    "DescribeClientVpnConnectionsResultTypeDef",
    "DescribeClientVpnEndpointsRequestRequestTypeDef",
    "DescribeClientVpnEndpointsResultTypeDef",
    "DescribeClientVpnRoutesRequestRequestTypeDef",
    "DescribeClientVpnRoutesResultTypeDef",
    "DescribeClientVpnTargetNetworksRequestRequestTypeDef",
    "DescribeClientVpnTargetNetworksResultTypeDef",
    "DescribeCoipPoolsRequestRequestTypeDef",
    "DescribeCoipPoolsResultTypeDef",
    "DescribeConversionTasksRequestRequestTypeDef",
    "DescribeConversionTasksResultTypeDef",
    "DescribeCustomerGatewaysRequestRequestTypeDef",
    "DescribeCustomerGatewaysResultTypeDef",
    "DescribeDhcpOptionsRequestRequestTypeDef",
    "DescribeDhcpOptionsResultTypeDef",
    "DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef",
    "DescribeEgressOnlyInternetGatewaysResultTypeDef",
    "DescribeElasticGpusRequestRequestTypeDef",
    "DescribeElasticGpusResultTypeDef",
    "DescribeExportImageTasksRequestRequestTypeDef",
    "DescribeExportImageTasksResultTypeDef",
    "DescribeExportTasksRequestRequestTypeDef",
    "DescribeExportTasksResultTypeDef",
    "DescribeFastLaunchImagesRequestRequestTypeDef",
    "DescribeFastLaunchImagesResultTypeDef",
    "DescribeFastLaunchImagesSuccessItemTypeDef",
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    "DescribeFastSnapshotRestoresRequestRequestTypeDef",
    "DescribeFastSnapshotRestoresResultTypeDef",
    "DescribeFleetErrorTypeDef",
    "DescribeFleetHistoryRequestRequestTypeDef",
    "DescribeFleetHistoryResultTypeDef",
    "DescribeFleetInstancesRequestRequestTypeDef",
    "DescribeFleetInstancesResultTypeDef",
    "DescribeFleetsInstancesTypeDef",
    "DescribeFleetsRequestRequestTypeDef",
    "DescribeFleetsResultTypeDef",
    "DescribeFlowLogsRequestRequestTypeDef",
    "DescribeFlowLogsResultTypeDef",
    "DescribeFpgaImageAttributeRequestRequestTypeDef",
    "DescribeFpgaImageAttributeResultTypeDef",
    "DescribeFpgaImagesRequestRequestTypeDef",
    "DescribeFpgaImagesResultTypeDef",
    "DescribeHostReservationOfferingsRequestRequestTypeDef",
    "DescribeHostReservationOfferingsResultTypeDef",
    "DescribeHostReservationsRequestRequestTypeDef",
    "DescribeHostReservationsResultTypeDef",
    "DescribeHostsRequestRequestTypeDef",
    "DescribeHostsResultTypeDef",
    "DescribeIamInstanceProfileAssociationsRequestRequestTypeDef",
    "DescribeIamInstanceProfileAssociationsResultTypeDef",
    "DescribeIdFormatRequestRequestTypeDef",
    "DescribeIdFormatResultTypeDef",
    "DescribeIdentityIdFormatRequestRequestTypeDef",
    "DescribeIdentityIdFormatResultTypeDef",
    "DescribeImageAttributeRequestImageTypeDef",
    "DescribeImageAttributeRequestRequestTypeDef",
    "DescribeImagesRequestRequestTypeDef",
    "DescribeImagesResultTypeDef",
    "DescribeImportImageTasksRequestRequestTypeDef",
    "DescribeImportImageTasksResultTypeDef",
    "DescribeImportSnapshotTasksRequestRequestTypeDef",
    "DescribeImportSnapshotTasksResultTypeDef",
    "DescribeInstanceAttributeRequestInstanceTypeDef",
    "DescribeInstanceAttributeRequestRequestTypeDef",
    "DescribeInstanceConnectEndpointsRequestRequestTypeDef",
    "DescribeInstanceConnectEndpointsResultTypeDef",
    "DescribeInstanceCreditSpecificationsRequestRequestTypeDef",
    "DescribeInstanceCreditSpecificationsResultTypeDef",
    "DescribeInstanceEventNotificationAttributesRequestRequestTypeDef",
    "DescribeInstanceEventNotificationAttributesResultTypeDef",
    "DescribeInstanceEventWindowsRequestRequestTypeDef",
    "DescribeInstanceEventWindowsResultTypeDef",
    "DescribeInstanceStatusRequestRequestTypeDef",
    "DescribeInstanceStatusResultTypeDef",
    "DescribeInstanceTopologyRequestRequestTypeDef",
    "DescribeInstanceTopologyResultTypeDef",
    "DescribeInstanceTypeOfferingsRequestRequestTypeDef",
    "DescribeInstanceTypeOfferingsResultTypeDef",
    "DescribeInstanceTypesRequestRequestTypeDef",
    "DescribeInstanceTypesResultTypeDef",
    "DescribeInstancesRequestRequestTypeDef",
    "DescribeInstancesResultTypeDef",
    "DescribeInternetGatewaysRequestRequestTypeDef",
    "DescribeInternetGatewaysResultTypeDef",
    "DescribeIpamPoolsRequestRequestTypeDef",
    "DescribeIpamPoolsResultTypeDef",
    "DescribeIpamResourceDiscoveriesRequestRequestTypeDef",
    "DescribeIpamResourceDiscoveriesResultTypeDef",
    "DescribeIpamResourceDiscoveryAssociationsRequestRequestTypeDef",
    "DescribeIpamResourceDiscoveryAssociationsResultTypeDef",
    "DescribeIpamScopesRequestRequestTypeDef",
    "DescribeIpamScopesResultTypeDef",
    "DescribeIpamsRequestRequestTypeDef",
    "DescribeIpamsResultTypeDef",
    "DescribeIpv6PoolsRequestRequestTypeDef",
    "DescribeIpv6PoolsResultTypeDef",
    "DescribeKeyPairsRequestRequestTypeDef",
    "DescribeKeyPairsResultTypeDef",
    "DescribeLaunchTemplateVersionsRequestRequestTypeDef",
    "DescribeLaunchTemplateVersionsResultTypeDef",
    "DescribeLaunchTemplatesRequestRequestTypeDef",
    "DescribeLaunchTemplatesResultTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef",
    "DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    "DescribeLocalGatewayRouteTablesRequestRequestTypeDef",
    "DescribeLocalGatewayRouteTablesResultTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef",
    "DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    "DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef",
    "DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    "DescribeLocalGatewaysRequestRequestTypeDef",
    "DescribeLocalGatewaysResultTypeDef",
    "DescribeManagedPrefixListsRequestRequestTypeDef",
    "DescribeManagedPrefixListsResultTypeDef",
    "DescribeMovingAddressesRequestRequestTypeDef",
    "DescribeMovingAddressesResultTypeDef",
    "DescribeNatGatewaysRequestRequestTypeDef",
    "DescribeNatGatewaysResultTypeDef",
    "DescribeNetworkAclsRequestRequestTypeDef",
    "DescribeNetworkAclsResultTypeDef",
    "DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef",
    "DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef",
    "DescribeNetworkInsightsAccessScopesRequestRequestTypeDef",
    "DescribeNetworkInsightsAccessScopesResultTypeDef",
    "DescribeNetworkInsightsAnalysesRequestRequestTypeDef",
    "DescribeNetworkInsightsAnalysesResultTypeDef",
    "DescribeNetworkInsightsPathsRequestRequestTypeDef",
    "DescribeNetworkInsightsPathsResultTypeDef",
    "DescribeNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    "DescribeNetworkInterfaceAttributeRequestRequestTypeDef",
    "DescribeNetworkInterfaceAttributeResultTypeDef",
    "DescribeNetworkInterfacePermissionsRequestRequestTypeDef",
    "DescribeNetworkInterfacePermissionsResultTypeDef",
    "DescribeNetworkInterfacesRequestRequestTypeDef",
    "DescribeNetworkInterfacesResultTypeDef",
    "DescribePlacementGroupsRequestRequestTypeDef",
    "DescribePlacementGroupsResultTypeDef",
    "DescribePrefixListsRequestRequestTypeDef",
    "DescribePrefixListsResultTypeDef",
    "DescribePrincipalIdFormatRequestRequestTypeDef",
    "DescribePrincipalIdFormatResultTypeDef",
    "DescribePublicIpv4PoolsRequestRequestTypeDef",
    "DescribePublicIpv4PoolsResultTypeDef",
    "DescribeRegionsRequestRequestTypeDef",
    "DescribeRegionsResultTypeDef",
    "DescribeReplaceRootVolumeTasksRequestRequestTypeDef",
    "DescribeReplaceRootVolumeTasksResultTypeDef",
    "DescribeReservedInstancesListingsRequestRequestTypeDef",
    "DescribeReservedInstancesListingsResultTypeDef",
    "DescribeReservedInstancesModificationsRequestRequestTypeDef",
    "DescribeReservedInstancesModificationsResultTypeDef",
    "DescribeReservedInstancesOfferingsRequestRequestTypeDef",
    "DescribeReservedInstancesOfferingsResultTypeDef",
    "DescribeReservedInstancesRequestRequestTypeDef",
    "DescribeReservedInstancesResultTypeDef",
    "DescribeRouteTablesRequestRequestTypeDef",
    "DescribeRouteTablesResultTypeDef",
    "DescribeScheduledInstanceAvailabilityRequestRequestTypeDef",
    "DescribeScheduledInstanceAvailabilityResultTypeDef",
    "DescribeScheduledInstancesRequestRequestTypeDef",
    "DescribeScheduledInstancesResultTypeDef",
    "DescribeSecurityGroupReferencesRequestRequestTypeDef",
    "DescribeSecurityGroupReferencesResultTypeDef",
    "DescribeSecurityGroupRulesRequestRequestTypeDef",
    "DescribeSecurityGroupRulesResultTypeDef",
    "DescribeSecurityGroupsRequestRequestTypeDef",
    "DescribeSecurityGroupsResultTypeDef",
    "DescribeSnapshotAttributeRequestRequestTypeDef",
    "DescribeSnapshotAttributeRequestSnapshotTypeDef",
    "DescribeSnapshotAttributeResultTypeDef",
    "DescribeSnapshotTierStatusRequestRequestTypeDef",
    "DescribeSnapshotTierStatusResultTypeDef",
    "DescribeSnapshotsRequestRequestTypeDef",
    "DescribeSnapshotsResultTypeDef",
    "DescribeSpotDatafeedSubscriptionRequestRequestTypeDef",
    "DescribeSpotDatafeedSubscriptionResultTypeDef",
    "DescribeSpotFleetInstancesRequestRequestTypeDef",
    "DescribeSpotFleetInstancesResponseTypeDef",
    "DescribeSpotFleetRequestHistoryRequestRequestTypeDef",
    "DescribeSpotFleetRequestHistoryResponseTypeDef",
    "DescribeSpotFleetRequestsRequestRequestTypeDef",
    "DescribeSpotFleetRequestsResponseTypeDef",
    "DescribeSpotInstanceRequestsRequestRequestTypeDef",
    "DescribeSpotInstanceRequestsResultTypeDef",
    "DescribeSpotPriceHistoryRequestRequestTypeDef",
    "DescribeSpotPriceHistoryResultTypeDef",
    "DescribeStaleSecurityGroupsRequestRequestTypeDef",
    "DescribeStaleSecurityGroupsResultTypeDef",
    "DescribeStoreImageTasksRequestRequestTypeDef",
    "DescribeStoreImageTasksResultTypeDef",
    "DescribeSubnetsRequestRequestTypeDef",
    "DescribeSubnetsResultTypeDef",
    "DescribeTagsRequestRequestTypeDef",
    "DescribeTagsResultTypeDef",
    "DescribeTrafficMirrorFiltersRequestRequestTypeDef",
    "DescribeTrafficMirrorFiltersResultTypeDef",
    "DescribeTrafficMirrorSessionsRequestRequestTypeDef",
    "DescribeTrafficMirrorSessionsResultTypeDef",
    "DescribeTrafficMirrorTargetsRequestRequestTypeDef",
    "DescribeTrafficMirrorTargetsResultTypeDef",
    "DescribeTransitGatewayAttachmentsRequestRequestTypeDef",
    "DescribeTransitGatewayAttachmentsResultTypeDef",
    "DescribeTransitGatewayConnectPeersRequestRequestTypeDef",
    "DescribeTransitGatewayConnectPeersResultTypeDef",
    "DescribeTransitGatewayConnectsRequestRequestTypeDef",
    "DescribeTransitGatewayConnectsResultTypeDef",
    "DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef",
    "DescribeTransitGatewayMulticastDomainsResultTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef",
    "DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    "DescribeTransitGatewayPolicyTablesRequestRequestTypeDef",
    "DescribeTransitGatewayPolicyTablesResultTypeDef",
    "DescribeTransitGatewayRouteTableAnnouncementsRequestRequestTypeDef",
    "DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef",
    "DescribeTransitGatewayRouteTablesRequestRequestTypeDef",
    "DescribeTransitGatewayRouteTablesResultTypeDef",
    "DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef",
    "DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    "DescribeTransitGatewaysRequestRequestTypeDef",
    "DescribeTransitGatewaysResultTypeDef",
    "DescribeTrunkInterfaceAssociationsRequestRequestTypeDef",
    "DescribeTrunkInterfaceAssociationsResultTypeDef",
    "DescribeVerifiedAccessEndpointsRequestRequestTypeDef",
    "DescribeVerifiedAccessEndpointsResultTypeDef",
    "DescribeVerifiedAccessGroupsRequestRequestTypeDef",
    "DescribeVerifiedAccessGroupsResultTypeDef",
    "DescribeVerifiedAccessInstanceLoggingConfigurationsRequestRequestTypeDef",
    "DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef",
    "DescribeVerifiedAccessInstancesRequestRequestTypeDef",
    "DescribeVerifiedAccessInstancesResultTypeDef",
    "DescribeVerifiedAccessTrustProvidersRequestRequestTypeDef",
    "DescribeVerifiedAccessTrustProvidersResultTypeDef",
    "DescribeVolumeAttributeRequestRequestTypeDef",
    "DescribeVolumeAttributeRequestVolumeTypeDef",
    "DescribeVolumeAttributeResultTypeDef",
    "DescribeVolumeStatusRequestRequestTypeDef",
    "DescribeVolumeStatusRequestVolumeTypeDef",
    "DescribeVolumeStatusResultTypeDef",
    "DescribeVolumesModificationsRequestRequestTypeDef",
    "DescribeVolumesModificationsResultTypeDef",
    "DescribeVolumesRequestRequestTypeDef",
    "DescribeVolumesResultTypeDef",
    "DescribeVpcAttributeRequestRequestTypeDef",
    "DescribeVpcAttributeRequestVpcTypeDef",
    "DescribeVpcAttributeResultTypeDef",
    "DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef",
    "DescribeVpcClassicLinkDnsSupportResultTypeDef",
    "DescribeVpcClassicLinkRequestRequestTypeDef",
    "DescribeVpcClassicLinkResultTypeDef",
    "DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    "DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    "DescribeVpcEndpointConnectionsRequestRequestTypeDef",
    "DescribeVpcEndpointConnectionsResultTypeDef",
    "DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    "DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    "DescribeVpcEndpointServicePermissionsRequestRequestTypeDef",
    "DescribeVpcEndpointServicePermissionsResultTypeDef",
    "DescribeVpcEndpointServicesRequestRequestTypeDef",
    "DescribeVpcEndpointServicesResultTypeDef",
    "DescribeVpcEndpointsRequestRequestTypeDef",
    "DescribeVpcEndpointsResultTypeDef",
    "DescribeVpcPeeringConnectionsRequestRequestTypeDef",
    "DescribeVpcPeeringConnectionsResultTypeDef",
    "DescribeVpcsRequestRequestTypeDef",
    "DescribeVpcsResultTypeDef",
    "DescribeVpnConnectionsRequestRequestTypeDef",
    "DescribeVpnConnectionsResultTypeDef",
    "DescribeVpnGatewaysRequestRequestTypeDef",
    "DescribeVpnGatewaysResultTypeDef",
    "DestinationOptionsRequestTypeDef",
    "DestinationOptionsResponseTypeDef",
    "DetachClassicLinkVpcRequestInstanceTypeDef",
    "DetachClassicLinkVpcRequestRequestTypeDef",
    "DetachClassicLinkVpcRequestVpcTypeDef",
    "DetachClassicLinkVpcResultTypeDef",
    "DetachInternetGatewayRequestInternetGatewayTypeDef",
    "DetachInternetGatewayRequestRequestTypeDef",
    "DetachInternetGatewayRequestVpcTypeDef",
    "DetachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    "DetachNetworkInterfaceRequestRequestTypeDef",
    "DetachVerifiedAccessTrustProviderRequestRequestTypeDef",
    "DetachVerifiedAccessTrustProviderResultTypeDef",
    "DetachVolumeRequestInstanceTypeDef",
    "DetachVolumeRequestRequestTypeDef",
    "DetachVolumeRequestVolumeTypeDef",
    "DetachVpnGatewayRequestRequestTypeDef",
    "DeviceOptionsTypeDef",
    "DhcpConfigurationTypeDef",
    "DhcpOptionsTypeDef",
    "DirectoryServiceAuthenticationRequestTypeDef",
    "DirectoryServiceAuthenticationTypeDef",
    "DisableAddressTransferRequestRequestTypeDef",
    "DisableAddressTransferResultTypeDef",
    "DisableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef",
    "DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    "DisableEbsEncryptionByDefaultRequestRequestTypeDef",
    "DisableEbsEncryptionByDefaultResultTypeDef",
    "DisableFastLaunchRequestRequestTypeDef",
    "DisableFastLaunchResultTypeDef",
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    "DisableFastSnapshotRestoresRequestRequestTypeDef",
    "DisableFastSnapshotRestoresResultTypeDef",
    "DisableImageBlockPublicAccessRequestRequestTypeDef",
    "DisableImageBlockPublicAccessResultTypeDef",
    "DisableImageDeprecationRequestRequestTypeDef",
    "DisableImageDeprecationResultTypeDef",
    "DisableImageRequestRequestTypeDef",
    "DisableImageResultTypeDef",
    "DisableIpamOrganizationAdminAccountRequestRequestTypeDef",
    "DisableIpamOrganizationAdminAccountResultTypeDef",
    "DisableSerialConsoleAccessRequestRequestTypeDef",
    "DisableSerialConsoleAccessResultTypeDef",
    "DisableSnapshotBlockPublicAccessRequestRequestTypeDef",
    "DisableSnapshotBlockPublicAccessResultTypeDef",
    "DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    "DisableTransitGatewayRouteTablePropagationResultTypeDef",
    "DisableVgwRoutePropagationRequestRequestTypeDef",
    "DisableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    "DisableVpcClassicLinkDnsSupportResultTypeDef",
    "DisableVpcClassicLinkRequestRequestTypeDef",
    "DisableVpcClassicLinkRequestVpcTypeDef",
    "DisableVpcClassicLinkResultTypeDef",
    "DisassociateAddressRequestClassicAddressTypeDef",
    "DisassociateAddressRequestNetworkInterfaceAssociationTypeDef",
    "DisassociateAddressRequestRequestTypeDef",
    "DisassociateClientVpnTargetNetworkRequestRequestTypeDef",
    "DisassociateClientVpnTargetNetworkResultTypeDef",
    "DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    "DisassociateEnclaveCertificateIamRoleResultTypeDef",
    "DisassociateIamInstanceProfileRequestRequestTypeDef",
    "DisassociateIamInstanceProfileResultTypeDef",
    "DisassociateInstanceEventWindowRequestRequestTypeDef",
    "DisassociateInstanceEventWindowResultTypeDef",
    "DisassociateIpamResourceDiscoveryRequestRequestTypeDef",
    "DisassociateIpamResourceDiscoveryResultTypeDef",
    "DisassociateNatGatewayAddressRequestRequestTypeDef",
    "DisassociateNatGatewayAddressResultTypeDef",
    "DisassociateRouteTableRequestRequestTypeDef",
    "DisassociateRouteTableRequestRouteTableAssociationTypeDef",
    "DisassociateRouteTableRequestServiceResourceTypeDef",
    "DisassociateSubnetCidrBlockRequestRequestTypeDef",
    "DisassociateSubnetCidrBlockResultTypeDef",
    "DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    "DisassociateTransitGatewayMulticastDomainResultTypeDef",
    "DisassociateTransitGatewayPolicyTableRequestRequestTypeDef",
    "DisassociateTransitGatewayPolicyTableResultTypeDef",
    "DisassociateTransitGatewayRouteTableRequestRequestTypeDef",
    "DisassociateTransitGatewayRouteTableResultTypeDef",
    "DisassociateTrunkInterfaceRequestRequestTypeDef",
    "DisassociateTrunkInterfaceResultTypeDef",
    "DisassociateVpcCidrBlockRequestRequestTypeDef",
    "DisassociateVpcCidrBlockResultTypeDef",
    "DiskImageDescriptionTypeDef",
    "DiskImageDetailTypeDef",
    "DiskImageTypeDef",
    "DiskImageVolumeDescriptionTypeDef",
    "DiskInfoTypeDef",
    "DnsEntryTypeDef",
    "DnsOptionsSpecificationTypeDef",
    "DnsOptionsTypeDef",
    "DnsServersOptionsModifyStructureTypeDef",
    "EbsBlockDeviceTypeDef",
    "EbsInfoTypeDef",
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    "EbsInstanceBlockDeviceTypeDef",
    "EbsOptimizedInfoTypeDef",
    "Ec2InstanceConnectEndpointTypeDef",
    "EfaInfoTypeDef",
    "EgressOnlyInternetGatewayTypeDef",
    "ElasticGpuAssociationTypeDef",
    "ElasticGpuHealthTypeDef",
    "ElasticGpuSpecificationResponseTypeDef",
    "ElasticGpuSpecificationTypeDef",
    "ElasticGpusTypeDef",
    "ElasticInferenceAcceleratorAssociationTypeDef",
    "ElasticInferenceAcceleratorTypeDef",
    "EnaSrdSpecificationRequestTypeDef",
    "EnaSrdSpecificationTypeDef",
    "EnaSrdUdpSpecificationRequestTypeDef",
    "EnaSrdUdpSpecificationTypeDef",
    "EnableAddressTransferRequestRequestTypeDef",
    "EnableAddressTransferResultTypeDef",
    "EnableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef",
    "EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    "EnableEbsEncryptionByDefaultRequestRequestTypeDef",
    "EnableEbsEncryptionByDefaultResultTypeDef",
    "EnableFastLaunchRequestRequestTypeDef",
    "EnableFastLaunchResultTypeDef",
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    "EnableFastSnapshotRestoresRequestRequestTypeDef",
    "EnableFastSnapshotRestoresResultTypeDef",
    "EnableImageBlockPublicAccessRequestRequestTypeDef",
    "EnableImageBlockPublicAccessResultTypeDef",
    "EnableImageDeprecationRequestRequestTypeDef",
    "EnableImageDeprecationResultTypeDef",
    "EnableImageRequestRequestTypeDef",
    "EnableImageResultTypeDef",
    "EnableIpamOrganizationAdminAccountRequestRequestTypeDef",
    "EnableIpamOrganizationAdminAccountResultTypeDef",
    "EnableReachabilityAnalyzerOrganizationSharingRequestRequestTypeDef",
    "EnableReachabilityAnalyzerOrganizationSharingResultTypeDef",
    "EnableSerialConsoleAccessRequestRequestTypeDef",
    "EnableSerialConsoleAccessResultTypeDef",
    "EnableSnapshotBlockPublicAccessRequestRequestTypeDef",
    "EnableSnapshotBlockPublicAccessResultTypeDef",
    "EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    "EnableTransitGatewayRouteTablePropagationResultTypeDef",
    "EnableVgwRoutePropagationRequestRequestTypeDef",
    "EnableVolumeIORequestRequestTypeDef",
    "EnableVolumeIORequestVolumeTypeDef",
    "EnableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    "EnableVpcClassicLinkDnsSupportResultTypeDef",
    "EnableVpcClassicLinkRequestRequestTypeDef",
    "EnableVpcClassicLinkRequestVpcTypeDef",
    "EnableVpcClassicLinkResultTypeDef",
    "EnclaveOptionsRequestTypeDef",
    "EnclaveOptionsTypeDef",
    "EventInformationTypeDef",
    "ExplanationTypeDef",
    "ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    "ExportClientVpnClientCertificateRevocationListResultTypeDef",
    "ExportClientVpnClientConfigurationRequestRequestTypeDef",
    "ExportClientVpnClientConfigurationResultTypeDef",
    "ExportImageRequestRequestTypeDef",
    "ExportImageResultTypeDef",
    "ExportImageTaskTypeDef",
    "ExportTaskS3LocationRequestTypeDef",
    "ExportTaskS3LocationTypeDef",
    "ExportTaskTypeDef",
    "ExportToS3TaskSpecificationTypeDef",
    "ExportToS3TaskTypeDef",
    "ExportTransitGatewayRoutesRequestRequestTypeDef",
    "ExportTransitGatewayRoutesResultTypeDef",
    "FailedCapacityReservationFleetCancellationResultTypeDef",
    "FailedQueuedPurchaseDeletionTypeDef",
    "FastLaunchLaunchTemplateSpecificationRequestTypeDef",
    "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
    "FastLaunchSnapshotConfigurationRequestTypeDef",
    "FastLaunchSnapshotConfigurationResponseTypeDef",
    "FederatedAuthenticationRequestTypeDef",
    "FederatedAuthenticationTypeDef",
    "FilterPortRangeTypeDef",
    "FilterTypeDef",
    "FirewallStatefulRuleTypeDef",
    "FirewallStatelessRuleTypeDef",
    "FleetCapacityReservationTypeDef",
    "FleetDataTypeDef",
    "FleetLaunchTemplateConfigRequestTypeDef",
    "FleetLaunchTemplateConfigTypeDef",
    "FleetLaunchTemplateOverridesRequestTypeDef",
    "FleetLaunchTemplateOverridesTypeDef",
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    "FleetLaunchTemplateSpecificationTypeDef",
    "FleetSpotCapacityRebalanceRequestTypeDef",
    "FleetSpotCapacityRebalanceTypeDef",
    "FleetSpotMaintenanceStrategiesRequestTypeDef",
    "FleetSpotMaintenanceStrategiesTypeDef",
    "FlowLogTypeDef",
    "FpgaDeviceInfoTypeDef",
    "FpgaDeviceMemoryInfoTypeDef",
    "FpgaImageAttributeTypeDef",
    "FpgaImageStateTypeDef",
    "FpgaImageTypeDef",
    "FpgaInfoTypeDef",
    "GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef",
    "GetAssociatedEnclaveCertificateIamRolesResultTypeDef",
    "GetAssociatedIpv6PoolCidrsRequestRequestTypeDef",
    "GetAssociatedIpv6PoolCidrsResultTypeDef",
    "GetAwsNetworkPerformanceDataRequestRequestTypeDef",
    "GetAwsNetworkPerformanceDataResultTypeDef",
    "GetCapacityReservationUsageRequestRequestTypeDef",
    "GetCapacityReservationUsageResultTypeDef",
    "GetCoipPoolUsageRequestRequestTypeDef",
    "GetCoipPoolUsageResultTypeDef",
    "GetConsoleOutputRequestInstanceTypeDef",
    "GetConsoleOutputRequestRequestTypeDef",
    "GetConsoleOutputResultTypeDef",
    "GetConsoleScreenshotRequestRequestTypeDef",
    "GetConsoleScreenshotResultTypeDef",
    "GetDefaultCreditSpecificationRequestRequestTypeDef",
    "GetDefaultCreditSpecificationResultTypeDef",
    "GetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    "GetEbsDefaultKmsKeyIdResultTypeDef",
    "GetEbsEncryptionByDefaultRequestRequestTypeDef",
    "GetEbsEncryptionByDefaultResultTypeDef",
    "GetFlowLogsIntegrationTemplateRequestRequestTypeDef",
    "GetFlowLogsIntegrationTemplateResultTypeDef",
    "GetGroupsForCapacityReservationRequestRequestTypeDef",
    "GetGroupsForCapacityReservationResultTypeDef",
    "GetHostReservationPurchasePreviewRequestRequestTypeDef",
    "GetHostReservationPurchasePreviewResultTypeDef",
    "GetImageBlockPublicAccessStateRequestRequestTypeDef",
    "GetImageBlockPublicAccessStateResultTypeDef",
    "GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef",
    "GetInstanceTypesFromInstanceRequirementsResultTypeDef",
    "GetInstanceUefiDataRequestRequestTypeDef",
    "GetInstanceUefiDataResultTypeDef",
    "GetIpamAddressHistoryRequestRequestTypeDef",
    "GetIpamAddressHistoryResultTypeDef",
    "GetIpamDiscoveredAccountsRequestRequestTypeDef",
    "GetIpamDiscoveredAccountsResultTypeDef",
    "GetIpamDiscoveredResourceCidrsRequestRequestTypeDef",
    "GetIpamDiscoveredResourceCidrsResultTypeDef",
    "GetIpamPoolAllocationsRequestRequestTypeDef",
    "GetIpamPoolAllocationsResultTypeDef",
    "GetIpamPoolCidrsRequestRequestTypeDef",
    "GetIpamPoolCidrsResultTypeDef",
    "GetIpamResourceCidrsRequestRequestTypeDef",
    "GetIpamResourceCidrsResultTypeDef",
    "GetLaunchTemplateDataRequestRequestTypeDef",
    "GetLaunchTemplateDataResultTypeDef",
    "GetManagedPrefixListAssociationsRequestRequestTypeDef",
    "GetManagedPrefixListAssociationsResultTypeDef",
    "GetManagedPrefixListEntriesRequestRequestTypeDef",
    "GetManagedPrefixListEntriesResultTypeDef",
    "GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef",
    "GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef",
    "GetNetworkInsightsAccessScopeContentRequestRequestTypeDef",
    "GetNetworkInsightsAccessScopeContentResultTypeDef",
    "GetPasswordDataRequestInstanceTypeDef",
    "GetPasswordDataRequestRequestTypeDef",
    "GetPasswordDataResultTypeDef",
    "GetReservedInstancesExchangeQuoteRequestRequestTypeDef",
    "GetReservedInstancesExchangeQuoteResultTypeDef",
    "GetSecurityGroupsForVpcRequestRequestTypeDef",
    "GetSecurityGroupsForVpcResultTypeDef",
    "GetSerialConsoleAccessStatusRequestRequestTypeDef",
    "GetSerialConsoleAccessStatusResultTypeDef",
    "GetSnapshotBlockPublicAccessStateRequestRequestTypeDef",
    "GetSnapshotBlockPublicAccessStateResultTypeDef",
    "GetSpotPlacementScoresRequestRequestTypeDef",
    "GetSpotPlacementScoresResultTypeDef",
    "GetSubnetCidrReservationsRequestRequestTypeDef",
    "GetSubnetCidrReservationsResultTypeDef",
    "GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef",
    "GetTransitGatewayAttachmentPropagationsResultTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    "GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "GetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef",
    "GetTransitGatewayPolicyTableAssociationsResultTypeDef",
    "GetTransitGatewayPolicyTableEntriesRequestRequestTypeDef",
    "GetTransitGatewayPolicyTableEntriesResultTypeDef",
    "GetTransitGatewayPrefixListReferencesRequestRequestTypeDef",
    "GetTransitGatewayPrefixListReferencesResultTypeDef",
    "GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef",
    "GetTransitGatewayRouteTableAssociationsResultTypeDef",
    "GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef",
    "GetTransitGatewayRouteTablePropagationsResultTypeDef",
    "GetVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    "GetVerifiedAccessEndpointPolicyResultTypeDef",
    "GetVerifiedAccessGroupPolicyRequestRequestTypeDef",
    "GetVerifiedAccessGroupPolicyResultTypeDef",
    "GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef",
    "GetVpnConnectionDeviceSampleConfigurationResultTypeDef",
    "GetVpnConnectionDeviceTypesRequestRequestTypeDef",
    "GetVpnConnectionDeviceTypesResultTypeDef",
    "GetVpnTunnelReplacementStatusRequestRequestTypeDef",
    "GetVpnTunnelReplacementStatusResultTypeDef",
    "GpuDeviceInfoTypeDef",
    "GpuDeviceMemoryInfoTypeDef",
    "GpuInfoTypeDef",
    "GroupIdentifierTypeDef",
    "HibernationOptionsRequestTypeDef",
    "HibernationOptionsTypeDef",
    "HistoryRecordEntryTypeDef",
    "HistoryRecordTypeDef",
    "HostInstanceTypeDef",
    "HostOfferingTypeDef",
    "HostPropertiesTypeDef",
    "HostReservationTypeDef",
    "HostTypeDef",
    "IKEVersionsListValueTypeDef",
    "IKEVersionsRequestListValueTypeDef",
    "IamInstanceProfileAssociationTypeDef",
    "IamInstanceProfileSpecificationTypeDef",
    "IamInstanceProfileTypeDef",
    "IcmpTypeCodeTypeDef",
    "IdFormatTypeDef",
    "ImageAttributeTypeDef",
    "ImageDiskContainerTypeDef",
    "ImageRecycleBinInfoTypeDef",
    "ImageTypeDef",
    "ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    "ImportClientVpnClientCertificateRevocationListResultTypeDef",
    "ImportImageLicenseConfigurationRequestTypeDef",
    "ImportImageLicenseConfigurationResponseTypeDef",
    "ImportImageRequestRequestTypeDef",
    "ImportImageResultTypeDef",
    "ImportImageTaskTypeDef",
    "ImportInstanceLaunchSpecificationTypeDef",
    "ImportInstanceRequestRequestTypeDef",
    "ImportInstanceResultTypeDef",
    "ImportInstanceTaskDetailsTypeDef",
    "ImportInstanceVolumeDetailItemTypeDef",
    "ImportKeyPairRequestRequestTypeDef",
    "ImportKeyPairRequestServiceResourceTypeDef",
    "ImportKeyPairResultTypeDef",
    "ImportSnapshotRequestRequestTypeDef",
    "ImportSnapshotResultTypeDef",
    "ImportSnapshotTaskTypeDef",
    "ImportVolumeRequestRequestTypeDef",
    "ImportVolumeResultTypeDef",
    "ImportVolumeTaskDetailsTypeDef",
    "InferenceAcceleratorInfoTypeDef",
    "InferenceDeviceInfoTypeDef",
    "InferenceDeviceMemoryInfoTypeDef",
    "InstanceAttachmentEnaSrdSpecificationTypeDef",
    "InstanceAttachmentEnaSrdUdpSpecificationTypeDef",
    "InstanceAttributeTypeDef",
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    "InstanceBlockDeviceMappingTypeDef",
    "InstanceCapacityTypeDef",
    "InstanceCountTypeDef",
    "InstanceCreditSpecificationRequestTypeDef",
    "InstanceCreditSpecificationTypeDef",
    "InstanceDeleteTagsRequestTypeDef",
    "InstanceEventWindowAssociationRequestTypeDef",
    "InstanceEventWindowAssociationTargetTypeDef",
    "InstanceEventWindowDisassociationRequestTypeDef",
    "InstanceEventWindowStateChangeTypeDef",
    "InstanceEventWindowTimeRangeRequestTypeDef",
    "InstanceEventWindowTimeRangeTypeDef",
    "InstanceEventWindowTypeDef",
    "InstanceExportDetailsTypeDef",
    "InstanceFamilyCreditSpecificationTypeDef",
    "InstanceIpv4PrefixTypeDef",
    "InstanceIpv6AddressRequestTypeDef",
    "InstanceIpv6AddressTypeDef",
    "InstanceIpv6PrefixTypeDef",
    "InstanceMaintenanceOptionsRequestTypeDef",
    "InstanceMaintenanceOptionsTypeDef",
    "InstanceMarketOptionsRequestTypeDef",
    "InstanceMetadataOptionsRequestTypeDef",
    "InstanceMetadataOptionsResponseTypeDef",
    "InstanceMonitoringTypeDef",
    "InstanceNetworkInterfaceAssociationTypeDef",
    "InstanceNetworkInterfaceAttachmentTypeDef",
    "InstanceNetworkInterfaceSpecificationTypeDef",
    "InstanceNetworkInterfaceTypeDef",
    "InstancePrivateIpAddressTypeDef",
    "InstanceRequirementsRequestTypeDef",
    "InstanceRequirementsTypeDef",
    "InstanceRequirementsWithMetadataRequestTypeDef",
    "InstanceSpecificationTypeDef",
    "InstanceStateChangeTypeDef",
    "InstanceStateTypeDef",
    "InstanceStatusDetailsTypeDef",
    "InstanceStatusEventTypeDef",
    "InstanceStatusSummaryTypeDef",
    "InstanceStatusTypeDef",
    "InstanceStorageInfoTypeDef",
    "InstanceTagNotificationAttributeTypeDef",
    "InstanceTopologyTypeDef",
    "InstanceTypeDef",
    "InstanceTypeInfoFromInstanceRequirementsTypeDef",
    "InstanceTypeInfoTypeDef",
    "InstanceTypeOfferingTypeDef",
    "InstanceUsageTypeDef",
    "IntegrateServicesTypeDef",
    "InternetGatewayAttachmentTypeDef",
    "InternetGatewayTypeDef",
    "IpPermissionTypeDef",
    "IpRangeTypeDef",
    "IpamAddressHistoryRecordTypeDef",
    "IpamCidrAuthorizationContextTypeDef",
    "IpamDiscoveredAccountTypeDef",
    "IpamDiscoveredResourceCidrTypeDef",
    "IpamDiscoveryFailureReasonTypeDef",
    "IpamOperatingRegionTypeDef",
    "IpamPoolAllocationTypeDef",
    "IpamPoolCidrFailureReasonTypeDef",
    "IpamPoolCidrTypeDef",
    "IpamPoolTypeDef",
    "IpamResourceCidrTypeDef",
    "IpamResourceDiscoveryAssociationTypeDef",
    "IpamResourceDiscoveryTypeDef",
    "IpamResourceTagTypeDef",
    "IpamScopeTypeDef",
    "IpamTypeDef",
    "Ipv4PrefixSpecificationRequestTypeDef",
    "Ipv4PrefixSpecificationResponseTypeDef",
    "Ipv4PrefixSpecificationTypeDef",
    "Ipv6CidrAssociationTypeDef",
    "Ipv6CidrBlockTypeDef",
    "Ipv6PoolTypeDef",
    "Ipv6PrefixSpecificationRequestTypeDef",
    "Ipv6PrefixSpecificationResponseTypeDef",
    "Ipv6PrefixSpecificationTypeDef",
    "Ipv6RangeTypeDef",
    "KeyPairInfoTypeDef",
    "KeyPairTypeDef",
    "LastErrorTypeDef",
    "LaunchPermissionModificationsTypeDef",
    "LaunchPermissionTypeDef",
    "LaunchSpecificationTypeDef",
    "LaunchTemplateAndOverridesResponseTypeDef",
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    "LaunchTemplateBlockDeviceMappingTypeDef",
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    "LaunchTemplateConfigTypeDef",
    "LaunchTemplateCpuOptionsRequestTypeDef",
    "LaunchTemplateCpuOptionsTypeDef",
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    "LaunchTemplateEbsBlockDeviceTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    "LaunchTemplateElasticInferenceAcceleratorTypeDef",
    "LaunchTemplateEnaSrdSpecificationTypeDef",
    "LaunchTemplateEnaSrdUdpSpecificationTypeDef",
    "LaunchTemplateEnclaveOptionsRequestTypeDef",
    "LaunchTemplateEnclaveOptionsTypeDef",
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    "LaunchTemplateHibernationOptionsTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    "LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef",
    "LaunchTemplateInstanceMaintenanceOptionsTypeDef",
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    "LaunchTemplateLicenseConfigurationTypeDef",
    "LaunchTemplateOverridesTypeDef",
    "LaunchTemplatePlacementRequestTypeDef",
    "LaunchTemplatePlacementTypeDef",
    "LaunchTemplatePrivateDnsNameOptionsRequestTypeDef",
    "LaunchTemplatePrivateDnsNameOptionsTypeDef",
    "LaunchTemplateSpecificationTypeDef",
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    "LaunchTemplateSpotMarketOptionsTypeDef",
    "LaunchTemplateTagSpecificationRequestTypeDef",
    "LaunchTemplateTagSpecificationTypeDef",
    "LaunchTemplateTypeDef",
    "LaunchTemplateVersionTypeDef",
    "LaunchTemplatesMonitoringRequestTypeDef",
    "LaunchTemplatesMonitoringTypeDef",
    "LicenseConfigurationRequestTypeDef",
    "LicenseConfigurationTypeDef",
    "ListImagesInRecycleBinRequestRequestTypeDef",
    "ListImagesInRecycleBinResultTypeDef",
    "ListSnapshotsInRecycleBinRequestRequestTypeDef",
    "ListSnapshotsInRecycleBinResultTypeDef",
    "LoadBalancersConfigTypeDef",
    "LoadPermissionModificationsTypeDef",
    "LoadPermissionRequestTypeDef",
    "LoadPermissionTypeDef",
    "LocalGatewayRouteTableTypeDef",
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    "LocalGatewayRouteTypeDef",
    "LocalGatewayTypeDef",
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    "LocalGatewayVirtualInterfaceTypeDef",
    "MaintenanceDetailsTypeDef",
    "ManagedPrefixListTypeDef",
    "MemoryGiBPerVCpuRequestTypeDef",
    "MemoryGiBPerVCpuTypeDef",
    "MemoryInfoTypeDef",
    "MemoryMiBRequestTypeDef",
    "MemoryMiBTypeDef",
    "MetricPointTypeDef",
    "ModifyAddressAttributeRequestRequestTypeDef",
    "ModifyAddressAttributeResultTypeDef",
    "ModifyAvailabilityZoneGroupRequestRequestTypeDef",
    "ModifyAvailabilityZoneGroupResultTypeDef",
    "ModifyCapacityReservationFleetRequestRequestTypeDef",
    "ModifyCapacityReservationFleetResultTypeDef",
    "ModifyCapacityReservationRequestRequestTypeDef",
    "ModifyCapacityReservationResultTypeDef",
    "ModifyClientVpnEndpointRequestRequestTypeDef",
    "ModifyClientVpnEndpointResultTypeDef",
    "ModifyDefaultCreditSpecificationRequestRequestTypeDef",
    "ModifyDefaultCreditSpecificationResultTypeDef",
    "ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef",
    "ModifyEbsDefaultKmsKeyIdResultTypeDef",
    "ModifyFleetRequestRequestTypeDef",
    "ModifyFleetResultTypeDef",
    "ModifyFpgaImageAttributeRequestRequestTypeDef",
    "ModifyFpgaImageAttributeResultTypeDef",
    "ModifyHostsRequestRequestTypeDef",
    "ModifyHostsResultTypeDef",
    "ModifyIdFormatRequestRequestTypeDef",
    "ModifyIdentityIdFormatRequestRequestTypeDef",
    "ModifyImageAttributeRequestImageTypeDef",
    "ModifyImageAttributeRequestRequestTypeDef",
    "ModifyInstanceAttributeRequestInstanceTypeDef",
    "ModifyInstanceAttributeRequestRequestTypeDef",
    "ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef",
    "ModifyInstanceCapacityReservationAttributesResultTypeDef",
    "ModifyInstanceCreditSpecificationRequestRequestTypeDef",
    "ModifyInstanceCreditSpecificationResultTypeDef",
    "ModifyInstanceEventStartTimeRequestRequestTypeDef",
    "ModifyInstanceEventStartTimeResultTypeDef",
    "ModifyInstanceEventWindowRequestRequestTypeDef",
    "ModifyInstanceEventWindowResultTypeDef",
    "ModifyInstanceMaintenanceOptionsRequestRequestTypeDef",
    "ModifyInstanceMaintenanceOptionsResultTypeDef",
    "ModifyInstanceMetadataOptionsRequestRequestTypeDef",
    "ModifyInstanceMetadataOptionsResultTypeDef",
    "ModifyInstancePlacementRequestRequestTypeDef",
    "ModifyInstancePlacementResultTypeDef",
    "ModifyIpamPoolRequestRequestTypeDef",
    "ModifyIpamPoolResultTypeDef",
    "ModifyIpamRequestRequestTypeDef",
    "ModifyIpamResourceCidrRequestRequestTypeDef",
    "ModifyIpamResourceCidrResultTypeDef",
    "ModifyIpamResourceDiscoveryRequestRequestTypeDef",
    "ModifyIpamResourceDiscoveryResultTypeDef",
    "ModifyIpamResultTypeDef",
    "ModifyIpamScopeRequestRequestTypeDef",
    "ModifyIpamScopeResultTypeDef",
    "ModifyLaunchTemplateRequestRequestTypeDef",
    "ModifyLaunchTemplateResultTypeDef",
    "ModifyLocalGatewayRouteRequestRequestTypeDef",
    "ModifyLocalGatewayRouteResultTypeDef",
    "ModifyManagedPrefixListRequestRequestTypeDef",
    "ModifyManagedPrefixListResultTypeDef",
    "ModifyNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    "ModifyNetworkInterfaceAttributeRequestRequestTypeDef",
    "ModifyPrivateDnsNameOptionsRequestRequestTypeDef",
    "ModifyPrivateDnsNameOptionsResultTypeDef",
    "ModifyReservedInstancesRequestRequestTypeDef",
    "ModifyReservedInstancesResultTypeDef",
    "ModifySecurityGroupRulesRequestRequestTypeDef",
    "ModifySecurityGroupRulesResultTypeDef",
    "ModifySnapshotAttributeRequestRequestTypeDef",
    "ModifySnapshotAttributeRequestSnapshotTypeDef",
    "ModifySnapshotTierRequestRequestTypeDef",
    "ModifySnapshotTierResultTypeDef",
    "ModifySpotFleetRequestRequestRequestTypeDef",
    "ModifySpotFleetRequestResponseTypeDef",
    "ModifySubnetAttributeRequestRequestTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef",
    "ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    "ModifyTrafficMirrorFilterRuleRequestRequestTypeDef",
    "ModifyTrafficMirrorFilterRuleResultTypeDef",
    "ModifyTrafficMirrorSessionRequestRequestTypeDef",
    "ModifyTrafficMirrorSessionResultTypeDef",
    "ModifyTransitGatewayOptionsTypeDef",
    "ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    "ModifyTransitGatewayPrefixListReferenceResultTypeDef",
    "ModifyTransitGatewayRequestRequestTypeDef",
    "ModifyTransitGatewayResultTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    "ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "ModifyTransitGatewayVpcAttachmentResultTypeDef",
    "ModifyVerifiedAccessEndpointEniOptionsTypeDef",
    "ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    "ModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    "ModifyVerifiedAccessEndpointPolicyResultTypeDef",
    "ModifyVerifiedAccessEndpointRequestRequestTypeDef",
    "ModifyVerifiedAccessEndpointResultTypeDef",
    "ModifyVerifiedAccessGroupPolicyRequestRequestTypeDef",
    "ModifyVerifiedAccessGroupPolicyResultTypeDef",
    "ModifyVerifiedAccessGroupRequestRequestTypeDef",
    "ModifyVerifiedAccessGroupResultTypeDef",
    "ModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef",
    "ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef",
    "ModifyVerifiedAccessInstanceRequestRequestTypeDef",
    "ModifyVerifiedAccessInstanceResultTypeDef",
    "ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef",
    "ModifyVerifiedAccessTrustProviderRequestRequestTypeDef",
    "ModifyVerifiedAccessTrustProviderResultTypeDef",
    "ModifyVolumeAttributeRequestRequestTypeDef",
    "ModifyVolumeAttributeRequestVolumeTypeDef",
    "ModifyVolumeRequestRequestTypeDef",
    "ModifyVolumeResultTypeDef",
    "ModifyVpcAttributeRequestRequestTypeDef",
    "ModifyVpcAttributeRequestVpcTypeDef",
    "ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef",
    "ModifyVpcEndpointConnectionNotificationResultTypeDef",
    "ModifyVpcEndpointRequestRequestTypeDef",
    "ModifyVpcEndpointResultTypeDef",
    "ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef",
    "ModifyVpcEndpointServiceConfigurationResultTypeDef",
    "ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef",
    "ModifyVpcEndpointServicePayerResponsibilityResultTypeDef",
    "ModifyVpcEndpointServicePermissionsRequestRequestTypeDef",
    "ModifyVpcEndpointServicePermissionsResultTypeDef",
    "ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef",
    "ModifyVpcPeeringConnectionOptionsResultTypeDef",
    "ModifyVpcTenancyRequestRequestTypeDef",
    "ModifyVpcTenancyResultTypeDef",
    "ModifyVpnConnectionOptionsRequestRequestTypeDef",
    "ModifyVpnConnectionOptionsResultTypeDef",
    "ModifyVpnConnectionRequestRequestTypeDef",
    "ModifyVpnConnectionResultTypeDef",
    "ModifyVpnTunnelCertificateRequestRequestTypeDef",
    "ModifyVpnTunnelCertificateResultTypeDef",
    "ModifyVpnTunnelOptionsRequestRequestTypeDef",
    "ModifyVpnTunnelOptionsResultTypeDef",
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    "MonitorInstancesRequestInstanceTypeDef",
    "MonitorInstancesRequestRequestTypeDef",
    "MonitorInstancesResultTypeDef",
    "MonitoringTypeDef",
    "MoveAddressToVpcRequestRequestTypeDef",
    "MoveAddressToVpcResultTypeDef",
    "MoveByoipCidrToIpamRequestRequestTypeDef",
    "MoveByoipCidrToIpamResultTypeDef",
    "MovingAddressStatusTypeDef",
    "NatGatewayAddressTypeDef",
    "NatGatewayTypeDef",
    "NetworkAclAssociationTypeDef",
    "NetworkAclEntryTypeDef",
    "NetworkAclTypeDef",
    "NetworkBandwidthGbpsRequestTypeDef",
    "NetworkBandwidthGbpsTypeDef",
    "NetworkCardInfoTypeDef",
    "NetworkInfoTypeDef",
    "NetworkInsightsAccessScopeAnalysisTypeDef",
    "NetworkInsightsAccessScopeContentTypeDef",
    "NetworkInsightsAccessScopeTypeDef",
    "NetworkInsightsAnalysisTypeDef",
    "NetworkInsightsPathTypeDef",
    "NetworkInterfaceAssociationTypeDef",
    "NetworkInterfaceAttachmentChangesTypeDef",
    "NetworkInterfaceAttachmentTypeDef",
    "NetworkInterfaceCountRequestTypeDef",
    "NetworkInterfaceCountTypeDef",
    "NetworkInterfaceIpv6AddressTypeDef",
    "NetworkInterfacePermissionStateTypeDef",
    "NetworkInterfacePermissionTypeDef",
    "NetworkInterfacePrivateIpAddressTypeDef",
    "NetworkInterfaceTypeDef",
    "NewDhcpConfigurationTypeDef",
    "NitroTpmInfoTypeDef",
    "OidcOptionsTypeDef",
    "OnDemandOptionsRequestTypeDef",
    "OnDemandOptionsTypeDef",
    "PacketHeaderStatementRequestTypeDef",
    "PacketHeaderStatementTypeDef",
    "PaginatorConfigTypeDef",
    "PathComponentTypeDef",
    "PathFilterTypeDef",
    "PathRequestFilterTypeDef",
    "PathStatementRequestTypeDef",
    "PathStatementTypeDef",
    "PciIdTypeDef",
    "PeeringAttachmentStatusTypeDef",
    "PeeringConnectionOptionsRequestTypeDef",
    "PeeringConnectionOptionsTypeDef",
    "PeeringTgwInfoTypeDef",
    "Phase1DHGroupNumbersListValueTypeDef",
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    "Phase2DHGroupNumbersListValueTypeDef",
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    "PlacementGroupInfoTypeDef",
    "PlacementGroupTypeDef",
    "PlacementResponseTypeDef",
    "PlacementTypeDef",
    "PoolCidrBlockTypeDef",
    "PortRangeTypeDef",
    "PrefixListAssociationTypeDef",
    "PrefixListEntryTypeDef",
    "PrefixListIdTypeDef",
    "PrefixListTypeDef",
    "PriceScheduleSpecificationTypeDef",
    "PriceScheduleTypeDef",
    "PricingDetailTypeDef",
    "PrincipalIdFormatTypeDef",
    "PrivateDnsDetailsTypeDef",
    "PrivateDnsNameConfigurationTypeDef",
    "PrivateDnsNameOptionsOnLaunchTypeDef",
    "PrivateDnsNameOptionsRequestTypeDef",
    "PrivateDnsNameOptionsResponseTypeDef",
    "PrivateIpAddressSpecificationTypeDef",
    "ProcessorInfoTypeDef",
    "ProductCodeTypeDef",
    "PropagatingVgwTypeDef",
    "ProvisionByoipCidrRequestRequestTypeDef",
    "ProvisionByoipCidrResultTypeDef",
    "ProvisionIpamPoolCidrRequestRequestTypeDef",
    "ProvisionIpamPoolCidrResultTypeDef",
    "ProvisionPublicIpv4PoolCidrRequestRequestTypeDef",
    "ProvisionPublicIpv4PoolCidrResultTypeDef",
    "ProvisionedBandwidthTypeDef",
    "PtrUpdateStatusTypeDef",
    "PublicIpv4PoolRangeTypeDef",
    "PublicIpv4PoolTypeDef",
    "PurchaseCapacityBlockRequestRequestTypeDef",
    "PurchaseCapacityBlockResultTypeDef",
    "PurchaseHostReservationRequestRequestTypeDef",
    "PurchaseHostReservationResultTypeDef",
    "PurchaseRequestTypeDef",
    "PurchaseReservedInstancesOfferingRequestRequestTypeDef",
    "PurchaseReservedInstancesOfferingResultTypeDef",
    "PurchaseScheduledInstancesRequestRequestTypeDef",
    "PurchaseScheduledInstancesResultTypeDef",
    "PurchaseTypeDef",
    "RebootInstancesRequestInstanceTypeDef",
    "RebootInstancesRequestRequestTypeDef",
    "RecurringChargeTypeDef",
    "ReferencedSecurityGroupTypeDef",
    "RegionTypeDef",
    "RegisterImageRequestRequestTypeDef",
    "RegisterImageRequestServiceResourceTypeDef",
    "RegisterImageResultTypeDef",
    "RegisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    "RegisterInstanceEventNotificationAttributesResultTypeDef",
    "RegisterInstanceTagAttributeRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    "RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    "RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    "RejectTransitGatewayMulticastDomainAssociationsResultTypeDef",
    "RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    "RejectTransitGatewayPeeringAttachmentResultTypeDef",
    "RejectTransitGatewayVpcAttachmentRequestRequestTypeDef",
    "RejectTransitGatewayVpcAttachmentResultTypeDef",
    "RejectVpcEndpointConnectionsRequestRequestTypeDef",
    "RejectVpcEndpointConnectionsResultTypeDef",
    "RejectVpcPeeringConnectionRequestRequestTypeDef",
    "RejectVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    "RejectVpcPeeringConnectionResultTypeDef",
    "ReleaseAddressRequestClassicAddressTypeDef",
    "ReleaseAddressRequestRequestTypeDef",
    "ReleaseAddressRequestVpcAddressTypeDef",
    "ReleaseHostsRequestRequestTypeDef",
    "ReleaseHostsResultTypeDef",
    "ReleaseIpamPoolAllocationRequestRequestTypeDef",
    "ReleaseIpamPoolAllocationResultTypeDef",
    "RemoveIpamOperatingRegionTypeDef",
    "RemovePrefixListEntryTypeDef",
    "ReplaceIamInstanceProfileAssociationRequestRequestTypeDef",
    "ReplaceIamInstanceProfileAssociationResultTypeDef",
    "ReplaceNetworkAclAssociationRequestNetworkAclTypeDef",
    "ReplaceNetworkAclAssociationRequestRequestTypeDef",
    "ReplaceNetworkAclAssociationResultTypeDef",
    "ReplaceNetworkAclEntryRequestNetworkAclTypeDef",
    "ReplaceNetworkAclEntryRequestRequestTypeDef",
    "ReplaceRootVolumeTaskTypeDef",
    "ReplaceRouteRequestRequestTypeDef",
    "ReplaceRouteRequestRouteTypeDef",
    "ReplaceRouteTableAssociationRequestRequestTypeDef",
    "ReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef",
    "ReplaceRouteTableAssociationResultTypeDef",
    "ReplaceTransitGatewayRouteRequestRequestTypeDef",
    "ReplaceTransitGatewayRouteResultTypeDef",
    "ReplaceVpnTunnelRequestRequestTypeDef",
    "ReplaceVpnTunnelResultTypeDef",
    "ReportInstanceStatusRequestInstanceTypeDef",
    "ReportInstanceStatusRequestRequestTypeDef",
    "RequestFilterPortRangeTypeDef",
    "RequestIpamResourceTagTypeDef",
    "RequestLaunchTemplateDataTypeDef",
    "RequestSpotFleetRequestRequestTypeDef",
    "RequestSpotFleetResponseTypeDef",
    "RequestSpotInstancesRequestRequestTypeDef",
    "RequestSpotInstancesResultTypeDef",
    "RequestSpotLaunchSpecificationTypeDef",
    "ReservationFleetInstanceSpecificationTypeDef",
    "ReservationResponseMetadataTypeDef",
    "ReservationTypeDef",
    "ReservationValueTypeDef",
    "ReservedInstanceLimitPriceTypeDef",
    "ReservedInstanceReservationValueTypeDef",
    "ReservedInstancesConfigurationTypeDef",
    "ReservedInstancesIdTypeDef",
    "ReservedInstancesListingTypeDef",
    "ReservedInstancesModificationResultTypeDef",
    "ReservedInstancesModificationTypeDef",
    "ReservedInstancesOfferingTypeDef",
    "ReservedInstancesTypeDef",
    "ResetAddressAttributeRequestRequestTypeDef",
    "ResetAddressAttributeResultTypeDef",
    "ResetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    "ResetEbsDefaultKmsKeyIdResultTypeDef",
    "ResetFpgaImageAttributeRequestRequestTypeDef",
    "ResetFpgaImageAttributeResultTypeDef",
    "ResetImageAttributeRequestImageTypeDef",
    "ResetImageAttributeRequestRequestTypeDef",
    "ResetInstanceAttributeRequestInstanceTypeDef",
    "ResetInstanceAttributeRequestRequestTypeDef",
    "ResetNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    "ResetNetworkInterfaceAttributeRequestRequestTypeDef",
    "ResetSnapshotAttributeRequestRequestTypeDef",
    "ResetSnapshotAttributeRequestSnapshotTypeDef",
    "ResourceStatementRequestTypeDef",
    "ResourceStatementTypeDef",
    "ResponseErrorTypeDef",
    "ResponseLaunchTemplateDataTypeDef",
    "ResponseMetadataTypeDef",
    "RestoreAddressToClassicRequestRequestTypeDef",
    "RestoreAddressToClassicResultTypeDef",
    "RestoreImageFromRecycleBinRequestRequestTypeDef",
    "RestoreImageFromRecycleBinResultTypeDef",
    "RestoreManagedPrefixListVersionRequestRequestTypeDef",
    "RestoreManagedPrefixListVersionResultTypeDef",
    "RestoreSnapshotFromRecycleBinRequestRequestTypeDef",
    "RestoreSnapshotFromRecycleBinResultTypeDef",
    "RestoreSnapshotTierRequestRequestTypeDef",
    "RestoreSnapshotTierResultTypeDef",
    "RevokeClientVpnIngressRequestRequestTypeDef",
    "RevokeClientVpnIngressResultTypeDef",
    "RevokeSecurityGroupEgressRequestRequestTypeDef",
    "RevokeSecurityGroupEgressRequestSecurityGroupTypeDef",
    "RevokeSecurityGroupEgressResultTypeDef",
    "RevokeSecurityGroupIngressRequestRequestTypeDef",
    "RevokeSecurityGroupIngressRequestSecurityGroupTypeDef",
    "RevokeSecurityGroupIngressResultTypeDef",
    "RouteTableAssociationStateTypeDef",
    "RouteTableAssociationTypeDef",
    "RouteTableTypeDef",
    "RouteTypeDef",
    "RuleGroupRuleOptionsPairTypeDef",
    "RuleGroupTypePairTypeDef",
    "RuleOptionTypeDef",
    "RunInstancesMonitoringEnabledTypeDef",
    "RunInstancesRequestRequestTypeDef",
    "RunInstancesRequestServiceResourceTypeDef",
    "RunInstancesRequestSubnetTypeDef",
    "RunScheduledInstancesRequestRequestTypeDef",
    "RunScheduledInstancesResultTypeDef",
    "S3ObjectTagTypeDef",
    "S3StorageTypeDef",
    "ScheduledInstanceAvailabilityTypeDef",
    "ScheduledInstanceRecurrenceRequestTypeDef",
    "ScheduledInstanceRecurrenceTypeDef",
    "ScheduledInstanceTypeDef",
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    "ScheduledInstancesEbsTypeDef",
    "ScheduledInstancesIamInstanceProfileTypeDef",
    "ScheduledInstancesIpv6AddressTypeDef",
    "ScheduledInstancesLaunchSpecificationTypeDef",
    "ScheduledInstancesMonitoringTypeDef",
    "ScheduledInstancesNetworkInterfaceTypeDef",
    "ScheduledInstancesPlacementTypeDef",
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    "SearchLocalGatewayRoutesRequestRequestTypeDef",
    "SearchLocalGatewayRoutesResultTypeDef",
    "SearchTransitGatewayMulticastGroupsRequestRequestTypeDef",
    "SearchTransitGatewayMulticastGroupsResultTypeDef",
    "SearchTransitGatewayRoutesRequestRequestTypeDef",
    "SearchTransitGatewayRoutesResultTypeDef",
    "SecurityGroupForVpcTypeDef",
    "SecurityGroupIdentifierTypeDef",
    "SecurityGroupReferenceTypeDef",
    "SecurityGroupRuleDescriptionTypeDef",
    "SecurityGroupRuleRequestTypeDef",
    "SecurityGroupRuleTypeDef",
    "SecurityGroupRuleUpdateTypeDef",
    "SecurityGroupTypeDef",
    "SendDiagnosticInterruptRequestRequestTypeDef",
    "ServiceConfigurationTypeDef",
    "ServiceDetailTypeDef",
    "ServiceResourceClassicAddressRequestTypeDef",
    "ServiceResourceDhcpOptionsRequestTypeDef",
    "ServiceResourceImageRequestTypeDef",
    "ServiceResourceInstanceRequestTypeDef",
    "ServiceResourceInternetGatewayRequestTypeDef",
    "ServiceResourceKeyPairRequestTypeDef",
    "ServiceResourceNetworkAclRequestTypeDef",
    "ServiceResourceNetworkInterfaceAssociationRequestTypeDef",
    "ServiceResourceNetworkInterfaceRequestTypeDef",
    "ServiceResourcePlacementGroupRequestTypeDef",
    "ServiceResourceRouteRequestTypeDef",
    "ServiceResourceRouteTableAssociationRequestTypeDef",
    "ServiceResourceRouteTableRequestTypeDef",
    "ServiceResourceSecurityGroupRequestTypeDef",
    "ServiceResourceSnapshotRequestTypeDef",
    "ServiceResourceSubnetRequestTypeDef",
    "ServiceResourceTagRequestTypeDef",
    "ServiceResourceVolumeRequestTypeDef",
    "ServiceResourceVpcAddressRequestTypeDef",
    "ServiceResourceVpcPeeringConnectionRequestTypeDef",
    "ServiceResourceVpcRequestTypeDef",
    "ServiceTypeDetailTypeDef",
    "SlotDateTimeRangeRequestTypeDef",
    "SlotStartTimeRangeRequestTypeDef",
    "SnapshotDetailTypeDef",
    "SnapshotDiskContainerTypeDef",
    "SnapshotInfoTypeDef",
    "SnapshotRecycleBinInfoTypeDef",
    "SnapshotResponseMetadataTypeDef",
    "SnapshotTaskDetailTypeDef",
    "SnapshotTierStatusTypeDef",
    "SnapshotTypeDef",
    "SpotCapacityRebalanceTypeDef",
    "SpotDatafeedSubscriptionTypeDef",
    "SpotFleetLaunchSpecificationTypeDef",
    "SpotFleetMonitoringTypeDef",
    "SpotFleetRequestConfigDataTypeDef",
    "SpotFleetRequestConfigTypeDef",
    "SpotFleetTagSpecificationTypeDef",
    "SpotInstanceRequestTypeDef",
    "SpotInstanceStateFaultTypeDef",
    "SpotInstanceStatusTypeDef",
    "SpotMaintenanceStrategiesTypeDef",
    "SpotMarketOptionsTypeDef",
    "SpotOptionsRequestTypeDef",
    "SpotOptionsTypeDef",
    "SpotPlacementScoreTypeDef",
    "SpotPlacementTypeDef",
    "SpotPriceTypeDef",
    "StaleIpPermissionTypeDef",
    "StaleSecurityGroupTypeDef",
    "StartInstancesRequestInstanceTypeDef",
    "StartInstancesRequestRequestTypeDef",
    "StartInstancesResultTypeDef",
    "StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    "StartNetworkInsightsAccessScopeAnalysisResultTypeDef",
    "StartNetworkInsightsAnalysisRequestRequestTypeDef",
    "StartNetworkInsightsAnalysisResultTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef",
    "StartVpcEndpointServicePrivateDnsVerificationResultTypeDef",
    "StateReasonTypeDef",
    "StopInstancesRequestInstanceTypeDef",
    "StopInstancesRequestRequestTypeDef",
    "StopInstancesResultTypeDef",
    "StorageLocationTypeDef",
    "StorageTypeDef",
    "StoreImageTaskResultTypeDef",
    "SubnetAssociationTypeDef",
    "SubnetCidrBlockStateTypeDef",
    "SubnetCidrReservationTypeDef",
    "SubnetConfigurationTypeDef",
    "SubnetIpv6CidrBlockAssociationTypeDef",
    "SubnetTypeDef",
    "SubscriptionTypeDef",
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    "TagDescriptionTypeDef",
    "TagSpecificationTypeDef",
    "TagTypeDef",
    "TargetCapacitySpecificationRequestTypeDef",
    "TargetCapacitySpecificationTypeDef",
    "TargetConfigurationRequestTypeDef",
    "TargetConfigurationTypeDef",
    "TargetGroupTypeDef",
    "TargetGroupsConfigTypeDef",
    "TargetNetworkTypeDef",
    "TargetReservationValueTypeDef",
    "TerminateClientVpnConnectionsRequestRequestTypeDef",
    "TerminateClientVpnConnectionsResultTypeDef",
    "TerminateConnectionStatusTypeDef",
    "TerminateInstancesRequestInstanceTypeDef",
    "TerminateInstancesRequestRequestTypeDef",
    "TerminateInstancesResultTypeDef",
    "ThroughResourcesStatementRequestTypeDef",
    "ThroughResourcesStatementTypeDef",
    "TotalLocalStorageGBRequestTypeDef",
    "TotalLocalStorageGBTypeDef",
    "TrafficMirrorFilterRuleTypeDef",
    "TrafficMirrorFilterTypeDef",
    "TrafficMirrorPortRangeRequestTypeDef",
    "TrafficMirrorPortRangeTypeDef",
    "TrafficMirrorSessionTypeDef",
    "TrafficMirrorTargetTypeDef",
    "TransitGatewayAssociationTypeDef",
    "TransitGatewayAttachmentAssociationTypeDef",
    "TransitGatewayAttachmentBgpConfigurationTypeDef",
    "TransitGatewayAttachmentPropagationTypeDef",
    "TransitGatewayAttachmentTypeDef",
    "TransitGatewayConnectOptionsTypeDef",
    "TransitGatewayConnectPeerConfigurationTypeDef",
    "TransitGatewayConnectPeerTypeDef",
    "TransitGatewayConnectRequestBgpOptionsTypeDef",
    "TransitGatewayConnectTypeDef",
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    "TransitGatewayMulticastDomainAssociationTypeDef",
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    "TransitGatewayMulticastDomainOptionsTypeDef",
    "TransitGatewayMulticastDomainTypeDef",
    "TransitGatewayMulticastGroupTypeDef",
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    "TransitGatewayOptionsTypeDef",
    "TransitGatewayPeeringAttachmentOptionsTypeDef",
    "TransitGatewayPeeringAttachmentTypeDef",
    "TransitGatewayPolicyRuleMetaDataTypeDef",
    "TransitGatewayPolicyRuleTypeDef",
    "TransitGatewayPolicyTableAssociationTypeDef",
    "TransitGatewayPolicyTableEntryTypeDef",
    "TransitGatewayPolicyTableTypeDef",
    "TransitGatewayPrefixListAttachmentTypeDef",
    "TransitGatewayPrefixListReferenceTypeDef",
    "TransitGatewayPropagationTypeDef",
    "TransitGatewayRequestOptionsTypeDef",
    "TransitGatewayRouteAttachmentTypeDef",
    "TransitGatewayRouteTableAnnouncementTypeDef",
    "TransitGatewayRouteTableAssociationTypeDef",
    "TransitGatewayRouteTablePropagationTypeDef",
    "TransitGatewayRouteTableRouteTypeDef",
    "TransitGatewayRouteTableTypeDef",
    "TransitGatewayRouteTypeDef",
    "TransitGatewayTypeDef",
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    "TransitGatewayVpcAttachmentTypeDef",
    "TrunkInterfaceAssociationTypeDef",
    "TunnelOptionTypeDef",
    "UnassignIpv6AddressesRequestRequestTypeDef",
    "UnassignIpv6AddressesResultTypeDef",
    "UnassignPrivateIpAddressesRequestNetworkInterfaceTypeDef",
    "UnassignPrivateIpAddressesRequestRequestTypeDef",
    "UnassignPrivateNatGatewayAddressRequestRequestTypeDef",
    "UnassignPrivateNatGatewayAddressResultTypeDef",
    "UnmonitorInstancesRequestInstanceTypeDef",
    "UnmonitorInstancesRequestRequestTypeDef",
    "UnmonitorInstancesResultTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    "UnsuccessfulItemErrorTypeDef",
    "UnsuccessfulItemTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef",
    "UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef",
    "UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef",
    "UserBucketDetailsTypeDef",
    "UserBucketTypeDef",
    "UserDataTypeDef",
    "UserIdGroupPairTypeDef",
    "VCpuCountRangeRequestTypeDef",
    "VCpuCountRangeTypeDef",
    "VCpuInfoTypeDef",
    "ValidationErrorTypeDef",
    "ValidationWarningTypeDef",
    "VerifiedAccessEndpointEniOptionsTypeDef",
    "VerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    "VerifiedAccessEndpointStatusTypeDef",
    "VerifiedAccessEndpointTypeDef",
    "VerifiedAccessGroupTypeDef",
    "VerifiedAccessInstanceLoggingConfigurationTypeDef",
    "VerifiedAccessInstanceTypeDef",
    "VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef",
    "VerifiedAccessLogCloudWatchLogsDestinationTypeDef",
    "VerifiedAccessLogDeliveryStatusTypeDef",
    "VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef",
    "VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef",
    "VerifiedAccessLogOptionsTypeDef",
    "VerifiedAccessLogS3DestinationOptionsTypeDef",
    "VerifiedAccessLogS3DestinationTypeDef",
    "VerifiedAccessLogsTypeDef",
    "VerifiedAccessSseSpecificationRequestTypeDef",
    "VerifiedAccessSseSpecificationResponseTypeDef",
    "VerifiedAccessTrustProviderCondensedTypeDef",
    "VerifiedAccessTrustProviderTypeDef",
    "VgwTelemetryTypeDef",
    "VolumeAttachmentResponseMetadataTypeDef",
    "VolumeAttachmentTypeDef",
    "VolumeDetailTypeDef",
    "VolumeModificationTypeDef",
    "VolumeResponseMetadataTypeDef",
    "VolumeStatusActionTypeDef",
    "VolumeStatusAttachmentStatusTypeDef",
    "VolumeStatusDetailsTypeDef",
    "VolumeStatusEventTypeDef",
    "VolumeStatusInfoTypeDef",
    "VolumeStatusItemTypeDef",
    "VolumeTypeDef",
    "VpcAttachmentTypeDef",
    "VpcCidrBlockAssociationTypeDef",
    "VpcCidrBlockStateTypeDef",
    "VpcClassicLinkTypeDef",
    "VpcEndpointConnectionTypeDef",
    "VpcEndpointTypeDef",
    "VpcIpv6CidrBlockAssociationTypeDef",
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    "VpcPeeringConnectionStateReasonTypeDef",
    "VpcPeeringConnectionTypeDef",
    "VpcPeeringConnectionVpcInfoTypeDef",
    "VpcTypeDef",
    "VpnConnectionDeviceTypeTypeDef",
    "VpnConnectionOptionsSpecificationTypeDef",
    "VpnConnectionOptionsTypeDef",
    "VpnConnectionTypeDef",
    "VpnGatewayTypeDef",
    "VpnStaticRouteTypeDef",
    "VpnTunnelLogOptionsSpecificationTypeDef",
    "VpnTunnelLogOptionsTypeDef",
    "VpnTunnelOptionsSpecificationTypeDef",
    "WaiterConfigTypeDef",
    "WithdrawByoipCidrRequestRequestTypeDef",
    "WithdrawByoipCidrResultTypeDef",
)

AcceleratorCountRequestTypeDef = TypedDict(
    "AcceleratorCountRequestTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

AcceleratorCountTypeDef = TypedDict(
    "AcceleratorCountTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

AcceleratorTotalMemoryMiBRequestTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBRequestTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

AcceleratorTotalMemoryMiBTypeDef = TypedDict(
    "AcceleratorTotalMemoryMiBTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

_RequiredAcceptAddressTransferRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptAddressTransferRequestRequestTypeDef",
    {
        "Address": str,
    },
)
_OptionalAcceptAddressTransferRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptAddressTransferRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class AcceptAddressTransferRequestRequestTypeDef(
    _RequiredAcceptAddressTransferRequestRequestTypeDef,
    _OptionalAcceptAddressTransferRequestRequestTypeDef,
):
    pass

AcceptAddressTransferResultTypeDef = TypedDict(
    "AcceptAddressTransferResultTypeDef",
    {
        "AddressTransfer": "AddressTransferTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAcceptReservedInstancesExchangeQuoteRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptReservedInstancesExchangeQuoteRequestRequestTypeDef",
    {
        "ReservedInstanceIds": List[str],
    },
)
_OptionalAcceptReservedInstancesExchangeQuoteRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptReservedInstancesExchangeQuoteRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TargetConfigurations": List["TargetConfigurationRequestTypeDef"],
    },
    total=False,
)

class AcceptReservedInstancesExchangeQuoteRequestRequestTypeDef(
    _RequiredAcceptReservedInstancesExchangeQuoteRequestRequestTypeDef,
    _OptionalAcceptReservedInstancesExchangeQuoteRequestRequestTypeDef,
):
    pass

AcceptReservedInstancesExchangeQuoteResultTypeDef = TypedDict(
    "AcceptReservedInstancesExchangeQuoteResultTypeDef",
    {
        "ExchangeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "AcceptTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalAcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef(
    _RequiredAcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef,
    _OptionalAcceptTransitGatewayPeeringAttachmentRequestRequestTypeDef,
):
    pass

AcceptTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "AcceptTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAcceptTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalAcceptTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AcceptTransitGatewayVpcAttachmentRequestRequestTypeDef(
    _RequiredAcceptTransitGatewayVpcAttachmentRequestRequestTypeDef,
    _OptionalAcceptTransitGatewayVpcAttachmentRequestRequestTypeDef,
):
    pass

AcceptTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "AcceptTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAcceptVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointIds": List[str],
    },
)
_OptionalAcceptVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AcceptVpcEndpointConnectionsRequestRequestTypeDef(
    _RequiredAcceptVpcEndpointConnectionsRequestRequestTypeDef,
    _OptionalAcceptVpcEndpointConnectionsRequestRequestTypeDef,
):
    pass

AcceptVpcEndpointConnectionsResultTypeDef = TypedDict(
    "AcceptVpcEndpointConnectionsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAcceptVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredAcceptVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
    },
)
_OptionalAcceptVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalAcceptVpcPeeringConnectionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AcceptVpcPeeringConnectionRequestRequestTypeDef(
    _RequiredAcceptVpcPeeringConnectionRequestRequestTypeDef,
    _OptionalAcceptVpcPeeringConnectionRequestRequestTypeDef,
):
    pass

AcceptVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

AcceptVpcPeeringConnectionResultTypeDef = TypedDict(
    "AcceptVpcPeeringConnectionResultTypeDef",
    {
        "VpcPeeringConnection": "VpcPeeringConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AccessScopeAnalysisFindingTypeDef = TypedDict(
    "AccessScopeAnalysisFindingTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "NetworkInsightsAccessScopeId": str,
        "FindingId": str,
        "FindingComponents": List["PathComponentTypeDef"],
    },
    total=False,
)

AccessScopePathRequestTypeDef = TypedDict(
    "AccessScopePathRequestTypeDef",
    {
        "Source": "PathStatementRequestTypeDef",
        "Destination": "PathStatementRequestTypeDef",
        "ThroughResources": List["ThroughResourcesStatementRequestTypeDef"],
    },
    total=False,
)

AccessScopePathTypeDef = TypedDict(
    "AccessScopePathTypeDef",
    {
        "Source": "PathStatementTypeDef",
        "Destination": "PathStatementTypeDef",
        "ThroughResources": List["ThroughResourcesStatementTypeDef"],
    },
    total=False,
)

AccountAttributeTypeDef = TypedDict(
    "AccountAttributeTypeDef",
    {
        "AttributeName": str,
        "AttributeValues": List["AccountAttributeValueTypeDef"],
    },
    total=False,
)

AccountAttributeValueTypeDef = TypedDict(
    "AccountAttributeValueTypeDef",
    {
        "AttributeValue": str,
    },
    total=False,
)

ActiveInstanceTypeDef = TypedDict(
    "ActiveInstanceTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "SpotInstanceRequestId": str,
        "InstanceHealth": InstanceHealthStatusType,
    },
    total=False,
)

AddIpamOperatingRegionTypeDef = TypedDict(
    "AddIpamOperatingRegionTypeDef",
    {
        "RegionName": str,
    },
    total=False,
)

_RequiredAddPrefixListEntryTypeDef = TypedDict(
    "_RequiredAddPrefixListEntryTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalAddPrefixListEntryTypeDef = TypedDict(
    "_OptionalAddPrefixListEntryTypeDef",
    {
        "Description": str,
    },
    total=False,
)

class AddPrefixListEntryTypeDef(
    _RequiredAddPrefixListEntryTypeDef, _OptionalAddPrefixListEntryTypeDef
):
    pass

AddedPrincipalTypeDef = TypedDict(
    "AddedPrincipalTypeDef",
    {
        "PrincipalType": PrincipalTypeType,
        "Principal": str,
        "ServicePermissionId": str,
        "ServiceId": str,
    },
    total=False,
)

AdditionalDetailTypeDef = TypedDict(
    "AdditionalDetailTypeDef",
    {
        "AdditionalDetailType": str,
        "Component": "AnalysisComponentTypeDef",
        "VpcEndpointService": "AnalysisComponentTypeDef",
        "RuleOptions": List["RuleOptionTypeDef"],
        "RuleGroupTypePairs": List["RuleGroupTypePairTypeDef"],
        "RuleGroupRuleOptionsPairs": List["RuleGroupRuleOptionsPairTypeDef"],
        "ServiceName": str,
        "LoadBalancers": List["AnalysisComponentTypeDef"],
    },
    total=False,
)

AddressAttributeTypeDef = TypedDict(
    "AddressAttributeTypeDef",
    {
        "PublicIp": str,
        "AllocationId": str,
        "PtrRecord": str,
        "PtrRecordUpdate": "PtrUpdateStatusTypeDef",
    },
    total=False,
)

AddressTransferTypeDef = TypedDict(
    "AddressTransferTypeDef",
    {
        "PublicIp": str,
        "AllocationId": str,
        "TransferAccountId": str,
        "TransferOfferExpirationTimestamp": datetime,
        "TransferOfferAcceptedTimestamp": datetime,
        "AddressTransferStatus": AddressTransferStatusType,
    },
    total=False,
)

AddressTypeDef = TypedDict(
    "AddressTypeDef",
    {
        "InstanceId": str,
        "PublicIp": str,
        "AllocationId": str,
        "AssociationId": str,
        "Domain": DomainTypeType,
        "NetworkInterfaceId": str,
        "NetworkInterfaceOwnerId": str,
        "PrivateIpAddress": str,
        "Tags": List["TagTypeDef"],
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "CustomerOwnedIp": str,
        "CustomerOwnedIpv4Pool": str,
        "CarrierIp": str,
    },
    total=False,
)

_RequiredAdvertiseByoipCidrRequestRequestTypeDef = TypedDict(
    "_RequiredAdvertiseByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalAdvertiseByoipCidrRequestRequestTypeDef = TypedDict(
    "_OptionalAdvertiseByoipCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AdvertiseByoipCidrRequestRequestTypeDef(
    _RequiredAdvertiseByoipCidrRequestRequestTypeDef,
    _OptionalAdvertiseByoipCidrRequestRequestTypeDef,
):
    pass

AdvertiseByoipCidrResultTypeDef = TypedDict(
    "AdvertiseByoipCidrResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllocateAddressRequestRequestTypeDef = TypedDict(
    "AllocateAddressRequestRequestTypeDef",
    {
        "Domain": DomainTypeType,
        "Address": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "CustomerOwnedIpv4Pool": str,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

AllocateAddressResultTypeDef = TypedDict(
    "AllocateAddressResultTypeDef",
    {
        "PublicIp": str,
        "AllocationId": str,
        "PublicIpv4Pool": str,
        "NetworkBorderGroup": str,
        "Domain": DomainTypeType,
        "CustomerOwnedIp": str,
        "CustomerOwnedIpv4Pool": str,
        "CarrierIp": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAllocateHostsRequestRequestTypeDef = TypedDict(
    "_RequiredAllocateHostsRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
    },
)
_OptionalAllocateHostsRequestRequestTypeDef = TypedDict(
    "_OptionalAllocateHostsRequestRequestTypeDef",
    {
        "AutoPlacement": AutoPlacementType,
        "ClientToken": str,
        "InstanceType": str,
        "InstanceFamily": str,
        "Quantity": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "HostRecovery": HostRecoveryType,
        "OutpostArn": str,
        "HostMaintenance": HostMaintenanceType,
        "AssetIds": List[str],
    },
    total=False,
)

class AllocateHostsRequestRequestTypeDef(
    _RequiredAllocateHostsRequestRequestTypeDef, _OptionalAllocateHostsRequestRequestTypeDef
):
    pass

AllocateHostsResultTypeDef = TypedDict(
    "AllocateHostsResultTypeDef",
    {
        "HostIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAllocateIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "_RequiredAllocateIpamPoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
    },
)
_OptionalAllocateIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "_OptionalAllocateIpamPoolCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Cidr": str,
        "NetmaskLength": int,
        "ClientToken": str,
        "Description": str,
        "PreviewNextCidr": bool,
        "DisallowedCidrs": List[str],
    },
    total=False,
)

class AllocateIpamPoolCidrRequestRequestTypeDef(
    _RequiredAllocateIpamPoolCidrRequestRequestTypeDef,
    _OptionalAllocateIpamPoolCidrRequestRequestTypeDef,
):
    pass

AllocateIpamPoolCidrResultTypeDef = TypedDict(
    "AllocateIpamPoolCidrResultTypeDef",
    {
        "IpamPoolAllocation": "IpamPoolAllocationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AllowedPrincipalTypeDef = TypedDict(
    "AllowedPrincipalTypeDef",
    {
        "PrincipalType": PrincipalTypeType,
        "Principal": str,
        "ServicePermissionId": str,
        "Tags": List["TagTypeDef"],
        "ServiceId": str,
    },
    total=False,
)

AlternatePathHintTypeDef = TypedDict(
    "AlternatePathHintTypeDef",
    {
        "ComponentId": str,
        "ComponentArn": str,
    },
    total=False,
)

AnalysisAclRuleTypeDef = TypedDict(
    "AnalysisAclRuleTypeDef",
    {
        "Cidr": str,
        "Egress": bool,
        "PortRange": "PortRangeTypeDef",
        "Protocol": str,
        "RuleAction": str,
        "RuleNumber": int,
    },
    total=False,
)

AnalysisComponentTypeDef = TypedDict(
    "AnalysisComponentTypeDef",
    {
        "Id": str,
        "Arn": str,
        "Name": str,
    },
    total=False,
)

AnalysisLoadBalancerListenerTypeDef = TypedDict(
    "AnalysisLoadBalancerListenerTypeDef",
    {
        "LoadBalancerPort": int,
        "InstancePort": int,
    },
    total=False,
)

AnalysisLoadBalancerTargetTypeDef = TypedDict(
    "AnalysisLoadBalancerTargetTypeDef",
    {
        "Address": str,
        "AvailabilityZone": str,
        "Instance": "AnalysisComponentTypeDef",
        "Port": int,
    },
    total=False,
)

AnalysisPacketHeaderTypeDef = TypedDict(
    "AnalysisPacketHeaderTypeDef",
    {
        "DestinationAddresses": List[str],
        "DestinationPortRanges": List["PortRangeTypeDef"],
        "Protocol": str,
        "SourceAddresses": List[str],
        "SourcePortRanges": List["PortRangeTypeDef"],
    },
    total=False,
)

AnalysisRouteTableRouteTypeDef = TypedDict(
    "AnalysisRouteTableRouteTypeDef",
    {
        "DestinationCidr": str,
        "DestinationPrefixListId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "NatGatewayId": str,
        "NetworkInterfaceId": str,
        "Origin": str,
        "TransitGatewayId": str,
        "VpcPeeringConnectionId": str,
        "State": str,
        "CarrierGatewayId": str,
        "CoreNetworkArn": str,
        "LocalGatewayId": str,
    },
    total=False,
)

AnalysisSecurityGroupRuleTypeDef = TypedDict(
    "AnalysisSecurityGroupRuleTypeDef",
    {
        "Cidr": str,
        "Direction": str,
        "SecurityGroupId": str,
        "PortRange": "PortRangeTypeDef",
        "PrefixListId": str,
        "Protocol": str,
    },
    total=False,
)

_RequiredApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "VpcId": str,
        "SecurityGroupIds": List[str],
    },
)
_OptionalApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef(
    _RequiredApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef,
    _OptionalApplySecurityGroupsToClientVpnTargetNetworkRequestRequestTypeDef,
):
    pass

ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef = TypedDict(
    "ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef",
    {
        "SecurityGroupIds": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssignIpv6AddressesRequestRequestTypeDef = TypedDict(
    "_RequiredAssignIpv6AddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalAssignIpv6AddressesRequestRequestTypeDef = TypedDict(
    "_OptionalAssignIpv6AddressesRequestRequestTypeDef",
    {
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List[str],
        "Ipv6PrefixCount": int,
        "Ipv6Prefixes": List[str],
    },
    total=False,
)

class AssignIpv6AddressesRequestRequestTypeDef(
    _RequiredAssignIpv6AddressesRequestRequestTypeDef,
    _OptionalAssignIpv6AddressesRequestRequestTypeDef,
):
    pass

AssignIpv6AddressesResultTypeDef = TypedDict(
    "AssignIpv6AddressesResultTypeDef",
    {
        "AssignedIpv6Addresses": List[str],
        "AssignedIpv6Prefixes": List[str],
        "NetworkInterfaceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssignPrivateIpAddressesRequestNetworkInterfaceTypeDef = TypedDict(
    "AssignPrivateIpAddressesRequestNetworkInterfaceTypeDef",
    {
        "AllowReassignment": bool,
        "PrivateIpAddresses": List[str],
        "SecondaryPrivateIpAddressCount": int,
        "Ipv4Prefixes": List[str],
        "Ipv4PrefixCount": int,
    },
    total=False,
)

_RequiredAssignPrivateIpAddressesRequestRequestTypeDef = TypedDict(
    "_RequiredAssignPrivateIpAddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalAssignPrivateIpAddressesRequestRequestTypeDef = TypedDict(
    "_OptionalAssignPrivateIpAddressesRequestRequestTypeDef",
    {
        "AllowReassignment": bool,
        "PrivateIpAddresses": List[str],
        "SecondaryPrivateIpAddressCount": int,
        "Ipv4Prefixes": List[str],
        "Ipv4PrefixCount": int,
    },
    total=False,
)

class AssignPrivateIpAddressesRequestRequestTypeDef(
    _RequiredAssignPrivateIpAddressesRequestRequestTypeDef,
    _OptionalAssignPrivateIpAddressesRequestRequestTypeDef,
):
    pass

AssignPrivateIpAddressesResultTypeDef = TypedDict(
    "AssignPrivateIpAddressesResultTypeDef",
    {
        "NetworkInterfaceId": str,
        "AssignedPrivateIpAddresses": List["AssignedPrivateIpAddressTypeDef"],
        "AssignedIpv4Prefixes": List["Ipv4PrefixSpecificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssignPrivateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "_RequiredAssignPrivateNatGatewayAddressRequestRequestTypeDef",
    {
        "NatGatewayId": str,
    },
)
_OptionalAssignPrivateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "_OptionalAssignPrivateNatGatewayAddressRequestRequestTypeDef",
    {
        "PrivateIpAddresses": List[str],
        "PrivateIpAddressCount": int,
        "DryRun": bool,
    },
    total=False,
)

class AssignPrivateNatGatewayAddressRequestRequestTypeDef(
    _RequiredAssignPrivateNatGatewayAddressRequestRequestTypeDef,
    _OptionalAssignPrivateNatGatewayAddressRequestRequestTypeDef,
):
    pass

AssignPrivateNatGatewayAddressResultTypeDef = TypedDict(
    "AssignPrivateNatGatewayAddressResultTypeDef",
    {
        "NatGatewayId": str,
        "NatGatewayAddresses": List["NatGatewayAddressTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssignedPrivateIpAddressTypeDef = TypedDict(
    "AssignedPrivateIpAddressTypeDef",
    {
        "PrivateIpAddress": str,
    },
    total=False,
)

AssociateAddressRequestClassicAddressTypeDef = TypedDict(
    "AssociateAddressRequestClassicAddressTypeDef",
    {
        "AllocationId": str,
        "InstanceId": str,
        "AllowReassociation": bool,
        "DryRun": bool,
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

AssociateAddressRequestRequestTypeDef = TypedDict(
    "AssociateAddressRequestRequestTypeDef",
    {
        "AllocationId": str,
        "InstanceId": str,
        "PublicIp": str,
        "AllowReassociation": bool,
        "DryRun": bool,
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

AssociateAddressRequestVpcAddressTypeDef = TypedDict(
    "AssociateAddressRequestVpcAddressTypeDef",
    {
        "InstanceId": str,
        "PublicIp": str,
        "AllowReassociation": bool,
        "DryRun": bool,
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

AssociateAddressResultTypeDef = TypedDict(
    "AssociateAddressResultTypeDef",
    {
        "AssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "SubnetId": str,
    },
)
_OptionalAssociateClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class AssociateClientVpnTargetNetworkRequestRequestTypeDef(
    _RequiredAssociateClientVpnTargetNetworkRequestRequestTypeDef,
    _OptionalAssociateClientVpnTargetNetworkRequestRequestTypeDef,
):
    pass

AssociateClientVpnTargetNetworkResultTypeDef = TypedDict(
    "AssociateClientVpnTargetNetworkResultTypeDef",
    {
        "AssociationId": str,
        "Status": "AssociationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateDhcpOptionsRequestDhcpOptionsTypeDef = TypedDict(
    "_RequiredAssociateDhcpOptionsRequestDhcpOptionsTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalAssociateDhcpOptionsRequestDhcpOptionsTypeDef = TypedDict(
    "_OptionalAssociateDhcpOptionsRequestDhcpOptionsTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AssociateDhcpOptionsRequestDhcpOptionsTypeDef(
    _RequiredAssociateDhcpOptionsRequestDhcpOptionsTypeDef,
    _OptionalAssociateDhcpOptionsRequestDhcpOptionsTypeDef,
):
    pass

_RequiredAssociateDhcpOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpOptionsId": str,
        "VpcId": str,
    },
)
_OptionalAssociateDhcpOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateDhcpOptionsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AssociateDhcpOptionsRequestRequestTypeDef(
    _RequiredAssociateDhcpOptionsRequestRequestTypeDef,
    _OptionalAssociateDhcpOptionsRequestRequestTypeDef,
):
    pass

_RequiredAssociateDhcpOptionsRequestVpcTypeDef = TypedDict(
    "_RequiredAssociateDhcpOptionsRequestVpcTypeDef",
    {
        "DhcpOptionsId": str,
    },
)
_OptionalAssociateDhcpOptionsRequestVpcTypeDef = TypedDict(
    "_OptionalAssociateDhcpOptionsRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AssociateDhcpOptionsRequestVpcTypeDef(
    _RequiredAssociateDhcpOptionsRequestVpcTypeDef, _OptionalAssociateDhcpOptionsRequestVpcTypeDef
):
    pass

_RequiredAssociateEnclaveCertificateIamRoleRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "RoleArn": str,
    },
)
_OptionalAssociateEnclaveCertificateIamRoleRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AssociateEnclaveCertificateIamRoleRequestRequestTypeDef(
    _RequiredAssociateEnclaveCertificateIamRoleRequestRequestTypeDef,
    _OptionalAssociateEnclaveCertificateIamRoleRequestRequestTypeDef,
):
    pass

AssociateEnclaveCertificateIamRoleResultTypeDef = TypedDict(
    "AssociateEnclaveCertificateIamRoleResultTypeDef",
    {
        "CertificateS3BucketName": str,
        "CertificateS3ObjectKey": str,
        "EncryptionKmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateIamInstanceProfileRequestRequestTypeDef = TypedDict(
    "AssociateIamInstanceProfileRequestRequestTypeDef",
    {
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "InstanceId": str,
    },
)

AssociateIamInstanceProfileResultTypeDef = TypedDict(
    "AssociateIamInstanceProfileResultTypeDef",
    {
        "IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "AssociationTarget": "InstanceEventWindowAssociationRequestTypeDef",
    },
)
_OptionalAssociateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateInstanceEventWindowRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AssociateInstanceEventWindowRequestRequestTypeDef(
    _RequiredAssociateInstanceEventWindowRequestRequestTypeDef,
    _OptionalAssociateInstanceEventWindowRequestRequestTypeDef,
):
    pass

AssociateInstanceEventWindowResultTypeDef = TypedDict(
    "AssociateInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": "InstanceEventWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "IpamId": str,
        "IpamResourceDiscoveryId": str,
    },
)
_OptionalAssociateIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class AssociateIpamResourceDiscoveryRequestRequestTypeDef(
    _RequiredAssociateIpamResourceDiscoveryRequestRequestTypeDef,
    _OptionalAssociateIpamResourceDiscoveryRequestRequestTypeDef,
):
    pass

AssociateIpamResourceDiscoveryResultTypeDef = TypedDict(
    "AssociateIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscoveryAssociation": "IpamResourceDiscoveryAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateNatGatewayAddressRequestRequestTypeDef",
    {
        "NatGatewayId": str,
        "AllocationIds": List[str],
    },
)
_OptionalAssociateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateNatGatewayAddressRequestRequestTypeDef",
    {
        "PrivateIpAddresses": List[str],
        "DryRun": bool,
    },
    total=False,
)

class AssociateNatGatewayAddressRequestRequestTypeDef(
    _RequiredAssociateNatGatewayAddressRequestRequestTypeDef,
    _OptionalAssociateNatGatewayAddressRequestRequestTypeDef,
):
    pass

AssociateNatGatewayAddressResultTypeDef = TypedDict(
    "AssociateNatGatewayAddressResultTypeDef",
    {
        "NatGatewayId": str,
        "NatGatewayAddresses": List["NatGatewayAddressTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateRouteTableRequestRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalAssociateRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateRouteTableRequestRequestTypeDef",
    {
        "DryRun": bool,
        "SubnetId": str,
        "GatewayId": str,
    },
    total=False,
)

class AssociateRouteTableRequestRequestTypeDef(
    _RequiredAssociateRouteTableRequestRequestTypeDef,
    _OptionalAssociateRouteTableRequestRequestTypeDef,
):
    pass

AssociateRouteTableRequestRouteTableTypeDef = TypedDict(
    "AssociateRouteTableRequestRouteTableTypeDef",
    {
        "DryRun": bool,
        "SubnetId": str,
        "GatewayId": str,
    },
    total=False,
)

AssociateRouteTableResultTypeDef = TypedDict(
    "AssociateRouteTableResultTypeDef",
    {
        "AssociationId": str,
        "AssociationState": "RouteTableAssociationStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociateSubnetCidrBlockRequestRequestTypeDef = TypedDict(
    "AssociateSubnetCidrBlockRequestRequestTypeDef",
    {
        "Ipv6CidrBlock": str,
        "SubnetId": str,
    },
)

AssociateSubnetCidrBlockResultTypeDef = TypedDict(
    "AssociateSubnetCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "SubnetIpv6CidrBlockAssociationTypeDef",
        "SubnetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": List[str],
    },
)
_OptionalAssociateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AssociateTransitGatewayMulticastDomainRequestRequestTypeDef(
    _RequiredAssociateTransitGatewayMulticastDomainRequestRequestTypeDef,
    _OptionalAssociateTransitGatewayMulticastDomainRequestRequestTypeDef,
):
    pass

AssociateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "AssociateTransitGatewayMulticastDomainResultTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalAssociateTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AssociateTransitGatewayPolicyTableRequestRequestTypeDef(
    _RequiredAssociateTransitGatewayPolicyTableRequestRequestTypeDef,
    _OptionalAssociateTransitGatewayPolicyTableRequestRequestTypeDef,
):
    pass

AssociateTransitGatewayPolicyTableResultTypeDef = TypedDict(
    "AssociateTransitGatewayPolicyTableResultTypeDef",
    {
        "Association": "TransitGatewayPolicyTableAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalAssociateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AssociateTransitGatewayRouteTableRequestRequestTypeDef(
    _RequiredAssociateTransitGatewayRouteTableRequestRequestTypeDef,
    _OptionalAssociateTransitGatewayRouteTableRequestRequestTypeDef,
):
    pass

AssociateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "AssociateTransitGatewayRouteTableResultTypeDef",
    {
        "Association": "TransitGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateTrunkInterfaceRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateTrunkInterfaceRequestRequestTypeDef",
    {
        "BranchInterfaceId": str,
        "TrunkInterfaceId": str,
    },
)
_OptionalAssociateTrunkInterfaceRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateTrunkInterfaceRequestRequestTypeDef",
    {
        "VlanId": int,
        "GreKey": int,
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class AssociateTrunkInterfaceRequestRequestTypeDef(
    _RequiredAssociateTrunkInterfaceRequestRequestTypeDef,
    _OptionalAssociateTrunkInterfaceRequestRequestTypeDef,
):
    pass

AssociateTrunkInterfaceResultTypeDef = TypedDict(
    "AssociateTrunkInterfaceResultTypeDef",
    {
        "InterfaceAssociation": "TrunkInterfaceAssociationTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateVpcCidrBlockRequestRequestTypeDef = TypedDict(
    "_RequiredAssociateVpcCidrBlockRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalAssociateVpcCidrBlockRequestRequestTypeDef = TypedDict(
    "_OptionalAssociateVpcCidrBlockRequestRequestTypeDef",
    {
        "AmazonProvidedIpv6CidrBlock": bool,
        "CidrBlock": str,
        "Ipv6CidrBlockNetworkBorderGroup": str,
        "Ipv6Pool": str,
        "Ipv6CidrBlock": str,
        "Ipv4IpamPoolId": str,
        "Ipv4NetmaskLength": int,
        "Ipv6IpamPoolId": str,
        "Ipv6NetmaskLength": int,
    },
    total=False,
)

class AssociateVpcCidrBlockRequestRequestTypeDef(
    _RequiredAssociateVpcCidrBlockRequestRequestTypeDef,
    _OptionalAssociateVpcCidrBlockRequestRequestTypeDef,
):
    pass

AssociateVpcCidrBlockResultTypeDef = TypedDict(
    "AssociateVpcCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "VpcIpv6CidrBlockAssociationTypeDef",
        "CidrBlockAssociation": "VpcCidrBlockAssociationTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AssociatedRoleTypeDef = TypedDict(
    "AssociatedRoleTypeDef",
    {
        "AssociatedRoleArn": str,
        "CertificateS3BucketName": str,
        "CertificateS3ObjectKey": str,
        "EncryptionKmsKeyId": str,
    },
    total=False,
)

AssociatedTargetNetworkTypeDef = TypedDict(
    "AssociatedTargetNetworkTypeDef",
    {
        "NetworkId": str,
        "NetworkType": Literal["vpc"],
    },
    total=False,
)

AssociationStatusTypeDef = TypedDict(
    "AssociationStatusTypeDef",
    {
        "Code": AssociationStatusCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredAthenaIntegrationTypeDef = TypedDict(
    "_RequiredAthenaIntegrationTypeDef",
    {
        "IntegrationResultS3DestinationArn": str,
        "PartitionLoadFrequency": PartitionLoadFrequencyType,
    },
)
_OptionalAthenaIntegrationTypeDef = TypedDict(
    "_OptionalAthenaIntegrationTypeDef",
    {
        "PartitionStartDate": Union[datetime, str],
        "PartitionEndDate": Union[datetime, str],
    },
    total=False,
)

class AthenaIntegrationTypeDef(
    _RequiredAthenaIntegrationTypeDef, _OptionalAthenaIntegrationTypeDef
):
    pass

_RequiredAttachClassicLinkVpcRequestInstanceTypeDef = TypedDict(
    "_RequiredAttachClassicLinkVpcRequestInstanceTypeDef",
    {
        "Groups": List[str],
        "VpcId": str,
    },
)
_OptionalAttachClassicLinkVpcRequestInstanceTypeDef = TypedDict(
    "_OptionalAttachClassicLinkVpcRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachClassicLinkVpcRequestInstanceTypeDef(
    _RequiredAttachClassicLinkVpcRequestInstanceTypeDef,
    _OptionalAttachClassicLinkVpcRequestInstanceTypeDef,
):
    pass

_RequiredAttachClassicLinkVpcRequestRequestTypeDef = TypedDict(
    "_RequiredAttachClassicLinkVpcRequestRequestTypeDef",
    {
        "Groups": List[str],
        "InstanceId": str,
        "VpcId": str,
    },
)
_OptionalAttachClassicLinkVpcRequestRequestTypeDef = TypedDict(
    "_OptionalAttachClassicLinkVpcRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachClassicLinkVpcRequestRequestTypeDef(
    _RequiredAttachClassicLinkVpcRequestRequestTypeDef,
    _OptionalAttachClassicLinkVpcRequestRequestTypeDef,
):
    pass

_RequiredAttachClassicLinkVpcRequestVpcTypeDef = TypedDict(
    "_RequiredAttachClassicLinkVpcRequestVpcTypeDef",
    {
        "Groups": List[str],
        "InstanceId": str,
    },
)
_OptionalAttachClassicLinkVpcRequestVpcTypeDef = TypedDict(
    "_OptionalAttachClassicLinkVpcRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachClassicLinkVpcRequestVpcTypeDef(
    _RequiredAttachClassicLinkVpcRequestVpcTypeDef, _OptionalAttachClassicLinkVpcRequestVpcTypeDef
):
    pass

AttachClassicLinkVpcResultTypeDef = TypedDict(
    "AttachClassicLinkVpcResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttachInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "_RequiredAttachInternetGatewayRequestInternetGatewayTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalAttachInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "_OptionalAttachInternetGatewayRequestInternetGatewayTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachInternetGatewayRequestInternetGatewayTypeDef(
    _RequiredAttachInternetGatewayRequestInternetGatewayTypeDef,
    _OptionalAttachInternetGatewayRequestInternetGatewayTypeDef,
):
    pass

_RequiredAttachInternetGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredAttachInternetGatewayRequestRequestTypeDef",
    {
        "InternetGatewayId": str,
        "VpcId": str,
    },
)
_OptionalAttachInternetGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalAttachInternetGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachInternetGatewayRequestRequestTypeDef(
    _RequiredAttachInternetGatewayRequestRequestTypeDef,
    _OptionalAttachInternetGatewayRequestRequestTypeDef,
):
    pass

_RequiredAttachInternetGatewayRequestVpcTypeDef = TypedDict(
    "_RequiredAttachInternetGatewayRequestVpcTypeDef",
    {
        "InternetGatewayId": str,
    },
)
_OptionalAttachInternetGatewayRequestVpcTypeDef = TypedDict(
    "_OptionalAttachInternetGatewayRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachInternetGatewayRequestVpcTypeDef(
    _RequiredAttachInternetGatewayRequestVpcTypeDef, _OptionalAttachInternetGatewayRequestVpcTypeDef
):
    pass

_RequiredAttachNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "_RequiredAttachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "DeviceIndex": int,
        "InstanceId": str,
    },
)
_OptionalAttachNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "_OptionalAttachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
        "NetworkCardIndex": int,
        "EnaSrdSpecification": "EnaSrdSpecificationTypeDef",
    },
    total=False,
)

class AttachNetworkInterfaceRequestNetworkInterfaceTypeDef(
    _RequiredAttachNetworkInterfaceRequestNetworkInterfaceTypeDef,
    _OptionalAttachNetworkInterfaceRequestNetworkInterfaceTypeDef,
):
    pass

_RequiredAttachNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "_RequiredAttachNetworkInterfaceRequestRequestTypeDef",
    {
        "DeviceIndex": int,
        "InstanceId": str,
        "NetworkInterfaceId": str,
    },
)
_OptionalAttachNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "_OptionalAttachNetworkInterfaceRequestRequestTypeDef",
    {
        "DryRun": bool,
        "NetworkCardIndex": int,
        "EnaSrdSpecification": "EnaSrdSpecificationTypeDef",
    },
    total=False,
)

class AttachNetworkInterfaceRequestRequestTypeDef(
    _RequiredAttachNetworkInterfaceRequestRequestTypeDef,
    _OptionalAttachNetworkInterfaceRequestRequestTypeDef,
):
    pass

AttachNetworkInterfaceResultTypeDef = TypedDict(
    "AttachNetworkInterfaceResultTypeDef",
    {
        "AttachmentId": str,
        "NetworkCardIndex": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttachVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_RequiredAttachVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "VerifiedAccessTrustProviderId": str,
    },
)
_OptionalAttachVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_OptionalAttachVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class AttachVerifiedAccessTrustProviderRequestRequestTypeDef(
    _RequiredAttachVerifiedAccessTrustProviderRequestRequestTypeDef,
    _OptionalAttachVerifiedAccessTrustProviderRequestRequestTypeDef,
):
    pass

AttachVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "AttachVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": "VerifiedAccessTrustProviderTypeDef",
        "VerifiedAccessInstance": "VerifiedAccessInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttachVolumeRequestInstanceTypeDef = TypedDict(
    "_RequiredAttachVolumeRequestInstanceTypeDef",
    {
        "Device": str,
        "VolumeId": str,
    },
)
_OptionalAttachVolumeRequestInstanceTypeDef = TypedDict(
    "_OptionalAttachVolumeRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachVolumeRequestInstanceTypeDef(
    _RequiredAttachVolumeRequestInstanceTypeDef, _OptionalAttachVolumeRequestInstanceTypeDef
):
    pass

_RequiredAttachVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredAttachVolumeRequestRequestTypeDef",
    {
        "Device": str,
        "InstanceId": str,
        "VolumeId": str,
    },
)
_OptionalAttachVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalAttachVolumeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachVolumeRequestRequestTypeDef(
    _RequiredAttachVolumeRequestRequestTypeDef, _OptionalAttachVolumeRequestRequestTypeDef
):
    pass

_RequiredAttachVolumeRequestVolumeTypeDef = TypedDict(
    "_RequiredAttachVolumeRequestVolumeTypeDef",
    {
        "Device": str,
        "InstanceId": str,
    },
)
_OptionalAttachVolumeRequestVolumeTypeDef = TypedDict(
    "_OptionalAttachVolumeRequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachVolumeRequestVolumeTypeDef(
    _RequiredAttachVolumeRequestVolumeTypeDef, _OptionalAttachVolumeRequestVolumeTypeDef
):
    pass

_RequiredAttachVpnGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredAttachVpnGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "VpnGatewayId": str,
    },
)
_OptionalAttachVpnGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalAttachVpnGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class AttachVpnGatewayRequestRequestTypeDef(
    _RequiredAttachVpnGatewayRequestRequestTypeDef, _OptionalAttachVpnGatewayRequestRequestTypeDef
):
    pass

AttachVpnGatewayResultTypeDef = TypedDict(
    "AttachVpnGatewayResultTypeDef",
    {
        "VpcAttachment": "VpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AttachmentEnaSrdSpecificationTypeDef = TypedDict(
    "AttachmentEnaSrdSpecificationTypeDef",
    {
        "EnaSrdEnabled": bool,
        "EnaSrdUdpSpecification": "AttachmentEnaSrdUdpSpecificationTypeDef",
    },
    total=False,
)

AttachmentEnaSrdUdpSpecificationTypeDef = TypedDict(
    "AttachmentEnaSrdUdpSpecificationTypeDef",
    {
        "EnaSrdUdpEnabled": bool,
    },
    total=False,
)

AttributeBooleanValueTypeDef = TypedDict(
    "AttributeBooleanValueTypeDef",
    {
        "Value": bool,
    },
    total=False,
)

AttributeValueTypeDef = TypedDict(
    "AttributeValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

AuthorizationRuleTypeDef = TypedDict(
    "AuthorizationRuleTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Description": str,
        "GroupId": str,
        "AccessAll": bool,
        "DestinationCidr": str,
        "Status": "ClientVpnAuthorizationRuleStatusTypeDef",
    },
    total=False,
)

_RequiredAuthorizeClientVpnIngressRequestRequestTypeDef = TypedDict(
    "_RequiredAuthorizeClientVpnIngressRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "TargetNetworkCidr": str,
    },
)
_OptionalAuthorizeClientVpnIngressRequestRequestTypeDef = TypedDict(
    "_OptionalAuthorizeClientVpnIngressRequestRequestTypeDef",
    {
        "AccessGroupId": str,
        "AuthorizeAllGroups": bool,
        "Description": str,
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class AuthorizeClientVpnIngressRequestRequestTypeDef(
    _RequiredAuthorizeClientVpnIngressRequestRequestTypeDef,
    _OptionalAuthorizeClientVpnIngressRequestRequestTypeDef,
):
    pass

AuthorizeClientVpnIngressResultTypeDef = TypedDict(
    "AuthorizeClientVpnIngressResultTypeDef",
    {
        "Status": "ClientVpnAuthorizationRuleStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAuthorizeSecurityGroupEgressRequestRequestTypeDef = TypedDict(
    "_RequiredAuthorizeSecurityGroupEgressRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalAuthorizeSecurityGroupEgressRequestRequestTypeDef = TypedDict(
    "_OptionalAuthorizeSecurityGroupEgressRequestRequestTypeDef",
    {
        "DryRun": bool,
        "IpPermissions": List["IpPermissionTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "CidrIp": str,
        "FromPort": int,
        "IpProtocol": str,
        "ToPort": int,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
    },
    total=False,
)

class AuthorizeSecurityGroupEgressRequestRequestTypeDef(
    _RequiredAuthorizeSecurityGroupEgressRequestRequestTypeDef,
    _OptionalAuthorizeSecurityGroupEgressRequestRequestTypeDef,
):
    pass

AuthorizeSecurityGroupEgressRequestSecurityGroupTypeDef = TypedDict(
    "AuthorizeSecurityGroupEgressRequestSecurityGroupTypeDef",
    {
        "DryRun": bool,
        "IpPermissions": List["IpPermissionTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "CidrIp": str,
        "FromPort": int,
        "IpProtocol": str,
        "ToPort": int,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
    },
    total=False,
)

AuthorizeSecurityGroupEgressResultTypeDef = TypedDict(
    "AuthorizeSecurityGroupEgressResultTypeDef",
    {
        "Return": bool,
        "SecurityGroupRules": List["SecurityGroupRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AuthorizeSecurityGroupIngressRequestRequestTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressRequestRequestTypeDef",
    {
        "CidrIp": str,
        "FromPort": int,
        "GroupId": str,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "IpProtocol": str,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
        "ToPort": int,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

AuthorizeSecurityGroupIngressRequestSecurityGroupTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressRequestSecurityGroupTypeDef",
    {
        "CidrIp": str,
        "FromPort": int,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "IpProtocol": str,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
        "ToPort": int,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

AuthorizeSecurityGroupIngressResultTypeDef = TypedDict(
    "AuthorizeSecurityGroupIngressResultTypeDef",
    {
        "Return": bool,
        "SecurityGroupRules": List["SecurityGroupRuleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AvailabilityZoneMessageTypeDef = TypedDict(
    "AvailabilityZoneMessageTypeDef",
    {
        "Message": str,
    },
    total=False,
)

AvailabilityZoneTypeDef = TypedDict(
    "AvailabilityZoneTypeDef",
    {
        "State": AvailabilityZoneStateType,
        "OptInStatus": AvailabilityZoneOptInStatusType,
        "Messages": List["AvailabilityZoneMessageTypeDef"],
        "RegionName": str,
        "ZoneName": str,
        "ZoneId": str,
        "GroupName": str,
        "NetworkBorderGroup": str,
        "ZoneType": str,
        "ParentZoneName": str,
        "ParentZoneId": str,
    },
    total=False,
)

AvailableCapacityTypeDef = TypedDict(
    "AvailableCapacityTypeDef",
    {
        "AvailableInstanceCapacity": List["InstanceCapacityTypeDef"],
        "AvailableVCpus": int,
    },
    total=False,
)

BaselineEbsBandwidthMbpsRequestTypeDef = TypedDict(
    "BaselineEbsBandwidthMbpsRequestTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

BaselineEbsBandwidthMbpsTypeDef = TypedDict(
    "BaselineEbsBandwidthMbpsTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

BlobAttributeValueTypeDef = TypedDict(
    "BlobAttributeValueTypeDef",
    {
        "Value": Union[bytes, IO[bytes], StreamingBody],
    },
    total=False,
)

BlockDeviceMappingTypeDef = TypedDict(
    "BlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "VirtualName": str,
        "Ebs": "EbsBlockDeviceTypeDef",
        "NoDevice": str,
    },
    total=False,
)

_RequiredBundleInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredBundleInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Storage": "StorageTypeDef",
    },
)
_OptionalBundleInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalBundleInstanceRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class BundleInstanceRequestRequestTypeDef(
    _RequiredBundleInstanceRequestRequestTypeDef, _OptionalBundleInstanceRequestRequestTypeDef
):
    pass

BundleInstanceResultTypeDef = TypedDict(
    "BundleInstanceResultTypeDef",
    {
        "BundleTask": "BundleTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

BundleTaskErrorTypeDef = TypedDict(
    "BundleTaskErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

BundleTaskTypeDef = TypedDict(
    "BundleTaskTypeDef",
    {
        "BundleId": str,
        "BundleTaskError": "BundleTaskErrorTypeDef",
        "InstanceId": str,
        "Progress": str,
        "StartTime": datetime,
        "State": BundleTaskStateType,
        "Storage": "StorageTypeDef",
        "UpdateTime": datetime,
    },
    total=False,
)

ByoipCidrTypeDef = TypedDict(
    "ByoipCidrTypeDef",
    {
        "Cidr": str,
        "Description": str,
        "StatusMessage": str,
        "State": ByoipCidrStateType,
    },
    total=False,
)

_RequiredCancelBundleTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCancelBundleTaskRequestRequestTypeDef",
    {
        "BundleId": str,
    },
)
_OptionalCancelBundleTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCancelBundleTaskRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CancelBundleTaskRequestRequestTypeDef(
    _RequiredCancelBundleTaskRequestRequestTypeDef, _OptionalCancelBundleTaskRequestRequestTypeDef
):
    pass

CancelBundleTaskResultTypeDef = TypedDict(
    "CancelBundleTaskResultTypeDef",
    {
        "BundleTask": "BundleTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelCapacityReservationFleetErrorTypeDef = TypedDict(
    "CancelCapacityReservationFleetErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

_RequiredCancelCapacityReservationFleetsRequestRequestTypeDef = TypedDict(
    "_RequiredCancelCapacityReservationFleetsRequestRequestTypeDef",
    {
        "CapacityReservationFleetIds": List[str],
    },
)
_OptionalCancelCapacityReservationFleetsRequestRequestTypeDef = TypedDict(
    "_OptionalCancelCapacityReservationFleetsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CancelCapacityReservationFleetsRequestRequestTypeDef(
    _RequiredCancelCapacityReservationFleetsRequestRequestTypeDef,
    _OptionalCancelCapacityReservationFleetsRequestRequestTypeDef,
):
    pass

CancelCapacityReservationFleetsResultTypeDef = TypedDict(
    "CancelCapacityReservationFleetsResultTypeDef",
    {
        "SuccessfulFleetCancellations": List["CapacityReservationFleetCancellationStateTypeDef"],
        "FailedFleetCancellations": List["FailedCapacityReservationFleetCancellationResultTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelCapacityReservationRequestRequestTypeDef = TypedDict(
    "_RequiredCancelCapacityReservationRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
    },
)
_OptionalCancelCapacityReservationRequestRequestTypeDef = TypedDict(
    "_OptionalCancelCapacityReservationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CancelCapacityReservationRequestRequestTypeDef(
    _RequiredCancelCapacityReservationRequestRequestTypeDef,
    _OptionalCancelCapacityReservationRequestRequestTypeDef,
):
    pass

CancelCapacityReservationResultTypeDef = TypedDict(
    "CancelCapacityReservationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCancelConversionRequestRequestTypeDef = TypedDict(
    "_RequiredCancelConversionRequestRequestTypeDef",
    {
        "ConversionTaskId": str,
    },
)
_OptionalCancelConversionRequestRequestTypeDef = TypedDict(
    "_OptionalCancelConversionRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ReasonMessage": str,
    },
    total=False,
)

class CancelConversionRequestRequestTypeDef(
    _RequiredCancelConversionRequestRequestTypeDef, _OptionalCancelConversionRequestRequestTypeDef
):
    pass

CancelExportTaskRequestRequestTypeDef = TypedDict(
    "CancelExportTaskRequestRequestTypeDef",
    {
        "ExportTaskId": str,
    },
)

_RequiredCancelImageLaunchPermissionRequestRequestTypeDef = TypedDict(
    "_RequiredCancelImageLaunchPermissionRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalCancelImageLaunchPermissionRequestRequestTypeDef = TypedDict(
    "_OptionalCancelImageLaunchPermissionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CancelImageLaunchPermissionRequestRequestTypeDef(
    _RequiredCancelImageLaunchPermissionRequestRequestTypeDef,
    _OptionalCancelImageLaunchPermissionRequestRequestTypeDef,
):
    pass

CancelImageLaunchPermissionResultTypeDef = TypedDict(
    "CancelImageLaunchPermissionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelImportTaskRequestRequestTypeDef = TypedDict(
    "CancelImportTaskRequestRequestTypeDef",
    {
        "CancelReason": str,
        "DryRun": bool,
        "ImportTaskId": str,
    },
    total=False,
)

CancelImportTaskResultTypeDef = TypedDict(
    "CancelImportTaskResultTypeDef",
    {
        "ImportTaskId": str,
        "PreviousState": str,
        "State": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelReservedInstancesListingRequestRequestTypeDef = TypedDict(
    "CancelReservedInstancesListingRequestRequestTypeDef",
    {
        "ReservedInstancesListingId": str,
    },
)

CancelReservedInstancesListingResultTypeDef = TypedDict(
    "CancelReservedInstancesListingResultTypeDef",
    {
        "ReservedInstancesListings": List["ReservedInstancesListingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSpotFleetRequestsErrorItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorItemTypeDef",
    {
        "Error": "CancelSpotFleetRequestsErrorTypeDef",
        "SpotFleetRequestId": str,
    },
    total=False,
)

CancelSpotFleetRequestsErrorTypeDef = TypedDict(
    "CancelSpotFleetRequestsErrorTypeDef",
    {
        "Code": CancelBatchErrorCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredCancelSpotFleetRequestsRequestRequestTypeDef = TypedDict(
    "_RequiredCancelSpotFleetRequestsRequestRequestTypeDef",
    {
        "SpotFleetRequestIds": List[str],
        "TerminateInstances": bool,
    },
)
_OptionalCancelSpotFleetRequestsRequestRequestTypeDef = TypedDict(
    "_OptionalCancelSpotFleetRequestsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CancelSpotFleetRequestsRequestRequestTypeDef(
    _RequiredCancelSpotFleetRequestsRequestRequestTypeDef,
    _OptionalCancelSpotFleetRequestsRequestRequestTypeDef,
):
    pass

CancelSpotFleetRequestsResponseTypeDef = TypedDict(
    "CancelSpotFleetRequestsResponseTypeDef",
    {
        "SuccessfulFleetRequests": List["CancelSpotFleetRequestsSuccessItemTypeDef"],
        "UnsuccessfulFleetRequests": List["CancelSpotFleetRequestsErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelSpotFleetRequestsSuccessItemTypeDef = TypedDict(
    "CancelSpotFleetRequestsSuccessItemTypeDef",
    {
        "CurrentSpotFleetRequestState": BatchStateType,
        "PreviousSpotFleetRequestState": BatchStateType,
        "SpotFleetRequestId": str,
    },
    total=False,
)

_RequiredCancelSpotInstanceRequestsRequestRequestTypeDef = TypedDict(
    "_RequiredCancelSpotInstanceRequestsRequestRequestTypeDef",
    {
        "SpotInstanceRequestIds": List[str],
    },
)
_OptionalCancelSpotInstanceRequestsRequestRequestTypeDef = TypedDict(
    "_OptionalCancelSpotInstanceRequestsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CancelSpotInstanceRequestsRequestRequestTypeDef(
    _RequiredCancelSpotInstanceRequestsRequestRequestTypeDef,
    _OptionalCancelSpotInstanceRequestsRequestRequestTypeDef,
):
    pass

CancelSpotInstanceRequestsResultTypeDef = TypedDict(
    "CancelSpotInstanceRequestsResultTypeDef",
    {
        "CancelledSpotInstanceRequests": List["CancelledSpotInstanceRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelledSpotInstanceRequestTypeDef = TypedDict(
    "CancelledSpotInstanceRequestTypeDef",
    {
        "SpotInstanceRequestId": str,
        "State": CancelSpotInstanceRequestStateType,
    },
    total=False,
)

CapacityAllocationTypeDef = TypedDict(
    "CapacityAllocationTypeDef",
    {
        "AllocationType": Literal["used"],
        "Count": int,
    },
    total=False,
)

CapacityBlockOfferingTypeDef = TypedDict(
    "CapacityBlockOfferingTypeDef",
    {
        "CapacityBlockOfferingId": str,
        "InstanceType": str,
        "AvailabilityZone": str,
        "InstanceCount": int,
        "StartDate": datetime,
        "EndDate": datetime,
        "CapacityBlockDurationHours": int,
        "UpfrontFee": str,
        "CurrencyCode": str,
        "Tenancy": CapacityReservationTenancyType,
    },
    total=False,
)

CapacityReservationFleetCancellationStateTypeDef = TypedDict(
    "CapacityReservationFleetCancellationStateTypeDef",
    {
        "CurrentFleetState": CapacityReservationFleetStateType,
        "PreviousFleetState": CapacityReservationFleetStateType,
        "CapacityReservationFleetId": str,
    },
    total=False,
)

CapacityReservationFleetTypeDef = TypedDict(
    "CapacityReservationFleetTypeDef",
    {
        "CapacityReservationFleetId": str,
        "CapacityReservationFleetArn": str,
        "State": CapacityReservationFleetStateType,
        "TotalTargetCapacity": int,
        "TotalFulfilledCapacity": float,
        "Tenancy": Literal["default"],
        "EndDate": datetime,
        "CreateTime": datetime,
        "InstanceMatchCriteria": Literal["open"],
        "AllocationStrategy": str,
        "InstanceTypeSpecifications": List["FleetCapacityReservationTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CapacityReservationGroupTypeDef = TypedDict(
    "CapacityReservationGroupTypeDef",
    {
        "GroupArn": str,
        "OwnerId": str,
    },
    total=False,
)

CapacityReservationOptionsRequestTypeDef = TypedDict(
    "CapacityReservationOptionsRequestTypeDef",
    {
        "UsageStrategy": Literal["use-capacity-reservations-first"],
    },
    total=False,
)

CapacityReservationOptionsTypeDef = TypedDict(
    "CapacityReservationOptionsTypeDef",
    {
        "UsageStrategy": Literal["use-capacity-reservations-first"],
    },
    total=False,
)

CapacityReservationSpecificationResponseTypeDef = TypedDict(
    "CapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": "CapacityReservationTargetResponseTypeDef",
    },
    total=False,
)

CapacityReservationSpecificationTypeDef = TypedDict(
    "CapacityReservationSpecificationTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": "CapacityReservationTargetTypeDef",
    },
    total=False,
)

CapacityReservationTargetResponseTypeDef = TypedDict(
    "CapacityReservationTargetResponseTypeDef",
    {
        "CapacityReservationId": str,
        "CapacityReservationResourceGroupArn": str,
    },
    total=False,
)

CapacityReservationTargetTypeDef = TypedDict(
    "CapacityReservationTargetTypeDef",
    {
        "CapacityReservationId": str,
        "CapacityReservationResourceGroupArn": str,
    },
    total=False,
)

CapacityReservationTypeDef = TypedDict(
    "CapacityReservationTypeDef",
    {
        "CapacityReservationId": str,
        "OwnerId": str,
        "CapacityReservationArn": str,
        "AvailabilityZoneId": str,
        "InstanceType": str,
        "InstancePlatform": CapacityReservationInstancePlatformType,
        "AvailabilityZone": str,
        "Tenancy": CapacityReservationTenancyType,
        "TotalInstanceCount": int,
        "AvailableInstanceCount": int,
        "EbsOptimized": bool,
        "EphemeralStorage": bool,
        "State": CapacityReservationStateType,
        "StartDate": datetime,
        "EndDate": datetime,
        "EndDateType": EndDateTypeType,
        "InstanceMatchCriteria": InstanceMatchCriteriaType,
        "CreateDate": datetime,
        "Tags": List["TagTypeDef"],
        "OutpostArn": str,
        "CapacityReservationFleetId": str,
        "PlacementGroupArn": str,
        "CapacityAllocations": List["CapacityAllocationTypeDef"],
        "ReservationType": CapacityReservationTypeType,
    },
    total=False,
)

CarrierGatewayTypeDef = TypedDict(
    "CarrierGatewayTypeDef",
    {
        "CarrierGatewayId": str,
        "VpcId": str,
        "State": CarrierGatewayStateType,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

CertificateAuthenticationRequestTypeDef = TypedDict(
    "CertificateAuthenticationRequestTypeDef",
    {
        "ClientRootCertificateChainArn": str,
    },
    total=False,
)

CertificateAuthenticationTypeDef = TypedDict(
    "CertificateAuthenticationTypeDef",
    {
        "ClientRootCertificateChain": str,
    },
    total=False,
)

CidrAuthorizationContextTypeDef = TypedDict(
    "CidrAuthorizationContextTypeDef",
    {
        "Message": str,
        "Signature": str,
    },
)

CidrBlockTypeDef = TypedDict(
    "CidrBlockTypeDef",
    {
        "CidrBlock": str,
    },
    total=False,
)

ClassicLinkDnsSupportTypeDef = TypedDict(
    "ClassicLinkDnsSupportTypeDef",
    {
        "ClassicLinkDnsSupported": bool,
        "VpcId": str,
    },
    total=False,
)

ClassicLinkInstanceTypeDef = TypedDict(
    "ClassicLinkInstanceTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "InstanceId": str,
        "Tags": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

ClassicLoadBalancerTypeDef = TypedDict(
    "ClassicLoadBalancerTypeDef",
    {
        "Name": str,
    },
    total=False,
)

ClassicLoadBalancersConfigTypeDef = TypedDict(
    "ClassicLoadBalancersConfigTypeDef",
    {
        "ClassicLoadBalancers": List["ClassicLoadBalancerTypeDef"],
    },
    total=False,
)

ClientCertificateRevocationListStatusTypeDef = TypedDict(
    "ClientCertificateRevocationListStatusTypeDef",
    {
        "Code": ClientCertificateRevocationListStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientConnectOptionsTypeDef = TypedDict(
    "ClientConnectOptionsTypeDef",
    {
        "Enabled": bool,
        "LambdaFunctionArn": str,
    },
    total=False,
)

ClientConnectResponseOptionsTypeDef = TypedDict(
    "ClientConnectResponseOptionsTypeDef",
    {
        "Enabled": bool,
        "LambdaFunctionArn": str,
        "Status": "ClientVpnEndpointAttributeStatusTypeDef",
    },
    total=False,
)

ClientDataTypeDef = TypedDict(
    "ClientDataTypeDef",
    {
        "Comment": str,
        "UploadEnd": Union[datetime, str],
        "UploadSize": float,
        "UploadStart": Union[datetime, str],
    },
    total=False,
)

ClientLoginBannerOptionsTypeDef = TypedDict(
    "ClientLoginBannerOptionsTypeDef",
    {
        "Enabled": bool,
        "BannerText": str,
    },
    total=False,
)

ClientLoginBannerResponseOptionsTypeDef = TypedDict(
    "ClientLoginBannerResponseOptionsTypeDef",
    {
        "Enabled": bool,
        "BannerText": str,
    },
    total=False,
)

ClientVpnAuthenticationRequestTypeDef = TypedDict(
    "ClientVpnAuthenticationRequestTypeDef",
    {
        "Type": ClientVpnAuthenticationTypeType,
        "ActiveDirectory": "DirectoryServiceAuthenticationRequestTypeDef",
        "MutualAuthentication": "CertificateAuthenticationRequestTypeDef",
        "FederatedAuthentication": "FederatedAuthenticationRequestTypeDef",
    },
    total=False,
)

ClientVpnAuthenticationTypeDef = TypedDict(
    "ClientVpnAuthenticationTypeDef",
    {
        "Type": ClientVpnAuthenticationTypeType,
        "ActiveDirectory": "DirectoryServiceAuthenticationTypeDef",
        "MutualAuthentication": "CertificateAuthenticationTypeDef",
        "FederatedAuthentication": "FederatedAuthenticationTypeDef",
    },
    total=False,
)

ClientVpnAuthorizationRuleStatusTypeDef = TypedDict(
    "ClientVpnAuthorizationRuleStatusTypeDef",
    {
        "Code": ClientVpnAuthorizationRuleStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnConnectionStatusTypeDef = TypedDict(
    "ClientVpnConnectionStatusTypeDef",
    {
        "Code": ClientVpnConnectionStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnConnectionTypeDef = TypedDict(
    "ClientVpnConnectionTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Timestamp": str,
        "ConnectionId": str,
        "Username": str,
        "ConnectionEstablishedTime": str,
        "IngressBytes": str,
        "EgressBytes": str,
        "IngressPackets": str,
        "EgressPackets": str,
        "ClientIp": str,
        "CommonName": str,
        "Status": "ClientVpnConnectionStatusTypeDef",
        "ConnectionEndTime": str,
        "PostureComplianceStatuses": List[str],
    },
    total=False,
)

ClientVpnEndpointAttributeStatusTypeDef = TypedDict(
    "ClientVpnEndpointAttributeStatusTypeDef",
    {
        "Code": ClientVpnEndpointAttributeStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnEndpointStatusTypeDef = TypedDict(
    "ClientVpnEndpointStatusTypeDef",
    {
        "Code": ClientVpnEndpointStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnEndpointTypeDef = TypedDict(
    "ClientVpnEndpointTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Description": str,
        "Status": "ClientVpnEndpointStatusTypeDef",
        "CreationTime": str,
        "DeletionTime": str,
        "DnsName": str,
        "ClientCidrBlock": str,
        "DnsServers": List[str],
        "SplitTunnel": bool,
        "VpnProtocol": Literal["openvpn"],
        "TransportProtocol": TransportProtocolType,
        "VpnPort": int,
        "AssociatedTargetNetworks": List["AssociatedTargetNetworkTypeDef"],
        "ServerCertificateArn": str,
        "AuthenticationOptions": List["ClientVpnAuthenticationTypeDef"],
        "ConnectionLogOptions": "ConnectionLogResponseOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "SecurityGroupIds": List[str],
        "VpcId": str,
        "SelfServicePortalUrl": str,
        "ClientConnectOptions": "ClientConnectResponseOptionsTypeDef",
        "SessionTimeoutHours": int,
        "ClientLoginBannerOptions": "ClientLoginBannerResponseOptionsTypeDef",
    },
    total=False,
)

ClientVpnRouteStatusTypeDef = TypedDict(
    "ClientVpnRouteStatusTypeDef",
    {
        "Code": ClientVpnRouteStatusCodeType,
        "Message": str,
    },
    total=False,
)

ClientVpnRouteTypeDef = TypedDict(
    "ClientVpnRouteTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidr": str,
        "TargetSubnet": str,
        "Type": str,
        "Origin": str,
        "Status": "ClientVpnRouteStatusTypeDef",
        "Description": str,
    },
    total=False,
)

CloudWatchLogOptionsSpecificationTypeDef = TypedDict(
    "CloudWatchLogOptionsSpecificationTypeDef",
    {
        "LogEnabled": bool,
        "LogGroupArn": str,
        "LogOutputFormat": str,
    },
    total=False,
)

CloudWatchLogOptionsTypeDef = TypedDict(
    "CloudWatchLogOptionsTypeDef",
    {
        "LogEnabled": bool,
        "LogGroupArn": str,
        "LogOutputFormat": str,
    },
    total=False,
)

CoipAddressUsageTypeDef = TypedDict(
    "CoipAddressUsageTypeDef",
    {
        "AllocationId": str,
        "AwsAccountId": str,
        "AwsService": str,
        "CoIp": str,
    },
    total=False,
)

CoipCidrTypeDef = TypedDict(
    "CoipCidrTypeDef",
    {
        "Cidr": str,
        "CoipPoolId": str,
        "LocalGatewayRouteTableId": str,
    },
    total=False,
)

CoipPoolTypeDef = TypedDict(
    "CoipPoolTypeDef",
    {
        "PoolId": str,
        "PoolCidrs": List[str],
        "LocalGatewayRouteTableId": str,
        "Tags": List["TagTypeDef"],
        "PoolArn": str,
    },
    total=False,
)

_RequiredConfirmProductInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredConfirmProductInstanceRequestRequestTypeDef",
    {
        "InstanceId": str,
        "ProductCode": str,
    },
)
_OptionalConfirmProductInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalConfirmProductInstanceRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ConfirmProductInstanceRequestRequestTypeDef(
    _RequiredConfirmProductInstanceRequestRequestTypeDef,
    _OptionalConfirmProductInstanceRequestRequestTypeDef,
):
    pass

ConfirmProductInstanceResultTypeDef = TypedDict(
    "ConfirmProductInstanceResultTypeDef",
    {
        "OwnerId": str,
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ConnectionLogOptionsTypeDef = TypedDict(
    "ConnectionLogOptionsTypeDef",
    {
        "Enabled": bool,
        "CloudwatchLogGroup": str,
        "CloudwatchLogStream": str,
    },
    total=False,
)

ConnectionLogResponseOptionsTypeDef = TypedDict(
    "ConnectionLogResponseOptionsTypeDef",
    {
        "Enabled": bool,
        "CloudwatchLogGroup": str,
        "CloudwatchLogStream": str,
    },
    total=False,
)

ConnectionNotificationTypeDef = TypedDict(
    "ConnectionNotificationTypeDef",
    {
        "ConnectionNotificationId": str,
        "ServiceId": str,
        "VpcEndpointId": str,
        "ConnectionNotificationType": Literal["Topic"],
        "ConnectionNotificationArn": str,
        "ConnectionEvents": List[str],
        "ConnectionNotificationState": ConnectionNotificationStateType,
    },
    total=False,
)

ConversionTaskTypeDef = TypedDict(
    "ConversionTaskTypeDef",
    {
        "ConversionTaskId": str,
        "ExpirationTime": str,
        "ImportInstance": "ImportInstanceTaskDetailsTypeDef",
        "ImportVolume": "ImportVolumeTaskDetailsTypeDef",
        "State": ConversionTaskStateType,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredCopyFpgaImageRequestRequestTypeDef = TypedDict(
    "_RequiredCopyFpgaImageRequestRequestTypeDef",
    {
        "SourceFpgaImageId": str,
        "SourceRegion": str,
    },
)
_OptionalCopyFpgaImageRequestRequestTypeDef = TypedDict(
    "_OptionalCopyFpgaImageRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Description": str,
        "Name": str,
        "ClientToken": str,
    },
    total=False,
)

class CopyFpgaImageRequestRequestTypeDef(
    _RequiredCopyFpgaImageRequestRequestTypeDef, _OptionalCopyFpgaImageRequestRequestTypeDef
):
    pass

CopyFpgaImageResultTypeDef = TypedDict(
    "CopyFpgaImageResultTypeDef",
    {
        "FpgaImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopyImageRequestRequestTypeDef = TypedDict(
    "_RequiredCopyImageRequestRequestTypeDef",
    {
        "Name": str,
        "SourceImageId": str,
        "SourceRegion": str,
    },
)
_OptionalCopyImageRequestRequestTypeDef = TypedDict(
    "_OptionalCopyImageRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "DestinationOutpostArn": str,
        "DryRun": bool,
        "CopyImageTags": bool,
    },
    total=False,
)

class CopyImageRequestRequestTypeDef(
    _RequiredCopyImageRequestRequestTypeDef, _OptionalCopyImageRequestRequestTypeDef
):
    pass

CopyImageResultTypeDef = TypedDict(
    "CopyImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCopySnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCopySnapshotRequestRequestTypeDef",
    {
        "SourceRegion": str,
        "SourceSnapshotId": str,
    },
)
_OptionalCopySnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCopySnapshotRequestRequestTypeDef",
    {
        "Description": str,
        "DestinationOutpostArn": str,
        "DestinationRegion": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "PresignedUrl": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CopySnapshotRequestRequestTypeDef(
    _RequiredCopySnapshotRequestRequestTypeDef, _OptionalCopySnapshotRequestRequestTypeDef
):
    pass

_RequiredCopySnapshotRequestSnapshotTypeDef = TypedDict(
    "_RequiredCopySnapshotRequestSnapshotTypeDef",
    {
        "SourceRegion": str,
    },
)
_OptionalCopySnapshotRequestSnapshotTypeDef = TypedDict(
    "_OptionalCopySnapshotRequestSnapshotTypeDef",
    {
        "Description": str,
        "DestinationOutpostArn": str,
        "DestinationRegion": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "PresignedUrl": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CopySnapshotRequestSnapshotTypeDef(
    _RequiredCopySnapshotRequestSnapshotTypeDef, _OptionalCopySnapshotRequestSnapshotTypeDef
):
    pass

CopySnapshotResultTypeDef = TypedDict(
    "CopySnapshotResultTypeDef",
    {
        "SnapshotId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CpuOptionsRequestTypeDef = TypedDict(
    "CpuOptionsRequestTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
        "AmdSevSnp": AmdSevSnpSpecificationType,
    },
    total=False,
)

CpuOptionsTypeDef = TypedDict(
    "CpuOptionsTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
        "AmdSevSnp": AmdSevSnpSpecificationType,
    },
    total=False,
)

_RequiredCreateCapacityReservationFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCapacityReservationFleetRequestRequestTypeDef",
    {
        "InstanceTypeSpecifications": List["ReservationFleetInstanceSpecificationTypeDef"],
        "TotalTargetCapacity": int,
    },
)
_OptionalCreateCapacityReservationFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCapacityReservationFleetRequestRequestTypeDef",
    {
        "AllocationStrategy": str,
        "ClientToken": str,
        "Tenancy": Literal["default"],
        "EndDate": Union[datetime, str],
        "InstanceMatchCriteria": Literal["open"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateCapacityReservationFleetRequestRequestTypeDef(
    _RequiredCreateCapacityReservationFleetRequestRequestTypeDef,
    _OptionalCreateCapacityReservationFleetRequestRequestTypeDef,
):
    pass

CreateCapacityReservationFleetResultTypeDef = TypedDict(
    "CreateCapacityReservationFleetResultTypeDef",
    {
        "CapacityReservationFleetId": str,
        "State": CapacityReservationFleetStateType,
        "TotalTargetCapacity": int,
        "TotalFulfilledCapacity": float,
        "InstanceMatchCriteria": Literal["open"],
        "AllocationStrategy": str,
        "CreateTime": datetime,
        "EndDate": datetime,
        "Tenancy": Literal["default"],
        "FleetCapacityReservations": List["FleetCapacityReservationTypeDef"],
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCapacityReservationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCapacityReservationRequestRequestTypeDef",
    {
        "InstanceType": str,
        "InstancePlatform": CapacityReservationInstancePlatformType,
        "InstanceCount": int,
    },
)
_OptionalCreateCapacityReservationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCapacityReservationRequestRequestTypeDef",
    {
        "ClientToken": str,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "Tenancy": CapacityReservationTenancyType,
        "EbsOptimized": bool,
        "EphemeralStorage": bool,
        "EndDate": Union[datetime, str],
        "EndDateType": EndDateTypeType,
        "InstanceMatchCriteria": InstanceMatchCriteriaType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "OutpostArn": str,
        "PlacementGroupArn": str,
    },
    total=False,
)

class CreateCapacityReservationRequestRequestTypeDef(
    _RequiredCreateCapacityReservationRequestRequestTypeDef,
    _OptionalCreateCapacityReservationRequestRequestTypeDef,
):
    pass

CreateCapacityReservationResultTypeDef = TypedDict(
    "CreateCapacityReservationResultTypeDef",
    {
        "CapacityReservation": "CapacityReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCarrierGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCarrierGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateCarrierGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCarrierGatewayRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

class CreateCarrierGatewayRequestRequestTypeDef(
    _RequiredCreateCarrierGatewayRequestRequestTypeDef,
    _OptionalCreateCarrierGatewayRequestRequestTypeDef,
):
    pass

CreateCarrierGatewayResultTypeDef = TypedDict(
    "CreateCarrierGatewayResultTypeDef",
    {
        "CarrierGateway": "CarrierGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClientVpnEndpointRequestRequestTypeDef",
    {
        "ClientCidrBlock": str,
        "ServerCertificateArn": str,
        "AuthenticationOptions": List["ClientVpnAuthenticationRequestTypeDef"],
        "ConnectionLogOptions": "ConnectionLogOptionsTypeDef",
    },
)
_OptionalCreateClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClientVpnEndpointRequestRequestTypeDef",
    {
        "DnsServers": List[str],
        "TransportProtocol": TransportProtocolType,
        "VpnPort": int,
        "Description": str,
        "SplitTunnel": bool,
        "DryRun": bool,
        "ClientToken": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "SecurityGroupIds": List[str],
        "VpcId": str,
        "SelfServicePortal": SelfServicePortalType,
        "ClientConnectOptions": "ClientConnectOptionsTypeDef",
        "SessionTimeoutHours": int,
        "ClientLoginBannerOptions": "ClientLoginBannerOptionsTypeDef",
    },
    total=False,
)

class CreateClientVpnEndpointRequestRequestTypeDef(
    _RequiredCreateClientVpnEndpointRequestRequestTypeDef,
    _OptionalCreateClientVpnEndpointRequestRequestTypeDef,
):
    pass

CreateClientVpnEndpointResultTypeDef = TypedDict(
    "CreateClientVpnEndpointResultTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Status": "ClientVpnEndpointStatusTypeDef",
        "DnsName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateClientVpnRouteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateClientVpnRouteRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidrBlock": str,
        "TargetVpcSubnetId": str,
    },
)
_OptionalCreateClientVpnRouteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateClientVpnRouteRequestRequestTypeDef",
    {
        "Description": str,
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class CreateClientVpnRouteRequestRequestTypeDef(
    _RequiredCreateClientVpnRouteRequestRequestTypeDef,
    _OptionalCreateClientVpnRouteRequestRequestTypeDef,
):
    pass

CreateClientVpnRouteResultTypeDef = TypedDict(
    "CreateClientVpnRouteResultTypeDef",
    {
        "Status": "ClientVpnRouteStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCoipCidrRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "CoipPoolId": str,
    },
)
_OptionalCreateCoipCidrRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCoipCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateCoipCidrRequestRequestTypeDef(
    _RequiredCreateCoipCidrRequestRequestTypeDef, _OptionalCreateCoipCidrRequestRequestTypeDef
):
    pass

CreateCoipCidrResultTypeDef = TypedDict(
    "CreateCoipCidrResultTypeDef",
    {
        "CoipCidr": "CoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCoipPoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCoipPoolRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
    },
)
_OptionalCreateCoipPoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCoipPoolRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateCoipPoolRequestRequestTypeDef(
    _RequiredCreateCoipPoolRequestRequestTypeDef, _OptionalCreateCoipPoolRequestRequestTypeDef
):
    pass

CreateCoipPoolResultTypeDef = TypedDict(
    "CreateCoipPoolResultTypeDef",
    {
        "CoipPool": "CoipPoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredCreateCustomerGatewayRequestRequestTypeDef",
    {
        "Type": Literal["ipsec.1"],
    },
)
_OptionalCreateCustomerGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalCreateCustomerGatewayRequestRequestTypeDef",
    {
        "BgpAsn": int,
        "PublicIp": str,
        "CertificateArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DeviceName": str,
        "IpAddress": str,
        "DryRun": bool,
    },
    total=False,
)

class CreateCustomerGatewayRequestRequestTypeDef(
    _RequiredCreateCustomerGatewayRequestRequestTypeDef,
    _OptionalCreateCustomerGatewayRequestRequestTypeDef,
):
    pass

CreateCustomerGatewayResultTypeDef = TypedDict(
    "CreateCustomerGatewayResultTypeDef",
    {
        "CustomerGateway": "CustomerGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDefaultSubnetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDefaultSubnetRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
    },
)
_OptionalCreateDefaultSubnetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDefaultSubnetRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Ipv6Native": bool,
    },
    total=False,
)

class CreateDefaultSubnetRequestRequestTypeDef(
    _RequiredCreateDefaultSubnetRequestRequestTypeDef,
    _OptionalCreateDefaultSubnetRequestRequestTypeDef,
):
    pass

CreateDefaultSubnetResultTypeDef = TypedDict(
    "CreateDefaultSubnetResultTypeDef",
    {
        "Subnet": "SubnetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateDefaultVpcRequestRequestTypeDef = TypedDict(
    "CreateDefaultVpcRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

CreateDefaultVpcResultTypeDef = TypedDict(
    "CreateDefaultVpcResultTypeDef",
    {
        "Vpc": "VpcTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateDhcpOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpConfigurations": List["NewDhcpConfigurationTypeDef"],
    },
)
_OptionalCreateDhcpOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDhcpOptionsRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateDhcpOptionsRequestRequestTypeDef(
    _RequiredCreateDhcpOptionsRequestRequestTypeDef, _OptionalCreateDhcpOptionsRequestRequestTypeDef
):
    pass

_RequiredCreateDhcpOptionsRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateDhcpOptionsRequestServiceResourceTypeDef",
    {
        "DhcpConfigurations": List["NewDhcpConfigurationTypeDef"],
    },
)
_OptionalCreateDhcpOptionsRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateDhcpOptionsRequestServiceResourceTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateDhcpOptionsRequestServiceResourceTypeDef(
    _RequiredCreateDhcpOptionsRequestServiceResourceTypeDef,
    _OptionalCreateDhcpOptionsRequestServiceResourceTypeDef,
):
    pass

CreateDhcpOptionsResultTypeDef = TypedDict(
    "CreateDhcpOptionsResultTypeDef",
    {
        "DhcpOptions": "DhcpOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateEgressOnlyInternetGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredCreateEgressOnlyInternetGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateEgressOnlyInternetGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalCreateEgressOnlyInternetGatewayRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateEgressOnlyInternetGatewayRequestRequestTypeDef(
    _RequiredCreateEgressOnlyInternetGatewayRequestRequestTypeDef,
    _OptionalCreateEgressOnlyInternetGatewayRequestRequestTypeDef,
):
    pass

CreateEgressOnlyInternetGatewayResultTypeDef = TypedDict(
    "CreateEgressOnlyInternetGatewayResultTypeDef",
    {
        "ClientToken": str,
        "EgressOnlyInternetGateway": "EgressOnlyInternetGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateFleetErrorTypeDef = TypedDict(
    "CreateFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": InstanceLifecycleType,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

CreateFleetInstanceTypeDef = TypedDict(
    "CreateFleetInstanceTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": InstanceLifecycleType,
        "InstanceIds": List[str],
        "InstanceType": InstanceTypeType,
        "Platform": Literal["Windows"],
    },
    total=False,
)

_RequiredCreateFleetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFleetRequestRequestTypeDef",
    {
        "LaunchTemplateConfigs": List["FleetLaunchTemplateConfigRequestTypeDef"],
        "TargetCapacitySpecification": "TargetCapacitySpecificationRequestTypeDef",
    },
)
_OptionalCreateFleetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFleetRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "SpotOptions": "SpotOptionsRequestTypeDef",
        "OnDemandOptions": "OnDemandOptionsRequestTypeDef",
        "ExcessCapacityTerminationPolicy": FleetExcessCapacityTerminationPolicyType,
        "TerminateInstancesWithExpiration": bool,
        "Type": FleetTypeType,
        "ValidFrom": Union[datetime, str],
        "ValidUntil": Union[datetime, str],
        "ReplaceUnhealthyInstances": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "Context": str,
    },
    total=False,
)

class CreateFleetRequestRequestTypeDef(
    _RequiredCreateFleetRequestRequestTypeDef, _OptionalCreateFleetRequestRequestTypeDef
):
    pass

CreateFleetResultTypeDef = TypedDict(
    "CreateFleetResultTypeDef",
    {
        "FleetId": str,
        "Errors": List["CreateFleetErrorTypeDef"],
        "Instances": List["CreateFleetInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFlowLogsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFlowLogsRequestRequestTypeDef",
    {
        "ResourceIds": List[str],
        "ResourceType": FlowLogsResourceTypeType,
    },
)
_OptionalCreateFlowLogsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFlowLogsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "DeliverLogsPermissionArn": str,
        "DeliverCrossAccountRole": str,
        "LogGroupName": str,
        "TrafficType": TrafficTypeType,
        "LogDestinationType": LogDestinationTypeType,
        "LogDestination": str,
        "LogFormat": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "MaxAggregationInterval": int,
        "DestinationOptions": "DestinationOptionsRequestTypeDef",
    },
    total=False,
)

class CreateFlowLogsRequestRequestTypeDef(
    _RequiredCreateFlowLogsRequestRequestTypeDef, _OptionalCreateFlowLogsRequestRequestTypeDef
):
    pass

CreateFlowLogsResultTypeDef = TypedDict(
    "CreateFlowLogsResultTypeDef",
    {
        "ClientToken": str,
        "FlowLogIds": List[str],
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateFpgaImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateFpgaImageRequestRequestTypeDef",
    {
        "InputStorageLocation": "StorageLocationTypeDef",
    },
)
_OptionalCreateFpgaImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateFpgaImageRequestRequestTypeDef",
    {
        "DryRun": bool,
        "LogsStorageLocation": "StorageLocationTypeDef",
        "Description": str,
        "Name": str,
        "ClientToken": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateFpgaImageRequestRequestTypeDef(
    _RequiredCreateFpgaImageRequestRequestTypeDef, _OptionalCreateFpgaImageRequestRequestTypeDef
):
    pass

CreateFpgaImageResultTypeDef = TypedDict(
    "CreateFpgaImageResultTypeDef",
    {
        "FpgaImageId": str,
        "FpgaImageGlobalId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateImageRequestInstanceTypeDef = TypedDict(
    "_RequiredCreateImageRequestInstanceTypeDef",
    {
        "Name": str,
    },
)
_OptionalCreateImageRequestInstanceTypeDef = TypedDict(
    "_OptionalCreateImageRequestInstanceTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "DryRun": bool,
        "NoReboot": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateImageRequestInstanceTypeDef(
    _RequiredCreateImageRequestInstanceTypeDef, _OptionalCreateImageRequestInstanceTypeDef
):
    pass

_RequiredCreateImageRequestRequestTypeDef = TypedDict(
    "_RequiredCreateImageRequestRequestTypeDef",
    {
        "InstanceId": str,
        "Name": str,
    },
)
_OptionalCreateImageRequestRequestTypeDef = TypedDict(
    "_OptionalCreateImageRequestRequestTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "DryRun": bool,
        "NoReboot": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateImageRequestRequestTypeDef(
    _RequiredCreateImageRequestRequestTypeDef, _OptionalCreateImageRequestRequestTypeDef
):
    pass

CreateImageResultTypeDef = TypedDict(
    "CreateImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceConnectEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceConnectEndpointRequestRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalCreateInstanceConnectEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceConnectEndpointRequestRequestTypeDef",
    {
        "DryRun": bool,
        "SecurityGroupIds": List[str],
        "PreserveClientIp": bool,
        "ClientToken": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateInstanceConnectEndpointRequestRequestTypeDef(
    _RequiredCreateInstanceConnectEndpointRequestRequestTypeDef,
    _OptionalCreateInstanceConnectEndpointRequestRequestTypeDef,
):
    pass

CreateInstanceConnectEndpointResultTypeDef = TypedDict(
    "CreateInstanceConnectEndpointResultTypeDef",
    {
        "InstanceConnectEndpoint": "Ec2InstanceConnectEndpointTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "CreateInstanceEventWindowRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Name": str,
        "TimeRanges": List["InstanceEventWindowTimeRangeRequestTypeDef"],
        "CronExpression": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateInstanceEventWindowResultTypeDef = TypedDict(
    "CreateInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": "InstanceEventWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateInstanceExportTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInstanceExportTaskRequestRequestTypeDef",
    {
        "ExportToS3Task": "ExportToS3TaskSpecificationTypeDef",
        "InstanceId": str,
        "TargetEnvironment": ExportEnvironmentType,
    },
)
_OptionalCreateInstanceExportTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInstanceExportTaskRequestRequestTypeDef",
    {
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateInstanceExportTaskRequestRequestTypeDef(
    _RequiredCreateInstanceExportTaskRequestRequestTypeDef,
    _OptionalCreateInstanceExportTaskRequestRequestTypeDef,
):
    pass

CreateInstanceExportTaskResultTypeDef = TypedDict(
    "CreateInstanceExportTaskResultTypeDef",
    {
        "ExportTask": "ExportTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateInternetGatewayRequestRequestTypeDef = TypedDict(
    "CreateInternetGatewayRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

CreateInternetGatewayRequestServiceResourceTypeDef = TypedDict(
    "CreateInternetGatewayRequestServiceResourceTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

CreateInternetGatewayResultTypeDef = TypedDict(
    "CreateInternetGatewayResultTypeDef",
    {
        "InternetGateway": "InternetGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIpamPoolRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIpamPoolRequestRequestTypeDef",
    {
        "IpamScopeId": str,
        "AddressFamily": AddressFamilyType,
    },
)
_OptionalCreateIpamPoolRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIpamPoolRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Locale": str,
        "SourceIpamPoolId": str,
        "Description": str,
        "AutoImport": bool,
        "PubliclyAdvertisable": bool,
        "AllocationMinNetmaskLength": int,
        "AllocationMaxNetmaskLength": int,
        "AllocationDefaultNetmaskLength": int,
        "AllocationResourceTags": List["RequestIpamResourceTagTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
        "AwsService": Literal["ec2"],
        "PublicIpSource": IpamPoolPublicIpSourceType,
    },
    total=False,
)

class CreateIpamPoolRequestRequestTypeDef(
    _RequiredCreateIpamPoolRequestRequestTypeDef, _OptionalCreateIpamPoolRequestRequestTypeDef
):
    pass

CreateIpamPoolResultTypeDef = TypedDict(
    "CreateIpamPoolResultTypeDef",
    {
        "IpamPool": "IpamPoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIpamRequestRequestTypeDef = TypedDict(
    "CreateIpamRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Description": str,
        "OperatingRegions": List["AddIpamOperatingRegionTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

CreateIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "CreateIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Description": str,
        "OperatingRegions": List["AddIpamOperatingRegionTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

CreateIpamResourceDiscoveryResultTypeDef = TypedDict(
    "CreateIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscovery": "IpamResourceDiscoveryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateIpamResultTypeDef = TypedDict(
    "CreateIpamResultTypeDef",
    {
        "Ipam": "IpamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateIpamScopeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateIpamScopeRequestRequestTypeDef",
    {
        "IpamId": str,
    },
)
_OptionalCreateIpamScopeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateIpamScopeRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateIpamScopeRequestRequestTypeDef(
    _RequiredCreateIpamScopeRequestRequestTypeDef, _OptionalCreateIpamScopeRequestRequestTypeDef
):
    pass

CreateIpamScopeResultTypeDef = TypedDict(
    "CreateIpamScopeResultTypeDef",
    {
        "IpamScope": "IpamScopeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateKeyPairRequestRequestTypeDef = TypedDict(
    "_RequiredCreateKeyPairRequestRequestTypeDef",
    {
        "KeyName": str,
    },
)
_OptionalCreateKeyPairRequestRequestTypeDef = TypedDict(
    "_OptionalCreateKeyPairRequestRequestTypeDef",
    {
        "DryRun": bool,
        "KeyType": KeyTypeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "KeyFormat": KeyFormatType,
    },
    total=False,
)

class CreateKeyPairRequestRequestTypeDef(
    _RequiredCreateKeyPairRequestRequestTypeDef, _OptionalCreateKeyPairRequestRequestTypeDef
):
    pass

_RequiredCreateKeyPairRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateKeyPairRequestServiceResourceTypeDef",
    {
        "KeyName": str,
    },
)
_OptionalCreateKeyPairRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateKeyPairRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "KeyType": KeyTypeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "KeyFormat": KeyFormatType,
    },
    total=False,
)

class CreateKeyPairRequestServiceResourceTypeDef(
    _RequiredCreateKeyPairRequestServiceResourceTypeDef,
    _OptionalCreateKeyPairRequestServiceResourceTypeDef,
):
    pass

_RequiredCreateLaunchTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLaunchTemplateRequestRequestTypeDef",
    {
        "LaunchTemplateName": str,
        "LaunchTemplateData": "RequestLaunchTemplateDataTypeDef",
    },
)
_OptionalCreateLaunchTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLaunchTemplateRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "VersionDescription": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateLaunchTemplateRequestRequestTypeDef(
    _RequiredCreateLaunchTemplateRequestRequestTypeDef,
    _OptionalCreateLaunchTemplateRequestRequestTypeDef,
):
    pass

CreateLaunchTemplateResultTypeDef = TypedDict(
    "CreateLaunchTemplateResultTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "Warning": "ValidationWarningTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLaunchTemplateVersionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLaunchTemplateVersionRequestRequestTypeDef",
    {
        "LaunchTemplateData": "RequestLaunchTemplateDataTypeDef",
    },
)
_OptionalCreateLaunchTemplateVersionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLaunchTemplateVersionRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "SourceVersion": str,
        "VersionDescription": str,
        "ResolveAlias": bool,
    },
    total=False,
)

class CreateLaunchTemplateVersionRequestRequestTypeDef(
    _RequiredCreateLaunchTemplateVersionRequestRequestTypeDef,
    _OptionalCreateLaunchTemplateVersionRequestRequestTypeDef,
):
    pass

CreateLaunchTemplateVersionResultTypeDef = TypedDict(
    "CreateLaunchTemplateVersionResultTypeDef",
    {
        "LaunchTemplateVersion": "LaunchTemplateVersionTypeDef",
        "Warning": "ValidationWarningTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocalGatewayRouteRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
    },
)
_OptionalCreateLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocalGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "DryRun": bool,
        "NetworkInterfaceId": str,
        "DestinationPrefixListId": str,
    },
    total=False,
)

class CreateLocalGatewayRouteRequestRequestTypeDef(
    _RequiredCreateLocalGatewayRouteRequestRequestTypeDef,
    _OptionalCreateLocalGatewayRouteRequestRequestTypeDef,
):
    pass

CreateLocalGatewayRouteResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteResultTypeDef",
    {
        "Route": "LocalGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocalGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocalGatewayRouteTableRequestRequestTypeDef",
    {
        "LocalGatewayId": str,
    },
)
_OptionalCreateLocalGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocalGatewayRouteTableRequestRequestTypeDef",
    {
        "Mode": LocalGatewayRouteTableModeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateLocalGatewayRouteTableRequestRequestTypeDef(
    _RequiredCreateLocalGatewayRouteTableRequestRequestTypeDef,
    _OptionalCreateLocalGatewayRouteTableRequestRequestTypeDef,
):
    pass

CreateLocalGatewayRouteTableResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableResultTypeDef",
    {
        "LocalGatewayRouteTable": "LocalGatewayRouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
    },
)
_OptionalCreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef(
    _RequiredCreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef,
    _OptionalCreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef,
):
    pass

CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociation": "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "VpcId": str,
    },
)
_OptionalCreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef(
    _RequiredCreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef,
    _OptionalCreateLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef,
):
    pass

CreateLocalGatewayRouteTableVpcAssociationResultTypeDef = TypedDict(
    "CreateLocalGatewayRouteTableVpcAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociation": "LocalGatewayRouteTableVpcAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateManagedPrefixListRequestRequestTypeDef = TypedDict(
    "_RequiredCreateManagedPrefixListRequestRequestTypeDef",
    {
        "PrefixListName": str,
        "MaxEntries": int,
        "AddressFamily": str,
    },
)
_OptionalCreateManagedPrefixListRequestRequestTypeDef = TypedDict(
    "_OptionalCreateManagedPrefixListRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Entries": List["AddPrefixListEntryTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
    },
    total=False,
)

class CreateManagedPrefixListRequestRequestTypeDef(
    _RequiredCreateManagedPrefixListRequestRequestTypeDef,
    _OptionalCreateManagedPrefixListRequestRequestTypeDef,
):
    pass

CreateManagedPrefixListResultTypeDef = TypedDict(
    "CreateManagedPrefixListResultTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNatGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNatGatewayRequestRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalCreateNatGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNatGatewayRequestRequestTypeDef",
    {
        "AllocationId": str,
        "ClientToken": str,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ConnectivityType": ConnectivityTypeType,
        "PrivateIpAddress": str,
        "SecondaryAllocationIds": List[str],
        "SecondaryPrivateIpAddresses": List[str],
        "SecondaryPrivateIpAddressCount": int,
    },
    total=False,
)

class CreateNatGatewayRequestRequestTypeDef(
    _RequiredCreateNatGatewayRequestRequestTypeDef, _OptionalCreateNatGatewayRequestRequestTypeDef
):
    pass

CreateNatGatewayResultTypeDef = TypedDict(
    "CreateNatGatewayResultTypeDef",
    {
        "ClientToken": str,
        "NatGateway": "NatGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_RequiredCreateNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "Egress": bool,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
)
_OptionalCreateNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_OptionalCreateNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "CidrBlock": str,
        "DryRun": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
    },
    total=False,
)

class CreateNetworkAclEntryRequestNetworkAclTypeDef(
    _RequiredCreateNetworkAclEntryRequestNetworkAclTypeDef,
    _OptionalCreateNetworkAclEntryRequestNetworkAclTypeDef,
):
    pass

_RequiredCreateNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkAclEntryRequestRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
)
_OptionalCreateNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkAclEntryRequestRequestTypeDef",
    {
        "CidrBlock": str,
        "DryRun": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
    },
    total=False,
)

class CreateNetworkAclEntryRequestRequestTypeDef(
    _RequiredCreateNetworkAclEntryRequestRequestTypeDef,
    _OptionalCreateNetworkAclEntryRequestRequestTypeDef,
):
    pass

_RequiredCreateNetworkAclRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkAclRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateNetworkAclRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkAclRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateNetworkAclRequestRequestTypeDef(
    _RequiredCreateNetworkAclRequestRequestTypeDef, _OptionalCreateNetworkAclRequestRequestTypeDef
):
    pass

_RequiredCreateNetworkAclRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateNetworkAclRequestServiceResourceTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateNetworkAclRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateNetworkAclRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateNetworkAclRequestServiceResourceTypeDef(
    _RequiredCreateNetworkAclRequestServiceResourceTypeDef,
    _OptionalCreateNetworkAclRequestServiceResourceTypeDef,
):
    pass

CreateNetworkAclRequestVpcTypeDef = TypedDict(
    "CreateNetworkAclRequestVpcTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateNetworkAclResultTypeDef = TypedDict(
    "CreateNetworkAclResultTypeDef",
    {
        "NetworkAcl": "NetworkAclTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkInsightsAccessScopeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkInsightsAccessScopeRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
)
_OptionalCreateNetworkInsightsAccessScopeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkInsightsAccessScopeRequestRequestTypeDef",
    {
        "MatchPaths": List["AccessScopePathRequestTypeDef"],
        "ExcludePaths": List["AccessScopePathRequestTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateNetworkInsightsAccessScopeRequestRequestTypeDef(
    _RequiredCreateNetworkInsightsAccessScopeRequestRequestTypeDef,
    _OptionalCreateNetworkInsightsAccessScopeRequestRequestTypeDef,
):
    pass

CreateNetworkInsightsAccessScopeResultTypeDef = TypedDict(
    "CreateNetworkInsightsAccessScopeResultTypeDef",
    {
        "NetworkInsightsAccessScope": "NetworkInsightsAccessScopeTypeDef",
        "NetworkInsightsAccessScopeContent": "NetworkInsightsAccessScopeContentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkInsightsPathRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkInsightsPathRequestRequestTypeDef",
    {
        "Source": str,
        "Protocol": ProtocolType,
        "ClientToken": str,
    },
)
_OptionalCreateNetworkInsightsPathRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkInsightsPathRequestRequestTypeDef",
    {
        "SourceIp": str,
        "DestinationIp": str,
        "Destination": str,
        "DestinationPort": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "FilterAtSource": "PathRequestFilterTypeDef",
        "FilterAtDestination": "PathRequestFilterTypeDef",
    },
    total=False,
)

class CreateNetworkInsightsPathRequestRequestTypeDef(
    _RequiredCreateNetworkInsightsPathRequestRequestTypeDef,
    _OptionalCreateNetworkInsightsPathRequestRequestTypeDef,
):
    pass

CreateNetworkInsightsPathResultTypeDef = TypedDict(
    "CreateNetworkInsightsPathResultTypeDef",
    {
        "NetworkInsightsPath": "NetworkInsightsPathTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkInterfacePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkInterfacePermissionRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "Permission": InterfacePermissionTypeType,
    },
)
_OptionalCreateNetworkInterfacePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkInterfacePermissionRequestRequestTypeDef",
    {
        "AwsAccountId": str,
        "AwsService": str,
        "DryRun": bool,
    },
    total=False,
)

class CreateNetworkInterfacePermissionRequestRequestTypeDef(
    _RequiredCreateNetworkInterfacePermissionRequestRequestTypeDef,
    _OptionalCreateNetworkInterfacePermissionRequestRequestTypeDef,
):
    pass

CreateNetworkInterfacePermissionResultTypeDef = TypedDict(
    "CreateNetworkInterfacePermissionResultTypeDef",
    {
        "InterfacePermission": "NetworkInterfacePermissionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateNetworkInterfaceRequestRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalCreateNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateNetworkInterfaceRequestRequestTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "Ipv4Prefixes": List["Ipv4PrefixSpecificationRequestTypeDef"],
        "Ipv4PrefixCount": int,
        "Ipv6Prefixes": List["Ipv6PrefixSpecificationRequestTypeDef"],
        "Ipv6PrefixCount": int,
        "InterfaceType": NetworkInterfaceCreationTypeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
        "EnablePrimaryIpv6": bool,
    },
    total=False,
)

class CreateNetworkInterfaceRequestRequestTypeDef(
    _RequiredCreateNetworkInterfaceRequestRequestTypeDef,
    _OptionalCreateNetworkInterfaceRequestRequestTypeDef,
):
    pass

_RequiredCreateNetworkInterfaceRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateNetworkInterfaceRequestServiceResourceTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalCreateNetworkInterfaceRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateNetworkInterfaceRequestServiceResourceTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "Ipv4Prefixes": List["Ipv4PrefixSpecificationRequestTypeDef"],
        "Ipv4PrefixCount": int,
        "Ipv6Prefixes": List["Ipv6PrefixSpecificationRequestTypeDef"],
        "Ipv6PrefixCount": int,
        "InterfaceType": NetworkInterfaceCreationTypeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
        "EnablePrimaryIpv6": bool,
    },
    total=False,
)

class CreateNetworkInterfaceRequestServiceResourceTypeDef(
    _RequiredCreateNetworkInterfaceRequestServiceResourceTypeDef,
    _OptionalCreateNetworkInterfaceRequestServiceResourceTypeDef,
):
    pass

CreateNetworkInterfaceRequestSubnetTypeDef = TypedDict(
    "CreateNetworkInterfaceRequestSubnetTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "Ipv4Prefixes": List["Ipv4PrefixSpecificationRequestTypeDef"],
        "Ipv4PrefixCount": int,
        "Ipv6Prefixes": List["Ipv6PrefixSpecificationRequestTypeDef"],
        "Ipv6PrefixCount": int,
        "InterfaceType": NetworkInterfaceCreationTypeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
        "EnablePrimaryIpv6": bool,
    },
    total=False,
)

CreateNetworkInterfaceResultTypeDef = TypedDict(
    "CreateNetworkInterfaceResultTypeDef",
    {
        "NetworkInterface": "NetworkInterfaceTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePlacementGroupRequestRequestTypeDef = TypedDict(
    "CreatePlacementGroupRequestRequestTypeDef",
    {
        "DryRun": bool,
        "GroupName": str,
        "Strategy": PlacementStrategyType,
        "PartitionCount": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "SpreadLevel": SpreadLevelType,
    },
    total=False,
)

CreatePlacementGroupRequestServiceResourceTypeDef = TypedDict(
    "CreatePlacementGroupRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "GroupName": str,
        "Strategy": PlacementStrategyType,
        "PartitionCount": int,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "SpreadLevel": SpreadLevelType,
    },
    total=False,
)

CreatePlacementGroupResultTypeDef = TypedDict(
    "CreatePlacementGroupResultTypeDef",
    {
        "PlacementGroup": "PlacementGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreatePublicIpv4PoolRequestRequestTypeDef = TypedDict(
    "CreatePublicIpv4PoolRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreatePublicIpv4PoolResultTypeDef = TypedDict(
    "CreatePublicIpv4PoolResultTypeDef",
    {
        "PoolId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateReplaceRootVolumeTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateReplaceRootVolumeTaskRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalCreateReplaceRootVolumeTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateReplaceRootVolumeTaskRequestRequestTypeDef",
    {
        "SnapshotId": str,
        "ClientToken": str,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ImageId": str,
        "DeleteReplacedRootVolume": bool,
    },
    total=False,
)

class CreateReplaceRootVolumeTaskRequestRequestTypeDef(
    _RequiredCreateReplaceRootVolumeTaskRequestRequestTypeDef,
    _OptionalCreateReplaceRootVolumeTaskRequestRequestTypeDef,
):
    pass

CreateReplaceRootVolumeTaskResultTypeDef = TypedDict(
    "CreateReplaceRootVolumeTaskResultTypeDef",
    {
        "ReplaceRootVolumeTask": "ReplaceRootVolumeTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateReservedInstancesListingRequestRequestTypeDef = TypedDict(
    "CreateReservedInstancesListingRequestRequestTypeDef",
    {
        "ClientToken": str,
        "InstanceCount": int,
        "PriceSchedules": List["PriceScheduleSpecificationTypeDef"],
        "ReservedInstancesId": str,
    },
)

CreateReservedInstancesListingResultTypeDef = TypedDict(
    "CreateReservedInstancesListingResultTypeDef",
    {
        "ReservedInstancesListings": List["ReservedInstancesListingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRestoreImageTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRestoreImageTaskRequestRequestTypeDef",
    {
        "Bucket": str,
        "ObjectKey": str,
    },
)
_OptionalCreateRestoreImageTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRestoreImageTaskRequestRequestTypeDef",
    {
        "Name": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateRestoreImageTaskRequestRequestTypeDef(
    _RequiredCreateRestoreImageTaskRequestRequestTypeDef,
    _OptionalCreateRestoreImageTaskRequestRequestTypeDef,
):
    pass

CreateRestoreImageTaskResultTypeDef = TypedDict(
    "CreateRestoreImageTaskResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRouteRequestRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalCreateRouteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
        "VpcEndpointId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "VpcPeeringConnectionId": str,
        "CoreNetworkArn": str,
    },
    total=False,
)

class CreateRouteRequestRequestTypeDef(
    _RequiredCreateRouteRequestRequestTypeDef, _OptionalCreateRouteRequestRequestTypeDef
):
    pass

CreateRouteRequestRouteTableTypeDef = TypedDict(
    "CreateRouteRequestRouteTableTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
        "VpcEndpointId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "VpcPeeringConnectionId": str,
        "CoreNetworkArn": str,
    },
    total=False,
)

CreateRouteResultTypeDef = TypedDict(
    "CreateRouteResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredCreateRouteTableRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalCreateRouteTableRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateRouteTableRequestRequestTypeDef(
    _RequiredCreateRouteTableRequestRequestTypeDef, _OptionalCreateRouteTableRequestRequestTypeDef
):
    pass

_RequiredCreateRouteTableRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateRouteTableRequestServiceResourceTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateRouteTableRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateRouteTableRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateRouteTableRequestServiceResourceTypeDef(
    _RequiredCreateRouteTableRequestServiceResourceTypeDef,
    _OptionalCreateRouteTableRequestServiceResourceTypeDef,
):
    pass

CreateRouteTableRequestVpcTypeDef = TypedDict(
    "CreateRouteTableRequestVpcTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateRouteTableResultTypeDef = TypedDict(
    "CreateRouteTableResultTypeDef",
    {
        "RouteTable": "RouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSecurityGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSecurityGroupRequestRequestTypeDef",
    {
        "Description": str,
        "GroupName": str,
    },
)
_OptionalCreateSecurityGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSecurityGroupRequestRequestTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateSecurityGroupRequestRequestTypeDef(
    _RequiredCreateSecurityGroupRequestRequestTypeDef,
    _OptionalCreateSecurityGroupRequestRequestTypeDef,
):
    pass

_RequiredCreateSecurityGroupRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateSecurityGroupRequestServiceResourceTypeDef",
    {
        "Description": str,
        "GroupName": str,
    },
)
_OptionalCreateSecurityGroupRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateSecurityGroupRequestServiceResourceTypeDef",
    {
        "VpcId": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateSecurityGroupRequestServiceResourceTypeDef(
    _RequiredCreateSecurityGroupRequestServiceResourceTypeDef,
    _OptionalCreateSecurityGroupRequestServiceResourceTypeDef,
):
    pass

_RequiredCreateSecurityGroupRequestVpcTypeDef = TypedDict(
    "_RequiredCreateSecurityGroupRequestVpcTypeDef",
    {
        "Description": str,
        "GroupName": str,
    },
)
_OptionalCreateSecurityGroupRequestVpcTypeDef = TypedDict(
    "_OptionalCreateSecurityGroupRequestVpcTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateSecurityGroupRequestVpcTypeDef(
    _RequiredCreateSecurityGroupRequestVpcTypeDef, _OptionalCreateSecurityGroupRequestVpcTypeDef
):
    pass

CreateSecurityGroupResultTypeDef = TypedDict(
    "CreateSecurityGroupResultTypeDef",
    {
        "GroupId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalCreateSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestRequestTypeDef",
    {
        "Description": str,
        "OutpostArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateSnapshotRequestRequestTypeDef(
    _RequiredCreateSnapshotRequestRequestTypeDef, _OptionalCreateSnapshotRequestRequestTypeDef
):
    pass

_RequiredCreateSnapshotRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateSnapshotRequestServiceResourceTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalCreateSnapshotRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateSnapshotRequestServiceResourceTypeDef",
    {
        "Description": str,
        "OutpostArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateSnapshotRequestServiceResourceTypeDef(
    _RequiredCreateSnapshotRequestServiceResourceTypeDef,
    _OptionalCreateSnapshotRequestServiceResourceTypeDef,
):
    pass

CreateSnapshotRequestVolumeTypeDef = TypedDict(
    "CreateSnapshotRequestVolumeTypeDef",
    {
        "Description": str,
        "OutpostArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

_RequiredCreateSnapshotsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotsRequestRequestTypeDef",
    {
        "InstanceSpecification": "InstanceSpecificationTypeDef",
    },
)
_OptionalCreateSnapshotsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotsRequestRequestTypeDef",
    {
        "Description": str,
        "OutpostArn": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "CopyTagsFromSource": Literal["volume"],
    },
    total=False,
)

class CreateSnapshotsRequestRequestTypeDef(
    _RequiredCreateSnapshotsRequestRequestTypeDef, _OptionalCreateSnapshotsRequestRequestTypeDef
):
    pass

CreateSnapshotsResultTypeDef = TypedDict(
    "CreateSnapshotsResultTypeDef",
    {
        "Snapshots": List["SnapshotInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalCreateSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Prefix": str,
    },
    total=False,
)

class CreateSpotDatafeedSubscriptionRequestRequestTypeDef(
    _RequiredCreateSpotDatafeedSubscriptionRequestRequestTypeDef,
    _OptionalCreateSpotDatafeedSubscriptionRequestRequestTypeDef,
):
    pass

CreateSpotDatafeedSubscriptionResultTypeDef = TypedDict(
    "CreateSpotDatafeedSubscriptionResultTypeDef",
    {
        "SpotDatafeedSubscription": "SpotDatafeedSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStoreImageTaskRequestRequestTypeDef = TypedDict(
    "_RequiredCreateStoreImageTaskRequestRequestTypeDef",
    {
        "ImageId": str,
        "Bucket": str,
    },
)
_OptionalCreateStoreImageTaskRequestRequestTypeDef = TypedDict(
    "_OptionalCreateStoreImageTaskRequestRequestTypeDef",
    {
        "S3ObjectTags": List["S3ObjectTagTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateStoreImageTaskRequestRequestTypeDef(
    _RequiredCreateStoreImageTaskRequestRequestTypeDef,
    _OptionalCreateStoreImageTaskRequestRequestTypeDef,
):
    pass

CreateStoreImageTaskResultTypeDef = TypedDict(
    "CreateStoreImageTaskResultTypeDef",
    {
        "ObjectKey": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubnetCidrReservationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSubnetCidrReservationRequestRequestTypeDef",
    {
        "SubnetId": str,
        "Cidr": str,
        "ReservationType": SubnetCidrReservationTypeType,
    },
)
_OptionalCreateSubnetCidrReservationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSubnetCidrReservationRequestRequestTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateSubnetCidrReservationRequestRequestTypeDef(
    _RequiredCreateSubnetCidrReservationRequestRequestTypeDef,
    _OptionalCreateSubnetCidrReservationRequestRequestTypeDef,
):
    pass

CreateSubnetCidrReservationResultTypeDef = TypedDict(
    "CreateSubnetCidrReservationResultTypeDef",
    {
        "SubnetCidrReservation": "SubnetCidrReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSubnetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateSubnetRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateSubnetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateSubnetRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "CidrBlock": str,
        "Ipv6CidrBlock": str,
        "OutpostArn": str,
        "DryRun": bool,
        "Ipv6Native": bool,
    },
    total=False,
)

class CreateSubnetRequestRequestTypeDef(
    _RequiredCreateSubnetRequestRequestTypeDef, _OptionalCreateSubnetRequestRequestTypeDef
):
    pass

_RequiredCreateSubnetRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateSubnetRequestServiceResourceTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateSubnetRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateSubnetRequestServiceResourceTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "CidrBlock": str,
        "Ipv6CidrBlock": str,
        "OutpostArn": str,
        "DryRun": bool,
        "Ipv6Native": bool,
    },
    total=False,
)

class CreateSubnetRequestServiceResourceTypeDef(
    _RequiredCreateSubnetRequestServiceResourceTypeDef,
    _OptionalCreateSubnetRequestServiceResourceTypeDef,
):
    pass

CreateSubnetRequestVpcTypeDef = TypedDict(
    "CreateSubnetRequestVpcTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "CidrBlock": str,
        "Ipv6CidrBlock": str,
        "OutpostArn": str,
        "DryRun": bool,
        "Ipv6Native": bool,
    },
    total=False,
)

CreateSubnetResultTypeDef = TypedDict(
    "CreateSubnetResultTypeDef",
    {
        "Subnet": "SubnetTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTagsRequestDhcpOptionsTypeDef = TypedDict(
    "_RequiredCreateTagsRequestDhcpOptionsTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestDhcpOptionsTypeDef = TypedDict(
    "_OptionalCreateTagsRequestDhcpOptionsTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestDhcpOptionsTypeDef(
    _RequiredCreateTagsRequestDhcpOptionsTypeDef, _OptionalCreateTagsRequestDhcpOptionsTypeDef
):
    pass

_RequiredCreateTagsRequestImageTypeDef = TypedDict(
    "_RequiredCreateTagsRequestImageTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestImageTypeDef = TypedDict(
    "_OptionalCreateTagsRequestImageTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestImageTypeDef(
    _RequiredCreateTagsRequestImageTypeDef, _OptionalCreateTagsRequestImageTypeDef
):
    pass

_RequiredCreateTagsRequestInstanceTypeDef = TypedDict(
    "_RequiredCreateTagsRequestInstanceTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestInstanceTypeDef = TypedDict(
    "_OptionalCreateTagsRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestInstanceTypeDef(
    _RequiredCreateTagsRequestInstanceTypeDef, _OptionalCreateTagsRequestInstanceTypeDef
):
    pass

_RequiredCreateTagsRequestInternetGatewayTypeDef = TypedDict(
    "_RequiredCreateTagsRequestInternetGatewayTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestInternetGatewayTypeDef = TypedDict(
    "_OptionalCreateTagsRequestInternetGatewayTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestInternetGatewayTypeDef(
    _RequiredCreateTagsRequestInternetGatewayTypeDef,
    _OptionalCreateTagsRequestInternetGatewayTypeDef,
):
    pass

_RequiredCreateTagsRequestNetworkAclTypeDef = TypedDict(
    "_RequiredCreateTagsRequestNetworkAclTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestNetworkAclTypeDef = TypedDict(
    "_OptionalCreateTagsRequestNetworkAclTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestNetworkAclTypeDef(
    _RequiredCreateTagsRequestNetworkAclTypeDef, _OptionalCreateTagsRequestNetworkAclTypeDef
):
    pass

_RequiredCreateTagsRequestNetworkInterfaceTypeDef = TypedDict(
    "_RequiredCreateTagsRequestNetworkInterfaceTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestNetworkInterfaceTypeDef = TypedDict(
    "_OptionalCreateTagsRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestNetworkInterfaceTypeDef(
    _RequiredCreateTagsRequestNetworkInterfaceTypeDef,
    _OptionalCreateTagsRequestNetworkInterfaceTypeDef,
):
    pass

_RequiredCreateTagsRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTagsRequestRequestTypeDef",
    {
        "Resources": List[Any],
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTagsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestRequestTypeDef(
    _RequiredCreateTagsRequestRequestTypeDef, _OptionalCreateTagsRequestRequestTypeDef
):
    pass

_RequiredCreateTagsRequestRouteTableTypeDef = TypedDict(
    "_RequiredCreateTagsRequestRouteTableTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestRouteTableTypeDef = TypedDict(
    "_OptionalCreateTagsRequestRouteTableTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestRouteTableTypeDef(
    _RequiredCreateTagsRequestRouteTableTypeDef, _OptionalCreateTagsRequestRouteTableTypeDef
):
    pass

_RequiredCreateTagsRequestSecurityGroupTypeDef = TypedDict(
    "_RequiredCreateTagsRequestSecurityGroupTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestSecurityGroupTypeDef = TypedDict(
    "_OptionalCreateTagsRequestSecurityGroupTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestSecurityGroupTypeDef(
    _RequiredCreateTagsRequestSecurityGroupTypeDef, _OptionalCreateTagsRequestSecurityGroupTypeDef
):
    pass

_RequiredCreateTagsRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateTagsRequestServiceResourceTypeDef",
    {
        "Resources": List[str],
        "Tags": List["TagTypeDef"],
    },
)
_OptionalCreateTagsRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateTagsRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestServiceResourceTypeDef(
    _RequiredCreateTagsRequestServiceResourceTypeDef,
    _OptionalCreateTagsRequestServiceResourceTypeDef,
):
    pass

_RequiredCreateTagsRequestSnapshotTypeDef = TypedDict(
    "_RequiredCreateTagsRequestSnapshotTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestSnapshotTypeDef = TypedDict(
    "_OptionalCreateTagsRequestSnapshotTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestSnapshotTypeDef(
    _RequiredCreateTagsRequestSnapshotTypeDef, _OptionalCreateTagsRequestSnapshotTypeDef
):
    pass

_RequiredCreateTagsRequestSubnetTypeDef = TypedDict(
    "_RequiredCreateTagsRequestSubnetTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestSubnetTypeDef = TypedDict(
    "_OptionalCreateTagsRequestSubnetTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestSubnetTypeDef(
    _RequiredCreateTagsRequestSubnetTypeDef, _OptionalCreateTagsRequestSubnetTypeDef
):
    pass

_RequiredCreateTagsRequestVolumeTypeDef = TypedDict(
    "_RequiredCreateTagsRequestVolumeTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestVolumeTypeDef = TypedDict(
    "_OptionalCreateTagsRequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestVolumeTypeDef(
    _RequiredCreateTagsRequestVolumeTypeDef, _OptionalCreateTagsRequestVolumeTypeDef
):
    pass

_RequiredCreateTagsRequestVpcTypeDef = TypedDict(
    "_RequiredCreateTagsRequestVpcTypeDef",
    {
        "Tags": Optional[List["TagTypeDef"]],
    },
)
_OptionalCreateTagsRequestVpcTypeDef = TypedDict(
    "_OptionalCreateTagsRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class CreateTagsRequestVpcTypeDef(
    _RequiredCreateTagsRequestVpcTypeDef, _OptionalCreateTagsRequestVpcTypeDef
):
    pass

CreateTrafficMirrorFilterRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRequestRequestTypeDef",
    {
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

CreateTrafficMirrorFilterResultTypeDef = TypedDict(
    "CreateTrafficMirrorFilterResultTypeDef",
    {
        "TrafficMirrorFilter": "TrafficMirrorFilterTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "TrafficDirection": TrafficDirectionType,
        "RuleNumber": int,
        "RuleAction": TrafficMirrorRuleActionType,
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
    },
)
_OptionalCreateTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "DestinationPortRange": "TrafficMirrorPortRangeRequestTypeDef",
        "SourcePortRange": "TrafficMirrorPortRangeRequestTypeDef",
        "Protocol": int,
        "Description": str,
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

class CreateTrafficMirrorFilterRuleRequestRequestTypeDef(
    _RequiredCreateTrafficMirrorFilterRuleRequestRequestTypeDef,
    _OptionalCreateTrafficMirrorFilterRuleRequestRequestTypeDef,
):
    pass

CreateTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "CreateTrafficMirrorFilterRuleResultTypeDef",
    {
        "TrafficMirrorFilterRule": "TrafficMirrorFilterRuleTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTrafficMirrorSessionRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "TrafficMirrorTargetId": str,
        "TrafficMirrorFilterId": str,
        "SessionNumber": int,
    },
)
_OptionalCreateTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTrafficMirrorSessionRequestRequestTypeDef",
    {
        "PacketLength": int,
        "VirtualNetworkId": int,
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

class CreateTrafficMirrorSessionRequestRequestTypeDef(
    _RequiredCreateTrafficMirrorSessionRequestRequestTypeDef,
    _OptionalCreateTrafficMirrorSessionRequestRequestTypeDef,
):
    pass

CreateTrafficMirrorSessionResultTypeDef = TypedDict(
    "CreateTrafficMirrorSessionResultTypeDef",
    {
        "TrafficMirrorSession": "TrafficMirrorSessionTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTrafficMirrorTargetRequestRequestTypeDef = TypedDict(
    "CreateTrafficMirrorTargetRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
        "NetworkLoadBalancerArn": str,
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
        "ClientToken": str,
        "GatewayLoadBalancerEndpointId": str,
    },
    total=False,
)

CreateTrafficMirrorTargetResultTypeDef = TypedDict(
    "CreateTrafficMirrorTargetResultTypeDef",
    {
        "TrafficMirrorTarget": "TrafficMirrorTargetTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "PeerAddress": str,
        "InsideCidrBlocks": List[str],
    },
)
_OptionalCreateTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "TransitGatewayAddress": str,
        "BgpOptions": "TransitGatewayConnectRequestBgpOptionsTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayConnectPeerRequestRequestTypeDef(
    _RequiredCreateTransitGatewayConnectPeerRequestRequestTypeDef,
    _OptionalCreateTransitGatewayConnectPeerRequestRequestTypeDef,
):
    pass

CreateTransitGatewayConnectPeerResultTypeDef = TypedDict(
    "CreateTransitGatewayConnectPeerResultTypeDef",
    {
        "TransitGatewayConnectPeer": "TransitGatewayConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayConnectRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayConnectRequestOptionsTypeDef",
    {
        "Protocol": Literal["gre"],
    },
)

_RequiredCreateTransitGatewayConnectRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayConnectRequestRequestTypeDef",
    {
        "TransportTransitGatewayAttachmentId": str,
        "Options": "CreateTransitGatewayConnectRequestOptionsTypeDef",
    },
)
_OptionalCreateTransitGatewayConnectRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayConnectRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayConnectRequestRequestTypeDef(
    _RequiredCreateTransitGatewayConnectRequestRequestTypeDef,
    _OptionalCreateTransitGatewayConnectRequestRequestTypeDef,
):
    pass

CreateTransitGatewayConnectResultTypeDef = TypedDict(
    "CreateTransitGatewayConnectResultTypeDef",
    {
        "TransitGatewayConnect": "TransitGatewayConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayMulticastDomainRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
    {
        "Igmpv2Support": Igmpv2SupportValueType,
        "StaticSourcesSupport": StaticSourcesSupportValueType,
        "AutoAcceptSharedAssociations": AutoAcceptSharedAssociationsValueType,
    },
    total=False,
)

_RequiredCreateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
    },
)
_OptionalCreateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "Options": "CreateTransitGatewayMulticastDomainRequestOptionsTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayMulticastDomainRequestRequestTypeDef(
    _RequiredCreateTransitGatewayMulticastDomainRequestRequestTypeDef,
    _OptionalCreateTransitGatewayMulticastDomainRequestRequestTypeDef,
):
    pass

CreateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "CreateTransitGatewayMulticastDomainResultTypeDef",
    {
        "TransitGatewayMulticastDomain": "TransitGatewayMulticastDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef",
    {
        "DynamicRouting": DynamicRoutingValueType,
    },
    total=False,
)

_RequiredCreateTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "PeerTransitGatewayId": str,
        "PeerAccountId": str,
        "PeerRegion": str,
    },
)
_OptionalCreateTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "Options": "CreateTransitGatewayPeeringAttachmentRequestOptionsTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayPeeringAttachmentRequestRequestTypeDef(
    _RequiredCreateTransitGatewayPeeringAttachmentRequestRequestTypeDef,
    _OptionalCreateTransitGatewayPeeringAttachmentRequestRequestTypeDef,
):
    pass

CreateTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "CreateTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
    },
)
_OptionalCreateTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayPolicyTableRequestRequestTypeDef(
    _RequiredCreateTransitGatewayPolicyTableRequestRequestTypeDef,
    _OptionalCreateTransitGatewayPolicyTableRequestRequestTypeDef,
):
    pass

CreateTransitGatewayPolicyTableResultTypeDef = TypedDict(
    "CreateTransitGatewayPolicyTableResultTypeDef",
    {
        "TransitGatewayPolicyTable": "TransitGatewayPolicyTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
    },
)
_OptionalCreateTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Blackhole": bool,
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayPrefixListReferenceRequestRequestTypeDef(
    _RequiredCreateTransitGatewayPrefixListReferenceRequestRequestTypeDef,
    _OptionalCreateTransitGatewayPrefixListReferenceRequestRequestTypeDef,
):
    pass

CreateTransitGatewayPrefixListReferenceResultTypeDef = TypedDict(
    "CreateTransitGatewayPrefixListReferenceResultTypeDef",
    {
        "TransitGatewayPrefixListReference": "TransitGatewayPrefixListReferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayRequestRequestTypeDef = TypedDict(
    "CreateTransitGatewayRequestRequestTypeDef",
    {
        "Description": str,
        "Options": "TransitGatewayRequestOptionsTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

CreateTransitGatewayResultTypeDef = TypedDict(
    "CreateTransitGatewayResultTypeDef",
    {
        "TransitGateway": "TransitGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalCreateTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayRouteRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Blackhole": bool,
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayRouteRequestRequestTypeDef(
    _RequiredCreateTransitGatewayRouteRequestRequestTypeDef,
    _OptionalCreateTransitGatewayRouteRequestRequestTypeDef,
):
    pass

CreateTransitGatewayRouteResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteResultTypeDef",
    {
        "Route": "TransitGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PeeringAttachmentId": str,
    },
)
_OptionalCreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef(
    _RequiredCreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef,
    _OptionalCreateTransitGatewayRouteTableAnnouncementRequestRequestTypeDef,
):
    pass

CreateTransitGatewayRouteTableAnnouncementResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableAnnouncementResultTypeDef",
    {
        "TransitGatewayRouteTableAnnouncement": "TransitGatewayRouteTableAnnouncementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
    },
)
_OptionalCreateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayRouteTableRequestRequestTypeDef(
    _RequiredCreateTransitGatewayRouteTableRequestRequestTypeDef,
    _OptionalCreateTransitGatewayRouteTableRequestRequestTypeDef,
):
    pass

CreateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "CreateTransitGatewayRouteTableResultTypeDef",
    {
        "TransitGatewayRouteTable": "TransitGatewayRouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {
        "DnsSupport": DnsSupportValueType,
        "Ipv6Support": Ipv6SupportValueType,
        "ApplianceModeSupport": ApplianceModeSupportValueType,
    },
    total=False,
)

_RequiredCreateTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredCreateTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "VpcId": str,
        "SubnetIds": List[str],
    },
)
_OptionalCreateTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalCreateTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "Options": "CreateTransitGatewayVpcAttachmentRequestOptionsTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class CreateTransitGatewayVpcAttachmentRequestRequestTypeDef(
    _RequiredCreateTransitGatewayVpcAttachmentRequestRequestTypeDef,
    _OptionalCreateTransitGatewayVpcAttachmentRequestRequestTypeDef,
):
    pass

CreateTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "CreateTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVerifiedAccessEndpointEniOptionsTypeDef = TypedDict(
    "CreateVerifiedAccessEndpointEniOptionsTypeDef",
    {
        "NetworkInterfaceId": str,
        "Protocol": VerifiedAccessEndpointProtocolType,
        "Port": int,
    },
    total=False,
)

CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef = TypedDict(
    "CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    {
        "Protocol": VerifiedAccessEndpointProtocolType,
        "Port": int,
        "LoadBalancerArn": str,
        "SubnetIds": List[str],
    },
    total=False,
)

_RequiredCreateVerifiedAccessEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVerifiedAccessEndpointRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
        "EndpointType": VerifiedAccessEndpointTypeType,
        "AttachmentType": Literal["vpc"],
        "DomainCertificateArn": str,
        "ApplicationDomain": str,
        "EndpointDomainPrefix": str,
    },
)
_OptionalCreateVerifiedAccessEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVerifiedAccessEndpointRequestRequestTypeDef",
    {
        "SecurityGroupIds": List[str],
        "LoadBalancerOptions": "CreateVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
        "NetworkInterfaceOptions": "CreateVerifiedAccessEndpointEniOptionsTypeDef",
        "Description": str,
        "PolicyDocument": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
        "DryRun": bool,
        "SseSpecification": "VerifiedAccessSseSpecificationRequestTypeDef",
    },
    total=False,
)

class CreateVerifiedAccessEndpointRequestRequestTypeDef(
    _RequiredCreateVerifiedAccessEndpointRequestRequestTypeDef,
    _OptionalCreateVerifiedAccessEndpointRequestRequestTypeDef,
):
    pass

CreateVerifiedAccessEndpointResultTypeDef = TypedDict(
    "CreateVerifiedAccessEndpointResultTypeDef",
    {
        "VerifiedAccessEndpoint": "VerifiedAccessEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVerifiedAccessGroupRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVerifiedAccessGroupRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
    },
)
_OptionalCreateVerifiedAccessGroupRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVerifiedAccessGroupRequestRequestTypeDef",
    {
        "Description": str,
        "PolicyDocument": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
        "DryRun": bool,
        "SseSpecification": "VerifiedAccessSseSpecificationRequestTypeDef",
    },
    total=False,
)

class CreateVerifiedAccessGroupRequestRequestTypeDef(
    _RequiredCreateVerifiedAccessGroupRequestRequestTypeDef,
    _OptionalCreateVerifiedAccessGroupRequestRequestTypeDef,
):
    pass

CreateVerifiedAccessGroupResultTypeDef = TypedDict(
    "CreateVerifiedAccessGroupResultTypeDef",
    {
        "VerifiedAccessGroup": "VerifiedAccessGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVerifiedAccessInstanceRequestRequestTypeDef = TypedDict(
    "CreateVerifiedAccessInstanceRequestRequestTypeDef",
    {
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
        "DryRun": bool,
        "FIPSEnabled": bool,
    },
    total=False,
)

CreateVerifiedAccessInstanceResultTypeDef = TypedDict(
    "CreateVerifiedAccessInstanceResultTypeDef",
    {
        "VerifiedAccessInstance": "VerifiedAccessInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef = TypedDict(
    "CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef",
    {
        "TenantId": str,
    },
    total=False,
)

CreateVerifiedAccessTrustProviderOidcOptionsTypeDef = TypedDict(
    "CreateVerifiedAccessTrustProviderOidcOptionsTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "Scope": str,
    },
    total=False,
)

_RequiredCreateVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "TrustProviderType": TrustProviderTypeType,
        "PolicyReferenceName": str,
    },
)
_OptionalCreateVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "UserTrustProviderType": UserTrustProviderTypeType,
        "DeviceTrustProviderType": DeviceTrustProviderTypeType,
        "OidcOptions": "CreateVerifiedAccessTrustProviderOidcOptionsTypeDef",
        "DeviceOptions": "CreateVerifiedAccessTrustProviderDeviceOptionsTypeDef",
        "Description": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "ClientToken": str,
        "DryRun": bool,
        "SseSpecification": "VerifiedAccessSseSpecificationRequestTypeDef",
    },
    total=False,
)

class CreateVerifiedAccessTrustProviderRequestRequestTypeDef(
    _RequiredCreateVerifiedAccessTrustProviderRequestRequestTypeDef,
    _OptionalCreateVerifiedAccessTrustProviderRequestRequestTypeDef,
):
    pass

CreateVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "CreateVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": "VerifiedAccessTrustProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVolumePermissionModificationsTypeDef = TypedDict(
    "CreateVolumePermissionModificationsTypeDef",
    {
        "Add": List["CreateVolumePermissionTypeDef"],
        "Remove": List["CreateVolumePermissionTypeDef"],
    },
    total=False,
)

CreateVolumePermissionTypeDef = TypedDict(
    "CreateVolumePermissionTypeDef",
    {
        "Group": Literal["all"],
        "UserId": str,
    },
    total=False,
)

_RequiredCreateVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVolumeRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
    },
)
_OptionalCreateVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVolumeRequestRequestTypeDef",
    {
        "Encrypted": bool,
        "Iops": int,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "VolumeType": VolumeTypeType,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "MultiAttachEnabled": bool,
        "Throughput": int,
        "ClientToken": str,
    },
    total=False,
)

class CreateVolumeRequestRequestTypeDef(
    _RequiredCreateVolumeRequestRequestTypeDef, _OptionalCreateVolumeRequestRequestTypeDef
):
    pass

_RequiredCreateVolumeRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateVolumeRequestServiceResourceTypeDef",
    {
        "AvailabilityZone": str,
    },
)
_OptionalCreateVolumeRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateVolumeRequestServiceResourceTypeDef",
    {
        "Encrypted": bool,
        "Iops": int,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "VolumeType": VolumeTypeType,
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "MultiAttachEnabled": bool,
        "Throughput": int,
        "ClientToken": str,
    },
    total=False,
)

class CreateVolumeRequestServiceResourceTypeDef(
    _RequiredCreateVolumeRequestServiceResourceTypeDef,
    _OptionalCreateVolumeRequestServiceResourceTypeDef,
):
    pass

_RequiredCreateVpcEndpointConnectionNotificationRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcEndpointConnectionNotificationRequestRequestTypeDef",
    {
        "ConnectionNotificationArn": str,
        "ConnectionEvents": List[str],
    },
)
_OptionalCreateVpcEndpointConnectionNotificationRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcEndpointConnectionNotificationRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ServiceId": str,
        "VpcEndpointId": str,
        "ClientToken": str,
    },
    total=False,
)

class CreateVpcEndpointConnectionNotificationRequestRequestTypeDef(
    _RequiredCreateVpcEndpointConnectionNotificationRequestRequestTypeDef,
    _OptionalCreateVpcEndpointConnectionNotificationRequestRequestTypeDef,
):
    pass

CreateVpcEndpointConnectionNotificationResultTypeDef = TypedDict(
    "CreateVpcEndpointConnectionNotificationResultTypeDef",
    {
        "ConnectionNotification": "ConnectionNotificationTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcEndpointRequestRequestTypeDef",
    {
        "VpcId": str,
        "ServiceName": str,
    },
)
_OptionalCreateVpcEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcEndpointRequestRequestTypeDef",
    {
        "DryRun": bool,
        "VpcEndpointType": VpcEndpointTypeType,
        "PolicyDocument": str,
        "RouteTableIds": List[str],
        "SubnetIds": List[str],
        "SecurityGroupIds": List[str],
        "IpAddressType": IpAddressTypeType,
        "DnsOptions": "DnsOptionsSpecificationTypeDef",
        "ClientToken": str,
        "PrivateDnsEnabled": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "SubnetConfigurations": List["SubnetConfigurationTypeDef"],
    },
    total=False,
)

class CreateVpcEndpointRequestRequestTypeDef(
    _RequiredCreateVpcEndpointRequestRequestTypeDef, _OptionalCreateVpcEndpointRequestRequestTypeDef
):
    pass

CreateVpcEndpointResultTypeDef = TypedDict(
    "CreateVpcEndpointResultTypeDef",
    {
        "VpcEndpoint": "VpcEndpointTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcEndpointServiceConfigurationRequestRequestTypeDef = TypedDict(
    "CreateVpcEndpointServiceConfigurationRequestRequestTypeDef",
    {
        "DryRun": bool,
        "AcceptanceRequired": bool,
        "PrivateDnsName": str,
        "NetworkLoadBalancerArns": List[str],
        "GatewayLoadBalancerArns": List[str],
        "SupportedIpAddressTypes": List[str],
        "ClientToken": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateVpcEndpointServiceConfigurationResultTypeDef = TypedDict(
    "CreateVpcEndpointServiceConfigurationResultTypeDef",
    {
        "ServiceConfiguration": "ServiceConfigurationTypeDef",
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpcPeeringConnectionRequestRequestTypeDef",
    {
        "DryRun": bool,
        "PeerOwnerId": str,
        "PeerVpcId": str,
        "PeerRegion": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateVpcPeeringConnectionRequestRequestTypeDef(
    _RequiredCreateVpcPeeringConnectionRequestRequestTypeDef,
    _OptionalCreateVpcPeeringConnectionRequestRequestTypeDef,
):
    pass

_RequiredCreateVpcPeeringConnectionRequestServiceResourceTypeDef = TypedDict(
    "_RequiredCreateVpcPeeringConnectionRequestServiceResourceTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalCreateVpcPeeringConnectionRequestServiceResourceTypeDef = TypedDict(
    "_OptionalCreateVpcPeeringConnectionRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "PeerOwnerId": str,
        "PeerVpcId": str,
        "PeerRegion": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateVpcPeeringConnectionRequestServiceResourceTypeDef(
    _RequiredCreateVpcPeeringConnectionRequestServiceResourceTypeDef,
    _OptionalCreateVpcPeeringConnectionRequestServiceResourceTypeDef,
):
    pass

CreateVpcPeeringConnectionRequestVpcTypeDef = TypedDict(
    "CreateVpcPeeringConnectionRequestVpcTypeDef",
    {
        "DryRun": bool,
        "PeerOwnerId": str,
        "PeerVpcId": str,
        "PeerRegion": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateVpcPeeringConnectionResultTypeDef = TypedDict(
    "CreateVpcPeeringConnectionResultTypeDef",
    {
        "VpcPeeringConnection": "VpcPeeringConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpcRequestRequestTypeDef = TypedDict(
    "CreateVpcRequestRequestTypeDef",
    {
        "CidrBlock": str,
        "AmazonProvidedIpv6CidrBlock": bool,
        "Ipv6Pool": str,
        "Ipv6CidrBlock": str,
        "Ipv4IpamPoolId": str,
        "Ipv4NetmaskLength": int,
        "Ipv6IpamPoolId": str,
        "Ipv6NetmaskLength": int,
        "DryRun": bool,
        "InstanceTenancy": TenancyType,
        "Ipv6CidrBlockNetworkBorderGroup": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateVpcRequestServiceResourceTypeDef = TypedDict(
    "CreateVpcRequestServiceResourceTypeDef",
    {
        "CidrBlock": str,
        "AmazonProvidedIpv6CidrBlock": bool,
        "Ipv6Pool": str,
        "Ipv6CidrBlock": str,
        "Ipv4IpamPoolId": str,
        "Ipv4NetmaskLength": int,
        "Ipv6IpamPoolId": str,
        "Ipv6NetmaskLength": int,
        "DryRun": bool,
        "InstanceTenancy": TenancyType,
        "Ipv6CidrBlockNetworkBorderGroup": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

CreateVpcResultTypeDef = TypedDict(
    "CreateVpcResultTypeDef",
    {
        "Vpc": "VpcTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateVpnConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpnConnectionRequestRequestTypeDef",
    {
        "CustomerGatewayId": str,
        "Type": str,
    },
)
_OptionalCreateVpnConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpnConnectionRequestRequestTypeDef",
    {
        "VpnGatewayId": str,
        "TransitGatewayId": str,
        "DryRun": bool,
        "Options": "VpnConnectionOptionsSpecificationTypeDef",
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class CreateVpnConnectionRequestRequestTypeDef(
    _RequiredCreateVpnConnectionRequestRequestTypeDef,
    _OptionalCreateVpnConnectionRequestRequestTypeDef,
):
    pass

CreateVpnConnectionResultTypeDef = TypedDict(
    "CreateVpnConnectionResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreateVpnConnectionRouteRequestRequestTypeDef = TypedDict(
    "CreateVpnConnectionRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "VpnConnectionId": str,
    },
)

_RequiredCreateVpnGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredCreateVpnGatewayRequestRequestTypeDef",
    {
        "Type": Literal["ipsec.1"],
    },
)
_OptionalCreateVpnGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalCreateVpnGatewayRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "AmazonSideAsn": int,
        "DryRun": bool,
    },
    total=False,
)

class CreateVpnGatewayRequestRequestTypeDef(
    _RequiredCreateVpnGatewayRequestRequestTypeDef, _OptionalCreateVpnGatewayRequestRequestTypeDef
):
    pass

CreateVpnGatewayResultTypeDef = TypedDict(
    "CreateVpnGatewayResultTypeDef",
    {
        "VpnGateway": "VpnGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CreditSpecificationRequestTypeDef = TypedDict(
    "CreditSpecificationRequestTypeDef",
    {
        "CpuCredits": str,
    },
)

CreditSpecificationTypeDef = TypedDict(
    "CreditSpecificationTypeDef",
    {
        "CpuCredits": str,
    },
    total=False,
)

CustomerGatewayTypeDef = TypedDict(
    "CustomerGatewayTypeDef",
    {
        "BgpAsn": str,
        "CustomerGatewayId": str,
        "IpAddress": str,
        "CertificateArn": str,
        "State": str,
        "Type": str,
        "DeviceName": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

DataQueryTypeDef = TypedDict(
    "DataQueryTypeDef",
    {
        "Id": str,
        "Source": str,
        "Destination": str,
        "Metric": Literal["aggregate-latency"],
        "Statistic": Literal["p50"],
        "Period": PeriodTypeType,
    },
    total=False,
)

DataResponseTypeDef = TypedDict(
    "DataResponseTypeDef",
    {
        "Id": str,
        "Source": str,
        "Destination": str,
        "Metric": Literal["aggregate-latency"],
        "Statistic": Literal["p50"],
        "Period": PeriodTypeType,
        "MetricPoints": List["MetricPointTypeDef"],
    },
    total=False,
)

_RequiredDeleteCarrierGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCarrierGatewayRequestRequestTypeDef",
    {
        "CarrierGatewayId": str,
    },
)
_OptionalDeleteCarrierGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCarrierGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteCarrierGatewayRequestRequestTypeDef(
    _RequiredDeleteCarrierGatewayRequestRequestTypeDef,
    _OptionalDeleteCarrierGatewayRequestRequestTypeDef,
):
    pass

DeleteCarrierGatewayResultTypeDef = TypedDict(
    "DeleteCarrierGatewayResultTypeDef",
    {
        "CarrierGateway": "CarrierGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteClientVpnEndpointRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDeleteClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteClientVpnEndpointRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteClientVpnEndpointRequestRequestTypeDef(
    _RequiredDeleteClientVpnEndpointRequestRequestTypeDef,
    _OptionalDeleteClientVpnEndpointRequestRequestTypeDef,
):
    pass

DeleteClientVpnEndpointResultTypeDef = TypedDict(
    "DeleteClientVpnEndpointResultTypeDef",
    {
        "Status": "ClientVpnEndpointStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteClientVpnRouteRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteClientVpnRouteRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "DestinationCidrBlock": str,
    },
)
_OptionalDeleteClientVpnRouteRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteClientVpnRouteRequestRequestTypeDef",
    {
        "TargetVpcSubnetId": str,
        "DryRun": bool,
    },
    total=False,
)

class DeleteClientVpnRouteRequestRequestTypeDef(
    _RequiredDeleteClientVpnRouteRequestRequestTypeDef,
    _OptionalDeleteClientVpnRouteRequestRequestTypeDef,
):
    pass

DeleteClientVpnRouteResultTypeDef = TypedDict(
    "DeleteClientVpnRouteResultTypeDef",
    {
        "Status": "ClientVpnRouteStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteCoipCidrRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
        "CoipPoolId": str,
    },
)
_OptionalDeleteCoipCidrRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCoipCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteCoipCidrRequestRequestTypeDef(
    _RequiredDeleteCoipCidrRequestRequestTypeDef, _OptionalDeleteCoipCidrRequestRequestTypeDef
):
    pass

DeleteCoipCidrResultTypeDef = TypedDict(
    "DeleteCoipCidrResultTypeDef",
    {
        "CoipCidr": "CoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteCoipPoolRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCoipPoolRequestRequestTypeDef",
    {
        "CoipPoolId": str,
    },
)
_OptionalDeleteCoipPoolRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCoipPoolRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteCoipPoolRequestRequestTypeDef(
    _RequiredDeleteCoipPoolRequestRequestTypeDef, _OptionalDeleteCoipPoolRequestRequestTypeDef
):
    pass

DeleteCoipPoolResultTypeDef = TypedDict(
    "DeleteCoipPoolResultTypeDef",
    {
        "CoipPool": "CoipPoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteCustomerGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteCustomerGatewayRequestRequestTypeDef",
    {
        "CustomerGatewayId": str,
    },
)
_OptionalDeleteCustomerGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteCustomerGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteCustomerGatewayRequestRequestTypeDef(
    _RequiredDeleteCustomerGatewayRequestRequestTypeDef,
    _OptionalDeleteCustomerGatewayRequestRequestTypeDef,
):
    pass

DeleteDhcpOptionsRequestDhcpOptionsTypeDef = TypedDict(
    "DeleteDhcpOptionsRequestDhcpOptionsTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteDhcpOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpOptionsId": str,
    },
)
_OptionalDeleteDhcpOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteDhcpOptionsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteDhcpOptionsRequestRequestTypeDef(
    _RequiredDeleteDhcpOptionsRequestRequestTypeDef, _OptionalDeleteDhcpOptionsRequestRequestTypeDef
):
    pass

_RequiredDeleteEgressOnlyInternetGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteEgressOnlyInternetGatewayRequestRequestTypeDef",
    {
        "EgressOnlyInternetGatewayId": str,
    },
)
_OptionalDeleteEgressOnlyInternetGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteEgressOnlyInternetGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteEgressOnlyInternetGatewayRequestRequestTypeDef(
    _RequiredDeleteEgressOnlyInternetGatewayRequestRequestTypeDef,
    _OptionalDeleteEgressOnlyInternetGatewayRequestRequestTypeDef,
):
    pass

DeleteEgressOnlyInternetGatewayResultTypeDef = TypedDict(
    "DeleteEgressOnlyInternetGatewayResultTypeDef",
    {
        "ReturnCode": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteFleetErrorItemTypeDef = TypedDict(
    "DeleteFleetErrorItemTypeDef",
    {
        "Error": "DeleteFleetErrorTypeDef",
        "FleetId": str,
    },
    total=False,
)

DeleteFleetErrorTypeDef = TypedDict(
    "DeleteFleetErrorTypeDef",
    {
        "Code": DeleteFleetErrorCodeType,
        "Message": str,
    },
    total=False,
)

DeleteFleetSuccessItemTypeDef = TypedDict(
    "DeleteFleetSuccessItemTypeDef",
    {
        "CurrentFleetState": FleetStateCodeType,
        "PreviousFleetState": FleetStateCodeType,
        "FleetId": str,
    },
    total=False,
)

_RequiredDeleteFleetsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFleetsRequestRequestTypeDef",
    {
        "FleetIds": List[str],
        "TerminateInstances": bool,
    },
)
_OptionalDeleteFleetsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFleetsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteFleetsRequestRequestTypeDef(
    _RequiredDeleteFleetsRequestRequestTypeDef, _OptionalDeleteFleetsRequestRequestTypeDef
):
    pass

DeleteFleetsResultTypeDef = TypedDict(
    "DeleteFleetsResultTypeDef",
    {
        "SuccessfulFleetDeletions": List["DeleteFleetSuccessItemTypeDef"],
        "UnsuccessfulFleetDeletions": List["DeleteFleetErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteFlowLogsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFlowLogsRequestRequestTypeDef",
    {
        "FlowLogIds": List[str],
    },
)
_OptionalDeleteFlowLogsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFlowLogsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteFlowLogsRequestRequestTypeDef(
    _RequiredDeleteFlowLogsRequestRequestTypeDef, _OptionalDeleteFlowLogsRequestRequestTypeDef
):
    pass

DeleteFlowLogsResultTypeDef = TypedDict(
    "DeleteFlowLogsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteFpgaImageRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteFpgaImageRequestRequestTypeDef",
    {
        "FpgaImageId": str,
    },
)
_OptionalDeleteFpgaImageRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteFpgaImageRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteFpgaImageRequestRequestTypeDef(
    _RequiredDeleteFpgaImageRequestRequestTypeDef, _OptionalDeleteFpgaImageRequestRequestTypeDef
):
    pass

DeleteFpgaImageResultTypeDef = TypedDict(
    "DeleteFpgaImageResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteInstanceConnectEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteInstanceConnectEndpointRequestRequestTypeDef",
    {
        "InstanceConnectEndpointId": str,
    },
)
_OptionalDeleteInstanceConnectEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteInstanceConnectEndpointRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteInstanceConnectEndpointRequestRequestTypeDef(
    _RequiredDeleteInstanceConnectEndpointRequestRequestTypeDef,
    _OptionalDeleteInstanceConnectEndpointRequestRequestTypeDef,
):
    pass

DeleteInstanceConnectEndpointResultTypeDef = TypedDict(
    "DeleteInstanceConnectEndpointResultTypeDef",
    {
        "InstanceConnectEndpoint": "Ec2InstanceConnectEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
    },
)
_OptionalDeleteInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteInstanceEventWindowRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ForceDelete": bool,
    },
    total=False,
)

class DeleteInstanceEventWindowRequestRequestTypeDef(
    _RequiredDeleteInstanceEventWindowRequestRequestTypeDef,
    _OptionalDeleteInstanceEventWindowRequestRequestTypeDef,
):
    pass

DeleteInstanceEventWindowResultTypeDef = TypedDict(
    "DeleteInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindowState": "InstanceEventWindowStateChangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "DeleteInternetGatewayRequestInternetGatewayTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteInternetGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteInternetGatewayRequestRequestTypeDef",
    {
        "InternetGatewayId": str,
    },
)
_OptionalDeleteInternetGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteInternetGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteInternetGatewayRequestRequestTypeDef(
    _RequiredDeleteInternetGatewayRequestRequestTypeDef,
    _OptionalDeleteInternetGatewayRequestRequestTypeDef,
):
    pass

_RequiredDeleteIpamPoolRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteIpamPoolRequestRequestTypeDef",
    {
        "IpamPoolId": str,
    },
)
_OptionalDeleteIpamPoolRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteIpamPoolRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteIpamPoolRequestRequestTypeDef(
    _RequiredDeleteIpamPoolRequestRequestTypeDef, _OptionalDeleteIpamPoolRequestRequestTypeDef
):
    pass

DeleteIpamPoolResultTypeDef = TypedDict(
    "DeleteIpamPoolResultTypeDef",
    {
        "IpamPool": "IpamPoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteIpamRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteIpamRequestRequestTypeDef",
    {
        "IpamId": str,
    },
)
_OptionalDeleteIpamRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteIpamRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Cascade": bool,
    },
    total=False,
)

class DeleteIpamRequestRequestTypeDef(
    _RequiredDeleteIpamRequestRequestTypeDef, _OptionalDeleteIpamRequestRequestTypeDef
):
    pass

_RequiredDeleteIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryId": str,
    },
)
_OptionalDeleteIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteIpamResourceDiscoveryRequestRequestTypeDef(
    _RequiredDeleteIpamResourceDiscoveryRequestRequestTypeDef,
    _OptionalDeleteIpamResourceDiscoveryRequestRequestTypeDef,
):
    pass

DeleteIpamResourceDiscoveryResultTypeDef = TypedDict(
    "DeleteIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscovery": "IpamResourceDiscoveryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteIpamResultTypeDef = TypedDict(
    "DeleteIpamResultTypeDef",
    {
        "Ipam": "IpamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteIpamScopeRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteIpamScopeRequestRequestTypeDef",
    {
        "IpamScopeId": str,
    },
)
_OptionalDeleteIpamScopeRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteIpamScopeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteIpamScopeRequestRequestTypeDef(
    _RequiredDeleteIpamScopeRequestRequestTypeDef, _OptionalDeleteIpamScopeRequestRequestTypeDef
):
    pass

DeleteIpamScopeResultTypeDef = TypedDict(
    "DeleteIpamScopeResultTypeDef",
    {
        "IpamScope": "IpamScopeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteKeyPairRequestKeyPairInfoTypeDef = TypedDict(
    "DeleteKeyPairRequestKeyPairInfoTypeDef",
    {
        "KeyPairId": str,
        "DryRun": bool,
    },
    total=False,
)

DeleteKeyPairRequestKeyPairTypeDef = TypedDict(
    "DeleteKeyPairRequestKeyPairTypeDef",
    {
        "KeyPairId": str,
        "DryRun": bool,
    },
    total=False,
)

DeleteKeyPairRequestRequestTypeDef = TypedDict(
    "DeleteKeyPairRequestRequestTypeDef",
    {
        "KeyName": str,
        "KeyPairId": str,
        "DryRun": bool,
    },
    total=False,
)

DeleteKeyPairResultTypeDef = TypedDict(
    "DeleteKeyPairResultTypeDef",
    {
        "Return": bool,
        "KeyPairId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteLaunchTemplateRequestRequestTypeDef = TypedDict(
    "DeleteLaunchTemplateRequestRequestTypeDef",
    {
        "DryRun": bool,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
    },
    total=False,
)

DeleteLaunchTemplateResultTypeDef = TypedDict(
    "DeleteLaunchTemplateResultTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLaunchTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLaunchTemplateVersionsRequestRequestTypeDef",
    {
        "Versions": List[str],
    },
)
_OptionalDeleteLaunchTemplateVersionsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLaunchTemplateVersionsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
    },
    total=False,
)

class DeleteLaunchTemplateVersionsRequestRequestTypeDef(
    _RequiredDeleteLaunchTemplateVersionsRequestRequestTypeDef,
    _OptionalDeleteLaunchTemplateVersionsRequestRequestTypeDef,
):
    pass

DeleteLaunchTemplateVersionsResponseErrorItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "VersionNumber": int,
        "ResponseError": "ResponseErrorTypeDef",
    },
    total=False,
)

DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "VersionNumber": int,
    },
    total=False,
)

DeleteLaunchTemplateVersionsResultTypeDef = TypedDict(
    "DeleteLaunchTemplateVersionsResultTypeDef",
    {
        "SuccessfullyDeletedLaunchTemplateVersions": List[
            "DeleteLaunchTemplateVersionsResponseSuccessItemTypeDef"
        ],
        "UnsuccessfullyDeletedLaunchTemplateVersions": List[
            "DeleteLaunchTemplateVersionsResponseErrorItemTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLocalGatewayRouteRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
    },
)
_OptionalDeleteLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLocalGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "DryRun": bool,
        "DestinationPrefixListId": str,
    },
    total=False,
)

class DeleteLocalGatewayRouteRequestRequestTypeDef(
    _RequiredDeleteLocalGatewayRouteRequestRequestTypeDef,
    _OptionalDeleteLocalGatewayRouteRequestRequestTypeDef,
):
    pass

DeleteLocalGatewayRouteResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteResultTypeDef",
    {
        "Route": "LocalGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLocalGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLocalGatewayRouteTableRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
    },
)
_OptionalDeleteLocalGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLocalGatewayRouteTableRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteLocalGatewayRouteTableRequestRequestTypeDef(
    _RequiredDeleteLocalGatewayRouteTableRequestRequestTypeDef,
    _OptionalDeleteLocalGatewayRouteTableRequestRequestTypeDef,
):
    pass

DeleteLocalGatewayRouteTableResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableResultTypeDef",
    {
        "LocalGatewayRouteTable": "LocalGatewayRouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": str,
    },
)
_OptionalDeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef(
    _RequiredDeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef,
    _OptionalDeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestRequestTypeDef,
):
    pass

DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociation": "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationId": str,
    },
)
_OptionalDeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef(
    _RequiredDeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef,
    _OptionalDeleteLocalGatewayRouteTableVpcAssociationRequestRequestTypeDef,
):
    pass

DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef = TypedDict(
    "DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociation": "LocalGatewayRouteTableVpcAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteManagedPrefixListRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteManagedPrefixListRequestRequestTypeDef",
    {
        "PrefixListId": str,
    },
)
_OptionalDeleteManagedPrefixListRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteManagedPrefixListRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteManagedPrefixListRequestRequestTypeDef(
    _RequiredDeleteManagedPrefixListRequestRequestTypeDef,
    _OptionalDeleteManagedPrefixListRequestRequestTypeDef,
):
    pass

DeleteManagedPrefixListResultTypeDef = TypedDict(
    "DeleteManagedPrefixListResultTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNatGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNatGatewayRequestRequestTypeDef",
    {
        "NatGatewayId": str,
    },
)
_OptionalDeleteNatGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNatGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteNatGatewayRequestRequestTypeDef(
    _RequiredDeleteNatGatewayRequestRequestTypeDef, _OptionalDeleteNatGatewayRequestRequestTypeDef
):
    pass

DeleteNatGatewayResultTypeDef = TypedDict(
    "DeleteNatGatewayResultTypeDef",
    {
        "NatGatewayId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_RequiredDeleteNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "Egress": bool,
        "RuleNumber": int,
    },
)
_OptionalDeleteNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_OptionalDeleteNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteNetworkAclEntryRequestNetworkAclTypeDef(
    _RequiredDeleteNetworkAclEntryRequestNetworkAclTypeDef,
    _OptionalDeleteNetworkAclEntryRequestNetworkAclTypeDef,
):
    pass

_RequiredDeleteNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkAclEntryRequestRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "RuleNumber": int,
    },
)
_OptionalDeleteNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkAclEntryRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteNetworkAclEntryRequestRequestTypeDef(
    _RequiredDeleteNetworkAclEntryRequestRequestTypeDef,
    _OptionalDeleteNetworkAclEntryRequestRequestTypeDef,
):
    pass

DeleteNetworkAclRequestNetworkAclTypeDef = TypedDict(
    "DeleteNetworkAclRequestNetworkAclTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteNetworkAclRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkAclRequestRequestTypeDef",
    {
        "NetworkAclId": str,
    },
)
_OptionalDeleteNetworkAclRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkAclRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteNetworkAclRequestRequestTypeDef(
    _RequiredDeleteNetworkAclRequestRequestTypeDef, _OptionalDeleteNetworkAclRequestRequestTypeDef
):
    pass

_RequiredDeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
    },
)
_OptionalDeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef(
    _RequiredDeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef,
    _OptionalDeleteNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef,
):
    pass

DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkInsightsAccessScopeRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInsightsAccessScopeRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
    },
)
_OptionalDeleteNetworkInsightsAccessScopeRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInsightsAccessScopeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteNetworkInsightsAccessScopeRequestRequestTypeDef(
    _RequiredDeleteNetworkInsightsAccessScopeRequestRequestTypeDef,
    _OptionalDeleteNetworkInsightsAccessScopeRequestRequestTypeDef,
):
    pass

DeleteNetworkInsightsAccessScopeResultTypeDef = TypedDict(
    "DeleteNetworkInsightsAccessScopeResultTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkInsightsAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInsightsAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
    },
)
_OptionalDeleteNetworkInsightsAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInsightsAnalysisRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteNetworkInsightsAnalysisRequestRequestTypeDef(
    _RequiredDeleteNetworkInsightsAnalysisRequestRequestTypeDef,
    _OptionalDeleteNetworkInsightsAnalysisRequestRequestTypeDef,
):
    pass

DeleteNetworkInsightsAnalysisResultTypeDef = TypedDict(
    "DeleteNetworkInsightsAnalysisResultTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkInsightsPathRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInsightsPathRequestRequestTypeDef",
    {
        "NetworkInsightsPathId": str,
    },
)
_OptionalDeleteNetworkInsightsPathRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInsightsPathRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteNetworkInsightsPathRequestRequestTypeDef(
    _RequiredDeleteNetworkInsightsPathRequestRequestTypeDef,
    _OptionalDeleteNetworkInsightsPathRequestRequestTypeDef,
):
    pass

DeleteNetworkInsightsPathResultTypeDef = TypedDict(
    "DeleteNetworkInsightsPathResultTypeDef",
    {
        "NetworkInsightsPathId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteNetworkInterfacePermissionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInterfacePermissionRequestRequestTypeDef",
    {
        "NetworkInterfacePermissionId": str,
    },
)
_OptionalDeleteNetworkInterfacePermissionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInterfacePermissionRequestRequestTypeDef",
    {
        "Force": bool,
        "DryRun": bool,
    },
    total=False,
)

class DeleteNetworkInterfacePermissionRequestRequestTypeDef(
    _RequiredDeleteNetworkInterfacePermissionRequestRequestTypeDef,
    _OptionalDeleteNetworkInterfacePermissionRequestRequestTypeDef,
):
    pass

DeleteNetworkInterfacePermissionResultTypeDef = TypedDict(
    "DeleteNetworkInterfacePermissionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "DeleteNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteNetworkInterfaceRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalDeleteNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteNetworkInterfaceRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteNetworkInterfaceRequestRequestTypeDef(
    _RequiredDeleteNetworkInterfaceRequestRequestTypeDef,
    _OptionalDeleteNetworkInterfaceRequestRequestTypeDef,
):
    pass

DeletePlacementGroupRequestPlacementGroupTypeDef = TypedDict(
    "DeletePlacementGroupRequestPlacementGroupTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeletePlacementGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePlacementGroupRequestRequestTypeDef",
    {
        "GroupName": str,
    },
)
_OptionalDeletePlacementGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePlacementGroupRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeletePlacementGroupRequestRequestTypeDef(
    _RequiredDeletePlacementGroupRequestRequestTypeDef,
    _OptionalDeletePlacementGroupRequestRequestTypeDef,
):
    pass

_RequiredDeletePublicIpv4PoolRequestRequestTypeDef = TypedDict(
    "_RequiredDeletePublicIpv4PoolRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalDeletePublicIpv4PoolRequestRequestTypeDef = TypedDict(
    "_OptionalDeletePublicIpv4PoolRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeletePublicIpv4PoolRequestRequestTypeDef(
    _RequiredDeletePublicIpv4PoolRequestRequestTypeDef,
    _OptionalDeletePublicIpv4PoolRequestRequestTypeDef,
):
    pass

DeletePublicIpv4PoolResultTypeDef = TypedDict(
    "DeletePublicIpv4PoolResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteQueuedReservedInstancesErrorTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesErrorTypeDef",
    {
        "Code": DeleteQueuedReservedInstancesErrorCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredDeleteQueuedReservedInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteQueuedReservedInstancesRequestRequestTypeDef",
    {
        "ReservedInstancesIds": List[str],
    },
)
_OptionalDeleteQueuedReservedInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteQueuedReservedInstancesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteQueuedReservedInstancesRequestRequestTypeDef(
    _RequiredDeleteQueuedReservedInstancesRequestRequestTypeDef,
    _OptionalDeleteQueuedReservedInstancesRequestRequestTypeDef,
):
    pass

DeleteQueuedReservedInstancesResultTypeDef = TypedDict(
    "DeleteQueuedReservedInstancesResultTypeDef",
    {
        "SuccessfulQueuedPurchaseDeletions": List["SuccessfulQueuedPurchaseDeletionTypeDef"],
        "FailedQueuedPurchaseDeletions": List["FailedQueuedPurchaseDeletionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteRouteRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRouteRequestRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalDeleteRouteRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
    },
    total=False,
)

class DeleteRouteRequestRequestTypeDef(
    _RequiredDeleteRouteRequestRequestTypeDef, _OptionalDeleteRouteRequestRequestTypeDef
):
    pass

DeleteRouteRequestRouteTypeDef = TypedDict(
    "DeleteRouteRequestRouteTypeDef",
    {
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteRouteTableRequestRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalDeleteRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteRouteTableRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteRouteTableRequestRequestTypeDef(
    _RequiredDeleteRouteTableRequestRequestTypeDef, _OptionalDeleteRouteTableRequestRequestTypeDef
):
    pass

DeleteRouteTableRequestRouteTableTypeDef = TypedDict(
    "DeleteRouteTableRequestRouteTableTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DeleteSecurityGroupRequestRequestTypeDef = TypedDict(
    "DeleteSecurityGroupRequestRequestTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
        "DryRun": bool,
    },
    total=False,
)

DeleteSecurityGroupRequestSecurityGroupTypeDef = TypedDict(
    "DeleteSecurityGroupRequestSecurityGroupTypeDef",
    {
        "GroupName": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteSnapshotRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSnapshotRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalDeleteSnapshotRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSnapshotRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteSnapshotRequestRequestTypeDef(
    _RequiredDeleteSnapshotRequestRequestTypeDef, _OptionalDeleteSnapshotRequestRequestTypeDef
):
    pass

DeleteSnapshotRequestSnapshotTypeDef = TypedDict(
    "DeleteSnapshotRequestSnapshotTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DeleteSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "DeleteSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteSubnetCidrReservationRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSubnetCidrReservationRequestRequestTypeDef",
    {
        "SubnetCidrReservationId": str,
    },
)
_OptionalDeleteSubnetCidrReservationRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSubnetCidrReservationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteSubnetCidrReservationRequestRequestTypeDef(
    _RequiredDeleteSubnetCidrReservationRequestRequestTypeDef,
    _OptionalDeleteSubnetCidrReservationRequestRequestTypeDef,
):
    pass

DeleteSubnetCidrReservationResultTypeDef = TypedDict(
    "DeleteSubnetCidrReservationResultTypeDef",
    {
        "DeletedSubnetCidrReservation": "SubnetCidrReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteSubnetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteSubnetRequestRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalDeleteSubnetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteSubnetRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteSubnetRequestRequestTypeDef(
    _RequiredDeleteSubnetRequestRequestTypeDef, _OptionalDeleteSubnetRequestRequestTypeDef
):
    pass

DeleteSubnetRequestSubnetTypeDef = TypedDict(
    "DeleteSubnetRequestSubnetTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteTagsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTagsRequestRequestTypeDef",
    {
        "Resources": List[Any],
    },
)
_OptionalDeleteTagsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTagsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Tags": Optional[List["TagTypeDef"]],
    },
    total=False,
)

class DeleteTagsRequestRequestTypeDef(
    _RequiredDeleteTagsRequestRequestTypeDef, _OptionalDeleteTagsRequestRequestTypeDef
):
    pass

DeleteTagsRequestTagTypeDef = TypedDict(
    "DeleteTagsRequestTagTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteTrafficMirrorFilterRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTrafficMirrorFilterRequestRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
    },
)
_OptionalDeleteTrafficMirrorFilterRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTrafficMirrorFilterRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTrafficMirrorFilterRequestRequestTypeDef(
    _RequiredDeleteTrafficMirrorFilterRequestRequestTypeDef,
    _OptionalDeleteTrafficMirrorFilterRequestRequestTypeDef,
):
    pass

DeleteTrafficMirrorFilterResultTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterResultTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
    },
)
_OptionalDeleteTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTrafficMirrorFilterRuleRequestRequestTypeDef(
    _RequiredDeleteTrafficMirrorFilterRuleRequestRequestTypeDef,
    _OptionalDeleteTrafficMirrorFilterRuleRequestRequestTypeDef,
):
    pass

DeleteTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "DeleteTrafficMirrorFilterRuleResultTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTrafficMirrorSessionRequestRequestTypeDef",
    {
        "TrafficMirrorSessionId": str,
    },
)
_OptionalDeleteTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTrafficMirrorSessionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTrafficMirrorSessionRequestRequestTypeDef(
    _RequiredDeleteTrafficMirrorSessionRequestRequestTypeDef,
    _OptionalDeleteTrafficMirrorSessionRequestRequestTypeDef,
):
    pass

DeleteTrafficMirrorSessionResultTypeDef = TypedDict(
    "DeleteTrafficMirrorSessionResultTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTrafficMirrorTargetRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTrafficMirrorTargetRequestRequestTypeDef",
    {
        "TrafficMirrorTargetId": str,
    },
)
_OptionalDeleteTrafficMirrorTargetRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTrafficMirrorTargetRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTrafficMirrorTargetRequestRequestTypeDef(
    _RequiredDeleteTrafficMirrorTargetRequestRequestTypeDef,
    _OptionalDeleteTrafficMirrorTargetRequestRequestTypeDef,
):
    pass

DeleteTrafficMirrorTargetResultTypeDef = TypedDict(
    "DeleteTrafficMirrorTargetResultTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "TransitGatewayConnectPeerId": str,
    },
)
_OptionalDeleteTransitGatewayConnectPeerRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayConnectPeerRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayConnectPeerRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayConnectPeerRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayConnectPeerRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayConnectPeerResultTypeDef = TypedDict(
    "DeleteTransitGatewayConnectPeerResultTypeDef",
    {
        "TransitGatewayConnectPeer": "TransitGatewayConnectPeerTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayConnectRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayConnectRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDeleteTransitGatewayConnectRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayConnectRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayConnectRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayConnectRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayConnectRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayConnectResultTypeDef = TypedDict(
    "DeleteTransitGatewayConnectResultTypeDef",
    {
        "TransitGatewayConnect": "TransitGatewayConnectTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
    },
)
_OptionalDeleteTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayMulticastDomainRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayMulticastDomainRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayMulticastDomainRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "DeleteTransitGatewayMulticastDomainResultTypeDef",
    {
        "TransitGatewayMulticastDomain": "TransitGatewayMulticastDomainTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayPeeringAttachmentRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "DeleteTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
    },
)
_OptionalDeleteTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayPolicyTableRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayPolicyTableRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayPolicyTableRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayPolicyTableResultTypeDef = TypedDict(
    "DeleteTransitGatewayPolicyTableResultTypeDef",
    {
        "TransitGatewayPolicyTable": "TransitGatewayPolicyTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
    },
)
_OptionalDeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayPrefixListReferenceRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayPrefixListReferenceResultTypeDef = TypedDict(
    "DeleteTransitGatewayPrefixListReferenceResultTypeDef",
    {
        "TransitGatewayPrefixListReference": "TransitGatewayPrefixListReferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
    },
)
_OptionalDeleteTransitGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayResultTypeDef = TypedDict(
    "DeleteTransitGatewayResultTypeDef",
    {
        "TransitGateway": "TransitGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayRouteRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "DestinationCidrBlock": str,
    },
)
_OptionalDeleteTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayRouteRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayRouteRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayRouteRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayRouteRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayRouteResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteResultTypeDef",
    {
        "Route": "TransitGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableAnnouncementId": str,
    },
)
_OptionalDeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayRouteTableAnnouncementRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayRouteTableAnnouncementResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableAnnouncementResultTypeDef",
    {
        "TransitGatewayRouteTableAnnouncement": "TransitGatewayRouteTableAnnouncementTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalDeleteTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayRouteTableRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayRouteTableRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayRouteTableRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayRouteTableResultTypeDef = TypedDict(
    "DeleteTransitGatewayRouteTableResultTypeDef",
    {
        "TransitGatewayRouteTable": "TransitGatewayRouteTableTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDeleteTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteTransitGatewayVpcAttachmentRequestRequestTypeDef(
    _RequiredDeleteTransitGatewayVpcAttachmentRequestRequestTypeDef,
    _OptionalDeleteTransitGatewayVpcAttachmentRequestRequestTypeDef,
):
    pass

DeleteTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "DeleteTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVerifiedAccessEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVerifiedAccessEndpointRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointId": str,
    },
)
_OptionalDeleteVerifiedAccessEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVerifiedAccessEndpointRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class DeleteVerifiedAccessEndpointRequestRequestTypeDef(
    _RequiredDeleteVerifiedAccessEndpointRequestRequestTypeDef,
    _OptionalDeleteVerifiedAccessEndpointRequestRequestTypeDef,
):
    pass

DeleteVerifiedAccessEndpointResultTypeDef = TypedDict(
    "DeleteVerifiedAccessEndpointResultTypeDef",
    {
        "VerifiedAccessEndpoint": "VerifiedAccessEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVerifiedAccessGroupRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVerifiedAccessGroupRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
    },
)
_OptionalDeleteVerifiedAccessGroupRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVerifiedAccessGroupRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class DeleteVerifiedAccessGroupRequestRequestTypeDef(
    _RequiredDeleteVerifiedAccessGroupRequestRequestTypeDef,
    _OptionalDeleteVerifiedAccessGroupRequestRequestTypeDef,
):
    pass

DeleteVerifiedAccessGroupResultTypeDef = TypedDict(
    "DeleteVerifiedAccessGroupResultTypeDef",
    {
        "VerifiedAccessGroup": "VerifiedAccessGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVerifiedAccessInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVerifiedAccessInstanceRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
    },
)
_OptionalDeleteVerifiedAccessInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVerifiedAccessInstanceRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

class DeleteVerifiedAccessInstanceRequestRequestTypeDef(
    _RequiredDeleteVerifiedAccessInstanceRequestRequestTypeDef,
    _OptionalDeleteVerifiedAccessInstanceRequestRequestTypeDef,
):
    pass

DeleteVerifiedAccessInstanceResultTypeDef = TypedDict(
    "DeleteVerifiedAccessInstanceResultTypeDef",
    {
        "VerifiedAccessInstance": "VerifiedAccessInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "VerifiedAccessTrustProviderId": str,
    },
)
_OptionalDeleteVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

class DeleteVerifiedAccessTrustProviderRequestRequestTypeDef(
    _RequiredDeleteVerifiedAccessTrustProviderRequestRequestTypeDef,
    _OptionalDeleteVerifiedAccessTrustProviderRequestRequestTypeDef,
):
    pass

DeleteVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "DeleteVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": "VerifiedAccessTrustProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalDeleteVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVolumeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteVolumeRequestRequestTypeDef(
    _RequiredDeleteVolumeRequestRequestTypeDef, _OptionalDeleteVolumeRequestRequestTypeDef
):
    pass

DeleteVolumeRequestVolumeTypeDef = TypedDict(
    "DeleteVolumeRequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    {
        "ConnectionNotificationIds": List[str],
    },
)
_OptionalDeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef(
    _RequiredDeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef,
    _OptionalDeleteVpcEndpointConnectionNotificationsRequestRequestTypeDef,
):
    pass

DeleteVpcEndpointConnectionNotificationsResultTypeDef = TypedDict(
    "DeleteVpcEndpointConnectionNotificationsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    {
        "ServiceIds": List[str],
    },
)
_OptionalDeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef(
    _RequiredDeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef,
    _OptionalDeleteVpcEndpointServiceConfigurationsRequestRequestTypeDef,
):
    pass

DeleteVpcEndpointServiceConfigurationsResultTypeDef = TypedDict(
    "DeleteVpcEndpointServiceConfigurationsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVpcEndpointsRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcEndpointsRequestRequestTypeDef",
    {
        "VpcEndpointIds": List[str],
    },
)
_OptionalDeleteVpcEndpointsRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcEndpointsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteVpcEndpointsRequestRequestTypeDef(
    _RequiredDeleteVpcEndpointsRequestRequestTypeDef,
    _OptionalDeleteVpcEndpointsRequestRequestTypeDef,
):
    pass

DeleteVpcEndpointsResultTypeDef = TypedDict(
    "DeleteVpcEndpointsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
    },
)
_OptionalDeleteVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcPeeringConnectionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteVpcPeeringConnectionRequestRequestTypeDef(
    _RequiredDeleteVpcPeeringConnectionRequestRequestTypeDef,
    _OptionalDeleteVpcPeeringConnectionRequestRequestTypeDef,
):
    pass

DeleteVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DeleteVpcPeeringConnectionResultTypeDef = TypedDict(
    "DeleteVpcPeeringConnectionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteVpcRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVpcRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDeleteVpcRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVpcRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteVpcRequestRequestTypeDef(
    _RequiredDeleteVpcRequestRequestTypeDef, _OptionalDeleteVpcRequestRequestTypeDef
):
    pass

DeleteVpcRequestVpcTypeDef = TypedDict(
    "DeleteVpcRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeleteVpnConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVpnConnectionRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
    },
)
_OptionalDeleteVpnConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVpnConnectionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteVpnConnectionRequestRequestTypeDef(
    _RequiredDeleteVpnConnectionRequestRequestTypeDef,
    _OptionalDeleteVpnConnectionRequestRequestTypeDef,
):
    pass

DeleteVpnConnectionRouteRequestRequestTypeDef = TypedDict(
    "DeleteVpnConnectionRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "VpnConnectionId": str,
    },
)

_RequiredDeleteVpnGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredDeleteVpnGatewayRequestRequestTypeDef",
    {
        "VpnGatewayId": str,
    },
)
_OptionalDeleteVpnGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalDeleteVpnGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeleteVpnGatewayRequestRequestTypeDef(
    _RequiredDeleteVpnGatewayRequestRequestTypeDef, _OptionalDeleteVpnGatewayRequestRequestTypeDef
):
    pass

_RequiredDeprovisionByoipCidrRequestRequestTypeDef = TypedDict(
    "_RequiredDeprovisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalDeprovisionByoipCidrRequestRequestTypeDef = TypedDict(
    "_OptionalDeprovisionByoipCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeprovisionByoipCidrRequestRequestTypeDef(
    _RequiredDeprovisionByoipCidrRequestRequestTypeDef,
    _OptionalDeprovisionByoipCidrRequestRequestTypeDef,
):
    pass

DeprovisionByoipCidrResultTypeDef = TypedDict(
    "DeprovisionByoipCidrResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeprovisionIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "_RequiredDeprovisionIpamPoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
    },
)
_OptionalDeprovisionIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "_OptionalDeprovisionIpamPoolCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Cidr": str,
    },
    total=False,
)

class DeprovisionIpamPoolCidrRequestRequestTypeDef(
    _RequiredDeprovisionIpamPoolCidrRequestRequestTypeDef,
    _OptionalDeprovisionIpamPoolCidrRequestRequestTypeDef,
):
    pass

DeprovisionIpamPoolCidrResultTypeDef = TypedDict(
    "DeprovisionIpamPoolCidrResultTypeDef",
    {
        "IpamPoolCidr": "IpamPoolCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeprovisionPublicIpv4PoolCidrRequestRequestTypeDef = TypedDict(
    "_RequiredDeprovisionPublicIpv4PoolCidrRequestRequestTypeDef",
    {
        "PoolId": str,
        "Cidr": str,
    },
)
_OptionalDeprovisionPublicIpv4PoolCidrRequestRequestTypeDef = TypedDict(
    "_OptionalDeprovisionPublicIpv4PoolCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeprovisionPublicIpv4PoolCidrRequestRequestTypeDef(
    _RequiredDeprovisionPublicIpv4PoolCidrRequestRequestTypeDef,
    _OptionalDeprovisionPublicIpv4PoolCidrRequestRequestTypeDef,
):
    pass

DeprovisionPublicIpv4PoolCidrResultTypeDef = TypedDict(
    "DeprovisionPublicIpv4PoolCidrResultTypeDef",
    {
        "PoolId": str,
        "DeprovisionedAddresses": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterImageRequestImageTypeDef = TypedDict(
    "DeregisterImageRequestImageTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDeregisterImageRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterImageRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalDeregisterImageRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterImageRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeregisterImageRequestRequestTypeDef(
    _RequiredDeregisterImageRequestRequestTypeDef, _OptionalDeregisterImageRequestRequestTypeDef
):
    pass

_RequiredDeregisterInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredDeregisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "InstanceTagAttribute": "DeregisterInstanceTagAttributeRequestTypeDef",
    },
)
_OptionalDeregisterInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalDeregisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DeregisterInstanceEventNotificationAttributesRequestRequestTypeDef(
    _RequiredDeregisterInstanceEventNotificationAttributesRequestRequestTypeDef,
    _OptionalDeregisterInstanceEventNotificationAttributesRequestRequestTypeDef,
):
    pass

DeregisterInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "DeregisterInstanceEventNotificationAttributesResultTypeDef",
    {
        "InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "DeregisterInstanceTagAttributeRequestTypeDef",
    {
        "IncludeAllTagsOfInstance": bool,
        "InstanceTagKeys": List[str],
    },
    total=False,
)

DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "GroupIpAddress": str,
        "NetworkInterfaceIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DeregisterTransitGatewayMulticastGroupMembersResultTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupMembersResultTypeDef",
    {
        "DeregisteredMulticastGroupMembers": "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "GroupIpAddress": str,
        "NetworkInterfaceIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef = TypedDict(
    "DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    {
        "DeregisteredMulticastGroupSources": "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAccountAttributesRequestRequestTypeDef = TypedDict(
    "DescribeAccountAttributesRequestRequestTypeDef",
    {
        "AttributeNames": List[AccountAttributeNameType],
        "DryRun": bool,
    },
    total=False,
)

DescribeAccountAttributesResultTypeDef = TypedDict(
    "DescribeAccountAttributesResultTypeDef",
    {
        "AccountAttributes": List["AccountAttributeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressTransfersRequestRequestTypeDef = TypedDict(
    "DescribeAddressTransfersRequestRequestTypeDef",
    {
        "AllocationIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)

DescribeAddressTransfersResultTypeDef = TypedDict(
    "DescribeAddressTransfersResultTypeDef",
    {
        "AddressTransfers": List["AddressTransferTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressesAttributeRequestRequestTypeDef = TypedDict(
    "DescribeAddressesAttributeRequestRequestTypeDef",
    {
        "AllocationIds": List[str],
        "Attribute": Literal["domain-name"],
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)

DescribeAddressesAttributeResultTypeDef = TypedDict(
    "DescribeAddressesAttributeResultTypeDef",
    {
        "Addresses": List["AddressAttributeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAddressesRequestRequestTypeDef = TypedDict(
    "DescribeAddressesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "PublicIps": List[str],
        "AllocationIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeAddressesResultTypeDef = TypedDict(
    "DescribeAddressesResultTypeDef",
    {
        "Addresses": List["AddressTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAggregateIdFormatRequestRequestTypeDef = TypedDict(
    "DescribeAggregateIdFormatRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DescribeAggregateIdFormatResultTypeDef = TypedDict(
    "DescribeAggregateIdFormatResultTypeDef",
    {
        "UseLongIdsAggregated": bool,
        "Statuses": List["IdFormatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailabilityZonesRequestRequestTypeDef = TypedDict(
    "DescribeAvailabilityZonesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "ZoneNames": List[str],
        "ZoneIds": List[str],
        "AllAvailabilityZones": bool,
        "DryRun": bool,
    },
    total=False,
)

DescribeAvailabilityZonesResultTypeDef = TypedDict(
    "DescribeAvailabilityZonesResultTypeDef",
    {
        "AvailabilityZones": List["AvailabilityZoneTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAwsNetworkPerformanceMetricSubscriptionsRequestRequestTypeDef = TypedDict(
    "DescribeAwsNetworkPerformanceMetricSubscriptionsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef = TypedDict(
    "DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef",
    {
        "NextToken": str,
        "Subscriptions": List["SubscriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBundleTasksRequestRequestTypeDef = TypedDict(
    "DescribeBundleTasksRequestRequestTypeDef",
    {
        "BundleIds": List[str],
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeBundleTasksResultTypeDef = TypedDict(
    "DescribeBundleTasksResultTypeDef",
    {
        "BundleTasks": List["BundleTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeByoipCidrsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeByoipCidrsRequestRequestTypeDef",
    {
        "MaxResults": int,
    },
)
_OptionalDescribeByoipCidrsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeByoipCidrsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "NextToken": str,
    },
    total=False,
)

class DescribeByoipCidrsRequestRequestTypeDef(
    _RequiredDescribeByoipCidrsRequestRequestTypeDef,
    _OptionalDescribeByoipCidrsRequestRequestTypeDef,
):
    pass

DescribeByoipCidrsResultTypeDef = TypedDict(
    "DescribeByoipCidrsResultTypeDef",
    {
        "ByoipCidrs": List["ByoipCidrTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeCapacityBlockOfferingsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeCapacityBlockOfferingsRequestRequestTypeDef",
    {
        "InstanceType": str,
        "InstanceCount": int,
        "CapacityDurationHours": int,
    },
)
_OptionalDescribeCapacityBlockOfferingsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeCapacityBlockOfferingsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "StartDateRange": Union[datetime, str],
        "EndDateRange": Union[datetime, str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class DescribeCapacityBlockOfferingsRequestRequestTypeDef(
    _RequiredDescribeCapacityBlockOfferingsRequestRequestTypeDef,
    _OptionalDescribeCapacityBlockOfferingsRequestRequestTypeDef,
):
    pass

DescribeCapacityBlockOfferingsResultTypeDef = TypedDict(
    "DescribeCapacityBlockOfferingsResultTypeDef",
    {
        "CapacityBlockOfferings": List["CapacityBlockOfferingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCapacityReservationFleetsRequestRequestTypeDef = TypedDict(
    "DescribeCapacityReservationFleetsRequestRequestTypeDef",
    {
        "CapacityReservationFleetIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeCapacityReservationFleetsResultTypeDef = TypedDict(
    "DescribeCapacityReservationFleetsResultTypeDef",
    {
        "CapacityReservationFleets": List["CapacityReservationFleetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCapacityReservationsRequestRequestTypeDef = TypedDict(
    "DescribeCapacityReservationsRequestRequestTypeDef",
    {
        "CapacityReservationIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeCapacityReservationsResultTypeDef = TypedDict(
    "DescribeCapacityReservationsResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservations": List["CapacityReservationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCarrierGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeCarrierGatewaysRequestRequestTypeDef",
    {
        "CarrierGatewayIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeCarrierGatewaysResultTypeDef = TypedDict(
    "DescribeCarrierGatewaysResultTypeDef",
    {
        "CarrierGateways": List["CarrierGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClassicLinkInstancesRequestRequestTypeDef = TypedDict(
    "DescribeClassicLinkInstancesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "InstanceIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeClassicLinkInstancesResultTypeDef = TypedDict(
    "DescribeClassicLinkInstancesResultTypeDef",
    {
        "Instances": List["ClassicLinkInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeClientVpnAuthorizationRulesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeClientVpnAuthorizationRulesRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDescribeClientVpnAuthorizationRulesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeClientVpnAuthorizationRulesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
    },
    total=False,
)

class DescribeClientVpnAuthorizationRulesRequestRequestTypeDef(
    _RequiredDescribeClientVpnAuthorizationRulesRequestRequestTypeDef,
    _OptionalDescribeClientVpnAuthorizationRulesRequestRequestTypeDef,
):
    pass

DescribeClientVpnAuthorizationRulesResultTypeDef = TypedDict(
    "DescribeClientVpnAuthorizationRulesResultTypeDef",
    {
        "AuthorizationRules": List["AuthorizationRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeClientVpnConnectionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeClientVpnConnectionsRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDescribeClientVpnConnectionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeClientVpnConnectionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)

class DescribeClientVpnConnectionsRequestRequestTypeDef(
    _RequiredDescribeClientVpnConnectionsRequestRequestTypeDef,
    _OptionalDescribeClientVpnConnectionsRequestRequestTypeDef,
):
    pass

DescribeClientVpnConnectionsResultTypeDef = TypedDict(
    "DescribeClientVpnConnectionsResultTypeDef",
    {
        "Connections": List["ClientVpnConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeClientVpnEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeClientVpnEndpointsRequestRequestTypeDef",
    {
        "ClientVpnEndpointIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeClientVpnEndpointsResultTypeDef = TypedDict(
    "DescribeClientVpnEndpointsResultTypeDef",
    {
        "ClientVpnEndpoints": List["ClientVpnEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeClientVpnRoutesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeClientVpnRoutesRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDescribeClientVpnRoutesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeClientVpnRoutesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class DescribeClientVpnRoutesRequestRequestTypeDef(
    _RequiredDescribeClientVpnRoutesRequestRequestTypeDef,
    _OptionalDescribeClientVpnRoutesRequestRequestTypeDef,
):
    pass

DescribeClientVpnRoutesResultTypeDef = TypedDict(
    "DescribeClientVpnRoutesResultTypeDef",
    {
        "Routes": List["ClientVpnRouteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeClientVpnTargetNetworksRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeClientVpnTargetNetworksRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalDescribeClientVpnTargetNetworksRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeClientVpnTargetNetworksRequestRequestTypeDef",
    {
        "AssociationIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class DescribeClientVpnTargetNetworksRequestRequestTypeDef(
    _RequiredDescribeClientVpnTargetNetworksRequestRequestTypeDef,
    _OptionalDescribeClientVpnTargetNetworksRequestRequestTypeDef,
):
    pass

DescribeClientVpnTargetNetworksResultTypeDef = TypedDict(
    "DescribeClientVpnTargetNetworksResultTypeDef",
    {
        "ClientVpnTargetNetworks": List["TargetNetworkTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCoipPoolsRequestRequestTypeDef = TypedDict(
    "DescribeCoipPoolsRequestRequestTypeDef",
    {
        "PoolIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeCoipPoolsResultTypeDef = TypedDict(
    "DescribeCoipPoolsResultTypeDef",
    {
        "CoipPools": List["CoipPoolTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeConversionTasksRequestRequestTypeDef = TypedDict(
    "DescribeConversionTasksRequestRequestTypeDef",
    {
        "ConversionTaskIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeConversionTasksResultTypeDef = TypedDict(
    "DescribeConversionTasksResultTypeDef",
    {
        "ConversionTasks": List["ConversionTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCustomerGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeCustomerGatewaysRequestRequestTypeDef",
    {
        "CustomerGatewayIds": List[str],
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeCustomerGatewaysResultTypeDef = TypedDict(
    "DescribeCustomerGatewaysResultTypeDef",
    {
        "CustomerGateways": List["CustomerGatewayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeDhcpOptionsRequestRequestTypeDef = TypedDict(
    "DescribeDhcpOptionsRequestRequestTypeDef",
    {
        "DhcpOptionsIds": List[str],
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeDhcpOptionsResultTypeDef = TypedDict(
    "DescribeDhcpOptionsResultTypeDef",
    {
        "DhcpOptions": List["DhcpOptionsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysRequestRequestTypeDef",
    {
        "DryRun": bool,
        "EgressOnlyInternetGatewayIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeEgressOnlyInternetGatewaysResultTypeDef = TypedDict(
    "DescribeEgressOnlyInternetGatewaysResultTypeDef",
    {
        "EgressOnlyInternetGateways": List["EgressOnlyInternetGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeElasticGpusRequestRequestTypeDef = TypedDict(
    "DescribeElasticGpusRequestRequestTypeDef",
    {
        "ElasticGpuIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeElasticGpusResultTypeDef = TypedDict(
    "DescribeElasticGpusResultTypeDef",
    {
        "ElasticGpuSet": List["ElasticGpusTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportImageTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportImageTasksRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "ExportImageTaskIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeExportImageTasksResultTypeDef = TypedDict(
    "DescribeExportImageTasksResultTypeDef",
    {
        "ExportImageTasks": List["ExportImageTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeExportTasksRequestRequestTypeDef = TypedDict(
    "DescribeExportTasksRequestRequestTypeDef",
    {
        "ExportTaskIds": List[str],
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeExportTasksResultTypeDef = TypedDict(
    "DescribeExportTasksResultTypeDef",
    {
        "ExportTasks": List["ExportTaskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFastLaunchImagesRequestRequestTypeDef = TypedDict(
    "DescribeFastLaunchImagesRequestRequestTypeDef",
    {
        "ImageIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeFastLaunchImagesResultTypeDef = TypedDict(
    "DescribeFastLaunchImagesResultTypeDef",
    {
        "FastLaunchImages": List["DescribeFastLaunchImagesSuccessItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFastLaunchImagesSuccessItemTypeDef = TypedDict(
    "DescribeFastLaunchImagesSuccessItemTypeDef",
    {
        "ImageId": str,
        "ResourceType": Literal["snapshot"],
        "SnapshotConfiguration": "FastLaunchSnapshotConfigurationResponseTypeDef",
        "LaunchTemplate": "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
        "MaxParallelLaunches": int,
        "OwnerId": str,
        "State": FastLaunchStateCodeType,
        "StateTransitionReason": str,
        "StateTransitionTime": datetime,
    },
    total=False,
)

DescribeFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DescribeFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": str,
        "AvailabilityZone": str,
        "State": FastSnapshotRestoreStateCodeType,
        "StateTransitionReason": str,
        "OwnerId": str,
        "OwnerAlias": str,
        "EnablingTime": datetime,
        "OptimizingTime": datetime,
        "EnabledTime": datetime,
        "DisablingTime": datetime,
        "DisabledTime": datetime,
    },
    total=False,
)

DescribeFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeFastSnapshotRestoresResultTypeDef = TypedDict(
    "DescribeFastSnapshotRestoresResultTypeDef",
    {
        "FastSnapshotRestores": List["DescribeFastSnapshotRestoreSuccessItemTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetErrorTypeDef = TypedDict(
    "DescribeFleetErrorTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": InstanceLifecycleType,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

_RequiredDescribeFleetHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFleetHistoryRequestRequestTypeDef",
    {
        "FleetId": str,
        "StartTime": Union[datetime, str],
    },
)
_OptionalDescribeFleetHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFleetHistoryRequestRequestTypeDef",
    {
        "DryRun": bool,
        "EventType": FleetEventTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeFleetHistoryRequestRequestTypeDef(
    _RequiredDescribeFleetHistoryRequestRequestTypeDef,
    _OptionalDescribeFleetHistoryRequestRequestTypeDef,
):
    pass

DescribeFleetHistoryResultTypeDef = TypedDict(
    "DescribeFleetHistoryResultTypeDef",
    {
        "HistoryRecords": List["HistoryRecordEntryTypeDef"],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "FleetId": str,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFleetInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFleetInstancesRequestRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalDescribeFleetInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFleetInstancesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

class DescribeFleetInstancesRequestRequestTypeDef(
    _RequiredDescribeFleetInstancesRequestRequestTypeDef,
    _OptionalDescribeFleetInstancesRequestRequestTypeDef,
):
    pass

DescribeFleetInstancesResultTypeDef = TypedDict(
    "DescribeFleetInstancesResultTypeDef",
    {
        "ActiveInstances": List["ActiveInstanceTypeDef"],
        "NextToken": str,
        "FleetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFleetsInstancesTypeDef = TypedDict(
    "DescribeFleetsInstancesTypeDef",
    {
        "LaunchTemplateAndOverrides": "LaunchTemplateAndOverridesResponseTypeDef",
        "Lifecycle": InstanceLifecycleType,
        "InstanceIds": List[str],
        "InstanceType": InstanceTypeType,
        "Platform": Literal["Windows"],
    },
    total=False,
)

DescribeFleetsRequestRequestTypeDef = TypedDict(
    "DescribeFleetsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
        "FleetIds": List[str],
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeFleetsResultTypeDef = TypedDict(
    "DescribeFleetsResultTypeDef",
    {
        "NextToken": str,
        "Fleets": List["FleetDataTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFlowLogsRequestRequestTypeDef = TypedDict(
    "DescribeFlowLogsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "FlowLogIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeFlowLogsResultTypeDef = TypedDict(
    "DescribeFlowLogsResultTypeDef",
    {
        "FlowLogs": List["FlowLogTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeFpgaImageAttributeRequestRequestTypeDef",
    {
        "FpgaImageId": str,
        "Attribute": FpgaImageAttributeNameType,
    },
)
_OptionalDescribeFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeFpgaImageAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeFpgaImageAttributeRequestRequestTypeDef(
    _RequiredDescribeFpgaImageAttributeRequestRequestTypeDef,
    _OptionalDescribeFpgaImageAttributeRequestRequestTypeDef,
):
    pass

DescribeFpgaImageAttributeResultTypeDef = TypedDict(
    "DescribeFpgaImageAttributeResultTypeDef",
    {
        "FpgaImageAttribute": "FpgaImageAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFpgaImagesRequestRequestTypeDef = TypedDict(
    "DescribeFpgaImagesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "FpgaImageIds": List[str],
        "Owners": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeFpgaImagesResultTypeDef = TypedDict(
    "DescribeFpgaImagesResultTypeDef",
    {
        "FpgaImages": List["FpgaImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostReservationOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeHostReservationOfferingsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxDuration": int,
        "MaxResults": int,
        "MinDuration": int,
        "NextToken": str,
        "OfferingId": str,
    },
    total=False,
)

DescribeHostReservationOfferingsResultTypeDef = TypedDict(
    "DescribeHostReservationOfferingsResultTypeDef",
    {
        "NextToken": str,
        "OfferingSet": List["HostOfferingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostReservationsRequestRequestTypeDef = TypedDict(
    "DescribeHostReservationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "HostReservationIdSet": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeHostReservationsResultTypeDef = TypedDict(
    "DescribeHostReservationsResultTypeDef",
    {
        "HostReservationSet": List["HostReservationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeHostsRequestRequestTypeDef = TypedDict(
    "DescribeHostsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "HostIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeHostsResultTypeDef = TypedDict(
    "DescribeHostsResultTypeDef",
    {
        "Hosts": List["HostTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIamInstanceProfileAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsRequestRequestTypeDef",
    {
        "AssociationIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeIamInstanceProfileAssociationsResultTypeDef = TypedDict(
    "DescribeIamInstanceProfileAssociationsResultTypeDef",
    {
        "IamInstanceProfileAssociations": List["IamInstanceProfileAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIdFormatRequestRequestTypeDef = TypedDict(
    "DescribeIdFormatRequestRequestTypeDef",
    {
        "Resource": str,
    },
    total=False,
)

DescribeIdFormatResultTypeDef = TypedDict(
    "DescribeIdFormatResultTypeDef",
    {
        "Statuses": List["IdFormatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeIdentityIdFormatRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeIdentityIdFormatRequestRequestTypeDef",
    {
        "PrincipalArn": str,
    },
)
_OptionalDescribeIdentityIdFormatRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeIdentityIdFormatRequestRequestTypeDef",
    {
        "Resource": str,
    },
    total=False,
)

class DescribeIdentityIdFormatRequestRequestTypeDef(
    _RequiredDescribeIdentityIdFormatRequestRequestTypeDef,
    _OptionalDescribeIdentityIdFormatRequestRequestTypeDef,
):
    pass

DescribeIdentityIdFormatResultTypeDef = TypedDict(
    "DescribeIdentityIdFormatResultTypeDef",
    {
        "Statuses": List["IdFormatTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeImageAttributeRequestImageTypeDef = TypedDict(
    "_RequiredDescribeImageAttributeRequestImageTypeDef",
    {
        "Attribute": ImageAttributeNameType,
    },
)
_OptionalDescribeImageAttributeRequestImageTypeDef = TypedDict(
    "_OptionalDescribeImageAttributeRequestImageTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeImageAttributeRequestImageTypeDef(
    _RequiredDescribeImageAttributeRequestImageTypeDef,
    _OptionalDescribeImageAttributeRequestImageTypeDef,
):
    pass

_RequiredDescribeImageAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeImageAttributeRequestRequestTypeDef",
    {
        "Attribute": ImageAttributeNameType,
        "ImageId": str,
    },
)
_OptionalDescribeImageAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeImageAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeImageAttributeRequestRequestTypeDef(
    _RequiredDescribeImageAttributeRequestRequestTypeDef,
    _OptionalDescribeImageAttributeRequestRequestTypeDef,
):
    pass

DescribeImagesRequestRequestTypeDef = TypedDict(
    "DescribeImagesRequestRequestTypeDef",
    {
        "ExecutableUsers": List[str],
        "Filters": List["FilterTypeDef"],
        "ImageIds": List[str],
        "Owners": List[str],
        "IncludeDeprecated": bool,
        "IncludeDisabled": bool,
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeImagesResultTypeDef = TypedDict(
    "DescribeImagesResultTypeDef",
    {
        "Images": List["ImageTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportImageTasksRequestRequestTypeDef = TypedDict(
    "DescribeImportImageTasksRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "ImportTaskIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeImportImageTasksResultTypeDef = TypedDict(
    "DescribeImportImageTasksResultTypeDef",
    {
        "ImportImageTasks": List["ImportImageTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeImportSnapshotTasksRequestRequestTypeDef = TypedDict(
    "DescribeImportSnapshotTasksRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "ImportTaskIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeImportSnapshotTasksResultTypeDef = TypedDict(
    "DescribeImportSnapshotTasksResultTypeDef",
    {
        "ImportSnapshotTasks": List["ImportSnapshotTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "_RequiredDescribeInstanceAttributeRequestInstanceTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
    },
)
_OptionalDescribeInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "_OptionalDescribeInstanceAttributeRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeInstanceAttributeRequestInstanceTypeDef(
    _RequiredDescribeInstanceAttributeRequestInstanceTypeDef,
    _OptionalDescribeInstanceAttributeRequestInstanceTypeDef,
):
    pass

_RequiredDescribeInstanceAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeInstanceAttributeRequestRequestTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "InstanceId": str,
    },
)
_OptionalDescribeInstanceAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeInstanceAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeInstanceAttributeRequestRequestTypeDef(
    _RequiredDescribeInstanceAttributeRequestRequestTypeDef,
    _OptionalDescribeInstanceAttributeRequestRequestTypeDef,
):
    pass

DescribeInstanceConnectEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceConnectEndpointsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "InstanceConnectEndpointIds": List[str],
    },
    total=False,
)

DescribeInstanceConnectEndpointsResultTypeDef = TypedDict(
    "DescribeInstanceConnectEndpointsResultTypeDef",
    {
        "InstanceConnectEndpoints": List["Ec2InstanceConnectEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceCreditSpecificationsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "InstanceIds": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceCreditSpecificationsResultTypeDef = TypedDict(
    "DescribeInstanceCreditSpecificationsResultTypeDef",
    {
        "InstanceCreditSpecifications": List["InstanceCreditSpecificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "DescribeInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DescribeInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "DescribeInstanceEventNotificationAttributesResultTypeDef",
    {
        "InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceEventWindowsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceEventWindowsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "InstanceEventWindowIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceEventWindowsResultTypeDef = TypedDict(
    "DescribeInstanceEventWindowsResultTypeDef",
    {
        "InstanceEventWindows": List["InstanceEventWindowTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceStatusRequestRequestTypeDef = TypedDict(
    "DescribeInstanceStatusRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "InstanceIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
        "IncludeAllInstances": bool,
    },
    total=False,
)

DescribeInstanceStatusResultTypeDef = TypedDict(
    "DescribeInstanceStatusResultTypeDef",
    {
        "InstanceStatuses": List["InstanceStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceTopologyRequestRequestTypeDef = TypedDict(
    "DescribeInstanceTopologyRequestRequestTypeDef",
    {
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
        "InstanceIds": List[str],
        "GroupNames": List[str],
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeInstanceTopologyResultTypeDef = TypedDict(
    "DescribeInstanceTopologyResultTypeDef",
    {
        "Instances": List["InstanceTopologyTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceTypeOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "LocationType": LocationTypeType,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceTypeOfferingsResultTypeDef = TypedDict(
    "DescribeInstanceTypeOfferingsResultTypeDef",
    {
        "InstanceTypeOfferings": List["InstanceTypeOfferingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstanceTypesRequestRequestTypeDef = TypedDict(
    "DescribeInstanceTypesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "InstanceTypes": List[InstanceTypeType],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstanceTypesResultTypeDef = TypedDict(
    "DescribeInstanceTypesResultTypeDef",
    {
        "InstanceTypes": List["InstanceTypeInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInstancesRequestRequestTypeDef = TypedDict(
    "DescribeInstancesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "InstanceIds": List[str],
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeInstancesResultTypeDef = TypedDict(
    "DescribeInstancesResultTypeDef",
    {
        "Reservations": List["ReservationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeInternetGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeInternetGatewaysRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "InternetGatewayIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeInternetGatewaysResultTypeDef = TypedDict(
    "DescribeInternetGatewaysResultTypeDef",
    {
        "InternetGateways": List["InternetGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpamPoolsRequestRequestTypeDef = TypedDict(
    "DescribeIpamPoolsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "IpamPoolIds": List[str],
    },
    total=False,
)

DescribeIpamPoolsResultTypeDef = TypedDict(
    "DescribeIpamPoolsResultTypeDef",
    {
        "NextToken": str,
        "IpamPools": List["IpamPoolTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpamResourceDiscoveriesRequestRequestTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveriesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "IpamResourceDiscoveryIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeIpamResourceDiscoveriesResultTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveriesResultTypeDef",
    {
        "IpamResourceDiscoveries": List["IpamResourceDiscoveryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpamResourceDiscoveryAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveryAssociationsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "IpamResourceDiscoveryAssociationIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeIpamResourceDiscoveryAssociationsResultTypeDef = TypedDict(
    "DescribeIpamResourceDiscoveryAssociationsResultTypeDef",
    {
        "IpamResourceDiscoveryAssociations": List["IpamResourceDiscoveryAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpamScopesRequestRequestTypeDef = TypedDict(
    "DescribeIpamScopesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "IpamScopeIds": List[str],
    },
    total=False,
)

DescribeIpamScopesResultTypeDef = TypedDict(
    "DescribeIpamScopesResultTypeDef",
    {
        "NextToken": str,
        "IpamScopes": List["IpamScopeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpamsRequestRequestTypeDef = TypedDict(
    "DescribeIpamsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "IpamIds": List[str],
    },
    total=False,
)

DescribeIpamsResultTypeDef = TypedDict(
    "DescribeIpamsResultTypeDef",
    {
        "NextToken": str,
        "Ipams": List["IpamTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeIpv6PoolsRequestRequestTypeDef = TypedDict(
    "DescribeIpv6PoolsRequestRequestTypeDef",
    {
        "PoolIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribeIpv6PoolsResultTypeDef = TypedDict(
    "DescribeIpv6PoolsResultTypeDef",
    {
        "Ipv6Pools": List["Ipv6PoolTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeKeyPairsRequestRequestTypeDef = TypedDict(
    "DescribeKeyPairsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "KeyNames": List[str],
        "KeyPairIds": List[str],
        "DryRun": bool,
        "IncludePublicKey": bool,
    },
    total=False,
)

DescribeKeyPairsResultTypeDef = TypedDict(
    "DescribeKeyPairsResultTypeDef",
    {
        "KeyPairs": List["KeyPairInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLaunchTemplateVersionsRequestRequestTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Versions": List[str],
        "MinVersion": str,
        "MaxVersion": str,
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "ResolveAlias": bool,
    },
    total=False,
)

DescribeLaunchTemplateVersionsResultTypeDef = TypedDict(
    "DescribeLaunchTemplateVersionsResultTypeDef",
    {
        "LaunchTemplateVersions": List["LaunchTemplateVersionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLaunchTemplatesRequestRequestTypeDef = TypedDict(
    "DescribeLaunchTemplatesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "LaunchTemplateIds": List[str],
        "LaunchTemplateNames": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeLaunchTemplatesResultTypeDef = TypedDict(
    "DescribeLaunchTemplatesResultTypeDef",
    {
        "LaunchTemplates": List["LaunchTemplateTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociations": List[
            "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociations": List[
            "LocalGatewayRouteTableVpcAssociationTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayRouteTablesRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayRouteTablesResultTypeDef = TypedDict(
    "DescribeLocalGatewayRouteTablesResultTypeDef",
    {
        "LocalGatewayRouteTables": List["LocalGatewayRouteTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsRequestRequestTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroups": List["LocalGatewayVirtualInterfaceGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesRequestRequestTypeDef",
    {
        "LocalGatewayVirtualInterfaceIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewayVirtualInterfacesResultTypeDef = TypedDict(
    "DescribeLocalGatewayVirtualInterfacesResultTypeDef",
    {
        "LocalGatewayVirtualInterfaces": List["LocalGatewayVirtualInterfaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeLocalGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeLocalGatewaysRequestRequestTypeDef",
    {
        "LocalGatewayIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeLocalGatewaysResultTypeDef = TypedDict(
    "DescribeLocalGatewaysResultTypeDef",
    {
        "LocalGateways": List["LocalGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeManagedPrefixListsRequestRequestTypeDef = TypedDict(
    "DescribeManagedPrefixListsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "PrefixListIds": List[str],
    },
    total=False,
)

DescribeManagedPrefixListsResultTypeDef = TypedDict(
    "DescribeManagedPrefixListsResultTypeDef",
    {
        "NextToken": str,
        "PrefixLists": List["ManagedPrefixListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMovingAddressesRequestRequestTypeDef = TypedDict(
    "DescribeMovingAddressesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
        "PublicIps": List[str],
    },
    total=False,
)

DescribeMovingAddressesResultTypeDef = TypedDict(
    "DescribeMovingAddressesResultTypeDef",
    {
        "MovingAddressStatuses": List["MovingAddressStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNatGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeNatGatewaysRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NatGatewayIds": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeNatGatewaysResultTypeDef = TypedDict(
    "DescribeNatGatewaysResultTypeDef",
    {
        "NatGateways": List["NatGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkAclsRequestRequestTypeDef = TypedDict(
    "DescribeNetworkAclsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "NetworkAclIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeNetworkAclsResultTypeDef = TypedDict(
    "DescribeNetworkAclsResultTypeDef",
    {
        "NetworkAcls": List["NetworkAclTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopeAnalysesRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisIds": List[str],
        "NetworkInsightsAccessScopeId": str,
        "AnalysisStartTimeBegin": Union[datetime, str],
        "AnalysisStartTimeEnd": Union[datetime, str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "DryRun": bool,
        "NextToken": str,
    },
    total=False,
)

DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalyses": List["NetworkInsightsAccessScopeAnalysisTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsAccessScopesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopesRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "DryRun": bool,
        "NextToken": str,
    },
    total=False,
)

DescribeNetworkInsightsAccessScopesResultTypeDef = TypedDict(
    "DescribeNetworkInsightsAccessScopesResultTypeDef",
    {
        "NetworkInsightsAccessScopes": List["NetworkInsightsAccessScopeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsAnalysesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsAnalysesRequestRequestTypeDef",
    {
        "NetworkInsightsAnalysisIds": List[str],
        "NetworkInsightsPathId": str,
        "AnalysisStartTime": Union[datetime, str],
        "AnalysisEndTime": Union[datetime, str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "DryRun": bool,
        "NextToken": str,
    },
    total=False,
)

DescribeNetworkInsightsAnalysesResultTypeDef = TypedDict(
    "DescribeNetworkInsightsAnalysesResultTypeDef",
    {
        "NetworkInsightsAnalyses": List["NetworkInsightsAnalysisTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInsightsPathsRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInsightsPathsRequestRequestTypeDef",
    {
        "NetworkInsightsPathIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "DryRun": bool,
        "NextToken": str,
    },
    total=False,
)

DescribeNetworkInsightsPathsResultTypeDef = TypedDict(
    "DescribeNetworkInsightsPathsResultTypeDef",
    {
        "NetworkInsightsPaths": List["NetworkInsightsPathTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    {
        "Attribute": NetworkInterfaceAttributeType,
        "DryRun": bool,
    },
    total=False,
)

_RequiredDescribeNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalDescribeNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "Attribute": NetworkInterfaceAttributeType,
        "DryRun": bool,
    },
    total=False,
)

class DescribeNetworkInterfaceAttributeRequestRequestTypeDef(
    _RequiredDescribeNetworkInterfaceAttributeRequestRequestTypeDef,
    _OptionalDescribeNetworkInterfaceAttributeRequestRequestTypeDef,
):
    pass

DescribeNetworkInterfaceAttributeResultTypeDef = TypedDict(
    "DescribeNetworkInterfaceAttributeResultTypeDef",
    {
        "Attachment": "NetworkInterfaceAttachmentTypeDef",
        "Description": "AttributeValueTypeDef",
        "Groups": List["GroupIdentifierTypeDef"],
        "NetworkInterfaceId": str,
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInterfacePermissionsRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsRequestRequestTypeDef",
    {
        "NetworkInterfacePermissionIds": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeNetworkInterfacePermissionsResultTypeDef = TypedDict(
    "DescribeNetworkInterfacePermissionsResultTypeDef",
    {
        "NetworkInterfacePermissions": List["NetworkInterfacePermissionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNetworkInterfacesRequestRequestTypeDef = TypedDict(
    "DescribeNetworkInterfacesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "NetworkInterfaceIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeNetworkInterfacesResultTypeDef = TypedDict(
    "DescribeNetworkInterfacesResultTypeDef",
    {
        "NetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePlacementGroupsRequestRequestTypeDef = TypedDict(
    "DescribePlacementGroupsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "GroupNames": List[str],
        "GroupIds": List[str],
    },
    total=False,
)

DescribePlacementGroupsResultTypeDef = TypedDict(
    "DescribePlacementGroupsResultTypeDef",
    {
        "PlacementGroups": List["PlacementGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePrefixListsRequestRequestTypeDef = TypedDict(
    "DescribePrefixListsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "PrefixListIds": List[str],
    },
    total=False,
)

DescribePrefixListsResultTypeDef = TypedDict(
    "DescribePrefixListsResultTypeDef",
    {
        "NextToken": str,
        "PrefixLists": List["PrefixListTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePrincipalIdFormatRequestRequestTypeDef = TypedDict(
    "DescribePrincipalIdFormatRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Resources": List[str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribePrincipalIdFormatResultTypeDef = TypedDict(
    "DescribePrincipalIdFormatResultTypeDef",
    {
        "Principals": List["PrincipalIdFormatTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribePublicIpv4PoolsRequestRequestTypeDef = TypedDict(
    "DescribePublicIpv4PoolsRequestRequestTypeDef",
    {
        "PoolIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
    },
    total=False,
)

DescribePublicIpv4PoolsResultTypeDef = TypedDict(
    "DescribePublicIpv4PoolsResultTypeDef",
    {
        "PublicIpv4Pools": List["PublicIpv4PoolTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRegionsRequestRequestTypeDef = TypedDict(
    "DescribeRegionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "RegionNames": List[str],
        "DryRun": bool,
        "AllRegions": bool,
    },
    total=False,
)

DescribeRegionsResultTypeDef = TypedDict(
    "DescribeRegionsResultTypeDef",
    {
        "Regions": List["RegionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReplaceRootVolumeTasksRequestRequestTypeDef = TypedDict(
    "DescribeReplaceRootVolumeTasksRequestRequestTypeDef",
    {
        "ReplaceRootVolumeTaskIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeReplaceRootVolumeTasksResultTypeDef = TypedDict(
    "DescribeReplaceRootVolumeTasksResultTypeDef",
    {
        "ReplaceRootVolumeTasks": List["ReplaceRootVolumeTaskTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesListingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesListingsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "ReservedInstancesId": str,
        "ReservedInstancesListingId": str,
    },
    total=False,
)

DescribeReservedInstancesListingsResultTypeDef = TypedDict(
    "DescribeReservedInstancesListingsResultTypeDef",
    {
        "ReservedInstancesListings": List["ReservedInstancesListingTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesModificationsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "ReservedInstancesModificationIds": List[str],
        "NextToken": str,
    },
    total=False,
)

DescribeReservedInstancesModificationsResultTypeDef = TypedDict(
    "DescribeReservedInstancesModificationsResultTypeDef",
    {
        "NextToken": str,
        "ReservedInstancesModifications": List["ReservedInstancesModificationTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesOfferingsRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Filters": List["FilterTypeDef"],
        "IncludeMarketplace": bool,
        "InstanceType": InstanceTypeType,
        "MaxDuration": int,
        "MaxInstanceCount": int,
        "MinDuration": int,
        "OfferingClass": OfferingClassTypeType,
        "ProductDescription": RIProductDescriptionType,
        "ReservedInstancesOfferingIds": List[str],
        "DryRun": bool,
        "InstanceTenancy": TenancyType,
        "MaxResults": int,
        "NextToken": str,
        "OfferingType": OfferingTypeValuesType,
    },
    total=False,
)

DescribeReservedInstancesOfferingsResultTypeDef = TypedDict(
    "DescribeReservedInstancesOfferingsResultTypeDef",
    {
        "ReservedInstancesOfferings": List["ReservedInstancesOfferingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeReservedInstancesRequestRequestTypeDef = TypedDict(
    "DescribeReservedInstancesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "OfferingClass": OfferingClassTypeType,
        "ReservedInstancesIds": List[str],
        "DryRun": bool,
        "OfferingType": OfferingTypeValuesType,
    },
    total=False,
)

DescribeReservedInstancesResultTypeDef = TypedDict(
    "DescribeReservedInstancesResultTypeDef",
    {
        "ReservedInstances": List["ReservedInstancesTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeRouteTablesRequestRequestTypeDef = TypedDict(
    "DescribeRouteTablesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "RouteTableIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeRouteTablesResultTypeDef = TypedDict(
    "DescribeRouteTablesResultTypeDef",
    {
        "RouteTables": List["RouteTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeScheduledInstanceAvailabilityRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeScheduledInstanceAvailabilityRequestRequestTypeDef",
    {
        "FirstSlotStartTimeRange": "SlotDateTimeRangeRequestTypeDef",
        "Recurrence": "ScheduledInstanceRecurrenceRequestTypeDef",
    },
)
_OptionalDescribeScheduledInstanceAvailabilityRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeScheduledInstanceAvailabilityRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "MaxSlotDurationInHours": int,
        "MinSlotDurationInHours": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeScheduledInstanceAvailabilityRequestRequestTypeDef(
    _RequiredDescribeScheduledInstanceAvailabilityRequestRequestTypeDef,
    _OptionalDescribeScheduledInstanceAvailabilityRequestRequestTypeDef,
):
    pass

DescribeScheduledInstanceAvailabilityResultTypeDef = TypedDict(
    "DescribeScheduledInstanceAvailabilityResultTypeDef",
    {
        "NextToken": str,
        "ScheduledInstanceAvailabilitySet": List["ScheduledInstanceAvailabilityTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeScheduledInstancesRequestRequestTypeDef = TypedDict(
    "DescribeScheduledInstancesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "ScheduledInstanceIds": List[str],
        "SlotStartTimeRange": "SlotStartTimeRangeRequestTypeDef",
    },
    total=False,
)

DescribeScheduledInstancesResultTypeDef = TypedDict(
    "DescribeScheduledInstancesResultTypeDef",
    {
        "NextToken": str,
        "ScheduledInstanceSet": List["ScheduledInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSecurityGroupReferencesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSecurityGroupReferencesRequestRequestTypeDef",
    {
        "GroupId": List[str],
    },
)
_OptionalDescribeSecurityGroupReferencesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSecurityGroupReferencesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeSecurityGroupReferencesRequestRequestTypeDef(
    _RequiredDescribeSecurityGroupReferencesRequestRequestTypeDef,
    _OptionalDescribeSecurityGroupReferencesRequestRequestTypeDef,
):
    pass

DescribeSecurityGroupReferencesResultTypeDef = TypedDict(
    "DescribeSecurityGroupReferencesResultTypeDef",
    {
        "SecurityGroupReferenceSet": List["SecurityGroupReferenceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityGroupRulesRequestRequestTypeDef = TypedDict(
    "DescribeSecurityGroupRulesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "SecurityGroupRuleIds": List[str],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSecurityGroupRulesResultTypeDef = TypedDict(
    "DescribeSecurityGroupRulesResultTypeDef",
    {
        "SecurityGroupRules": List["SecurityGroupRuleTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSecurityGroupsRequestRequestTypeDef = TypedDict(
    "DescribeSecurityGroupsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "GroupIds": List[str],
        "GroupNames": List[str],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSecurityGroupsResultTypeDef = TypedDict(
    "DescribeSecurityGroupsResultTypeDef",
    {
        "SecurityGroups": List["SecurityGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSnapshotAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSnapshotAttributeRequestRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "SnapshotId": str,
    },
)
_OptionalDescribeSnapshotAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSnapshotAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeSnapshotAttributeRequestRequestTypeDef(
    _RequiredDescribeSnapshotAttributeRequestRequestTypeDef,
    _OptionalDescribeSnapshotAttributeRequestRequestTypeDef,
):
    pass

_RequiredDescribeSnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "_RequiredDescribeSnapshotAttributeRequestSnapshotTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
    },
)
_OptionalDescribeSnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "_OptionalDescribeSnapshotAttributeRequestSnapshotTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeSnapshotAttributeRequestSnapshotTypeDef(
    _RequiredDescribeSnapshotAttributeRequestSnapshotTypeDef,
    _OptionalDescribeSnapshotAttributeRequestSnapshotTypeDef,
):
    pass

DescribeSnapshotAttributeResultTypeDef = TypedDict(
    "DescribeSnapshotAttributeResultTypeDef",
    {
        "CreateVolumePermissions": List["CreateVolumePermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotTierStatusRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotTierStatusRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSnapshotTierStatusResultTypeDef = TypedDict(
    "DescribeSnapshotTierStatusResultTypeDef",
    {
        "SnapshotTierStatuses": List["SnapshotTierStatusTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotsRequestRequestTypeDef = TypedDict(
    "DescribeSnapshotsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "OwnerIds": List[str],
        "RestorableByUserIds": List[str],
        "SnapshotIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeSnapshotsResultTypeDef = TypedDict(
    "DescribeSnapshotsResultTypeDef",
    {
        "Snapshots": List["SnapshotTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotDatafeedSubscriptionRequestRequestTypeDef = TypedDict(
    "DescribeSpotDatafeedSubscriptionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DescribeSpotDatafeedSubscriptionResultTypeDef = TypedDict(
    "DescribeSpotDatafeedSubscriptionResultTypeDef",
    {
        "SpotDatafeedSubscription": "SpotDatafeedSubscriptionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSpotFleetInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSpotFleetInstancesRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
    },
)
_OptionalDescribeSpotFleetInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSpotFleetInstancesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeSpotFleetInstancesRequestRequestTypeDef(
    _RequiredDescribeSpotFleetInstancesRequestRequestTypeDef,
    _OptionalDescribeSpotFleetInstancesRequestRequestTypeDef,
):
    pass

DescribeSpotFleetInstancesResponseTypeDef = TypedDict(
    "DescribeSpotFleetInstancesResponseTypeDef",
    {
        "ActiveInstances": List["ActiveInstanceTypeDef"],
        "NextToken": str,
        "SpotFleetRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeSpotFleetRequestHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeSpotFleetRequestHistoryRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
        "StartTime": Union[datetime, str],
    },
)
_OptionalDescribeSpotFleetRequestHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeSpotFleetRequestHistoryRequestRequestTypeDef",
    {
        "DryRun": bool,
        "EventType": EventTypeType,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeSpotFleetRequestHistoryRequestRequestTypeDef(
    _RequiredDescribeSpotFleetRequestHistoryRequestRequestTypeDef,
    _OptionalDescribeSpotFleetRequestHistoryRequestRequestTypeDef,
):
    pass

DescribeSpotFleetRequestHistoryResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestHistoryResponseTypeDef",
    {
        "HistoryRecords": List["HistoryRecordTypeDef"],
        "LastEvaluatedTime": datetime,
        "NextToken": str,
        "SpotFleetRequestId": str,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotFleetRequestsRequestRequestTypeDef = TypedDict(
    "DescribeSpotFleetRequestsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
        "SpotFleetRequestIds": List[str],
    },
    total=False,
)

DescribeSpotFleetRequestsResponseTypeDef = TypedDict(
    "DescribeSpotFleetRequestsResponseTypeDef",
    {
        "NextToken": str,
        "SpotFleetRequestConfigs": List["SpotFleetRequestConfigTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotInstanceRequestsRequestRequestTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "SpotInstanceRequestIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSpotInstanceRequestsResultTypeDef = TypedDict(
    "DescribeSpotInstanceRequestsResultTypeDef",
    {
        "SpotInstanceRequests": List["SpotInstanceRequestTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSpotPriceHistoryRequestRequestTypeDef = TypedDict(
    "DescribeSpotPriceHistoryRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "AvailabilityZone": str,
        "DryRun": bool,
        "EndTime": Union[datetime, str],
        "InstanceTypes": List[InstanceTypeType],
        "MaxResults": int,
        "NextToken": str,
        "ProductDescriptions": List[str],
        "StartTime": Union[datetime, str],
    },
    total=False,
)

DescribeSpotPriceHistoryResultTypeDef = TypedDict(
    "DescribeSpotPriceHistoryResultTypeDef",
    {
        "NextToken": str,
        "SpotPriceHistory": List["SpotPriceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeStaleSecurityGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeStaleSecurityGroupsRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDescribeStaleSecurityGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeStaleSecurityGroupsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeStaleSecurityGroupsRequestRequestTypeDef(
    _RequiredDescribeStaleSecurityGroupsRequestRequestTypeDef,
    _OptionalDescribeStaleSecurityGroupsRequestRequestTypeDef,
):
    pass

DescribeStaleSecurityGroupsResultTypeDef = TypedDict(
    "DescribeStaleSecurityGroupsResultTypeDef",
    {
        "NextToken": str,
        "StaleSecurityGroupSet": List["StaleSecurityGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStoreImageTasksRequestRequestTypeDef = TypedDict(
    "DescribeStoreImageTasksRequestRequestTypeDef",
    {
        "ImageIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeStoreImageTasksResultTypeDef = TypedDict(
    "DescribeStoreImageTasksResultTypeDef",
    {
        "StoreImageTaskResults": List["StoreImageTaskResultTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSubnetsRequestRequestTypeDef = TypedDict(
    "DescribeSubnetsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "SubnetIds": List[str],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeSubnetsResultTypeDef = TypedDict(
    "DescribeSubnetsResultTypeDef",
    {
        "Subnets": List["SubnetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTagsRequestRequestTypeDef = TypedDict(
    "DescribeTagsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeTagsResultTypeDef = TypedDict(
    "DescribeTagsResultTypeDef",
    {
        "NextToken": str,
        "Tags": List["TagDescriptionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficMirrorFiltersRequestRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersRequestRequestTypeDef",
    {
        "TrafficMirrorFilterIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeTrafficMirrorFiltersResultTypeDef = TypedDict(
    "DescribeTrafficMirrorFiltersResultTypeDef",
    {
        "TrafficMirrorFilters": List["TrafficMirrorFilterTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficMirrorSessionsRequestRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsRequestRequestTypeDef",
    {
        "TrafficMirrorSessionIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeTrafficMirrorSessionsResultTypeDef = TypedDict(
    "DescribeTrafficMirrorSessionsResultTypeDef",
    {
        "TrafficMirrorSessions": List["TrafficMirrorSessionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrafficMirrorTargetsRequestRequestTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsRequestRequestTypeDef",
    {
        "TrafficMirrorTargetIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeTrafficMirrorTargetsResultTypeDef = TypedDict(
    "DescribeTrafficMirrorTargetsResultTypeDef",
    {
        "TrafficMirrorTargets": List["TrafficMirrorTargetTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayAttachmentsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayAttachmentsResultTypeDef",
    {
        "TransitGatewayAttachments": List["TransitGatewayAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayConnectPeersRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayConnectPeersRequestRequestTypeDef",
    {
        "TransitGatewayConnectPeerIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayConnectPeersResultTypeDef = TypedDict(
    "DescribeTransitGatewayConnectPeersResultTypeDef",
    {
        "TransitGatewayConnectPeers": List["TransitGatewayConnectPeerTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayConnectsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayConnectsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayConnectsResultTypeDef = TypedDict(
    "DescribeTransitGatewayConnectsResultTypeDef",
    {
        "TransitGatewayConnects": List["TransitGatewayConnectTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayMulticastDomainsResultTypeDef = TypedDict(
    "DescribeTransitGatewayMulticastDomainsResultTypeDef",
    {
        "TransitGatewayMulticastDomains": List["TransitGatewayMulticastDomainTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayPeeringAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayPeeringAttachmentsResultTypeDef",
    {
        "TransitGatewayPeeringAttachments": List["TransitGatewayPeeringAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayPolicyTablesRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayPolicyTablesRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayPolicyTablesResultTypeDef = TypedDict(
    "DescribeTransitGatewayPolicyTablesResultTypeDef",
    {
        "TransitGatewayPolicyTables": List["TransitGatewayPolicyTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayRouteTableAnnouncementsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTableAnnouncementsRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableAnnouncementIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef",
    {
        "TransitGatewayRouteTableAnnouncements": List[
            "TransitGatewayRouteTableAnnouncementTypeDef"
        ],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayRouteTablesRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTablesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayRouteTablesResultTypeDef = TypedDict(
    "DescribeTransitGatewayRouteTablesResultTypeDef",
    {
        "TransitGatewayRouteTables": List["TransitGatewayRouteTableTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewayVpcAttachmentsResultTypeDef = TypedDict(
    "DescribeTransitGatewayVpcAttachmentsResultTypeDef",
    {
        "TransitGatewayVpcAttachments": List["TransitGatewayVpcAttachmentTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTransitGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeTransitGatewaysRequestRequestTypeDef",
    {
        "TransitGatewayIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeTransitGatewaysResultTypeDef = TypedDict(
    "DescribeTransitGatewaysResultTypeDef",
    {
        "TransitGateways": List["TransitGatewayTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTrunkInterfaceAssociationsRequestRequestTypeDef = TypedDict(
    "DescribeTrunkInterfaceAssociationsRequestRequestTypeDef",
    {
        "AssociationIds": List[str],
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeTrunkInterfaceAssociationsResultTypeDef = TypedDict(
    "DescribeTrunkInterfaceAssociationsResultTypeDef",
    {
        "InterfaceAssociations": List["TrunkInterfaceAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVerifiedAccessEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessEndpointsRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointIds": List[str],
        "VerifiedAccessInstanceId": str,
        "VerifiedAccessGroupId": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeVerifiedAccessEndpointsResultTypeDef = TypedDict(
    "DescribeVerifiedAccessEndpointsResultTypeDef",
    {
        "VerifiedAccessEndpoints": List["VerifiedAccessEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVerifiedAccessGroupsRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessGroupsRequestRequestTypeDef",
    {
        "VerifiedAccessGroupIds": List[str],
        "VerifiedAccessInstanceId": str,
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeVerifiedAccessGroupsResultTypeDef = TypedDict(
    "DescribeVerifiedAccessGroupsResultTypeDef",
    {
        "VerifiedAccessGroups": List["VerifiedAccessGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVerifiedAccessInstanceLoggingConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessInstanceLoggingConfigurationsRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef = TypedDict(
    "DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef",
    {
        "LoggingConfigurations": List["VerifiedAccessInstanceLoggingConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVerifiedAccessInstancesRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessInstancesRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeVerifiedAccessInstancesResultTypeDef = TypedDict(
    "DescribeVerifiedAccessInstancesResultTypeDef",
    {
        "VerifiedAccessInstances": List["VerifiedAccessInstanceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVerifiedAccessTrustProvidersRequestRequestTypeDef = TypedDict(
    "DescribeVerifiedAccessTrustProvidersRequestRequestTypeDef",
    {
        "VerifiedAccessTrustProviderIds": List[str],
        "MaxResults": int,
        "NextToken": str,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

DescribeVerifiedAccessTrustProvidersResultTypeDef = TypedDict(
    "DescribeVerifiedAccessTrustProvidersResultTypeDef",
    {
        "VerifiedAccessTrustProviders": List["VerifiedAccessTrustProviderTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVolumeAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeVolumeAttributeRequestRequestTypeDef",
    {
        "Attribute": VolumeAttributeNameType,
        "VolumeId": str,
    },
)
_OptionalDescribeVolumeAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeVolumeAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeVolumeAttributeRequestRequestTypeDef(
    _RequiredDescribeVolumeAttributeRequestRequestTypeDef,
    _OptionalDescribeVolumeAttributeRequestRequestTypeDef,
):
    pass

_RequiredDescribeVolumeAttributeRequestVolumeTypeDef = TypedDict(
    "_RequiredDescribeVolumeAttributeRequestVolumeTypeDef",
    {
        "Attribute": VolumeAttributeNameType,
    },
)
_OptionalDescribeVolumeAttributeRequestVolumeTypeDef = TypedDict(
    "_OptionalDescribeVolumeAttributeRequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeVolumeAttributeRequestVolumeTypeDef(
    _RequiredDescribeVolumeAttributeRequestVolumeTypeDef,
    _OptionalDescribeVolumeAttributeRequestVolumeTypeDef,
):
    pass

DescribeVolumeAttributeResultTypeDef = TypedDict(
    "DescribeVolumeAttributeResultTypeDef",
    {
        "AutoEnableIO": "AttributeBooleanValueTypeDef",
        "ProductCodes": List["ProductCodeTypeDef"],
        "VolumeId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumeStatusRequestRequestTypeDef = TypedDict(
    "DescribeVolumeStatusRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "VolumeIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeVolumeStatusRequestVolumeTypeDef = TypedDict(
    "DescribeVolumeStatusRequestVolumeTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

DescribeVolumeStatusResultTypeDef = TypedDict(
    "DescribeVolumeStatusResultTypeDef",
    {
        "NextToken": str,
        "VolumeStatuses": List["VolumeStatusItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesModificationsRequestRequestTypeDef = TypedDict(
    "DescribeVolumesModificationsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "VolumeIds": List[str],
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeVolumesModificationsResultTypeDef = TypedDict(
    "DescribeVolumesModificationsResultTypeDef",
    {
        "VolumesModifications": List["VolumeModificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVolumesRequestRequestTypeDef = TypedDict(
    "DescribeVolumesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "VolumeIds": List[str],
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVolumesResultTypeDef = TypedDict(
    "DescribeVolumesResultTypeDef",
    {
        "Volumes": List["VolumeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVpcAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeVpcAttributeRequestRequestTypeDef",
    {
        "Attribute": VpcAttributeNameType,
        "VpcId": str,
    },
)
_OptionalDescribeVpcAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeVpcAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeVpcAttributeRequestRequestTypeDef(
    _RequiredDescribeVpcAttributeRequestRequestTypeDef,
    _OptionalDescribeVpcAttributeRequestRequestTypeDef,
):
    pass

_RequiredDescribeVpcAttributeRequestVpcTypeDef = TypedDict(
    "_RequiredDescribeVpcAttributeRequestVpcTypeDef",
    {
        "Attribute": VpcAttributeNameType,
    },
)
_OptionalDescribeVpcAttributeRequestVpcTypeDef = TypedDict(
    "_OptionalDescribeVpcAttributeRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DescribeVpcAttributeRequestVpcTypeDef(
    _RequiredDescribeVpcAttributeRequestVpcTypeDef, _OptionalDescribeVpcAttributeRequestVpcTypeDef
):
    pass

DescribeVpcAttributeResultTypeDef = TypedDict(
    "DescribeVpcAttributeResultTypeDef",
    {
        "VpcId": str,
        "EnableDnsHostnames": "AttributeBooleanValueTypeDef",
        "EnableDnsSupport": "AttributeBooleanValueTypeDef",
        "EnableNetworkAddressUsageMetrics": "AttributeBooleanValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "VpcIds": List[str],
    },
    total=False,
)

DescribeVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "DescribeVpcClassicLinkDnsSupportResultTypeDef",
    {
        "NextToken": str,
        "Vpcs": List["ClassicLinkDnsSupportTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "DescribeVpcClassicLinkRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "VpcIds": List[str],
    },
    total=False,
)

DescribeVpcClassicLinkResultTypeDef = TypedDict(
    "DescribeVpcClassicLinkResultTypeDef",
    {
        "Vpcs": List["VpcClassicLinkTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ConnectionNotificationId": str,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointConnectionNotificationsResultTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionNotificationsResultTypeDef",
    {
        "ConnectionNotificationSet": List["ConnectionNotificationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointConnectionsResultTypeDef = TypedDict(
    "DescribeVpcEndpointConnectionsResultTypeDef",
    {
        "VpcEndpointConnections": List["VpcEndpointConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ServiceIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointServiceConfigurationsResultTypeDef = TypedDict(
    "DescribeVpcEndpointServiceConfigurationsResultTypeDef",
    {
        "ServiceConfigurations": List["ServiceConfigurationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVpcEndpointServicePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredDescribeVpcEndpointServicePermissionsRequestRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalDescribeVpcEndpointServicePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalDescribeVpcEndpointServicePermissionsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class DescribeVpcEndpointServicePermissionsRequestRequestTypeDef(
    _RequiredDescribeVpcEndpointServicePermissionsRequestRequestTypeDef,
    _OptionalDescribeVpcEndpointServicePermissionsRequestRequestTypeDef,
):
    pass

DescribeVpcEndpointServicePermissionsResultTypeDef = TypedDict(
    "DescribeVpcEndpointServicePermissionsResultTypeDef",
    {
        "AllowedPrincipals": List["AllowedPrincipalTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointServicesRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointServicesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ServiceNames": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointServicesResultTypeDef = TypedDict(
    "DescribeVpcEndpointServicesResultTypeDef",
    {
        "ServiceNames": List[str],
        "ServiceDetails": List["ServiceDetailTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcEndpointsRequestRequestTypeDef = TypedDict(
    "DescribeVpcEndpointsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "VpcEndpointIds": List[str],
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

DescribeVpcEndpointsResultTypeDef = TypedDict(
    "DescribeVpcEndpointsResultTypeDef",
    {
        "VpcEndpoints": List["VpcEndpointTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcPeeringConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "VpcPeeringConnectionIds": List[str],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeVpcPeeringConnectionsResultTypeDef = TypedDict(
    "DescribeVpcPeeringConnectionsResultTypeDef",
    {
        "VpcPeeringConnections": List["VpcPeeringConnectionTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpcsRequestRequestTypeDef = TypedDict(
    "DescribeVpcsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "VpcIds": List[str],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

DescribeVpcsResultTypeDef = TypedDict(
    "DescribeVpcsResultTypeDef",
    {
        "Vpcs": List["VpcTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpnConnectionsRequestRequestTypeDef = TypedDict(
    "DescribeVpnConnectionsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "VpnConnectionIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeVpnConnectionsResultTypeDef = TypedDict(
    "DescribeVpnConnectionsResultTypeDef",
    {
        "VpnConnections": List["VpnConnectionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeVpnGatewaysRequestRequestTypeDef = TypedDict(
    "DescribeVpnGatewaysRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "VpnGatewayIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

DescribeVpnGatewaysResultTypeDef = TypedDict(
    "DescribeVpnGatewaysResultTypeDef",
    {
        "VpnGateways": List["VpnGatewayTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DestinationOptionsRequestTypeDef = TypedDict(
    "DestinationOptionsRequestTypeDef",
    {
        "FileFormat": DestinationFileFormatType,
        "HiveCompatiblePartitions": bool,
        "PerHourPartition": bool,
    },
    total=False,
)

DestinationOptionsResponseTypeDef = TypedDict(
    "DestinationOptionsResponseTypeDef",
    {
        "FileFormat": DestinationFileFormatType,
        "HiveCompatiblePartitions": bool,
        "PerHourPartition": bool,
    },
    total=False,
)

_RequiredDetachClassicLinkVpcRequestInstanceTypeDef = TypedDict(
    "_RequiredDetachClassicLinkVpcRequestInstanceTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDetachClassicLinkVpcRequestInstanceTypeDef = TypedDict(
    "_OptionalDetachClassicLinkVpcRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DetachClassicLinkVpcRequestInstanceTypeDef(
    _RequiredDetachClassicLinkVpcRequestInstanceTypeDef,
    _OptionalDetachClassicLinkVpcRequestInstanceTypeDef,
):
    pass

_RequiredDetachClassicLinkVpcRequestRequestTypeDef = TypedDict(
    "_RequiredDetachClassicLinkVpcRequestRequestTypeDef",
    {
        "InstanceId": str,
        "VpcId": str,
    },
)
_OptionalDetachClassicLinkVpcRequestRequestTypeDef = TypedDict(
    "_OptionalDetachClassicLinkVpcRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DetachClassicLinkVpcRequestRequestTypeDef(
    _RequiredDetachClassicLinkVpcRequestRequestTypeDef,
    _OptionalDetachClassicLinkVpcRequestRequestTypeDef,
):
    pass

_RequiredDetachClassicLinkVpcRequestVpcTypeDef = TypedDict(
    "_RequiredDetachClassicLinkVpcRequestVpcTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalDetachClassicLinkVpcRequestVpcTypeDef = TypedDict(
    "_OptionalDetachClassicLinkVpcRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DetachClassicLinkVpcRequestVpcTypeDef(
    _RequiredDetachClassicLinkVpcRequestVpcTypeDef, _OptionalDetachClassicLinkVpcRequestVpcTypeDef
):
    pass

DetachClassicLinkVpcResultTypeDef = TypedDict(
    "DetachClassicLinkVpcResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetachInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "_RequiredDetachInternetGatewayRequestInternetGatewayTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDetachInternetGatewayRequestInternetGatewayTypeDef = TypedDict(
    "_OptionalDetachInternetGatewayRequestInternetGatewayTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DetachInternetGatewayRequestInternetGatewayTypeDef(
    _RequiredDetachInternetGatewayRequestInternetGatewayTypeDef,
    _OptionalDetachInternetGatewayRequestInternetGatewayTypeDef,
):
    pass

_RequiredDetachInternetGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredDetachInternetGatewayRequestRequestTypeDef",
    {
        "InternetGatewayId": str,
        "VpcId": str,
    },
)
_OptionalDetachInternetGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalDetachInternetGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DetachInternetGatewayRequestRequestTypeDef(
    _RequiredDetachInternetGatewayRequestRequestTypeDef,
    _OptionalDetachInternetGatewayRequestRequestTypeDef,
):
    pass

_RequiredDetachInternetGatewayRequestVpcTypeDef = TypedDict(
    "_RequiredDetachInternetGatewayRequestVpcTypeDef",
    {
        "InternetGatewayId": str,
    },
)
_OptionalDetachInternetGatewayRequestVpcTypeDef = TypedDict(
    "_OptionalDetachInternetGatewayRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DetachInternetGatewayRequestVpcTypeDef(
    _RequiredDetachInternetGatewayRequestVpcTypeDef, _OptionalDetachInternetGatewayRequestVpcTypeDef
):
    pass

_RequiredDetachNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "_RequiredDetachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "AttachmentId": str,
    },
)
_OptionalDetachNetworkInterfaceRequestNetworkInterfaceTypeDef = TypedDict(
    "_OptionalDetachNetworkInterfaceRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
        "Force": bool,
    },
    total=False,
)

class DetachNetworkInterfaceRequestNetworkInterfaceTypeDef(
    _RequiredDetachNetworkInterfaceRequestNetworkInterfaceTypeDef,
    _OptionalDetachNetworkInterfaceRequestNetworkInterfaceTypeDef,
):
    pass

_RequiredDetachNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "_RequiredDetachNetworkInterfaceRequestRequestTypeDef",
    {
        "AttachmentId": str,
    },
)
_OptionalDetachNetworkInterfaceRequestRequestTypeDef = TypedDict(
    "_OptionalDetachNetworkInterfaceRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Force": bool,
    },
    total=False,
)

class DetachNetworkInterfaceRequestRequestTypeDef(
    _RequiredDetachNetworkInterfaceRequestRequestTypeDef,
    _OptionalDetachNetworkInterfaceRequestRequestTypeDef,
):
    pass

_RequiredDetachVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_RequiredDetachVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "VerifiedAccessTrustProviderId": str,
    },
)
_OptionalDetachVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_OptionalDetachVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class DetachVerifiedAccessTrustProviderRequestRequestTypeDef(
    _RequiredDetachVerifiedAccessTrustProviderRequestRequestTypeDef,
    _OptionalDetachVerifiedAccessTrustProviderRequestRequestTypeDef,
):
    pass

DetachVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "DetachVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": "VerifiedAccessTrustProviderTypeDef",
        "VerifiedAccessInstance": "VerifiedAccessInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetachVolumeRequestInstanceTypeDef = TypedDict(
    "_RequiredDetachVolumeRequestInstanceTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalDetachVolumeRequestInstanceTypeDef = TypedDict(
    "_OptionalDetachVolumeRequestInstanceTypeDef",
    {
        "Device": str,
        "Force": bool,
        "DryRun": bool,
    },
    total=False,
)

class DetachVolumeRequestInstanceTypeDef(
    _RequiredDetachVolumeRequestInstanceTypeDef, _OptionalDetachVolumeRequestInstanceTypeDef
):
    pass

_RequiredDetachVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredDetachVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalDetachVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalDetachVolumeRequestRequestTypeDef",
    {
        "Device": str,
        "Force": bool,
        "InstanceId": str,
        "DryRun": bool,
    },
    total=False,
)

class DetachVolumeRequestRequestTypeDef(
    _RequiredDetachVolumeRequestRequestTypeDef, _OptionalDetachVolumeRequestRequestTypeDef
):
    pass

DetachVolumeRequestVolumeTypeDef = TypedDict(
    "DetachVolumeRequestVolumeTypeDef",
    {
        "Device": str,
        "Force": bool,
        "InstanceId": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredDetachVpnGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredDetachVpnGatewayRequestRequestTypeDef",
    {
        "VpcId": str,
        "VpnGatewayId": str,
    },
)
_OptionalDetachVpnGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalDetachVpnGatewayRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DetachVpnGatewayRequestRequestTypeDef(
    _RequiredDetachVpnGatewayRequestRequestTypeDef, _OptionalDetachVpnGatewayRequestRequestTypeDef
):
    pass

DeviceOptionsTypeDef = TypedDict(
    "DeviceOptionsTypeDef",
    {
        "TenantId": str,
    },
    total=False,
)

DhcpConfigurationTypeDef = TypedDict(
    "DhcpConfigurationTypeDef",
    {
        "Key": str,
        "Values": List["AttributeValueTypeDef"],
    },
    total=False,
)

DhcpOptionsTypeDef = TypedDict(
    "DhcpOptionsTypeDef",
    {
        "DhcpConfigurations": List["DhcpConfigurationTypeDef"],
        "DhcpOptionsId": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

DirectoryServiceAuthenticationRequestTypeDef = TypedDict(
    "DirectoryServiceAuthenticationRequestTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

DirectoryServiceAuthenticationTypeDef = TypedDict(
    "DirectoryServiceAuthenticationTypeDef",
    {
        "DirectoryId": str,
    },
    total=False,
)

_RequiredDisableAddressTransferRequestRequestTypeDef = TypedDict(
    "_RequiredDisableAddressTransferRequestRequestTypeDef",
    {
        "AllocationId": str,
    },
)
_OptionalDisableAddressTransferRequestRequestTypeDef = TypedDict(
    "_OptionalDisableAddressTransferRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisableAddressTransferRequestRequestTypeDef(
    _RequiredDisableAddressTransferRequestRequestTypeDef,
    _OptionalDisableAddressTransferRequestRequestTypeDef,
):
    pass

DisableAddressTransferResultTypeDef = TypedDict(
    "DisableAddressTransferResultTypeDef",
    {
        "AddressTransfer": "AddressTransferTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef = TypedDict(
    "DisableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef",
    {
        "Source": str,
        "Destination": str,
        "Metric": Literal["aggregate-latency"],
        "Statistic": Literal["p50"],
        "DryRun": bool,
    },
    total=False,
)

DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef = TypedDict(
    "DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    {
        "Output": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableEbsEncryptionByDefaultRequestRequestTypeDef = TypedDict(
    "DisableEbsEncryptionByDefaultRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DisableEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "DisableEbsEncryptionByDefaultResultTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableFastLaunchRequestRequestTypeDef = TypedDict(
    "_RequiredDisableFastLaunchRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalDisableFastLaunchRequestRequestTypeDef = TypedDict(
    "_OptionalDisableFastLaunchRequestRequestTypeDef",
    {
        "Force": bool,
        "DryRun": bool,
    },
    total=False,
)

class DisableFastLaunchRequestRequestTypeDef(
    _RequiredDisableFastLaunchRequestRequestTypeDef, _OptionalDisableFastLaunchRequestRequestTypeDef
):
    pass

DisableFastLaunchResultTypeDef = TypedDict(
    "DisableFastLaunchResultTypeDef",
    {
        "ImageId": str,
        "ResourceType": Literal["snapshot"],
        "SnapshotConfiguration": "FastLaunchSnapshotConfigurationResponseTypeDef",
        "LaunchTemplate": "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
        "MaxParallelLaunches": int,
        "OwnerId": str,
        "State": FastLaunchStateCodeType,
        "StateTransitionReason": str,
        "StateTransitionTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": str,
        "FastSnapshotRestoreStateErrors": List["DisableFastSnapshotRestoreStateErrorItemTypeDef"],
    },
    total=False,
)

DisableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorItemTypeDef",
    {
        "AvailabilityZone": str,
        "Error": "DisableFastSnapshotRestoreStateErrorTypeDef",
    },
    total=False,
)

DisableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "DisableFastSnapshotRestoreStateErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

DisableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "DisableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": str,
        "AvailabilityZone": str,
        "State": FastSnapshotRestoreStateCodeType,
        "StateTransitionReason": str,
        "OwnerId": str,
        "OwnerAlias": str,
        "EnablingTime": datetime,
        "OptimizingTime": datetime,
        "EnabledTime": datetime,
        "DisablingTime": datetime,
        "DisabledTime": datetime,
    },
    total=False,
)

_RequiredDisableFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "_RequiredDisableFastSnapshotRestoresRequestRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "SourceSnapshotIds": List[str],
    },
)
_OptionalDisableFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "_OptionalDisableFastSnapshotRestoresRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisableFastSnapshotRestoresRequestRequestTypeDef(
    _RequiredDisableFastSnapshotRestoresRequestRequestTypeDef,
    _OptionalDisableFastSnapshotRestoresRequestRequestTypeDef,
):
    pass

DisableFastSnapshotRestoresResultTypeDef = TypedDict(
    "DisableFastSnapshotRestoresResultTypeDef",
    {
        "Successful": List["DisableFastSnapshotRestoreSuccessItemTypeDef"],
        "Unsuccessful": List["DisableFastSnapshotRestoreErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableImageBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "DisableImageBlockPublicAccessRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DisableImageBlockPublicAccessResultTypeDef = TypedDict(
    "DisableImageBlockPublicAccessResultTypeDef",
    {
        "ImageBlockPublicAccessState": Literal["unblocked"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableImageDeprecationRequestRequestTypeDef = TypedDict(
    "_RequiredDisableImageDeprecationRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalDisableImageDeprecationRequestRequestTypeDef = TypedDict(
    "_OptionalDisableImageDeprecationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisableImageDeprecationRequestRequestTypeDef(
    _RequiredDisableImageDeprecationRequestRequestTypeDef,
    _OptionalDisableImageDeprecationRequestRequestTypeDef,
):
    pass

DisableImageDeprecationResultTypeDef = TypedDict(
    "DisableImageDeprecationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableImageRequestRequestTypeDef = TypedDict(
    "_RequiredDisableImageRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalDisableImageRequestRequestTypeDef = TypedDict(
    "_OptionalDisableImageRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisableImageRequestRequestTypeDef(
    _RequiredDisableImageRequestRequestTypeDef, _OptionalDisableImageRequestRequestTypeDef
):
    pass

DisableImageResultTypeDef = TypedDict(
    "DisableImageResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableIpamOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "_RequiredDisableIpamOrganizationAdminAccountRequestRequestTypeDef",
    {
        "DelegatedAdminAccountId": str,
    },
)
_OptionalDisableIpamOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "_OptionalDisableIpamOrganizationAdminAccountRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisableIpamOrganizationAdminAccountRequestRequestTypeDef(
    _RequiredDisableIpamOrganizationAdminAccountRequestRequestTypeDef,
    _OptionalDisableIpamOrganizationAdminAccountRequestRequestTypeDef,
):
    pass

DisableIpamOrganizationAdminAccountResultTypeDef = TypedDict(
    "DisableIpamOrganizationAdminAccountResultTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableSerialConsoleAccessRequestRequestTypeDef = TypedDict(
    "DisableSerialConsoleAccessRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DisableSerialConsoleAccessResultTypeDef = TypedDict(
    "DisableSerialConsoleAccessResultTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisableSnapshotBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "DisableSnapshotBlockPublicAccessRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DisableSnapshotBlockPublicAccessResultTypeDef = TypedDict(
    "DisableSnapshotBlockPublicAccessResultTypeDef",
    {
        "State": SnapshotBlockPublicAccessStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableTransitGatewayRouteTablePropagationRequestRequestTypeDef = TypedDict(
    "_RequiredDisableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalDisableTransitGatewayRouteTablePropagationRequestRequestTypeDef = TypedDict(
    "_OptionalDisableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": bool,
        "TransitGatewayRouteTableAnnouncementId": str,
    },
    total=False,
)

class DisableTransitGatewayRouteTablePropagationRequestRequestTypeDef(
    _RequiredDisableTransitGatewayRouteTablePropagationRequestRequestTypeDef,
    _OptionalDisableTransitGatewayRouteTablePropagationRequestRequestTypeDef,
):
    pass

DisableTransitGatewayRouteTablePropagationResultTypeDef = TypedDict(
    "DisableTransitGatewayRouteTablePropagationResultTypeDef",
    {
        "Propagation": "TransitGatewayPropagationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableVgwRoutePropagationRequestRequestTypeDef = TypedDict(
    "_RequiredDisableVgwRoutePropagationRequestRequestTypeDef",
    {
        "GatewayId": str,
        "RouteTableId": str,
    },
)
_OptionalDisableVgwRoutePropagationRequestRequestTypeDef = TypedDict(
    "_OptionalDisableVgwRoutePropagationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisableVgwRoutePropagationRequestRequestTypeDef(
    _RequiredDisableVgwRoutePropagationRequestRequestTypeDef,
    _OptionalDisableVgwRoutePropagationRequestRequestTypeDef,
):
    pass

DisableVpcClassicLinkDnsSupportRequestRequestTypeDef = TypedDict(
    "DisableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    {
        "VpcId": str,
    },
    total=False,
)

DisableVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "DisableVpcClassicLinkDnsSupportResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisableVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "_RequiredDisableVpcClassicLinkRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalDisableVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "_OptionalDisableVpcClassicLinkRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisableVpcClassicLinkRequestRequestTypeDef(
    _RequiredDisableVpcClassicLinkRequestRequestTypeDef,
    _OptionalDisableVpcClassicLinkRequestRequestTypeDef,
):
    pass

DisableVpcClassicLinkRequestVpcTypeDef = TypedDict(
    "DisableVpcClassicLinkRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

DisableVpcClassicLinkResultTypeDef = TypedDict(
    "DisableVpcClassicLinkResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateAddressRequestClassicAddressTypeDef = TypedDict(
    "DisassociateAddressRequestClassicAddressTypeDef",
    {
        "AssociationId": str,
        "PublicIp": str,
        "DryRun": bool,
    },
    total=False,
)

DisassociateAddressRequestNetworkInterfaceAssociationTypeDef = TypedDict(
    "DisassociateAddressRequestNetworkInterfaceAssociationTypeDef",
    {
        "PublicIp": str,
        "DryRun": bool,
    },
    total=False,
)

DisassociateAddressRequestRequestTypeDef = TypedDict(
    "DisassociateAddressRequestRequestTypeDef",
    {
        "AssociationId": str,
        "PublicIp": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredDisassociateClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "AssociationId": str,
    },
)
_OptionalDisassociateClientVpnTargetNetworkRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateClientVpnTargetNetworkRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisassociateClientVpnTargetNetworkRequestRequestTypeDef(
    _RequiredDisassociateClientVpnTargetNetworkRequestRequestTypeDef,
    _OptionalDisassociateClientVpnTargetNetworkRequestRequestTypeDef,
):
    pass

DisassociateClientVpnTargetNetworkResultTypeDef = TypedDict(
    "DisassociateClientVpnTargetNetworkResultTypeDef",
    {
        "AssociationId": str,
        "Status": "AssociationStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateEnclaveCertificateIamRoleRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    {
        "CertificateArn": str,
        "RoleArn": str,
    },
)
_OptionalDisassociateEnclaveCertificateIamRoleRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateEnclaveCertificateIamRoleRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisassociateEnclaveCertificateIamRoleRequestRequestTypeDef(
    _RequiredDisassociateEnclaveCertificateIamRoleRequestRequestTypeDef,
    _OptionalDisassociateEnclaveCertificateIamRoleRequestRequestTypeDef,
):
    pass

DisassociateEnclaveCertificateIamRoleResultTypeDef = TypedDict(
    "DisassociateEnclaveCertificateIamRoleResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateIamInstanceProfileRequestRequestTypeDef = TypedDict(
    "DisassociateIamInstanceProfileRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)

DisassociateIamInstanceProfileResultTypeDef = TypedDict(
    "DisassociateIamInstanceProfileResultTypeDef",
    {
        "IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
        "AssociationTarget": "InstanceEventWindowDisassociationRequestTypeDef",
    },
)
_OptionalDisassociateInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateInstanceEventWindowRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisassociateInstanceEventWindowRequestRequestTypeDef(
    _RequiredDisassociateInstanceEventWindowRequestRequestTypeDef,
    _OptionalDisassociateInstanceEventWindowRequestRequestTypeDef,
):
    pass

DisassociateInstanceEventWindowResultTypeDef = TypedDict(
    "DisassociateInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": "InstanceEventWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryAssociationId": str,
    },
)
_OptionalDisassociateIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisassociateIpamResourceDiscoveryRequestRequestTypeDef(
    _RequiredDisassociateIpamResourceDiscoveryRequestRequestTypeDef,
    _OptionalDisassociateIpamResourceDiscoveryRequestRequestTypeDef,
):
    pass

DisassociateIpamResourceDiscoveryResultTypeDef = TypedDict(
    "DisassociateIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscoveryAssociation": "IpamResourceDiscoveryAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateNatGatewayAddressRequestRequestTypeDef",
    {
        "NatGatewayId": str,
        "AssociationIds": List[str],
    },
)
_OptionalDisassociateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateNatGatewayAddressRequestRequestTypeDef",
    {
        "MaxDrainDurationSeconds": int,
        "DryRun": bool,
    },
    total=False,
)

class DisassociateNatGatewayAddressRequestRequestTypeDef(
    _RequiredDisassociateNatGatewayAddressRequestRequestTypeDef,
    _OptionalDisassociateNatGatewayAddressRequestRequestTypeDef,
):
    pass

DisassociateNatGatewayAddressResultTypeDef = TypedDict(
    "DisassociateNatGatewayAddressResultTypeDef",
    {
        "NatGatewayId": str,
        "NatGatewayAddresses": List["NatGatewayAddressTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateRouteTableRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalDisassociateRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateRouteTableRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisassociateRouteTableRequestRequestTypeDef(
    _RequiredDisassociateRouteTableRequestRequestTypeDef,
    _OptionalDisassociateRouteTableRequestRequestTypeDef,
):
    pass

DisassociateRouteTableRequestRouteTableAssociationTypeDef = TypedDict(
    "DisassociateRouteTableRequestRouteTableAssociationTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredDisassociateRouteTableRequestServiceResourceTypeDef = TypedDict(
    "_RequiredDisassociateRouteTableRequestServiceResourceTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalDisassociateRouteTableRequestServiceResourceTypeDef = TypedDict(
    "_OptionalDisassociateRouteTableRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisassociateRouteTableRequestServiceResourceTypeDef(
    _RequiredDisassociateRouteTableRequestServiceResourceTypeDef,
    _OptionalDisassociateRouteTableRequestServiceResourceTypeDef,
):
    pass

DisassociateSubnetCidrBlockRequestRequestTypeDef = TypedDict(
    "DisassociateSubnetCidrBlockRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)

DisassociateSubnetCidrBlockResultTypeDef = TypedDict(
    "DisassociateSubnetCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "SubnetIpv6CidrBlockAssociationTypeDef",
        "SubnetId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": List[str],
    },
)
_OptionalDisassociateTransitGatewayMulticastDomainRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateTransitGatewayMulticastDomainRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisassociateTransitGatewayMulticastDomainRequestRequestTypeDef(
    _RequiredDisassociateTransitGatewayMulticastDomainRequestRequestTypeDef,
    _OptionalDisassociateTransitGatewayMulticastDomainRequestRequestTypeDef,
):
    pass

DisassociateTransitGatewayMulticastDomainResultTypeDef = TypedDict(
    "DisassociateTransitGatewayMulticastDomainResultTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDisassociateTransitGatewayPolicyTableRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateTransitGatewayPolicyTableRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisassociateTransitGatewayPolicyTableRequestRequestTypeDef(
    _RequiredDisassociateTransitGatewayPolicyTableRequestRequestTypeDef,
    _OptionalDisassociateTransitGatewayPolicyTableRequestRequestTypeDef,
):
    pass

DisassociateTransitGatewayPolicyTableResultTypeDef = TypedDict(
    "DisassociateTransitGatewayPolicyTableResultTypeDef",
    {
        "Association": "TransitGatewayPolicyTableAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalDisassociateTransitGatewayRouteTableRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateTransitGatewayRouteTableRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class DisassociateTransitGatewayRouteTableRequestRequestTypeDef(
    _RequiredDisassociateTransitGatewayRouteTableRequestRequestTypeDef,
    _OptionalDisassociateTransitGatewayRouteTableRequestRequestTypeDef,
):
    pass

DisassociateTransitGatewayRouteTableResultTypeDef = TypedDict(
    "DisassociateTransitGatewayRouteTableResultTypeDef",
    {
        "Association": "TransitGatewayAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateTrunkInterfaceRequestRequestTypeDef = TypedDict(
    "_RequiredDisassociateTrunkInterfaceRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalDisassociateTrunkInterfaceRequestRequestTypeDef = TypedDict(
    "_OptionalDisassociateTrunkInterfaceRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class DisassociateTrunkInterfaceRequestRequestTypeDef(
    _RequiredDisassociateTrunkInterfaceRequestRequestTypeDef,
    _OptionalDisassociateTrunkInterfaceRequestRequestTypeDef,
):
    pass

DisassociateTrunkInterfaceResultTypeDef = TypedDict(
    "DisassociateTrunkInterfaceResultTypeDef",
    {
        "Return": bool,
        "ClientToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DisassociateVpcCidrBlockRequestRequestTypeDef = TypedDict(
    "DisassociateVpcCidrBlockRequestRequestTypeDef",
    {
        "AssociationId": str,
    },
)

DisassociateVpcCidrBlockResultTypeDef = TypedDict(
    "DisassociateVpcCidrBlockResultTypeDef",
    {
        "Ipv6CidrBlockAssociation": "VpcIpv6CidrBlockAssociationTypeDef",
        "CidrBlockAssociation": "VpcCidrBlockAssociationTypeDef",
        "VpcId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskImageDescriptionTypeDef = TypedDict(
    "DiskImageDescriptionTypeDef",
    {
        "Checksum": str,
        "Format": DiskImageFormatType,
        "ImportManifestUrl": str,
        "Size": int,
    },
    total=False,
)

DiskImageDetailTypeDef = TypedDict(
    "DiskImageDetailTypeDef",
    {
        "Bytes": int,
        "Format": DiskImageFormatType,
        "ImportManifestUrl": str,
    },
)

DiskImageTypeDef = TypedDict(
    "DiskImageTypeDef",
    {
        "Description": str,
        "Image": "DiskImageDetailTypeDef",
        "Volume": "VolumeDetailTypeDef",
    },
    total=False,
)

DiskImageVolumeDescriptionTypeDef = TypedDict(
    "DiskImageVolumeDescriptionTypeDef",
    {
        "Id": str,
        "Size": int,
    },
    total=False,
)

DiskInfoTypeDef = TypedDict(
    "DiskInfoTypeDef",
    {
        "SizeInGB": int,
        "Count": int,
        "Type": DiskTypeType,
    },
    total=False,
)

DnsEntryTypeDef = TypedDict(
    "DnsEntryTypeDef",
    {
        "DnsName": str,
        "HostedZoneId": str,
    },
    total=False,
)

DnsOptionsSpecificationTypeDef = TypedDict(
    "DnsOptionsSpecificationTypeDef",
    {
        "DnsRecordIpType": DnsRecordIpTypeType,
        "PrivateDnsOnlyForInboundResolverEndpoint": bool,
    },
    total=False,
)

DnsOptionsTypeDef = TypedDict(
    "DnsOptionsTypeDef",
    {
        "DnsRecordIpType": DnsRecordIpTypeType,
        "PrivateDnsOnlyForInboundResolverEndpoint": bool,
    },
    total=False,
)

DnsServersOptionsModifyStructureTypeDef = TypedDict(
    "DnsServersOptionsModifyStructureTypeDef",
    {
        "CustomDnsServers": List[str],
        "Enabled": bool,
    },
    total=False,
)

EbsBlockDeviceTypeDef = TypedDict(
    "EbsBlockDeviceTypeDef",
    {
        "DeleteOnTermination": bool,
        "Iops": int,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": VolumeTypeType,
        "KmsKeyId": str,
        "Throughput": int,
        "OutpostArn": str,
        "Encrypted": bool,
    },
    total=False,
)

EbsInfoTypeDef = TypedDict(
    "EbsInfoTypeDef",
    {
        "EbsOptimizedSupport": EbsOptimizedSupportType,
        "EncryptionSupport": EbsEncryptionSupportType,
        "EbsOptimizedInfo": "EbsOptimizedInfoTypeDef",
        "NvmeSupport": EbsNvmeSupportType,
    },
    total=False,
)

EbsInstanceBlockDeviceSpecificationTypeDef = TypedDict(
    "EbsInstanceBlockDeviceSpecificationTypeDef",
    {
        "DeleteOnTermination": bool,
        "VolumeId": str,
    },
    total=False,
)

EbsInstanceBlockDeviceTypeDef = TypedDict(
    "EbsInstanceBlockDeviceTypeDef",
    {
        "AttachTime": datetime,
        "DeleteOnTermination": bool,
        "Status": AttachmentStatusType,
        "VolumeId": str,
    },
    total=False,
)

EbsOptimizedInfoTypeDef = TypedDict(
    "EbsOptimizedInfoTypeDef",
    {
        "BaselineBandwidthInMbps": int,
        "BaselineThroughputInMBps": float,
        "BaselineIops": int,
        "MaximumBandwidthInMbps": int,
        "MaximumThroughputInMBps": float,
        "MaximumIops": int,
    },
    total=False,
)

Ec2InstanceConnectEndpointTypeDef = TypedDict(
    "Ec2InstanceConnectEndpointTypeDef",
    {
        "OwnerId": str,
        "InstanceConnectEndpointId": str,
        "InstanceConnectEndpointArn": str,
        "State": Ec2InstanceConnectEndpointStateType,
        "StateMessage": str,
        "DnsName": str,
        "FipsDnsName": str,
        "NetworkInterfaceIds": List[str],
        "VpcId": str,
        "AvailabilityZone": str,
        "CreatedAt": datetime,
        "SubnetId": str,
        "PreserveClientIp": bool,
        "SecurityGroupIds": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

EfaInfoTypeDef = TypedDict(
    "EfaInfoTypeDef",
    {
        "MaximumEfaInterfaces": int,
    },
    total=False,
)

EgressOnlyInternetGatewayTypeDef = TypedDict(
    "EgressOnlyInternetGatewayTypeDef",
    {
        "Attachments": List["InternetGatewayAttachmentTypeDef"],
        "EgressOnlyInternetGatewayId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ElasticGpuAssociationTypeDef = TypedDict(
    "ElasticGpuAssociationTypeDef",
    {
        "ElasticGpuId": str,
        "ElasticGpuAssociationId": str,
        "ElasticGpuAssociationState": str,
        "ElasticGpuAssociationTime": str,
    },
    total=False,
)

ElasticGpuHealthTypeDef = TypedDict(
    "ElasticGpuHealthTypeDef",
    {
        "Status": ElasticGpuStatusType,
    },
    total=False,
)

ElasticGpuSpecificationResponseTypeDef = TypedDict(
    "ElasticGpuSpecificationResponseTypeDef",
    {
        "Type": str,
    },
    total=False,
)

ElasticGpuSpecificationTypeDef = TypedDict(
    "ElasticGpuSpecificationTypeDef",
    {
        "Type": str,
    },
)

ElasticGpusTypeDef = TypedDict(
    "ElasticGpusTypeDef",
    {
        "ElasticGpuId": str,
        "AvailabilityZone": str,
        "ElasticGpuType": str,
        "ElasticGpuHealth": "ElasticGpuHealthTypeDef",
        "ElasticGpuState": Literal["ATTACHED"],
        "InstanceId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ElasticInferenceAcceleratorAssociationTypeDef = TypedDict(
    "ElasticInferenceAcceleratorAssociationTypeDef",
    {
        "ElasticInferenceAcceleratorArn": str,
        "ElasticInferenceAcceleratorAssociationId": str,
        "ElasticInferenceAcceleratorAssociationState": str,
        "ElasticInferenceAcceleratorAssociationTime": datetime,
    },
    total=False,
)

_RequiredElasticInferenceAcceleratorTypeDef = TypedDict(
    "_RequiredElasticInferenceAcceleratorTypeDef",
    {
        "Type": str,
    },
)
_OptionalElasticInferenceAcceleratorTypeDef = TypedDict(
    "_OptionalElasticInferenceAcceleratorTypeDef",
    {
        "Count": int,
    },
    total=False,
)

class ElasticInferenceAcceleratorTypeDef(
    _RequiredElasticInferenceAcceleratorTypeDef, _OptionalElasticInferenceAcceleratorTypeDef
):
    pass

EnaSrdSpecificationRequestTypeDef = TypedDict(
    "EnaSrdSpecificationRequestTypeDef",
    {
        "EnaSrdEnabled": bool,
        "EnaSrdUdpSpecification": "EnaSrdUdpSpecificationRequestTypeDef",
    },
    total=False,
)

EnaSrdSpecificationTypeDef = TypedDict(
    "EnaSrdSpecificationTypeDef",
    {
        "EnaSrdEnabled": bool,
        "EnaSrdUdpSpecification": "EnaSrdUdpSpecificationTypeDef",
    },
    total=False,
)

EnaSrdUdpSpecificationRequestTypeDef = TypedDict(
    "EnaSrdUdpSpecificationRequestTypeDef",
    {
        "EnaSrdUdpEnabled": bool,
    },
    total=False,
)

EnaSrdUdpSpecificationTypeDef = TypedDict(
    "EnaSrdUdpSpecificationTypeDef",
    {
        "EnaSrdUdpEnabled": bool,
    },
    total=False,
)

_RequiredEnableAddressTransferRequestRequestTypeDef = TypedDict(
    "_RequiredEnableAddressTransferRequestRequestTypeDef",
    {
        "AllocationId": str,
        "TransferAccountId": str,
    },
)
_OptionalEnableAddressTransferRequestRequestTypeDef = TypedDict(
    "_OptionalEnableAddressTransferRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableAddressTransferRequestRequestTypeDef(
    _RequiredEnableAddressTransferRequestRequestTypeDef,
    _OptionalEnableAddressTransferRequestRequestTypeDef,
):
    pass

EnableAddressTransferResultTypeDef = TypedDict(
    "EnableAddressTransferResultTypeDef",
    {
        "AddressTransfer": "AddressTransferTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef = TypedDict(
    "EnableAwsNetworkPerformanceMetricSubscriptionRequestRequestTypeDef",
    {
        "Source": str,
        "Destination": str,
        "Metric": Literal["aggregate-latency"],
        "Statistic": Literal["p50"],
        "DryRun": bool,
    },
    total=False,
)

EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef = TypedDict(
    "EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef",
    {
        "Output": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableEbsEncryptionByDefaultRequestRequestTypeDef = TypedDict(
    "EnableEbsEncryptionByDefaultRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

EnableEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "EnableEbsEncryptionByDefaultResultTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableFastLaunchRequestRequestTypeDef = TypedDict(
    "_RequiredEnableFastLaunchRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalEnableFastLaunchRequestRequestTypeDef = TypedDict(
    "_OptionalEnableFastLaunchRequestRequestTypeDef",
    {
        "ResourceType": str,
        "SnapshotConfiguration": "FastLaunchSnapshotConfigurationRequestTypeDef",
        "LaunchTemplate": "FastLaunchLaunchTemplateSpecificationRequestTypeDef",
        "MaxParallelLaunches": int,
        "DryRun": bool,
    },
    total=False,
)

class EnableFastLaunchRequestRequestTypeDef(
    _RequiredEnableFastLaunchRequestRequestTypeDef, _OptionalEnableFastLaunchRequestRequestTypeDef
):
    pass

EnableFastLaunchResultTypeDef = TypedDict(
    "EnableFastLaunchResultTypeDef",
    {
        "ImageId": str,
        "ResourceType": Literal["snapshot"],
        "SnapshotConfiguration": "FastLaunchSnapshotConfigurationResponseTypeDef",
        "LaunchTemplate": "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
        "MaxParallelLaunches": int,
        "OwnerId": str,
        "State": FastLaunchStateCodeType,
        "StateTransitionReason": str,
        "StateTransitionTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableFastSnapshotRestoreErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreErrorItemTypeDef",
    {
        "SnapshotId": str,
        "FastSnapshotRestoreStateErrors": List["EnableFastSnapshotRestoreStateErrorItemTypeDef"],
    },
    total=False,
)

EnableFastSnapshotRestoreStateErrorItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorItemTypeDef",
    {
        "AvailabilityZone": str,
        "Error": "EnableFastSnapshotRestoreStateErrorTypeDef",
    },
    total=False,
)

EnableFastSnapshotRestoreStateErrorTypeDef = TypedDict(
    "EnableFastSnapshotRestoreStateErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

EnableFastSnapshotRestoreSuccessItemTypeDef = TypedDict(
    "EnableFastSnapshotRestoreSuccessItemTypeDef",
    {
        "SnapshotId": str,
        "AvailabilityZone": str,
        "State": FastSnapshotRestoreStateCodeType,
        "StateTransitionReason": str,
        "OwnerId": str,
        "OwnerAlias": str,
        "EnablingTime": datetime,
        "OptimizingTime": datetime,
        "EnabledTime": datetime,
        "DisablingTime": datetime,
        "DisabledTime": datetime,
    },
    total=False,
)

_RequiredEnableFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "_RequiredEnableFastSnapshotRestoresRequestRequestTypeDef",
    {
        "AvailabilityZones": List[str],
        "SourceSnapshotIds": List[str],
    },
)
_OptionalEnableFastSnapshotRestoresRequestRequestTypeDef = TypedDict(
    "_OptionalEnableFastSnapshotRestoresRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableFastSnapshotRestoresRequestRequestTypeDef(
    _RequiredEnableFastSnapshotRestoresRequestRequestTypeDef,
    _OptionalEnableFastSnapshotRestoresRequestRequestTypeDef,
):
    pass

EnableFastSnapshotRestoresResultTypeDef = TypedDict(
    "EnableFastSnapshotRestoresResultTypeDef",
    {
        "Successful": List["EnableFastSnapshotRestoreSuccessItemTypeDef"],
        "Unsuccessful": List["EnableFastSnapshotRestoreErrorItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableImageBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "_RequiredEnableImageBlockPublicAccessRequestRequestTypeDef",
    {
        "ImageBlockPublicAccessState": Literal["block-new-sharing"],
    },
)
_OptionalEnableImageBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "_OptionalEnableImageBlockPublicAccessRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableImageBlockPublicAccessRequestRequestTypeDef(
    _RequiredEnableImageBlockPublicAccessRequestRequestTypeDef,
    _OptionalEnableImageBlockPublicAccessRequestRequestTypeDef,
):
    pass

EnableImageBlockPublicAccessResultTypeDef = TypedDict(
    "EnableImageBlockPublicAccessResultTypeDef",
    {
        "ImageBlockPublicAccessState": Literal["block-new-sharing"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableImageDeprecationRequestRequestTypeDef = TypedDict(
    "_RequiredEnableImageDeprecationRequestRequestTypeDef",
    {
        "ImageId": str,
        "DeprecateAt": Union[datetime, str],
    },
)
_OptionalEnableImageDeprecationRequestRequestTypeDef = TypedDict(
    "_OptionalEnableImageDeprecationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableImageDeprecationRequestRequestTypeDef(
    _RequiredEnableImageDeprecationRequestRequestTypeDef,
    _OptionalEnableImageDeprecationRequestRequestTypeDef,
):
    pass

EnableImageDeprecationResultTypeDef = TypedDict(
    "EnableImageDeprecationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableImageRequestRequestTypeDef = TypedDict(
    "_RequiredEnableImageRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalEnableImageRequestRequestTypeDef = TypedDict(
    "_OptionalEnableImageRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableImageRequestRequestTypeDef(
    _RequiredEnableImageRequestRequestTypeDef, _OptionalEnableImageRequestRequestTypeDef
):
    pass

EnableImageResultTypeDef = TypedDict(
    "EnableImageResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableIpamOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "_RequiredEnableIpamOrganizationAdminAccountRequestRequestTypeDef",
    {
        "DelegatedAdminAccountId": str,
    },
)
_OptionalEnableIpamOrganizationAdminAccountRequestRequestTypeDef = TypedDict(
    "_OptionalEnableIpamOrganizationAdminAccountRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableIpamOrganizationAdminAccountRequestRequestTypeDef(
    _RequiredEnableIpamOrganizationAdminAccountRequestRequestTypeDef,
    _OptionalEnableIpamOrganizationAdminAccountRequestRequestTypeDef,
):
    pass

EnableIpamOrganizationAdminAccountResultTypeDef = TypedDict(
    "EnableIpamOrganizationAdminAccountResultTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableReachabilityAnalyzerOrganizationSharingRequestRequestTypeDef = TypedDict(
    "EnableReachabilityAnalyzerOrganizationSharingRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

EnableReachabilityAnalyzerOrganizationSharingResultTypeDef = TypedDict(
    "EnableReachabilityAnalyzerOrganizationSharingResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnableSerialConsoleAccessRequestRequestTypeDef = TypedDict(
    "EnableSerialConsoleAccessRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

EnableSerialConsoleAccessResultTypeDef = TypedDict(
    "EnableSerialConsoleAccessResultTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableSnapshotBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "_RequiredEnableSnapshotBlockPublicAccessRequestRequestTypeDef",
    {
        "State": SnapshotBlockPublicAccessStateType,
    },
)
_OptionalEnableSnapshotBlockPublicAccessRequestRequestTypeDef = TypedDict(
    "_OptionalEnableSnapshotBlockPublicAccessRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableSnapshotBlockPublicAccessRequestRequestTypeDef(
    _RequiredEnableSnapshotBlockPublicAccessRequestRequestTypeDef,
    _OptionalEnableSnapshotBlockPublicAccessRequestRequestTypeDef,
):
    pass

EnableSnapshotBlockPublicAccessResultTypeDef = TypedDict(
    "EnableSnapshotBlockPublicAccessResultTypeDef",
    {
        "State": SnapshotBlockPublicAccessStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableTransitGatewayRouteTablePropagationRequestRequestTypeDef = TypedDict(
    "_RequiredEnableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalEnableTransitGatewayRouteTablePropagationRequestRequestTypeDef = TypedDict(
    "_OptionalEnableTransitGatewayRouteTablePropagationRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "DryRun": bool,
        "TransitGatewayRouteTableAnnouncementId": str,
    },
    total=False,
)

class EnableTransitGatewayRouteTablePropagationRequestRequestTypeDef(
    _RequiredEnableTransitGatewayRouteTablePropagationRequestRequestTypeDef,
    _OptionalEnableTransitGatewayRouteTablePropagationRequestRequestTypeDef,
):
    pass

EnableTransitGatewayRouteTablePropagationResultTypeDef = TypedDict(
    "EnableTransitGatewayRouteTablePropagationResultTypeDef",
    {
        "Propagation": "TransitGatewayPropagationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableVgwRoutePropagationRequestRequestTypeDef = TypedDict(
    "_RequiredEnableVgwRoutePropagationRequestRequestTypeDef",
    {
        "GatewayId": str,
        "RouteTableId": str,
    },
)
_OptionalEnableVgwRoutePropagationRequestRequestTypeDef = TypedDict(
    "_OptionalEnableVgwRoutePropagationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableVgwRoutePropagationRequestRequestTypeDef(
    _RequiredEnableVgwRoutePropagationRequestRequestTypeDef,
    _OptionalEnableVgwRoutePropagationRequestRequestTypeDef,
):
    pass

_RequiredEnableVolumeIORequestRequestTypeDef = TypedDict(
    "_RequiredEnableVolumeIORequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalEnableVolumeIORequestRequestTypeDef = TypedDict(
    "_OptionalEnableVolumeIORequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableVolumeIORequestRequestTypeDef(
    _RequiredEnableVolumeIORequestRequestTypeDef, _OptionalEnableVolumeIORequestRequestTypeDef
):
    pass

EnableVolumeIORequestVolumeTypeDef = TypedDict(
    "EnableVolumeIORequestVolumeTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

EnableVpcClassicLinkDnsSupportRequestRequestTypeDef = TypedDict(
    "EnableVpcClassicLinkDnsSupportRequestRequestTypeDef",
    {
        "VpcId": str,
    },
    total=False,
)

EnableVpcClassicLinkDnsSupportResultTypeDef = TypedDict(
    "EnableVpcClassicLinkDnsSupportResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredEnableVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "_RequiredEnableVpcClassicLinkRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalEnableVpcClassicLinkRequestRequestTypeDef = TypedDict(
    "_OptionalEnableVpcClassicLinkRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class EnableVpcClassicLinkRequestRequestTypeDef(
    _RequiredEnableVpcClassicLinkRequestRequestTypeDef,
    _OptionalEnableVpcClassicLinkRequestRequestTypeDef,
):
    pass

EnableVpcClassicLinkRequestVpcTypeDef = TypedDict(
    "EnableVpcClassicLinkRequestVpcTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

EnableVpcClassicLinkResultTypeDef = TypedDict(
    "EnableVpcClassicLinkResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

EnclaveOptionsRequestTypeDef = TypedDict(
    "EnclaveOptionsRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

EnclaveOptionsTypeDef = TypedDict(
    "EnclaveOptionsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

EventInformationTypeDef = TypedDict(
    "EventInformationTypeDef",
    {
        "EventDescription": str,
        "EventSubType": str,
        "InstanceId": str,
    },
    total=False,
)

ExplanationTypeDef = TypedDict(
    "ExplanationTypeDef",
    {
        "Acl": "AnalysisComponentTypeDef",
        "AclRule": "AnalysisAclRuleTypeDef",
        "Address": str,
        "Addresses": List[str],
        "AttachedTo": "AnalysisComponentTypeDef",
        "AvailabilityZones": List[str],
        "Cidrs": List[str],
        "Component": "AnalysisComponentTypeDef",
        "CustomerGateway": "AnalysisComponentTypeDef",
        "Destination": "AnalysisComponentTypeDef",
        "DestinationVpc": "AnalysisComponentTypeDef",
        "Direction": str,
        "ExplanationCode": str,
        "IngressRouteTable": "AnalysisComponentTypeDef",
        "InternetGateway": "AnalysisComponentTypeDef",
        "LoadBalancerArn": str,
        "ClassicLoadBalancerListener": "AnalysisLoadBalancerListenerTypeDef",
        "LoadBalancerListenerPort": int,
        "LoadBalancerTarget": "AnalysisLoadBalancerTargetTypeDef",
        "LoadBalancerTargetGroup": "AnalysisComponentTypeDef",
        "LoadBalancerTargetGroups": List["AnalysisComponentTypeDef"],
        "LoadBalancerTargetPort": int,
        "ElasticLoadBalancerListener": "AnalysisComponentTypeDef",
        "MissingComponent": str,
        "NatGateway": "AnalysisComponentTypeDef",
        "NetworkInterface": "AnalysisComponentTypeDef",
        "PacketField": str,
        "VpcPeeringConnection": "AnalysisComponentTypeDef",
        "Port": int,
        "PortRanges": List["PortRangeTypeDef"],
        "PrefixList": "AnalysisComponentTypeDef",
        "Protocols": List[str],
        "RouteTableRoute": "AnalysisRouteTableRouteTypeDef",
        "RouteTable": "AnalysisComponentTypeDef",
        "SecurityGroup": "AnalysisComponentTypeDef",
        "SecurityGroupRule": "AnalysisSecurityGroupRuleTypeDef",
        "SecurityGroups": List["AnalysisComponentTypeDef"],
        "SourceVpc": "AnalysisComponentTypeDef",
        "State": str,
        "Subnet": "AnalysisComponentTypeDef",
        "SubnetRouteTable": "AnalysisComponentTypeDef",
        "Vpc": "AnalysisComponentTypeDef",
        "VpcEndpoint": "AnalysisComponentTypeDef",
        "VpnConnection": "AnalysisComponentTypeDef",
        "VpnGateway": "AnalysisComponentTypeDef",
        "TransitGateway": "AnalysisComponentTypeDef",
        "TransitGatewayRouteTable": "AnalysisComponentTypeDef",
        "TransitGatewayRouteTableRoute": "TransitGatewayRouteTableRouteTypeDef",
        "TransitGatewayAttachment": "AnalysisComponentTypeDef",
        "ComponentAccount": str,
        "ComponentRegion": str,
        "FirewallStatelessRule": "FirewallStatelessRuleTypeDef",
        "FirewallStatefulRule": "FirewallStatefulRuleTypeDef",
    },
    total=False,
)

_RequiredExportClientVpnClientCertificateRevocationListRequestRequestTypeDef = TypedDict(
    "_RequiredExportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalExportClientVpnClientCertificateRevocationListRequestRequestTypeDef = TypedDict(
    "_OptionalExportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ExportClientVpnClientCertificateRevocationListRequestRequestTypeDef(
    _RequiredExportClientVpnClientCertificateRevocationListRequestRequestTypeDef,
    _OptionalExportClientVpnClientCertificateRevocationListRequestRequestTypeDef,
):
    pass

ExportClientVpnClientCertificateRevocationListResultTypeDef = TypedDict(
    "ExportClientVpnClientCertificateRevocationListResultTypeDef",
    {
        "CertificateRevocationList": str,
        "Status": "ClientCertificateRevocationListStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportClientVpnClientConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredExportClientVpnClientConfigurationRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalExportClientVpnClientConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalExportClientVpnClientConfigurationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ExportClientVpnClientConfigurationRequestRequestTypeDef(
    _RequiredExportClientVpnClientConfigurationRequestRequestTypeDef,
    _OptionalExportClientVpnClientConfigurationRequestRequestTypeDef,
):
    pass

ExportClientVpnClientConfigurationResultTypeDef = TypedDict(
    "ExportClientVpnClientConfigurationResultTypeDef",
    {
        "ClientConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredExportImageRequestRequestTypeDef = TypedDict(
    "_RequiredExportImageRequestRequestTypeDef",
    {
        "DiskImageFormat": DiskImageFormatType,
        "ImageId": str,
        "S3ExportLocation": "ExportTaskS3LocationRequestTypeDef",
    },
)
_OptionalExportImageRequestRequestTypeDef = TypedDict(
    "_OptionalExportImageRequestRequestTypeDef",
    {
        "ClientToken": str,
        "Description": str,
        "DryRun": bool,
        "RoleName": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class ExportImageRequestRequestTypeDef(
    _RequiredExportImageRequestRequestTypeDef, _OptionalExportImageRequestRequestTypeDef
):
    pass

ExportImageResultTypeDef = TypedDict(
    "ExportImageResultTypeDef",
    {
        "Description": str,
        "DiskImageFormat": DiskImageFormatType,
        "ExportImageTaskId": str,
        "ImageId": str,
        "RoleName": str,
        "Progress": str,
        "S3ExportLocation": "ExportTaskS3LocationTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ExportImageTaskTypeDef = TypedDict(
    "ExportImageTaskTypeDef",
    {
        "Description": str,
        "ExportImageTaskId": str,
        "ImageId": str,
        "Progress": str,
        "S3ExportLocation": "ExportTaskS3LocationTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredExportTaskS3LocationRequestTypeDef = TypedDict(
    "_RequiredExportTaskS3LocationRequestTypeDef",
    {
        "S3Bucket": str,
    },
)
_OptionalExportTaskS3LocationRequestTypeDef = TypedDict(
    "_OptionalExportTaskS3LocationRequestTypeDef",
    {
        "S3Prefix": str,
    },
    total=False,
)

class ExportTaskS3LocationRequestTypeDef(
    _RequiredExportTaskS3LocationRequestTypeDef, _OptionalExportTaskS3LocationRequestTypeDef
):
    pass

ExportTaskS3LocationTypeDef = TypedDict(
    "ExportTaskS3LocationTypeDef",
    {
        "S3Bucket": str,
        "S3Prefix": str,
    },
    total=False,
)

ExportTaskTypeDef = TypedDict(
    "ExportTaskTypeDef",
    {
        "Description": str,
        "ExportTaskId": str,
        "ExportToS3Task": "ExportToS3TaskTypeDef",
        "InstanceExportDetails": "InstanceExportDetailsTypeDef",
        "State": ExportTaskStateType,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ExportToS3TaskSpecificationTypeDef = TypedDict(
    "ExportToS3TaskSpecificationTypeDef",
    {
        "ContainerFormat": Literal["ova"],
        "DiskImageFormat": DiskImageFormatType,
        "S3Bucket": str,
        "S3Prefix": str,
    },
    total=False,
)

ExportToS3TaskTypeDef = TypedDict(
    "ExportToS3TaskTypeDef",
    {
        "ContainerFormat": Literal["ova"],
        "DiskImageFormat": DiskImageFormatType,
        "S3Bucket": str,
        "S3Key": str,
    },
    total=False,
)

_RequiredExportTransitGatewayRoutesRequestRequestTypeDef = TypedDict(
    "_RequiredExportTransitGatewayRoutesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "S3Bucket": str,
    },
)
_OptionalExportTransitGatewayRoutesRequestRequestTypeDef = TypedDict(
    "_OptionalExportTransitGatewayRoutesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class ExportTransitGatewayRoutesRequestRequestTypeDef(
    _RequiredExportTransitGatewayRoutesRequestRequestTypeDef,
    _OptionalExportTransitGatewayRoutesRequestRequestTypeDef,
):
    pass

ExportTransitGatewayRoutesResultTypeDef = TypedDict(
    "ExportTransitGatewayRoutesResultTypeDef",
    {
        "S3Location": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

FailedCapacityReservationFleetCancellationResultTypeDef = TypedDict(
    "FailedCapacityReservationFleetCancellationResultTypeDef",
    {
        "CapacityReservationFleetId": str,
        "CancelCapacityReservationFleetError": "CancelCapacityReservationFleetErrorTypeDef",
    },
    total=False,
)

FailedQueuedPurchaseDeletionTypeDef = TypedDict(
    "FailedQueuedPurchaseDeletionTypeDef",
    {
        "Error": "DeleteQueuedReservedInstancesErrorTypeDef",
        "ReservedInstancesId": str,
    },
    total=False,
)

_RequiredFastLaunchLaunchTemplateSpecificationRequestTypeDef = TypedDict(
    "_RequiredFastLaunchLaunchTemplateSpecificationRequestTypeDef",
    {
        "Version": str,
    },
)
_OptionalFastLaunchLaunchTemplateSpecificationRequestTypeDef = TypedDict(
    "_OptionalFastLaunchLaunchTemplateSpecificationRequestTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
    },
    total=False,
)

class FastLaunchLaunchTemplateSpecificationRequestTypeDef(
    _RequiredFastLaunchLaunchTemplateSpecificationRequestTypeDef,
    _OptionalFastLaunchLaunchTemplateSpecificationRequestTypeDef,
):
    pass

FastLaunchLaunchTemplateSpecificationResponseTypeDef = TypedDict(
    "FastLaunchLaunchTemplateSpecificationResponseTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

FastLaunchSnapshotConfigurationRequestTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationRequestTypeDef",
    {
        "TargetResourceCount": int,
    },
    total=False,
)

FastLaunchSnapshotConfigurationResponseTypeDef = TypedDict(
    "FastLaunchSnapshotConfigurationResponseTypeDef",
    {
        "TargetResourceCount": int,
    },
    total=False,
)

FederatedAuthenticationRequestTypeDef = TypedDict(
    "FederatedAuthenticationRequestTypeDef",
    {
        "SAMLProviderArn": str,
        "SelfServiceSAMLProviderArn": str,
    },
    total=False,
)

FederatedAuthenticationTypeDef = TypedDict(
    "FederatedAuthenticationTypeDef",
    {
        "SamlProviderArn": str,
        "SelfServiceSamlProviderArn": str,
    },
    total=False,
)

FilterPortRangeTypeDef = TypedDict(
    "FilterPortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

FilterTypeDef = TypedDict(
    "FilterTypeDef",
    {
        "Name": str,
        "Values": List[str],
    },
    total=False,
)

FirewallStatefulRuleTypeDef = TypedDict(
    "FirewallStatefulRuleTypeDef",
    {
        "RuleGroupArn": str,
        "Sources": List[str],
        "Destinations": List[str],
        "SourcePorts": List["PortRangeTypeDef"],
        "DestinationPorts": List["PortRangeTypeDef"],
        "Protocol": str,
        "RuleAction": str,
        "Direction": str,
    },
    total=False,
)

FirewallStatelessRuleTypeDef = TypedDict(
    "FirewallStatelessRuleTypeDef",
    {
        "RuleGroupArn": str,
        "Sources": List[str],
        "Destinations": List[str],
        "SourcePorts": List["PortRangeTypeDef"],
        "DestinationPorts": List["PortRangeTypeDef"],
        "Protocols": List[int],
        "RuleAction": str,
        "Priority": int,
    },
    total=False,
)

FleetCapacityReservationTypeDef = TypedDict(
    "FleetCapacityReservationTypeDef",
    {
        "CapacityReservationId": str,
        "AvailabilityZoneId": str,
        "InstanceType": InstanceTypeType,
        "InstancePlatform": CapacityReservationInstancePlatformType,
        "AvailabilityZone": str,
        "TotalInstanceCount": int,
        "FulfilledCapacity": float,
        "EbsOptimized": bool,
        "CreateDate": datetime,
        "Weight": float,
        "Priority": int,
    },
    total=False,
)

FleetDataTypeDef = TypedDict(
    "FleetDataTypeDef",
    {
        "ActivityStatus": FleetActivityStatusType,
        "CreateTime": datetime,
        "FleetId": str,
        "FleetState": FleetStateCodeType,
        "ClientToken": str,
        "ExcessCapacityTerminationPolicy": FleetExcessCapacityTerminationPolicyType,
        "FulfilledCapacity": float,
        "FulfilledOnDemandCapacity": float,
        "LaunchTemplateConfigs": List["FleetLaunchTemplateConfigTypeDef"],
        "TargetCapacitySpecification": "TargetCapacitySpecificationTypeDef",
        "TerminateInstancesWithExpiration": bool,
        "Type": FleetTypeType,
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "ReplaceUnhealthyInstances": bool,
        "SpotOptions": "SpotOptionsTypeDef",
        "OnDemandOptions": "OnDemandOptionsTypeDef",
        "Tags": List["TagTypeDef"],
        "Errors": List["DescribeFleetErrorTypeDef"],
        "Instances": List["DescribeFleetsInstancesTypeDef"],
        "Context": str,
    },
    total=False,
)

FleetLaunchTemplateConfigRequestTypeDef = TypedDict(
    "FleetLaunchTemplateConfigRequestTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationRequestTypeDef",
        "Overrides": List["FleetLaunchTemplateOverridesRequestTypeDef"],
    },
    total=False,
)

FleetLaunchTemplateConfigTypeDef = TypedDict(
    "FleetLaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationTypeDef",
        "Overrides": List["FleetLaunchTemplateOverridesTypeDef"],
    },
    total=False,
)

FleetLaunchTemplateOverridesRequestTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesRequestTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "MaxPrice": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "WeightedCapacity": float,
        "Priority": float,
        "Placement": "PlacementTypeDef",
        "InstanceRequirements": "InstanceRequirementsRequestTypeDef",
        "ImageId": str,
    },
    total=False,
)

FleetLaunchTemplateOverridesTypeDef = TypedDict(
    "FleetLaunchTemplateOverridesTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "MaxPrice": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "WeightedCapacity": float,
        "Priority": float,
        "Placement": "PlacementResponseTypeDef",
        "InstanceRequirements": "InstanceRequirementsTypeDef",
        "ImageId": str,
    },
    total=False,
)

FleetLaunchTemplateSpecificationRequestTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationRequestTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

FleetLaunchTemplateSpecificationTypeDef = TypedDict(
    "FleetLaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

FleetSpotCapacityRebalanceRequestTypeDef = TypedDict(
    "FleetSpotCapacityRebalanceRequestTypeDef",
    {
        "ReplacementStrategy": FleetReplacementStrategyType,
        "TerminationDelay": int,
    },
    total=False,
)

FleetSpotCapacityRebalanceTypeDef = TypedDict(
    "FleetSpotCapacityRebalanceTypeDef",
    {
        "ReplacementStrategy": FleetReplacementStrategyType,
        "TerminationDelay": int,
    },
    total=False,
)

FleetSpotMaintenanceStrategiesRequestTypeDef = TypedDict(
    "FleetSpotMaintenanceStrategiesRequestTypeDef",
    {
        "CapacityRebalance": "FleetSpotCapacityRebalanceRequestTypeDef",
    },
    total=False,
)

FleetSpotMaintenanceStrategiesTypeDef = TypedDict(
    "FleetSpotMaintenanceStrategiesTypeDef",
    {
        "CapacityRebalance": "FleetSpotCapacityRebalanceTypeDef",
    },
    total=False,
)

FlowLogTypeDef = TypedDict(
    "FlowLogTypeDef",
    {
        "CreationTime": datetime,
        "DeliverLogsErrorMessage": str,
        "DeliverLogsPermissionArn": str,
        "DeliverCrossAccountRole": str,
        "DeliverLogsStatus": str,
        "FlowLogId": str,
        "FlowLogStatus": str,
        "LogGroupName": str,
        "ResourceId": str,
        "TrafficType": TrafficTypeType,
        "LogDestinationType": LogDestinationTypeType,
        "LogDestination": str,
        "LogFormat": str,
        "Tags": List["TagTypeDef"],
        "MaxAggregationInterval": int,
        "DestinationOptions": "DestinationOptionsResponseTypeDef",
    },
    total=False,
)

FpgaDeviceInfoTypeDef = TypedDict(
    "FpgaDeviceInfoTypeDef",
    {
        "Name": str,
        "Manufacturer": str,
        "Count": int,
        "MemoryInfo": "FpgaDeviceMemoryInfoTypeDef",
    },
    total=False,
)

FpgaDeviceMemoryInfoTypeDef = TypedDict(
    "FpgaDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": int,
    },
    total=False,
)

FpgaImageAttributeTypeDef = TypedDict(
    "FpgaImageAttributeTypeDef",
    {
        "FpgaImageId": str,
        "Name": str,
        "Description": str,
        "LoadPermissions": List["LoadPermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
    },
    total=False,
)

FpgaImageStateTypeDef = TypedDict(
    "FpgaImageStateTypeDef",
    {
        "Code": FpgaImageStateCodeType,
        "Message": str,
    },
    total=False,
)

FpgaImageTypeDef = TypedDict(
    "FpgaImageTypeDef",
    {
        "FpgaImageId": str,
        "FpgaImageGlobalId": str,
        "Name": str,
        "Description": str,
        "ShellVersion": str,
        "PciId": "PciIdTypeDef",
        "State": "FpgaImageStateTypeDef",
        "CreateTime": datetime,
        "UpdateTime": datetime,
        "OwnerId": str,
        "OwnerAlias": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "Tags": List["TagTypeDef"],
        "Public": bool,
        "DataRetentionSupport": bool,
        "InstanceTypes": List[str],
    },
    total=False,
)

FpgaInfoTypeDef = TypedDict(
    "FpgaInfoTypeDef",
    {
        "Fpgas": List["FpgaDeviceInfoTypeDef"],
        "TotalFpgaMemoryInMiB": int,
    },
    total=False,
)

_RequiredGetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef = TypedDict(
    "_RequiredGetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef",
    {
        "CertificateArn": str,
    },
)
_OptionalGetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef = TypedDict(
    "_OptionalGetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef(
    _RequiredGetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef,
    _OptionalGetAssociatedEnclaveCertificateIamRolesRequestRequestTypeDef,
):
    pass

GetAssociatedEnclaveCertificateIamRolesResultTypeDef = TypedDict(
    "GetAssociatedEnclaveCertificateIamRolesResultTypeDef",
    {
        "AssociatedRoles": List["AssociatedRoleTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetAssociatedIpv6PoolCidrsRequestRequestTypeDef = TypedDict(
    "_RequiredGetAssociatedIpv6PoolCidrsRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalGetAssociatedIpv6PoolCidrsRequestRequestTypeDef = TypedDict(
    "_OptionalGetAssociatedIpv6PoolCidrsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)

class GetAssociatedIpv6PoolCidrsRequestRequestTypeDef(
    _RequiredGetAssociatedIpv6PoolCidrsRequestRequestTypeDef,
    _OptionalGetAssociatedIpv6PoolCidrsRequestRequestTypeDef,
):
    pass

GetAssociatedIpv6PoolCidrsResultTypeDef = TypedDict(
    "GetAssociatedIpv6PoolCidrsResultTypeDef",
    {
        "Ipv6CidrAssociations": List["Ipv6CidrAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetAwsNetworkPerformanceDataRequestRequestTypeDef = TypedDict(
    "GetAwsNetworkPerformanceDataRequestRequestTypeDef",
    {
        "DataQueries": List["DataQueryTypeDef"],
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

GetAwsNetworkPerformanceDataResultTypeDef = TypedDict(
    "GetAwsNetworkPerformanceDataResultTypeDef",
    {
        "DataResponses": List["DataResponseTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCapacityReservationUsageRequestRequestTypeDef = TypedDict(
    "_RequiredGetCapacityReservationUsageRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
    },
)
_OptionalGetCapacityReservationUsageRequestRequestTypeDef = TypedDict(
    "_OptionalGetCapacityReservationUsageRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)

class GetCapacityReservationUsageRequestRequestTypeDef(
    _RequiredGetCapacityReservationUsageRequestRequestTypeDef,
    _OptionalGetCapacityReservationUsageRequestRequestTypeDef,
):
    pass

GetCapacityReservationUsageResultTypeDef = TypedDict(
    "GetCapacityReservationUsageResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservationId": str,
        "InstanceType": str,
        "TotalInstanceCount": int,
        "AvailableInstanceCount": int,
        "State": CapacityReservationStateType,
        "InstanceUsages": List["InstanceUsageTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetCoipPoolUsageRequestRequestTypeDef = TypedDict(
    "_RequiredGetCoipPoolUsageRequestRequestTypeDef",
    {
        "PoolId": str,
    },
)
_OptionalGetCoipPoolUsageRequestRequestTypeDef = TypedDict(
    "_OptionalGetCoipPoolUsageRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class GetCoipPoolUsageRequestRequestTypeDef(
    _RequiredGetCoipPoolUsageRequestRequestTypeDef, _OptionalGetCoipPoolUsageRequestRequestTypeDef
):
    pass

GetCoipPoolUsageResultTypeDef = TypedDict(
    "GetCoipPoolUsageResultTypeDef",
    {
        "CoipPoolId": str,
        "CoipAddressUsages": List["CoipAddressUsageTypeDef"],
        "LocalGatewayRouteTableId": str,
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetConsoleOutputRequestInstanceTypeDef = TypedDict(
    "GetConsoleOutputRequestInstanceTypeDef",
    {
        "DryRun": bool,
        "Latest": bool,
    },
    total=False,
)

_RequiredGetConsoleOutputRequestRequestTypeDef = TypedDict(
    "_RequiredGetConsoleOutputRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGetConsoleOutputRequestRequestTypeDef = TypedDict(
    "_OptionalGetConsoleOutputRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Latest": bool,
    },
    total=False,
)

class GetConsoleOutputRequestRequestTypeDef(
    _RequiredGetConsoleOutputRequestRequestTypeDef, _OptionalGetConsoleOutputRequestRequestTypeDef
):
    pass

GetConsoleOutputResultTypeDef = TypedDict(
    "GetConsoleOutputResultTypeDef",
    {
        "InstanceId": str,
        "Output": str,
        "Timestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetConsoleScreenshotRequestRequestTypeDef = TypedDict(
    "_RequiredGetConsoleScreenshotRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGetConsoleScreenshotRequestRequestTypeDef = TypedDict(
    "_OptionalGetConsoleScreenshotRequestRequestTypeDef",
    {
        "DryRun": bool,
        "WakeUp": bool,
    },
    total=False,
)

class GetConsoleScreenshotRequestRequestTypeDef(
    _RequiredGetConsoleScreenshotRequestRequestTypeDef,
    _OptionalGetConsoleScreenshotRequestRequestTypeDef,
):
    pass

GetConsoleScreenshotResultTypeDef = TypedDict(
    "GetConsoleScreenshotResultTypeDef",
    {
        "ImageData": str,
        "InstanceId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetDefaultCreditSpecificationRequestRequestTypeDef = TypedDict(
    "_RequiredGetDefaultCreditSpecificationRequestRequestTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
    },
)
_OptionalGetDefaultCreditSpecificationRequestRequestTypeDef = TypedDict(
    "_OptionalGetDefaultCreditSpecificationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetDefaultCreditSpecificationRequestRequestTypeDef(
    _RequiredGetDefaultCreditSpecificationRequestRequestTypeDef,
    _OptionalGetDefaultCreditSpecificationRequestRequestTypeDef,
):
    pass

GetDefaultCreditSpecificationResultTypeDef = TypedDict(
    "GetDefaultCreditSpecificationResultTypeDef",
    {
        "InstanceFamilyCreditSpecification": "InstanceFamilyCreditSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "GetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

GetEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "GetEbsDefaultKmsKeyIdResultTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetEbsEncryptionByDefaultRequestRequestTypeDef = TypedDict(
    "GetEbsEncryptionByDefaultRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

GetEbsEncryptionByDefaultResultTypeDef = TypedDict(
    "GetEbsEncryptionByDefaultResultTypeDef",
    {
        "EbsEncryptionByDefault": bool,
        "SseType": SSETypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetFlowLogsIntegrationTemplateRequestRequestTypeDef = TypedDict(
    "_RequiredGetFlowLogsIntegrationTemplateRequestRequestTypeDef",
    {
        "FlowLogId": str,
        "ConfigDeliveryS3DestinationArn": str,
        "IntegrateServices": "IntegrateServicesTypeDef",
    },
)
_OptionalGetFlowLogsIntegrationTemplateRequestRequestTypeDef = TypedDict(
    "_OptionalGetFlowLogsIntegrationTemplateRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetFlowLogsIntegrationTemplateRequestRequestTypeDef(
    _RequiredGetFlowLogsIntegrationTemplateRequestRequestTypeDef,
    _OptionalGetFlowLogsIntegrationTemplateRequestRequestTypeDef,
):
    pass

GetFlowLogsIntegrationTemplateResultTypeDef = TypedDict(
    "GetFlowLogsIntegrationTemplateResultTypeDef",
    {
        "Result": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetGroupsForCapacityReservationRequestRequestTypeDef = TypedDict(
    "_RequiredGetGroupsForCapacityReservationRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
    },
)
_OptionalGetGroupsForCapacityReservationRequestRequestTypeDef = TypedDict(
    "_OptionalGetGroupsForCapacityReservationRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)

class GetGroupsForCapacityReservationRequestRequestTypeDef(
    _RequiredGetGroupsForCapacityReservationRequestRequestTypeDef,
    _OptionalGetGroupsForCapacityReservationRequestRequestTypeDef,
):
    pass

GetGroupsForCapacityReservationResultTypeDef = TypedDict(
    "GetGroupsForCapacityReservationResultTypeDef",
    {
        "NextToken": str,
        "CapacityReservationGroups": List["CapacityReservationGroupTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetHostReservationPurchasePreviewRequestRequestTypeDef = TypedDict(
    "GetHostReservationPurchasePreviewRequestRequestTypeDef",
    {
        "HostIdSet": List[str],
        "OfferingId": str,
    },
)

GetHostReservationPurchasePreviewResultTypeDef = TypedDict(
    "GetHostReservationPurchasePreviewResultTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Purchase": List["PurchaseTypeDef"],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetImageBlockPublicAccessStateRequestRequestTypeDef = TypedDict(
    "GetImageBlockPublicAccessStateRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

GetImageBlockPublicAccessStateResultTypeDef = TypedDict(
    "GetImageBlockPublicAccessStateResultTypeDef",
    {
        "ImageBlockPublicAccessState": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef = TypedDict(
    "_RequiredGetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef",
    {
        "ArchitectureTypes": List[ArchitectureTypeType],
        "VirtualizationTypes": List[VirtualizationTypeType],
        "InstanceRequirements": "InstanceRequirementsRequestTypeDef",
    },
)
_OptionalGetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef = TypedDict(
    "_OptionalGetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef(
    _RequiredGetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef,
    _OptionalGetInstanceTypesFromInstanceRequirementsRequestRequestTypeDef,
):
    pass

GetInstanceTypesFromInstanceRequirementsResultTypeDef = TypedDict(
    "GetInstanceTypesFromInstanceRequirementsResultTypeDef",
    {
        "InstanceTypes": List["InstanceTypeInfoFromInstanceRequirementsTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetInstanceUefiDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetInstanceUefiDataRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGetInstanceUefiDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetInstanceUefiDataRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetInstanceUefiDataRequestRequestTypeDef(
    _RequiredGetInstanceUefiDataRequestRequestTypeDef,
    _OptionalGetInstanceUefiDataRequestRequestTypeDef,
):
    pass

GetInstanceUefiDataResultTypeDef = TypedDict(
    "GetInstanceUefiDataResultTypeDef",
    {
        "InstanceId": str,
        "UefiData": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIpamAddressHistoryRequestRequestTypeDef = TypedDict(
    "_RequiredGetIpamAddressHistoryRequestRequestTypeDef",
    {
        "Cidr": str,
        "IpamScopeId": str,
    },
)
_OptionalGetIpamAddressHistoryRequestRequestTypeDef = TypedDict(
    "_OptionalGetIpamAddressHistoryRequestRequestTypeDef",
    {
        "DryRun": bool,
        "VpcId": str,
        "StartTime": Union[datetime, str],
        "EndTime": Union[datetime, str],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetIpamAddressHistoryRequestRequestTypeDef(
    _RequiredGetIpamAddressHistoryRequestRequestTypeDef,
    _OptionalGetIpamAddressHistoryRequestRequestTypeDef,
):
    pass

GetIpamAddressHistoryResultTypeDef = TypedDict(
    "GetIpamAddressHistoryResultTypeDef",
    {
        "HistoryRecords": List["IpamAddressHistoryRecordTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIpamDiscoveredAccountsRequestRequestTypeDef = TypedDict(
    "_RequiredGetIpamDiscoveredAccountsRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "DiscoveryRegion": str,
    },
)
_OptionalGetIpamDiscoveredAccountsRequestRequestTypeDef = TypedDict(
    "_OptionalGetIpamDiscoveredAccountsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetIpamDiscoveredAccountsRequestRequestTypeDef(
    _RequiredGetIpamDiscoveredAccountsRequestRequestTypeDef,
    _OptionalGetIpamDiscoveredAccountsRequestRequestTypeDef,
):
    pass

GetIpamDiscoveredAccountsResultTypeDef = TypedDict(
    "GetIpamDiscoveredAccountsResultTypeDef",
    {
        "IpamDiscoveredAccounts": List["IpamDiscoveredAccountTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIpamDiscoveredResourceCidrsRequestRequestTypeDef = TypedDict(
    "_RequiredGetIpamDiscoveredResourceCidrsRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "ResourceRegion": str,
    },
)
_OptionalGetIpamDiscoveredResourceCidrsRequestRequestTypeDef = TypedDict(
    "_OptionalGetIpamDiscoveredResourceCidrsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetIpamDiscoveredResourceCidrsRequestRequestTypeDef(
    _RequiredGetIpamDiscoveredResourceCidrsRequestRequestTypeDef,
    _OptionalGetIpamDiscoveredResourceCidrsRequestRequestTypeDef,
):
    pass

GetIpamDiscoveredResourceCidrsResultTypeDef = TypedDict(
    "GetIpamDiscoveredResourceCidrsResultTypeDef",
    {
        "IpamDiscoveredResourceCidrs": List["IpamDiscoveredResourceCidrTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIpamPoolAllocationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetIpamPoolAllocationsRequestRequestTypeDef",
    {
        "IpamPoolId": str,
    },
)
_OptionalGetIpamPoolAllocationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetIpamPoolAllocationsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "IpamPoolAllocationId": str,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetIpamPoolAllocationsRequestRequestTypeDef(
    _RequiredGetIpamPoolAllocationsRequestRequestTypeDef,
    _OptionalGetIpamPoolAllocationsRequestRequestTypeDef,
):
    pass

GetIpamPoolAllocationsResultTypeDef = TypedDict(
    "GetIpamPoolAllocationsResultTypeDef",
    {
        "IpamPoolAllocations": List["IpamPoolAllocationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIpamPoolCidrsRequestRequestTypeDef = TypedDict(
    "_RequiredGetIpamPoolCidrsRequestRequestTypeDef",
    {
        "IpamPoolId": str,
    },
)
_OptionalGetIpamPoolCidrsRequestRequestTypeDef = TypedDict(
    "_OptionalGetIpamPoolCidrsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetIpamPoolCidrsRequestRequestTypeDef(
    _RequiredGetIpamPoolCidrsRequestRequestTypeDef, _OptionalGetIpamPoolCidrsRequestRequestTypeDef
):
    pass

GetIpamPoolCidrsResultTypeDef = TypedDict(
    "GetIpamPoolCidrsResultTypeDef",
    {
        "IpamPoolCidrs": List["IpamPoolCidrTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetIpamResourceCidrsRequestRequestTypeDef = TypedDict(
    "_RequiredGetIpamResourceCidrsRequestRequestTypeDef",
    {
        "IpamScopeId": str,
    },
)
_OptionalGetIpamResourceCidrsRequestRequestTypeDef = TypedDict(
    "_OptionalGetIpamResourceCidrsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "IpamPoolId": str,
        "ResourceId": str,
        "ResourceType": IpamResourceTypeType,
        "ResourceTag": "RequestIpamResourceTagTypeDef",
        "ResourceOwner": str,
    },
    total=False,
)

class GetIpamResourceCidrsRequestRequestTypeDef(
    _RequiredGetIpamResourceCidrsRequestRequestTypeDef,
    _OptionalGetIpamResourceCidrsRequestRequestTypeDef,
):
    pass

GetIpamResourceCidrsResultTypeDef = TypedDict(
    "GetIpamResourceCidrsResultTypeDef",
    {
        "NextToken": str,
        "IpamResourceCidrs": List["IpamResourceCidrTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetLaunchTemplateDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetLaunchTemplateDataRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGetLaunchTemplateDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetLaunchTemplateDataRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetLaunchTemplateDataRequestRequestTypeDef(
    _RequiredGetLaunchTemplateDataRequestRequestTypeDef,
    _OptionalGetLaunchTemplateDataRequestRequestTypeDef,
):
    pass

GetLaunchTemplateDataResultTypeDef = TypedDict(
    "GetLaunchTemplateDataResultTypeDef",
    {
        "LaunchTemplateData": "ResponseLaunchTemplateDataTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetManagedPrefixListAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetManagedPrefixListAssociationsRequestRequestTypeDef",
    {
        "PrefixListId": str,
    },
)
_OptionalGetManagedPrefixListAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetManagedPrefixListAssociationsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetManagedPrefixListAssociationsRequestRequestTypeDef(
    _RequiredGetManagedPrefixListAssociationsRequestRequestTypeDef,
    _OptionalGetManagedPrefixListAssociationsRequestRequestTypeDef,
):
    pass

GetManagedPrefixListAssociationsResultTypeDef = TypedDict(
    "GetManagedPrefixListAssociationsResultTypeDef",
    {
        "PrefixListAssociations": List["PrefixListAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetManagedPrefixListEntriesRequestRequestTypeDef = TypedDict(
    "_RequiredGetManagedPrefixListEntriesRequestRequestTypeDef",
    {
        "PrefixListId": str,
    },
)
_OptionalGetManagedPrefixListEntriesRequestRequestTypeDef = TypedDict(
    "_OptionalGetManagedPrefixListEntriesRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TargetVersion": int,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetManagedPrefixListEntriesRequestRequestTypeDef(
    _RequiredGetManagedPrefixListEntriesRequestRequestTypeDef,
    _OptionalGetManagedPrefixListEntriesRequestRequestTypeDef,
):
    pass

GetManagedPrefixListEntriesResultTypeDef = TypedDict(
    "GetManagedPrefixListEntriesResultTypeDef",
    {
        "Entries": List["PrefixListEntryTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef = TypedDict(
    "_RequiredGetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
    },
)
_OptionalGetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef = TypedDict(
    "_OptionalGetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class GetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef(
    _RequiredGetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef,
    _OptionalGetNetworkInsightsAccessScopeAnalysisFindingsRequestRequestTypeDef,
):
    pass

GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "AnalysisStatus": AnalysisStatusType,
        "AnalysisFindings": List["AccessScopeAnalysisFindingTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetNetworkInsightsAccessScopeContentRequestRequestTypeDef = TypedDict(
    "_RequiredGetNetworkInsightsAccessScopeContentRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
    },
)
_OptionalGetNetworkInsightsAccessScopeContentRequestRequestTypeDef = TypedDict(
    "_OptionalGetNetworkInsightsAccessScopeContentRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetNetworkInsightsAccessScopeContentRequestRequestTypeDef(
    _RequiredGetNetworkInsightsAccessScopeContentRequestRequestTypeDef,
    _OptionalGetNetworkInsightsAccessScopeContentRequestRequestTypeDef,
):
    pass

GetNetworkInsightsAccessScopeContentResultTypeDef = TypedDict(
    "GetNetworkInsightsAccessScopeContentResultTypeDef",
    {
        "NetworkInsightsAccessScopeContent": "NetworkInsightsAccessScopeContentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetPasswordDataRequestInstanceTypeDef = TypedDict(
    "GetPasswordDataRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredGetPasswordDataRequestRequestTypeDef = TypedDict(
    "_RequiredGetPasswordDataRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalGetPasswordDataRequestRequestTypeDef = TypedDict(
    "_OptionalGetPasswordDataRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetPasswordDataRequestRequestTypeDef(
    _RequiredGetPasswordDataRequestRequestTypeDef, _OptionalGetPasswordDataRequestRequestTypeDef
):
    pass

GetPasswordDataResultTypeDef = TypedDict(
    "GetPasswordDataResultTypeDef",
    {
        "InstanceId": str,
        "PasswordData": str,
        "Timestamp": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetReservedInstancesExchangeQuoteRequestRequestTypeDef = TypedDict(
    "_RequiredGetReservedInstancesExchangeQuoteRequestRequestTypeDef",
    {
        "ReservedInstanceIds": List[str],
    },
)
_OptionalGetReservedInstancesExchangeQuoteRequestRequestTypeDef = TypedDict(
    "_OptionalGetReservedInstancesExchangeQuoteRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TargetConfigurations": List["TargetConfigurationRequestTypeDef"],
    },
    total=False,
)

class GetReservedInstancesExchangeQuoteRequestRequestTypeDef(
    _RequiredGetReservedInstancesExchangeQuoteRequestRequestTypeDef,
    _OptionalGetReservedInstancesExchangeQuoteRequestRequestTypeDef,
):
    pass

GetReservedInstancesExchangeQuoteResultTypeDef = TypedDict(
    "GetReservedInstancesExchangeQuoteResultTypeDef",
    {
        "CurrencyCode": str,
        "IsValidExchange": bool,
        "OutputReservedInstancesWillExpireAt": datetime,
        "PaymentDue": str,
        "ReservedInstanceValueRollup": "ReservationValueTypeDef",
        "ReservedInstanceValueSet": List["ReservedInstanceReservationValueTypeDef"],
        "TargetConfigurationValueRollup": "ReservationValueTypeDef",
        "TargetConfigurationValueSet": List["TargetReservationValueTypeDef"],
        "ValidationFailureReason": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSecurityGroupsForVpcRequestRequestTypeDef = TypedDict(
    "_RequiredGetSecurityGroupsForVpcRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalGetSecurityGroupsForVpcRequestRequestTypeDef = TypedDict(
    "_OptionalGetSecurityGroupsForVpcRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

class GetSecurityGroupsForVpcRequestRequestTypeDef(
    _RequiredGetSecurityGroupsForVpcRequestRequestTypeDef,
    _OptionalGetSecurityGroupsForVpcRequestRequestTypeDef,
):
    pass

GetSecurityGroupsForVpcResultTypeDef = TypedDict(
    "GetSecurityGroupsForVpcResultTypeDef",
    {
        "NextToken": str,
        "SecurityGroupForVpcs": List["SecurityGroupForVpcTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSerialConsoleAccessStatusRequestRequestTypeDef = TypedDict(
    "GetSerialConsoleAccessStatusRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

GetSerialConsoleAccessStatusResultTypeDef = TypedDict(
    "GetSerialConsoleAccessStatusResultTypeDef",
    {
        "SerialConsoleAccessEnabled": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetSnapshotBlockPublicAccessStateRequestRequestTypeDef = TypedDict(
    "GetSnapshotBlockPublicAccessStateRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

GetSnapshotBlockPublicAccessStateResultTypeDef = TypedDict(
    "GetSnapshotBlockPublicAccessStateResultTypeDef",
    {
        "State": SnapshotBlockPublicAccessStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSpotPlacementScoresRequestRequestTypeDef = TypedDict(
    "_RequiredGetSpotPlacementScoresRequestRequestTypeDef",
    {
        "TargetCapacity": int,
    },
)
_OptionalGetSpotPlacementScoresRequestRequestTypeDef = TypedDict(
    "_OptionalGetSpotPlacementScoresRequestRequestTypeDef",
    {
        "InstanceTypes": List[str],
        "TargetCapacityUnitType": TargetCapacityUnitTypeType,
        "SingleAvailabilityZone": bool,
        "RegionNames": List[str],
        "InstanceRequirementsWithMetadata": "InstanceRequirementsWithMetadataRequestTypeDef",
        "DryRun": bool,
        "MaxResults": int,
        "NextToken": str,
    },
    total=False,
)

class GetSpotPlacementScoresRequestRequestTypeDef(
    _RequiredGetSpotPlacementScoresRequestRequestTypeDef,
    _OptionalGetSpotPlacementScoresRequestRequestTypeDef,
):
    pass

GetSpotPlacementScoresResultTypeDef = TypedDict(
    "GetSpotPlacementScoresResultTypeDef",
    {
        "SpotPlacementScores": List["SpotPlacementScoreTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetSubnetCidrReservationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetSubnetCidrReservationsRequestRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalGetSubnetCidrReservationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetSubnetCidrReservationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "DryRun": bool,
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class GetSubnetCidrReservationsRequestRequestTypeDef(
    _RequiredGetSubnetCidrReservationsRequestRequestTypeDef,
    _OptionalGetSubnetCidrReservationsRequestRequestTypeDef,
):
    pass

GetSubnetCidrReservationsResultTypeDef = TypedDict(
    "GetSubnetCidrReservationsResultTypeDef",
    {
        "SubnetIpv4CidrReservations": List["SubnetCidrReservationTypeDef"],
        "SubnetIpv6CidrReservations": List["SubnetCidrReservationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayAttachmentPropagationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayAttachmentPropagationsRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalGetTransitGatewayAttachmentPropagationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayAttachmentPropagationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class GetTransitGatewayAttachmentPropagationsRequestRequestTypeDef(
    _RequiredGetTransitGatewayAttachmentPropagationsRequestRequestTypeDef,
    _OptionalGetTransitGatewayAttachmentPropagationsRequestRequestTypeDef,
):
    pass

GetTransitGatewayAttachmentPropagationsResultTypeDef = TypedDict(
    "GetTransitGatewayAttachmentPropagationsResultTypeDef",
    {
        "TransitGatewayAttachmentPropagations": List["TransitGatewayAttachmentPropagationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
    },
)
_OptionalGetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class GetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef(
    _RequiredGetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef,
    _OptionalGetTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef,
):
    pass

GetTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "MulticastDomainAssociations": List["TransitGatewayMulticastDomainAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
    },
)
_OptionalGetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class GetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef(
    _RequiredGetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef,
    _OptionalGetTransitGatewayPolicyTableAssociationsRequestRequestTypeDef,
):
    pass

GetTransitGatewayPolicyTableAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayPolicyTableAssociationsResultTypeDef",
    {
        "Associations": List["TransitGatewayPolicyTableAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayPolicyTableEntriesRequestRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayPolicyTableEntriesRequestRequestTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
    },
)
_OptionalGetTransitGatewayPolicyTableEntriesRequestRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayPolicyTableEntriesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class GetTransitGatewayPolicyTableEntriesRequestRequestTypeDef(
    _RequiredGetTransitGatewayPolicyTableEntriesRequestRequestTypeDef,
    _OptionalGetTransitGatewayPolicyTableEntriesRequestRequestTypeDef,
):
    pass

GetTransitGatewayPolicyTableEntriesResultTypeDef = TypedDict(
    "GetTransitGatewayPolicyTableEntriesResultTypeDef",
    {
        "TransitGatewayPolicyTableEntries": List["TransitGatewayPolicyTableEntryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayPrefixListReferencesRequestRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayPrefixListReferencesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalGetTransitGatewayPrefixListReferencesRequestRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayPrefixListReferencesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class GetTransitGatewayPrefixListReferencesRequestRequestTypeDef(
    _RequiredGetTransitGatewayPrefixListReferencesRequestRequestTypeDef,
    _OptionalGetTransitGatewayPrefixListReferencesRequestRequestTypeDef,
):
    pass

GetTransitGatewayPrefixListReferencesResultTypeDef = TypedDict(
    "GetTransitGatewayPrefixListReferencesResultTypeDef",
    {
        "TransitGatewayPrefixListReferences": List["TransitGatewayPrefixListReferenceTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayRouteTableAssociationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayRouteTableAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalGetTransitGatewayRouteTableAssociationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayRouteTableAssociationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class GetTransitGatewayRouteTableAssociationsRequestRequestTypeDef(
    _RequiredGetTransitGatewayRouteTableAssociationsRequestRequestTypeDef,
    _OptionalGetTransitGatewayRouteTableAssociationsRequestRequestTypeDef,
):
    pass

GetTransitGatewayRouteTableAssociationsResultTypeDef = TypedDict(
    "GetTransitGatewayRouteTableAssociationsResultTypeDef",
    {
        "Associations": List["TransitGatewayRouteTableAssociationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetTransitGatewayRouteTablePropagationsRequestRequestTypeDef = TypedDict(
    "_RequiredGetTransitGatewayRouteTablePropagationsRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalGetTransitGatewayRouteTablePropagationsRequestRequestTypeDef = TypedDict(
    "_OptionalGetTransitGatewayRouteTablePropagationsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class GetTransitGatewayRouteTablePropagationsRequestRequestTypeDef(
    _RequiredGetTransitGatewayRouteTablePropagationsRequestRequestTypeDef,
    _OptionalGetTransitGatewayRouteTablePropagationsRequestRequestTypeDef,
):
    pass

GetTransitGatewayRouteTablePropagationsResultTypeDef = TypedDict(
    "GetTransitGatewayRouteTablePropagationsResultTypeDef",
    {
        "TransitGatewayRouteTablePropagations": List["TransitGatewayRouteTablePropagationTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetVerifiedAccessEndpointPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointId": str,
    },
)
_OptionalGetVerifiedAccessEndpointPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetVerifiedAccessEndpointPolicyRequestRequestTypeDef(
    _RequiredGetVerifiedAccessEndpointPolicyRequestRequestTypeDef,
    _OptionalGetVerifiedAccessEndpointPolicyRequestRequestTypeDef,
):
    pass

GetVerifiedAccessEndpointPolicyResultTypeDef = TypedDict(
    "GetVerifiedAccessEndpointPolicyResultTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetVerifiedAccessGroupPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredGetVerifiedAccessGroupPolicyRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
    },
)
_OptionalGetVerifiedAccessGroupPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalGetVerifiedAccessGroupPolicyRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetVerifiedAccessGroupPolicyRequestRequestTypeDef(
    _RequiredGetVerifiedAccessGroupPolicyRequestRequestTypeDef,
    _OptionalGetVerifiedAccessGroupPolicyRequestRequestTypeDef,
):
    pass

GetVerifiedAccessGroupPolicyResultTypeDef = TypedDict(
    "GetVerifiedAccessGroupPolicyResultTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredGetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnConnectionDeviceTypeId": str,
    },
)
_OptionalGetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalGetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef",
    {
        "InternetKeyExchangeVersion": str,
        "DryRun": bool,
    },
    total=False,
)

class GetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef(
    _RequiredGetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef,
    _OptionalGetVpnConnectionDeviceSampleConfigurationRequestRequestTypeDef,
):
    pass

GetVpnConnectionDeviceSampleConfigurationResultTypeDef = TypedDict(
    "GetVpnConnectionDeviceSampleConfigurationResultTypeDef",
    {
        "VpnConnectionDeviceSampleConfiguration": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GetVpnConnectionDeviceTypesRequestRequestTypeDef = TypedDict(
    "GetVpnConnectionDeviceTypesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

GetVpnConnectionDeviceTypesResultTypeDef = TypedDict(
    "GetVpnConnectionDeviceTypesResultTypeDef",
    {
        "VpnConnectionDeviceTypes": List["VpnConnectionDeviceTypeTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredGetVpnTunnelReplacementStatusRequestRequestTypeDef = TypedDict(
    "_RequiredGetVpnTunnelReplacementStatusRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
    },
)
_OptionalGetVpnTunnelReplacementStatusRequestRequestTypeDef = TypedDict(
    "_OptionalGetVpnTunnelReplacementStatusRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class GetVpnTunnelReplacementStatusRequestRequestTypeDef(
    _RequiredGetVpnTunnelReplacementStatusRequestRequestTypeDef,
    _OptionalGetVpnTunnelReplacementStatusRequestRequestTypeDef,
):
    pass

GetVpnTunnelReplacementStatusResultTypeDef = TypedDict(
    "GetVpnTunnelReplacementStatusResultTypeDef",
    {
        "VpnConnectionId": str,
        "TransitGatewayId": str,
        "CustomerGatewayId": str,
        "VpnGatewayId": str,
        "VpnTunnelOutsideIpAddress": str,
        "MaintenanceDetails": "MaintenanceDetailsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

GpuDeviceInfoTypeDef = TypedDict(
    "GpuDeviceInfoTypeDef",
    {
        "Name": str,
        "Manufacturer": str,
        "Count": int,
        "MemoryInfo": "GpuDeviceMemoryInfoTypeDef",
    },
    total=False,
)

GpuDeviceMemoryInfoTypeDef = TypedDict(
    "GpuDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": int,
    },
    total=False,
)

GpuInfoTypeDef = TypedDict(
    "GpuInfoTypeDef",
    {
        "Gpus": List["GpuDeviceInfoTypeDef"],
        "TotalGpuMemoryInMiB": int,
    },
    total=False,
)

GroupIdentifierTypeDef = TypedDict(
    "GroupIdentifierTypeDef",
    {
        "GroupName": str,
        "GroupId": str,
    },
    total=False,
)

HibernationOptionsRequestTypeDef = TypedDict(
    "HibernationOptionsRequestTypeDef",
    {
        "Configured": bool,
    },
    total=False,
)

HibernationOptionsTypeDef = TypedDict(
    "HibernationOptionsTypeDef",
    {
        "Configured": bool,
    },
    total=False,
)

HistoryRecordEntryTypeDef = TypedDict(
    "HistoryRecordEntryTypeDef",
    {
        "EventInformation": "EventInformationTypeDef",
        "EventType": FleetEventTypeType,
        "Timestamp": datetime,
    },
    total=False,
)

HistoryRecordTypeDef = TypedDict(
    "HistoryRecordTypeDef",
    {
        "EventInformation": "EventInformationTypeDef",
        "EventType": EventTypeType,
        "Timestamp": datetime,
    },
    total=False,
)

HostInstanceTypeDef = TypedDict(
    "HostInstanceTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "OwnerId": str,
    },
    total=False,
)

HostOfferingTypeDef = TypedDict(
    "HostOfferingTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Duration": int,
        "HourlyPrice": str,
        "InstanceFamily": str,
        "OfferingId": str,
        "PaymentOption": PaymentOptionType,
        "UpfrontPrice": str,
    },
    total=False,
)

HostPropertiesTypeDef = TypedDict(
    "HostPropertiesTypeDef",
    {
        "Cores": int,
        "InstanceType": str,
        "InstanceFamily": str,
        "Sockets": int,
        "TotalVCpus": int,
    },
    total=False,
)

HostReservationTypeDef = TypedDict(
    "HostReservationTypeDef",
    {
        "Count": int,
        "CurrencyCode": Literal["USD"],
        "Duration": int,
        "End": datetime,
        "HostIdSet": List[str],
        "HostReservationId": str,
        "HourlyPrice": str,
        "InstanceFamily": str,
        "OfferingId": str,
        "PaymentOption": PaymentOptionType,
        "Start": datetime,
        "State": ReservationStateType,
        "UpfrontPrice": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

HostTypeDef = TypedDict(
    "HostTypeDef",
    {
        "AutoPlacement": AutoPlacementType,
        "AvailabilityZone": str,
        "AvailableCapacity": "AvailableCapacityTypeDef",
        "ClientToken": str,
        "HostId": str,
        "HostProperties": "HostPropertiesTypeDef",
        "HostReservationId": str,
        "Instances": List["HostInstanceTypeDef"],
        "State": AllocationStateType,
        "AllocationTime": datetime,
        "ReleaseTime": datetime,
        "Tags": List["TagTypeDef"],
        "HostRecovery": HostRecoveryType,
        "AllowsMultipleInstanceTypes": AllowsMultipleInstanceTypesType,
        "OwnerId": str,
        "AvailabilityZoneId": str,
        "MemberOfServiceLinkedResourceGroup": bool,
        "OutpostArn": str,
        "HostMaintenance": HostMaintenanceType,
        "AssetId": str,
    },
    total=False,
)

IKEVersionsListValueTypeDef = TypedDict(
    "IKEVersionsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

IKEVersionsRequestListValueTypeDef = TypedDict(
    "IKEVersionsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

IamInstanceProfileAssociationTypeDef = TypedDict(
    "IamInstanceProfileAssociationTypeDef",
    {
        "AssociationId": str,
        "InstanceId": str,
        "IamInstanceProfile": "IamInstanceProfileTypeDef",
        "State": IamInstanceProfileAssociationStateType,
        "Timestamp": datetime,
    },
    total=False,
)

IamInstanceProfileSpecificationTypeDef = TypedDict(
    "IamInstanceProfileSpecificationTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

IamInstanceProfileTypeDef = TypedDict(
    "IamInstanceProfileTypeDef",
    {
        "Arn": str,
        "Id": str,
    },
    total=False,
)

IcmpTypeCodeTypeDef = TypedDict(
    "IcmpTypeCodeTypeDef",
    {
        "Code": int,
        "Type": int,
    },
    total=False,
)

IdFormatTypeDef = TypedDict(
    "IdFormatTypeDef",
    {
        "Deadline": datetime,
        "Resource": str,
        "UseLongIds": bool,
    },
    total=False,
)

ImageAttributeTypeDef = TypedDict(
    "ImageAttributeTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "LaunchPermissions": List["LaunchPermissionTypeDef"],
        "ProductCodes": List["ProductCodeTypeDef"],
        "Description": "AttributeValueTypeDef",
        "KernelId": "AttributeValueTypeDef",
        "RamdiskId": "AttributeValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "BootMode": "AttributeValueTypeDef",
        "TpmSupport": "AttributeValueTypeDef",
        "UefiData": "AttributeValueTypeDef",
        "LastLaunchedTime": "AttributeValueTypeDef",
        "ImdsSupport": "AttributeValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImageDiskContainerTypeDef = TypedDict(
    "ImageDiskContainerTypeDef",
    {
        "Description": str,
        "DeviceName": str,
        "Format": str,
        "SnapshotId": str,
        "Url": str,
        "UserBucket": "UserBucketTypeDef",
    },
    total=False,
)

ImageRecycleBinInfoTypeDef = TypedDict(
    "ImageRecycleBinInfoTypeDef",
    {
        "ImageId": str,
        "Name": str,
        "Description": str,
        "RecycleBinEnterTime": datetime,
        "RecycleBinExitTime": datetime,
    },
    total=False,
)

ImageTypeDef = TypedDict(
    "ImageTypeDef",
    {
        "Architecture": ArchitectureValuesType,
        "CreationDate": str,
        "ImageId": str,
        "ImageLocation": str,
        "ImageType": ImageTypeValuesType,
        "Public": bool,
        "KernelId": str,
        "OwnerId": str,
        "Platform": Literal["Windows"],
        "PlatformDetails": str,
        "UsageOperation": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "RamdiskId": str,
        "State": ImageStateType,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "EnaSupport": bool,
        "Hypervisor": HypervisorTypeType,
        "ImageOwnerAlias": str,
        "Name": str,
        "RootDeviceName": str,
        "RootDeviceType": DeviceTypeType,
        "SriovNetSupport": str,
        "StateReason": "StateReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "VirtualizationType": VirtualizationTypeType,
        "BootMode": BootModeValuesType,
        "TpmSupport": Literal["v2.0"],
        "DeprecationTime": str,
        "ImdsSupport": Literal["v2.0"],
        "SourceInstanceId": str,
    },
    total=False,
)

_RequiredImportClientVpnClientCertificateRevocationListRequestRequestTypeDef = TypedDict(
    "_RequiredImportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "CertificateRevocationList": str,
    },
)
_OptionalImportClientVpnClientCertificateRevocationListRequestRequestTypeDef = TypedDict(
    "_OptionalImportClientVpnClientCertificateRevocationListRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ImportClientVpnClientCertificateRevocationListRequestRequestTypeDef(
    _RequiredImportClientVpnClientCertificateRevocationListRequestRequestTypeDef,
    _OptionalImportClientVpnClientCertificateRevocationListRequestRequestTypeDef,
):
    pass

ImportClientVpnClientCertificateRevocationListResultTypeDef = TypedDict(
    "ImportClientVpnClientCertificateRevocationListResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportImageLicenseConfigurationRequestTypeDef = TypedDict(
    "ImportImageLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

ImportImageLicenseConfigurationResponseTypeDef = TypedDict(
    "ImportImageLicenseConfigurationResponseTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

ImportImageRequestRequestTypeDef = TypedDict(
    "ImportImageRequestRequestTypeDef",
    {
        "Architecture": str,
        "ClientData": "ClientDataTypeDef",
        "ClientToken": str,
        "Description": str,
        "DiskContainers": List["ImageDiskContainerTypeDef"],
        "DryRun": bool,
        "Encrypted": bool,
        "Hypervisor": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "RoleName": str,
        "LicenseSpecifications": List["ImportImageLicenseConfigurationRequestTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "UsageOperation": str,
        "BootMode": BootModeValuesType,
    },
    total=False,
)

ImportImageResultTypeDef = TypedDict(
    "ImportImageResultTypeDef",
    {
        "Architecture": str,
        "Description": str,
        "Encrypted": bool,
        "Hypervisor": str,
        "ImageId": str,
        "ImportTaskId": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "Progress": str,
        "SnapshotDetails": List["SnapshotDetailTypeDef"],
        "Status": str,
        "StatusMessage": str,
        "LicenseSpecifications": List["ImportImageLicenseConfigurationResponseTypeDef"],
        "Tags": List["TagTypeDef"],
        "UsageOperation": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportImageTaskTypeDef = TypedDict(
    "ImportImageTaskTypeDef",
    {
        "Architecture": str,
        "Description": str,
        "Encrypted": bool,
        "Hypervisor": str,
        "ImageId": str,
        "ImportTaskId": str,
        "KmsKeyId": str,
        "LicenseType": str,
        "Platform": str,
        "Progress": str,
        "SnapshotDetails": List["SnapshotDetailTypeDef"],
        "Status": str,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
        "LicenseSpecifications": List["ImportImageLicenseConfigurationResponseTypeDef"],
        "UsageOperation": str,
        "BootMode": BootModeValuesType,
    },
    total=False,
)

ImportInstanceLaunchSpecificationTypeDef = TypedDict(
    "ImportInstanceLaunchSpecificationTypeDef",
    {
        "AdditionalInfo": str,
        "Architecture": ArchitectureValuesType,
        "GroupIds": List[str],
        "GroupNames": List[str],
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "InstanceType": InstanceTypeType,
        "Monitoring": bool,
        "Placement": "PlacementTypeDef",
        "PrivateIpAddress": str,
        "SubnetId": str,
        "UserData": "UserDataTypeDef",
    },
    total=False,
)

_RequiredImportInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredImportInstanceRequestRequestTypeDef",
    {
        "Platform": Literal["Windows"],
    },
)
_OptionalImportInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalImportInstanceRequestRequestTypeDef",
    {
        "Description": str,
        "DiskImages": List["DiskImageTypeDef"],
        "DryRun": bool,
        "LaunchSpecification": "ImportInstanceLaunchSpecificationTypeDef",
    },
    total=False,
)

class ImportInstanceRequestRequestTypeDef(
    _RequiredImportInstanceRequestRequestTypeDef, _OptionalImportInstanceRequestRequestTypeDef
):
    pass

ImportInstanceResultTypeDef = TypedDict(
    "ImportInstanceResultTypeDef",
    {
        "ConversionTask": "ConversionTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportInstanceTaskDetailsTypeDef = TypedDict(
    "ImportInstanceTaskDetailsTypeDef",
    {
        "Description": str,
        "InstanceId": str,
        "Platform": Literal["Windows"],
        "Volumes": List["ImportInstanceVolumeDetailItemTypeDef"],
    },
    total=False,
)

ImportInstanceVolumeDetailItemTypeDef = TypedDict(
    "ImportInstanceVolumeDetailItemTypeDef",
    {
        "AvailabilityZone": str,
        "BytesConverted": int,
        "Description": str,
        "Image": "DiskImageDescriptionTypeDef",
        "Status": str,
        "StatusMessage": str,
        "Volume": "DiskImageVolumeDescriptionTypeDef",
    },
    total=False,
)

_RequiredImportKeyPairRequestRequestTypeDef = TypedDict(
    "_RequiredImportKeyPairRequestRequestTypeDef",
    {
        "KeyName": str,
        "PublicKeyMaterial": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportKeyPairRequestRequestTypeDef = TypedDict(
    "_OptionalImportKeyPairRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class ImportKeyPairRequestRequestTypeDef(
    _RequiredImportKeyPairRequestRequestTypeDef, _OptionalImportKeyPairRequestRequestTypeDef
):
    pass

_RequiredImportKeyPairRequestServiceResourceTypeDef = TypedDict(
    "_RequiredImportKeyPairRequestServiceResourceTypeDef",
    {
        "KeyName": str,
        "PublicKeyMaterial": Union[bytes, IO[bytes], StreamingBody],
    },
)
_OptionalImportKeyPairRequestServiceResourceTypeDef = TypedDict(
    "_OptionalImportKeyPairRequestServiceResourceTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class ImportKeyPairRequestServiceResourceTypeDef(
    _RequiredImportKeyPairRequestServiceResourceTypeDef,
    _OptionalImportKeyPairRequestServiceResourceTypeDef,
):
    pass

ImportKeyPairResultTypeDef = TypedDict(
    "ImportKeyPairResultTypeDef",
    {
        "KeyFingerprint": str,
        "KeyName": str,
        "KeyPairId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportSnapshotRequestRequestTypeDef = TypedDict(
    "ImportSnapshotRequestRequestTypeDef",
    {
        "ClientData": "ClientDataTypeDef",
        "ClientToken": str,
        "Description": str,
        "DiskContainer": "SnapshotDiskContainerTypeDef",
        "DryRun": bool,
        "Encrypted": bool,
        "KmsKeyId": str,
        "RoleName": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

ImportSnapshotResultTypeDef = TypedDict(
    "ImportSnapshotResultTypeDef",
    {
        "Description": str,
        "ImportTaskId": str,
        "SnapshotTaskDetail": "SnapshotTaskDetailTypeDef",
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportSnapshotTaskTypeDef = TypedDict(
    "ImportSnapshotTaskTypeDef",
    {
        "Description": str,
        "ImportTaskId": str,
        "SnapshotTaskDetail": "SnapshotTaskDetailTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredImportVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredImportVolumeRequestRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Image": "DiskImageDetailTypeDef",
        "Volume": "VolumeDetailTypeDef",
    },
)
_OptionalImportVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalImportVolumeRequestRequestTypeDef",
    {
        "Description": str,
        "DryRun": bool,
    },
    total=False,
)

class ImportVolumeRequestRequestTypeDef(
    _RequiredImportVolumeRequestRequestTypeDef, _OptionalImportVolumeRequestRequestTypeDef
):
    pass

ImportVolumeResultTypeDef = TypedDict(
    "ImportVolumeResultTypeDef",
    {
        "ConversionTask": "ConversionTaskTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ImportVolumeTaskDetailsTypeDef = TypedDict(
    "ImportVolumeTaskDetailsTypeDef",
    {
        "AvailabilityZone": str,
        "BytesConverted": int,
        "Description": str,
        "Image": "DiskImageDescriptionTypeDef",
        "Volume": "DiskImageVolumeDescriptionTypeDef",
    },
    total=False,
)

InferenceAcceleratorInfoTypeDef = TypedDict(
    "InferenceAcceleratorInfoTypeDef",
    {
        "Accelerators": List["InferenceDeviceInfoTypeDef"],
        "TotalInferenceMemoryInMiB": int,
    },
    total=False,
)

InferenceDeviceInfoTypeDef = TypedDict(
    "InferenceDeviceInfoTypeDef",
    {
        "Count": int,
        "Name": str,
        "Manufacturer": str,
        "MemoryInfo": "InferenceDeviceMemoryInfoTypeDef",
    },
    total=False,
)

InferenceDeviceMemoryInfoTypeDef = TypedDict(
    "InferenceDeviceMemoryInfoTypeDef",
    {
        "SizeInMiB": int,
    },
    total=False,
)

InstanceAttachmentEnaSrdSpecificationTypeDef = TypedDict(
    "InstanceAttachmentEnaSrdSpecificationTypeDef",
    {
        "EnaSrdEnabled": bool,
        "EnaSrdUdpSpecification": "InstanceAttachmentEnaSrdUdpSpecificationTypeDef",
    },
    total=False,
)

InstanceAttachmentEnaSrdUdpSpecificationTypeDef = TypedDict(
    "InstanceAttachmentEnaSrdUdpSpecificationTypeDef",
    {
        "EnaSrdUdpEnabled": bool,
    },
    total=False,
)

InstanceAttributeTypeDef = TypedDict(
    "InstanceAttributeTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "DisableApiTermination": "AttributeBooleanValueTypeDef",
        "EnaSupport": "AttributeBooleanValueTypeDef",
        "EnclaveOptions": "EnclaveOptionsTypeDef",
        "EbsOptimized": "AttributeBooleanValueTypeDef",
        "InstanceId": str,
        "InstanceInitiatedShutdownBehavior": "AttributeValueTypeDef",
        "InstanceType": "AttributeValueTypeDef",
        "KernelId": "AttributeValueTypeDef",
        "ProductCodes": List["ProductCodeTypeDef"],
        "RamdiskId": "AttributeValueTypeDef",
        "RootDeviceName": "AttributeValueTypeDef",
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "UserData": "AttributeValueTypeDef",
        "DisableApiStop": "AttributeBooleanValueTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

InstanceBlockDeviceMappingSpecificationTypeDef = TypedDict(
    "InstanceBlockDeviceMappingSpecificationTypeDef",
    {
        "DeviceName": str,
        "Ebs": "EbsInstanceBlockDeviceSpecificationTypeDef",
        "NoDevice": str,
        "VirtualName": str,
    },
    total=False,
)

InstanceBlockDeviceMappingTypeDef = TypedDict(
    "InstanceBlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "Ebs": "EbsInstanceBlockDeviceTypeDef",
    },
    total=False,
)

InstanceCapacityTypeDef = TypedDict(
    "InstanceCapacityTypeDef",
    {
        "AvailableCapacity": int,
        "InstanceType": str,
        "TotalCapacity": int,
    },
    total=False,
)

InstanceCountTypeDef = TypedDict(
    "InstanceCountTypeDef",
    {
        "InstanceCount": int,
        "State": ListingStateType,
    },
    total=False,
)

_RequiredInstanceCreditSpecificationRequestTypeDef = TypedDict(
    "_RequiredInstanceCreditSpecificationRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalInstanceCreditSpecificationRequestTypeDef = TypedDict(
    "_OptionalInstanceCreditSpecificationRequestTypeDef",
    {
        "CpuCredits": str,
    },
    total=False,
)

class InstanceCreditSpecificationRequestTypeDef(
    _RequiredInstanceCreditSpecificationRequestTypeDef,
    _OptionalInstanceCreditSpecificationRequestTypeDef,
):
    pass

InstanceCreditSpecificationTypeDef = TypedDict(
    "InstanceCreditSpecificationTypeDef",
    {
        "InstanceId": str,
        "CpuCredits": str,
    },
    total=False,
)

InstanceDeleteTagsRequestTypeDef = TypedDict(
    "InstanceDeleteTagsRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "DryRun": bool,
    },
    total=False,
)

InstanceEventWindowAssociationRequestTypeDef = TypedDict(
    "InstanceEventWindowAssociationRequestTypeDef",
    {
        "InstanceIds": List[str],
        "InstanceTags": List["TagTypeDef"],
        "DedicatedHostIds": List[str],
    },
    total=False,
)

InstanceEventWindowAssociationTargetTypeDef = TypedDict(
    "InstanceEventWindowAssociationTargetTypeDef",
    {
        "InstanceIds": List[str],
        "Tags": List["TagTypeDef"],
        "DedicatedHostIds": List[str],
    },
    total=False,
)

InstanceEventWindowDisassociationRequestTypeDef = TypedDict(
    "InstanceEventWindowDisassociationRequestTypeDef",
    {
        "InstanceIds": List[str],
        "InstanceTags": List["TagTypeDef"],
        "DedicatedHostIds": List[str],
    },
    total=False,
)

InstanceEventWindowStateChangeTypeDef = TypedDict(
    "InstanceEventWindowStateChangeTypeDef",
    {
        "InstanceEventWindowId": str,
        "State": InstanceEventWindowStateType,
    },
    total=False,
)

InstanceEventWindowTimeRangeRequestTypeDef = TypedDict(
    "InstanceEventWindowTimeRangeRequestTypeDef",
    {
        "StartWeekDay": WeekDayType,
        "StartHour": int,
        "EndWeekDay": WeekDayType,
        "EndHour": int,
    },
    total=False,
)

InstanceEventWindowTimeRangeTypeDef = TypedDict(
    "InstanceEventWindowTimeRangeTypeDef",
    {
        "StartWeekDay": WeekDayType,
        "StartHour": int,
        "EndWeekDay": WeekDayType,
        "EndHour": int,
    },
    total=False,
)

InstanceEventWindowTypeDef = TypedDict(
    "InstanceEventWindowTypeDef",
    {
        "InstanceEventWindowId": str,
        "TimeRanges": List["InstanceEventWindowTimeRangeTypeDef"],
        "Name": str,
        "CronExpression": str,
        "AssociationTarget": "InstanceEventWindowAssociationTargetTypeDef",
        "State": InstanceEventWindowStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

InstanceExportDetailsTypeDef = TypedDict(
    "InstanceExportDetailsTypeDef",
    {
        "InstanceId": str,
        "TargetEnvironment": ExportEnvironmentType,
    },
    total=False,
)

InstanceFamilyCreditSpecificationTypeDef = TypedDict(
    "InstanceFamilyCreditSpecificationTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
        "CpuCredits": str,
    },
    total=False,
)

InstanceIpv4PrefixTypeDef = TypedDict(
    "InstanceIpv4PrefixTypeDef",
    {
        "Ipv4Prefix": str,
    },
    total=False,
)

InstanceIpv6AddressRequestTypeDef = TypedDict(
    "InstanceIpv6AddressRequestTypeDef",
    {
        "Ipv6Address": str,
    },
    total=False,
)

InstanceIpv6AddressTypeDef = TypedDict(
    "InstanceIpv6AddressTypeDef",
    {
        "Ipv6Address": str,
        "IsPrimaryIpv6": bool,
    },
    total=False,
)

InstanceIpv6PrefixTypeDef = TypedDict(
    "InstanceIpv6PrefixTypeDef",
    {
        "Ipv6Prefix": str,
    },
    total=False,
)

InstanceMaintenanceOptionsRequestTypeDef = TypedDict(
    "InstanceMaintenanceOptionsRequestTypeDef",
    {
        "AutoRecovery": InstanceAutoRecoveryStateType,
    },
    total=False,
)

InstanceMaintenanceOptionsTypeDef = TypedDict(
    "InstanceMaintenanceOptionsTypeDef",
    {
        "AutoRecovery": InstanceAutoRecoveryStateType,
    },
    total=False,
)

InstanceMarketOptionsRequestTypeDef = TypedDict(
    "InstanceMarketOptionsRequestTypeDef",
    {
        "MarketType": MarketTypeType,
        "SpotOptions": "SpotMarketOptionsTypeDef",
    },
    total=False,
)

InstanceMetadataOptionsRequestTypeDef = TypedDict(
    "InstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": HttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
        "HttpProtocolIpv6": InstanceMetadataProtocolStateType,
        "InstanceMetadataTags": InstanceMetadataTagsStateType,
    },
    total=False,
)

InstanceMetadataOptionsResponseTypeDef = TypedDict(
    "InstanceMetadataOptionsResponseTypeDef",
    {
        "State": InstanceMetadataOptionsStateType,
        "HttpTokens": HttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
        "HttpProtocolIpv6": InstanceMetadataProtocolStateType,
        "InstanceMetadataTags": InstanceMetadataTagsStateType,
    },
    total=False,
)

InstanceMonitoringTypeDef = TypedDict(
    "InstanceMonitoringTypeDef",
    {
        "InstanceId": str,
        "Monitoring": "MonitoringTypeDef",
    },
    total=False,
)

InstanceNetworkInterfaceAssociationTypeDef = TypedDict(
    "InstanceNetworkInterfaceAssociationTypeDef",
    {
        "CarrierIp": str,
        "CustomerOwnedIp": str,
        "IpOwnerId": str,
        "PublicDnsName": str,
        "PublicIp": str,
    },
    total=False,
)

InstanceNetworkInterfaceAttachmentTypeDef = TypedDict(
    "InstanceNetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": datetime,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "Status": AttachmentStatusType,
        "NetworkCardIndex": int,
        "EnaSrdSpecification": "InstanceAttachmentEnaSrdSpecificationTypeDef",
    },
    total=False,
)

InstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "InstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
        "AssociateCarrierIpAddress": bool,
        "InterfaceType": str,
        "NetworkCardIndex": int,
        "Ipv4Prefixes": List["Ipv4PrefixSpecificationRequestTypeDef"],
        "Ipv4PrefixCount": int,
        "Ipv6Prefixes": List["Ipv6PrefixSpecificationRequestTypeDef"],
        "Ipv6PrefixCount": int,
        "PrimaryIpv6": bool,
        "EnaSrdSpecification": "EnaSrdSpecificationRequestTypeDef",
    },
    total=False,
)

InstanceNetworkInterfaceTypeDef = TypedDict(
    "InstanceNetworkInterfaceTypeDef",
    {
        "Association": "InstanceNetworkInterfaceAssociationTypeDef",
        "Attachment": "InstanceNetworkInterfaceAttachmentTypeDef",
        "Description": str,
        "Groups": List["GroupIdentifierTypeDef"],
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "MacAddress": str,
        "NetworkInterfaceId": str,
        "OwnerId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["InstancePrivateIpAddressTypeDef"],
        "SourceDestCheck": bool,
        "Status": NetworkInterfaceStatusType,
        "SubnetId": str,
        "VpcId": str,
        "InterfaceType": str,
        "Ipv4Prefixes": List["InstanceIpv4PrefixTypeDef"],
        "Ipv6Prefixes": List["InstanceIpv6PrefixTypeDef"],
    },
    total=False,
)

InstancePrivateIpAddressTypeDef = TypedDict(
    "InstancePrivateIpAddressTypeDef",
    {
        "Association": "InstanceNetworkInterfaceAssociationTypeDef",
        "Primary": bool,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

_RequiredInstanceRequirementsRequestTypeDef = TypedDict(
    "_RequiredInstanceRequirementsRequestTypeDef",
    {
        "VCpuCount": "VCpuCountRangeRequestTypeDef",
        "MemoryMiB": "MemoryMiBRequestTypeDef",
    },
)
_OptionalInstanceRequirementsRequestTypeDef = TypedDict(
    "_OptionalInstanceRequirementsRequestTypeDef",
    {
        "CpuManufacturers": List[CpuManufacturerType],
        "MemoryGiBPerVCpu": "MemoryGiBPerVCpuRequestTypeDef",
        "ExcludedInstanceTypes": List[str],
        "InstanceGenerations": List[InstanceGenerationType],
        "SpotMaxPricePercentageOverLowestPrice": int,
        "OnDemandMaxPricePercentageOverLowestPrice": int,
        "BareMetal": BareMetalType,
        "BurstablePerformance": BurstablePerformanceType,
        "RequireHibernateSupport": bool,
        "NetworkInterfaceCount": "NetworkInterfaceCountRequestTypeDef",
        "LocalStorage": LocalStorageType,
        "LocalStorageTypes": List[LocalStorageTypeType],
        "TotalLocalStorageGB": "TotalLocalStorageGBRequestTypeDef",
        "BaselineEbsBandwidthMbps": "BaselineEbsBandwidthMbpsRequestTypeDef",
        "AcceleratorTypes": List[AcceleratorTypeType],
        "AcceleratorCount": "AcceleratorCountRequestTypeDef",
        "AcceleratorManufacturers": List[AcceleratorManufacturerType],
        "AcceleratorNames": List[AcceleratorNameType],
        "AcceleratorTotalMemoryMiB": "AcceleratorTotalMemoryMiBRequestTypeDef",
        "NetworkBandwidthGbps": "NetworkBandwidthGbpsRequestTypeDef",
        "AllowedInstanceTypes": List[str],
    },
    total=False,
)

class InstanceRequirementsRequestTypeDef(
    _RequiredInstanceRequirementsRequestTypeDef, _OptionalInstanceRequirementsRequestTypeDef
):
    pass

InstanceRequirementsTypeDef = TypedDict(
    "InstanceRequirementsTypeDef",
    {
        "VCpuCount": "VCpuCountRangeTypeDef",
        "MemoryMiB": "MemoryMiBTypeDef",
        "CpuManufacturers": List[CpuManufacturerType],
        "MemoryGiBPerVCpu": "MemoryGiBPerVCpuTypeDef",
        "ExcludedInstanceTypes": List[str],
        "InstanceGenerations": List[InstanceGenerationType],
        "SpotMaxPricePercentageOverLowestPrice": int,
        "OnDemandMaxPricePercentageOverLowestPrice": int,
        "BareMetal": BareMetalType,
        "BurstablePerformance": BurstablePerformanceType,
        "RequireHibernateSupport": bool,
        "NetworkInterfaceCount": "NetworkInterfaceCountTypeDef",
        "LocalStorage": LocalStorageType,
        "LocalStorageTypes": List[LocalStorageTypeType],
        "TotalLocalStorageGB": "TotalLocalStorageGBTypeDef",
        "BaselineEbsBandwidthMbps": "BaselineEbsBandwidthMbpsTypeDef",
        "AcceleratorTypes": List[AcceleratorTypeType],
        "AcceleratorCount": "AcceleratorCountTypeDef",
        "AcceleratorManufacturers": List[AcceleratorManufacturerType],
        "AcceleratorNames": List[AcceleratorNameType],
        "AcceleratorTotalMemoryMiB": "AcceleratorTotalMemoryMiBTypeDef",
        "NetworkBandwidthGbps": "NetworkBandwidthGbpsTypeDef",
        "AllowedInstanceTypes": List[str],
    },
    total=False,
)

InstanceRequirementsWithMetadataRequestTypeDef = TypedDict(
    "InstanceRequirementsWithMetadataRequestTypeDef",
    {
        "ArchitectureTypes": List[ArchitectureTypeType],
        "VirtualizationTypes": List[VirtualizationTypeType],
        "InstanceRequirements": "InstanceRequirementsRequestTypeDef",
    },
    total=False,
)

_RequiredInstanceSpecificationTypeDef = TypedDict(
    "_RequiredInstanceSpecificationTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalInstanceSpecificationTypeDef = TypedDict(
    "_OptionalInstanceSpecificationTypeDef",
    {
        "ExcludeBootVolume": bool,
        "ExcludeDataVolumeIds": List[str],
    },
    total=False,
)

class InstanceSpecificationTypeDef(
    _RequiredInstanceSpecificationTypeDef, _OptionalInstanceSpecificationTypeDef
):
    pass

InstanceStateChangeTypeDef = TypedDict(
    "InstanceStateChangeTypeDef",
    {
        "CurrentState": "InstanceStateTypeDef",
        "InstanceId": str,
        "PreviousState": "InstanceStateTypeDef",
    },
    total=False,
)

InstanceStateTypeDef = TypedDict(
    "InstanceStateTypeDef",
    {
        "Code": int,
        "Name": InstanceStateNameType,
    },
    total=False,
)

InstanceStatusDetailsTypeDef = TypedDict(
    "InstanceStatusDetailsTypeDef",
    {
        "ImpairedSince": datetime,
        "Name": Literal["reachability"],
        "Status": StatusTypeType,
    },
    total=False,
)

InstanceStatusEventTypeDef = TypedDict(
    "InstanceStatusEventTypeDef",
    {
        "InstanceEventId": str,
        "Code": EventCodeType,
        "Description": str,
        "NotAfter": datetime,
        "NotBefore": datetime,
        "NotBeforeDeadline": datetime,
    },
    total=False,
)

InstanceStatusSummaryTypeDef = TypedDict(
    "InstanceStatusSummaryTypeDef",
    {
        "Details": List["InstanceStatusDetailsTypeDef"],
        "Status": SummaryStatusType,
    },
    total=False,
)

InstanceStatusTypeDef = TypedDict(
    "InstanceStatusTypeDef",
    {
        "AvailabilityZone": str,
        "OutpostArn": str,
        "Events": List["InstanceStatusEventTypeDef"],
        "InstanceId": str,
        "InstanceState": "InstanceStateTypeDef",
        "InstanceStatus": "InstanceStatusSummaryTypeDef",
        "SystemStatus": "InstanceStatusSummaryTypeDef",
    },
    total=False,
)

InstanceStorageInfoTypeDef = TypedDict(
    "InstanceStorageInfoTypeDef",
    {
        "TotalSizeInGB": int,
        "Disks": List["DiskInfoTypeDef"],
        "NvmeSupport": EphemeralNvmeSupportType,
        "EncryptionSupport": InstanceStorageEncryptionSupportType,
    },
    total=False,
)

InstanceTagNotificationAttributeTypeDef = TypedDict(
    "InstanceTagNotificationAttributeTypeDef",
    {
        "InstanceTagKeys": List[str],
        "IncludeAllTagsOfInstance": bool,
    },
    total=False,
)

InstanceTopologyTypeDef = TypedDict(
    "InstanceTopologyTypeDef",
    {
        "InstanceId": str,
        "InstanceType": str,
        "GroupName": str,
        "NetworkNodes": List[str],
        "AvailabilityZone": str,
        "ZoneId": str,
    },
    total=False,
)

InstanceTypeDef = TypedDict(
    "InstanceTypeDef",
    {
        "AmiLaunchIndex": int,
        "ImageId": str,
        "InstanceId": str,
        "InstanceType": InstanceTypeType,
        "KernelId": str,
        "KeyName": str,
        "LaunchTime": datetime,
        "Monitoring": "MonitoringTypeDef",
        "Placement": "PlacementTypeDef",
        "Platform": Literal["Windows"],
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "ProductCodes": List["ProductCodeTypeDef"],
        "PublicDnsName": str,
        "PublicIpAddress": str,
        "RamdiskId": str,
        "State": "InstanceStateTypeDef",
        "StateTransitionReason": str,
        "SubnetId": str,
        "VpcId": str,
        "Architecture": ArchitectureValuesType,
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingTypeDef"],
        "ClientToken": str,
        "EbsOptimized": bool,
        "EnaSupport": bool,
        "Hypervisor": HypervisorTypeType,
        "IamInstanceProfile": "IamInstanceProfileTypeDef",
        "InstanceLifecycle": InstanceLifecycleTypeType,
        "ElasticGpuAssociations": List["ElasticGpuAssociationTypeDef"],
        "ElasticInferenceAcceleratorAssociations": List[
            "ElasticInferenceAcceleratorAssociationTypeDef"
        ],
        "NetworkInterfaces": List["InstanceNetworkInterfaceTypeDef"],
        "OutpostArn": str,
        "RootDeviceName": str,
        "RootDeviceType": DeviceTypeType,
        "SecurityGroups": List["GroupIdentifierTypeDef"],
        "SourceDestCheck": bool,
        "SpotInstanceRequestId": str,
        "SriovNetSupport": str,
        "StateReason": "StateReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "VirtualizationType": VirtualizationTypeType,
        "CpuOptions": "CpuOptionsTypeDef",
        "CapacityReservationId": str,
        "CapacityReservationSpecification": "CapacityReservationSpecificationResponseTypeDef",
        "HibernationOptions": "HibernationOptionsTypeDef",
        "Licenses": List["LicenseConfigurationTypeDef"],
        "MetadataOptions": "InstanceMetadataOptionsResponseTypeDef",
        "EnclaveOptions": "EnclaveOptionsTypeDef",
        "BootMode": BootModeValuesType,
        "PlatformDetails": str,
        "UsageOperation": str,
        "UsageOperationUpdateTime": datetime,
        "PrivateDnsNameOptions": "PrivateDnsNameOptionsResponseTypeDef",
        "Ipv6Address": str,
        "TpmSupport": str,
        "MaintenanceOptions": "InstanceMaintenanceOptionsTypeDef",
        "CurrentInstanceBootMode": InstanceBootModeValuesType,
    },
    total=False,
)

InstanceTypeInfoFromInstanceRequirementsTypeDef = TypedDict(
    "InstanceTypeInfoFromInstanceRequirementsTypeDef",
    {
        "InstanceType": str,
    },
    total=False,
)

InstanceTypeInfoTypeDef = TypedDict(
    "InstanceTypeInfoTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "CurrentGeneration": bool,
        "FreeTierEligible": bool,
        "SupportedUsageClasses": List[UsageClassTypeType],
        "SupportedRootDeviceTypes": List[RootDeviceTypeType],
        "SupportedVirtualizationTypes": List[VirtualizationTypeType],
        "BareMetal": bool,
        "Hypervisor": InstanceTypeHypervisorType,
        "ProcessorInfo": "ProcessorInfoTypeDef",
        "VCpuInfo": "VCpuInfoTypeDef",
        "MemoryInfo": "MemoryInfoTypeDef",
        "InstanceStorageSupported": bool,
        "InstanceStorageInfo": "InstanceStorageInfoTypeDef",
        "EbsInfo": "EbsInfoTypeDef",
        "NetworkInfo": "NetworkInfoTypeDef",
        "GpuInfo": "GpuInfoTypeDef",
        "FpgaInfo": "FpgaInfoTypeDef",
        "PlacementGroupInfo": "PlacementGroupInfoTypeDef",
        "InferenceAcceleratorInfo": "InferenceAcceleratorInfoTypeDef",
        "HibernationSupported": bool,
        "BurstablePerformanceSupported": bool,
        "DedicatedHostsSupported": bool,
        "AutoRecoverySupported": bool,
        "SupportedBootModes": List[BootModeTypeType],
        "NitroEnclavesSupport": NitroEnclavesSupportType,
        "NitroTpmSupport": NitroTpmSupportType,
        "NitroTpmInfo": "NitroTpmInfoTypeDef",
    },
    total=False,
)

InstanceTypeOfferingTypeDef = TypedDict(
    "InstanceTypeOfferingTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "LocationType": LocationTypeType,
        "Location": str,
    },
    total=False,
)

InstanceUsageTypeDef = TypedDict(
    "InstanceUsageTypeDef",
    {
        "AccountId": str,
        "UsedInstanceCount": int,
    },
    total=False,
)

IntegrateServicesTypeDef = TypedDict(
    "IntegrateServicesTypeDef",
    {
        "AthenaIntegrations": List["AthenaIntegrationTypeDef"],
    },
    total=False,
)

InternetGatewayAttachmentTypeDef = TypedDict(
    "InternetGatewayAttachmentTypeDef",
    {
        "State": AttachmentStatusType,
        "VpcId": str,
    },
    total=False,
)

InternetGatewayTypeDef = TypedDict(
    "InternetGatewayTypeDef",
    {
        "Attachments": List["InternetGatewayAttachmentTypeDef"],
        "InternetGatewayId": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

IpPermissionTypeDef = TypedDict(
    "IpPermissionTypeDef",
    {
        "FromPort": int,
        "IpProtocol": str,
        "IpRanges": List["IpRangeTypeDef"],
        "Ipv6Ranges": List["Ipv6RangeTypeDef"],
        "PrefixListIds": List["PrefixListIdTypeDef"],
        "ToPort": int,
        "UserIdGroupPairs": List["UserIdGroupPairTypeDef"],
    },
    total=False,
)

IpRangeTypeDef = TypedDict(
    "IpRangeTypeDef",
    {
        "CidrIp": str,
        "Description": str,
    },
    total=False,
)

IpamAddressHistoryRecordTypeDef = TypedDict(
    "IpamAddressHistoryRecordTypeDef",
    {
        "ResourceOwnerId": str,
        "ResourceRegion": str,
        "ResourceType": IpamAddressHistoryResourceTypeType,
        "ResourceId": str,
        "ResourceCidr": str,
        "ResourceName": str,
        "ResourceComplianceStatus": IpamComplianceStatusType,
        "ResourceOverlapStatus": IpamOverlapStatusType,
        "VpcId": str,
        "SampledStartTime": datetime,
        "SampledEndTime": datetime,
    },
    total=False,
)

IpamCidrAuthorizationContextTypeDef = TypedDict(
    "IpamCidrAuthorizationContextTypeDef",
    {
        "Message": str,
        "Signature": str,
    },
    total=False,
)

IpamDiscoveredAccountTypeDef = TypedDict(
    "IpamDiscoveredAccountTypeDef",
    {
        "AccountId": str,
        "DiscoveryRegion": str,
        "FailureReason": "IpamDiscoveryFailureReasonTypeDef",
        "LastAttemptedDiscoveryTime": datetime,
        "LastSuccessfulDiscoveryTime": datetime,
    },
    total=False,
)

IpamDiscoveredResourceCidrTypeDef = TypedDict(
    "IpamDiscoveredResourceCidrTypeDef",
    {
        "IpamResourceDiscoveryId": str,
        "ResourceRegion": str,
        "ResourceId": str,
        "ResourceOwnerId": str,
        "ResourceCidr": str,
        "ResourceType": IpamResourceTypeType,
        "ResourceTags": List["IpamResourceTagTypeDef"],
        "IpUsage": float,
        "VpcId": str,
        "SampleTime": datetime,
    },
    total=False,
)

IpamDiscoveryFailureReasonTypeDef = TypedDict(
    "IpamDiscoveryFailureReasonTypeDef",
    {
        "Code": IpamDiscoveryFailureCodeType,
        "Message": str,
    },
    total=False,
)

IpamOperatingRegionTypeDef = TypedDict(
    "IpamOperatingRegionTypeDef",
    {
        "RegionName": str,
    },
    total=False,
)

IpamPoolAllocationTypeDef = TypedDict(
    "IpamPoolAllocationTypeDef",
    {
        "Cidr": str,
        "IpamPoolAllocationId": str,
        "Description": str,
        "ResourceId": str,
        "ResourceType": IpamPoolAllocationResourceTypeType,
        "ResourceRegion": str,
        "ResourceOwner": str,
    },
    total=False,
)

IpamPoolCidrFailureReasonTypeDef = TypedDict(
    "IpamPoolCidrFailureReasonTypeDef",
    {
        "Code": IpamPoolCidrFailureCodeType,
        "Message": str,
    },
    total=False,
)

IpamPoolCidrTypeDef = TypedDict(
    "IpamPoolCidrTypeDef",
    {
        "Cidr": str,
        "State": IpamPoolCidrStateType,
        "FailureReason": "IpamPoolCidrFailureReasonTypeDef",
        "IpamPoolCidrId": str,
        "NetmaskLength": int,
    },
    total=False,
)

IpamPoolTypeDef = TypedDict(
    "IpamPoolTypeDef",
    {
        "OwnerId": str,
        "IpamPoolId": str,
        "SourceIpamPoolId": str,
        "IpamPoolArn": str,
        "IpamScopeArn": str,
        "IpamScopeType": IpamScopeTypeType,
        "IpamArn": str,
        "IpamRegion": str,
        "Locale": str,
        "PoolDepth": int,
        "State": IpamPoolStateType,
        "StateMessage": str,
        "Description": str,
        "AutoImport": bool,
        "PubliclyAdvertisable": bool,
        "AddressFamily": AddressFamilyType,
        "AllocationMinNetmaskLength": int,
        "AllocationMaxNetmaskLength": int,
        "AllocationDefaultNetmaskLength": int,
        "AllocationResourceTags": List["IpamResourceTagTypeDef"],
        "Tags": List["TagTypeDef"],
        "AwsService": Literal["ec2"],
        "PublicIpSource": IpamPoolPublicIpSourceType,
    },
    total=False,
)

IpamResourceCidrTypeDef = TypedDict(
    "IpamResourceCidrTypeDef",
    {
        "IpamId": str,
        "IpamScopeId": str,
        "IpamPoolId": str,
        "ResourceRegion": str,
        "ResourceOwnerId": str,
        "ResourceId": str,
        "ResourceName": str,
        "ResourceCidr": str,
        "ResourceType": IpamResourceTypeType,
        "ResourceTags": List["IpamResourceTagTypeDef"],
        "IpUsage": float,
        "ComplianceStatus": IpamComplianceStatusType,
        "ManagementState": IpamManagementStateType,
        "OverlapStatus": IpamOverlapStatusType,
        "VpcId": str,
    },
    total=False,
)

IpamResourceDiscoveryAssociationTypeDef = TypedDict(
    "IpamResourceDiscoveryAssociationTypeDef",
    {
        "OwnerId": str,
        "IpamResourceDiscoveryAssociationId": str,
        "IpamResourceDiscoveryAssociationArn": str,
        "IpamResourceDiscoveryId": str,
        "IpamId": str,
        "IpamArn": str,
        "IpamRegion": str,
        "IsDefault": bool,
        "ResourceDiscoveryStatus": IpamAssociatedResourceDiscoveryStatusType,
        "State": IpamResourceDiscoveryAssociationStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

IpamResourceDiscoveryTypeDef = TypedDict(
    "IpamResourceDiscoveryTypeDef",
    {
        "OwnerId": str,
        "IpamResourceDiscoveryId": str,
        "IpamResourceDiscoveryArn": str,
        "IpamResourceDiscoveryRegion": str,
        "Description": str,
        "OperatingRegions": List["IpamOperatingRegionTypeDef"],
        "IsDefault": bool,
        "State": IpamResourceDiscoveryStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

IpamResourceTagTypeDef = TypedDict(
    "IpamResourceTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

IpamScopeTypeDef = TypedDict(
    "IpamScopeTypeDef",
    {
        "OwnerId": str,
        "IpamScopeId": str,
        "IpamScopeArn": str,
        "IpamArn": str,
        "IpamRegion": str,
        "IpamScopeType": IpamScopeTypeType,
        "IsDefault": bool,
        "Description": str,
        "PoolCount": int,
        "State": IpamScopeStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

IpamTypeDef = TypedDict(
    "IpamTypeDef",
    {
        "OwnerId": str,
        "IpamId": str,
        "IpamArn": str,
        "IpamRegion": str,
        "PublicDefaultScopeId": str,
        "PrivateDefaultScopeId": str,
        "ScopeCount": int,
        "Description": str,
        "OperatingRegions": List["IpamOperatingRegionTypeDef"],
        "State": IpamStateType,
        "Tags": List["TagTypeDef"],
        "DefaultResourceDiscoveryId": str,
        "DefaultResourceDiscoveryAssociationId": str,
        "ResourceDiscoveryAssociationCount": int,
    },
    total=False,
)

Ipv4PrefixSpecificationRequestTypeDef = TypedDict(
    "Ipv4PrefixSpecificationRequestTypeDef",
    {
        "Ipv4Prefix": str,
    },
    total=False,
)

Ipv4PrefixSpecificationResponseTypeDef = TypedDict(
    "Ipv4PrefixSpecificationResponseTypeDef",
    {
        "Ipv4Prefix": str,
    },
    total=False,
)

Ipv4PrefixSpecificationTypeDef = TypedDict(
    "Ipv4PrefixSpecificationTypeDef",
    {
        "Ipv4Prefix": str,
    },
    total=False,
)

Ipv6CidrAssociationTypeDef = TypedDict(
    "Ipv6CidrAssociationTypeDef",
    {
        "Ipv6Cidr": str,
        "AssociatedResource": str,
    },
    total=False,
)

Ipv6CidrBlockTypeDef = TypedDict(
    "Ipv6CidrBlockTypeDef",
    {
        "Ipv6CidrBlock": str,
    },
    total=False,
)

Ipv6PoolTypeDef = TypedDict(
    "Ipv6PoolTypeDef",
    {
        "PoolId": str,
        "Description": str,
        "PoolCidrBlocks": List["PoolCidrBlockTypeDef"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

Ipv6PrefixSpecificationRequestTypeDef = TypedDict(
    "Ipv6PrefixSpecificationRequestTypeDef",
    {
        "Ipv6Prefix": str,
    },
    total=False,
)

Ipv6PrefixSpecificationResponseTypeDef = TypedDict(
    "Ipv6PrefixSpecificationResponseTypeDef",
    {
        "Ipv6Prefix": str,
    },
    total=False,
)

Ipv6PrefixSpecificationTypeDef = TypedDict(
    "Ipv6PrefixSpecificationTypeDef",
    {
        "Ipv6Prefix": str,
    },
    total=False,
)

Ipv6RangeTypeDef = TypedDict(
    "Ipv6RangeTypeDef",
    {
        "CidrIpv6": str,
        "Description": str,
    },
    total=False,
)

KeyPairInfoTypeDef = TypedDict(
    "KeyPairInfoTypeDef",
    {
        "KeyPairId": str,
        "KeyFingerprint": str,
        "KeyName": str,
        "KeyType": KeyTypeType,
        "Tags": List["TagTypeDef"],
        "PublicKey": str,
        "CreateTime": datetime,
    },
    total=False,
)

KeyPairTypeDef = TypedDict(
    "KeyPairTypeDef",
    {
        "KeyFingerprint": str,
        "KeyMaterial": str,
        "KeyName": str,
        "KeyPairId": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LastErrorTypeDef = TypedDict(
    "LastErrorTypeDef",
    {
        "Message": str,
        "Code": str,
    },
    total=False,
)

LaunchPermissionModificationsTypeDef = TypedDict(
    "LaunchPermissionModificationsTypeDef",
    {
        "Add": List["LaunchPermissionTypeDef"],
        "Remove": List["LaunchPermissionTypeDef"],
    },
    total=False,
)

LaunchPermissionTypeDef = TypedDict(
    "LaunchPermissionTypeDef",
    {
        "Group": Literal["all"],
        "UserId": str,
        "OrganizationArn": str,
        "OrganizationalUnitArn": str,
    },
    total=False,
)

LaunchSpecificationTypeDef = TypedDict(
    "LaunchSpecificationTypeDef",
    {
        "UserData": str,
        "SecurityGroups": List["GroupIdentifierTypeDef"],
        "AddressingType": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KernelId": str,
        "KeyName": str,
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "Placement": "SpotPlacementTypeDef",
        "RamdiskId": str,
        "SubnetId": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
    },
    total=False,
)

LaunchTemplateAndOverridesResponseTypeDef = TypedDict(
    "LaunchTemplateAndOverridesResponseTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationTypeDef",
        "Overrides": "FleetLaunchTemplateOverridesTypeDef",
    },
    total=False,
)

LaunchTemplateBlockDeviceMappingRequestTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingRequestTypeDef",
    {
        "DeviceName": str,
        "VirtualName": str,
        "Ebs": "LaunchTemplateEbsBlockDeviceRequestTypeDef",
        "NoDevice": str,
    },
    total=False,
)

LaunchTemplateBlockDeviceMappingTypeDef = TypedDict(
    "LaunchTemplateBlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "VirtualName": str,
        "Ebs": "LaunchTemplateEbsBlockDeviceTypeDef",
        "NoDevice": str,
    },
    total=False,
)

LaunchTemplateCapacityReservationSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": "CapacityReservationTargetTypeDef",
    },
    total=False,
)

LaunchTemplateCapacityReservationSpecificationResponseTypeDef = TypedDict(
    "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
    {
        "CapacityReservationPreference": CapacityReservationPreferenceType,
        "CapacityReservationTarget": "CapacityReservationTargetResponseTypeDef",
    },
    total=False,
)

LaunchTemplateConfigTypeDef = TypedDict(
    "LaunchTemplateConfigTypeDef",
    {
        "LaunchTemplateSpecification": "FleetLaunchTemplateSpecificationTypeDef",
        "Overrides": List["LaunchTemplateOverridesTypeDef"],
    },
    total=False,
)

LaunchTemplateCpuOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsRequestTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
        "AmdSevSnp": AmdSevSnpSpecificationType,
    },
    total=False,
)

LaunchTemplateCpuOptionsTypeDef = TypedDict(
    "LaunchTemplateCpuOptionsTypeDef",
    {
        "CoreCount": int,
        "ThreadsPerCore": int,
        "AmdSevSnp": AmdSevSnpSpecificationType,
    },
    total=False,
)

LaunchTemplateEbsBlockDeviceRequestTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceRequestTypeDef",
    {
        "Encrypted": bool,
        "DeleteOnTermination": bool,
        "Iops": int,
        "KmsKeyId": str,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": VolumeTypeType,
        "Throughput": int,
    },
    total=False,
)

LaunchTemplateEbsBlockDeviceTypeDef = TypedDict(
    "LaunchTemplateEbsBlockDeviceTypeDef",
    {
        "Encrypted": bool,
        "DeleteOnTermination": bool,
        "Iops": int,
        "KmsKeyId": str,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": VolumeTypeType,
        "Throughput": int,
    },
    total=False,
)

LaunchTemplateElasticInferenceAcceleratorResponseTypeDef = TypedDict(
    "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef",
    {
        "Type": str,
        "Count": int,
    },
    total=False,
)

_RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "_RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef",
    {
        "Type": str,
    },
)
_OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef = TypedDict(
    "_OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef",
    {
        "Count": int,
    },
    total=False,
)

class LaunchTemplateElasticInferenceAcceleratorTypeDef(
    _RequiredLaunchTemplateElasticInferenceAcceleratorTypeDef,
    _OptionalLaunchTemplateElasticInferenceAcceleratorTypeDef,
):
    pass

LaunchTemplateEnaSrdSpecificationTypeDef = TypedDict(
    "LaunchTemplateEnaSrdSpecificationTypeDef",
    {
        "EnaSrdEnabled": bool,
        "EnaSrdUdpSpecification": "LaunchTemplateEnaSrdUdpSpecificationTypeDef",
    },
    total=False,
)

LaunchTemplateEnaSrdUdpSpecificationTypeDef = TypedDict(
    "LaunchTemplateEnaSrdUdpSpecificationTypeDef",
    {
        "EnaSrdUdpEnabled": bool,
    },
    total=False,
)

LaunchTemplateEnclaveOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateEnclaveOptionsRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LaunchTemplateEnclaveOptionsTypeDef = TypedDict(
    "LaunchTemplateEnclaveOptionsTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LaunchTemplateHibernationOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsRequestTypeDef",
    {
        "Configured": bool,
    },
    total=False,
)

LaunchTemplateHibernationOptionsTypeDef = TypedDict(
    "LaunchTemplateHibernationOptionsTypeDef",
    {
        "Configured": bool,
    },
    total=False,
)

LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

LaunchTemplateIamInstanceProfileSpecificationTypeDef = TypedDict(
    "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef",
    {
        "AutoRecovery": LaunchTemplateAutoRecoveryStateType,
    },
    total=False,
)

LaunchTemplateInstanceMaintenanceOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMaintenanceOptionsTypeDef",
    {
        "AutoRecovery": LaunchTemplateAutoRecoveryStateType,
    },
    total=False,
)

LaunchTemplateInstanceMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
    {
        "MarketType": MarketTypeType,
        "SpotOptions": "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    },
    total=False,
)

LaunchTemplateInstanceMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMarketOptionsTypeDef",
    {
        "MarketType": MarketTypeType,
        "SpotOptions": "LaunchTemplateSpotMarketOptionsTypeDef",
    },
    total=False,
)

LaunchTemplateInstanceMetadataOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
    {
        "HttpTokens": LaunchTemplateHttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": LaunchTemplateInstanceMetadataEndpointStateType,
        "HttpProtocolIpv6": LaunchTemplateInstanceMetadataProtocolIpv6Type,
        "InstanceMetadataTags": LaunchTemplateInstanceMetadataTagsStateType,
    },
    total=False,
)

LaunchTemplateInstanceMetadataOptionsTypeDef = TypedDict(
    "LaunchTemplateInstanceMetadataOptionsTypeDef",
    {
        "State": LaunchTemplateInstanceMetadataOptionsStateType,
        "HttpTokens": LaunchTemplateHttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": LaunchTemplateInstanceMetadataEndpointStateType,
        "HttpProtocolIpv6": LaunchTemplateInstanceMetadataProtocolIpv6Type,
        "InstanceMetadataTags": LaunchTemplateInstanceMetadataTagsStateType,
    },
    total=False,
)

LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef",
    {
        "AssociateCarrierIpAddress": bool,
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "InterfaceType": str,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressRequestTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
        "NetworkCardIndex": int,
        "Ipv4Prefixes": List["Ipv4PrefixSpecificationRequestTypeDef"],
        "Ipv4PrefixCount": int,
        "Ipv6Prefixes": List["Ipv6PrefixSpecificationRequestTypeDef"],
        "Ipv6PrefixCount": int,
        "PrimaryIpv6": bool,
        "EnaSrdSpecification": "EnaSrdSpecificationRequestTypeDef",
    },
    total=False,
)

LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef = TypedDict(
    "LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef",
    {
        "AssociateCarrierIpAddress": bool,
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "InterfaceType": str,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["PrivateIpAddressSpecificationTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
        "NetworkCardIndex": int,
        "Ipv4Prefixes": List["Ipv4PrefixSpecificationResponseTypeDef"],
        "Ipv4PrefixCount": int,
        "Ipv6Prefixes": List["Ipv6PrefixSpecificationResponseTypeDef"],
        "Ipv6PrefixCount": int,
        "PrimaryIpv6": bool,
        "EnaSrdSpecification": "LaunchTemplateEnaSrdSpecificationTypeDef",
    },
    total=False,
)

LaunchTemplateLicenseConfigurationRequestTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

LaunchTemplateLicenseConfigurationTypeDef = TypedDict(
    "LaunchTemplateLicenseConfigurationTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

LaunchTemplateOverridesTypeDef = TypedDict(
    "LaunchTemplateOverridesTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "SpotPrice": str,
        "SubnetId": str,
        "AvailabilityZone": str,
        "WeightedCapacity": float,
        "Priority": float,
        "InstanceRequirements": "InstanceRequirementsTypeDef",
    },
    total=False,
)

LaunchTemplatePlacementRequestTypeDef = TypedDict(
    "LaunchTemplatePlacementRequestTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "HostId": str,
        "Tenancy": TenancyType,
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
        "PartitionNumber": int,
        "GroupId": str,
    },
    total=False,
)

LaunchTemplatePlacementTypeDef = TypedDict(
    "LaunchTemplatePlacementTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "HostId": str,
        "Tenancy": TenancyType,
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
        "PartitionNumber": int,
        "GroupId": str,
    },
    total=False,
)

LaunchTemplatePrivateDnsNameOptionsRequestTypeDef = TypedDict(
    "LaunchTemplatePrivateDnsNameOptionsRequestTypeDef",
    {
        "HostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
    },
    total=False,
)

LaunchTemplatePrivateDnsNameOptionsTypeDef = TypedDict(
    "LaunchTemplatePrivateDnsNameOptionsTypeDef",
    {
        "HostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
    },
    total=False,
)

LaunchTemplateSpecificationTypeDef = TypedDict(
    "LaunchTemplateSpecificationTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "Version": str,
    },
    total=False,
)

LaunchTemplateSpotMarketOptionsRequestTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsRequestTypeDef",
    {
        "MaxPrice": str,
        "SpotInstanceType": SpotInstanceTypeType,
        "BlockDurationMinutes": int,
        "ValidUntil": Union[datetime, str],
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

LaunchTemplateSpotMarketOptionsTypeDef = TypedDict(
    "LaunchTemplateSpotMarketOptionsTypeDef",
    {
        "MaxPrice": str,
        "SpotInstanceType": SpotInstanceTypeType,
        "BlockDurationMinutes": int,
        "ValidUntil": datetime,
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

LaunchTemplateTagSpecificationRequestTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationRequestTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchTemplateTagSpecificationTypeDef = TypedDict(
    "LaunchTemplateTagSpecificationTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchTemplateTypeDef = TypedDict(
    "LaunchTemplateTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "CreateTime": datetime,
        "CreatedBy": str,
        "DefaultVersionNumber": int,
        "LatestVersionNumber": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LaunchTemplateVersionTypeDef = TypedDict(
    "LaunchTemplateVersionTypeDef",
    {
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "VersionNumber": int,
        "VersionDescription": str,
        "CreateTime": datetime,
        "CreatedBy": str,
        "DefaultVersion": bool,
        "LaunchTemplateData": "ResponseLaunchTemplateDataTypeDef",
    },
    total=False,
)

LaunchTemplatesMonitoringRequestTypeDef = TypedDict(
    "LaunchTemplatesMonitoringRequestTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LaunchTemplatesMonitoringTypeDef = TypedDict(
    "LaunchTemplatesMonitoringTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

LicenseConfigurationRequestTypeDef = TypedDict(
    "LicenseConfigurationRequestTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

LicenseConfigurationTypeDef = TypedDict(
    "LicenseConfigurationTypeDef",
    {
        "LicenseConfigurationArn": str,
    },
    total=False,
)

ListImagesInRecycleBinRequestRequestTypeDef = TypedDict(
    "ListImagesInRecycleBinRequestRequestTypeDef",
    {
        "ImageIds": List[str],
        "NextToken": str,
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)

ListImagesInRecycleBinResultTypeDef = TypedDict(
    "ListImagesInRecycleBinResultTypeDef",
    {
        "Images": List["ImageRecycleBinInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListSnapshotsInRecycleBinRequestRequestTypeDef = TypedDict(
    "ListSnapshotsInRecycleBinRequestRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "SnapshotIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

ListSnapshotsInRecycleBinResultTypeDef = TypedDict(
    "ListSnapshotsInRecycleBinResultTypeDef",
    {
        "Snapshots": List["SnapshotRecycleBinInfoTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

LoadBalancersConfigTypeDef = TypedDict(
    "LoadBalancersConfigTypeDef",
    {
        "ClassicLoadBalancersConfig": "ClassicLoadBalancersConfigTypeDef",
        "TargetGroupsConfig": "TargetGroupsConfigTypeDef",
    },
    total=False,
)

LoadPermissionModificationsTypeDef = TypedDict(
    "LoadPermissionModificationsTypeDef",
    {
        "Add": List["LoadPermissionRequestTypeDef"],
        "Remove": List["LoadPermissionRequestTypeDef"],
    },
    total=False,
)

LoadPermissionRequestTypeDef = TypedDict(
    "LoadPermissionRequestTypeDef",
    {
        "Group": Literal["all"],
        "UserId": str,
    },
    total=False,
)

LoadPermissionTypeDef = TypedDict(
    "LoadPermissionTypeDef",
    {
        "UserId": str,
        "Group": Literal["all"],
    },
    total=False,
)

LocalGatewayRouteTableTypeDef = TypedDict(
    "LocalGatewayRouteTableTypeDef",
    {
        "LocalGatewayRouteTableId": str,
        "LocalGatewayRouteTableArn": str,
        "LocalGatewayId": str,
        "OutpostArn": str,
        "OwnerId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
        "Mode": LocalGatewayRouteTableModeType,
        "StateReason": "StateReasonTypeDef",
    },
    total=False,
)

LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVirtualInterfaceGroupAssociationTypeDef",
    {
        "LocalGatewayRouteTableVirtualInterfaceGroupAssociationId": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "LocalGatewayId": str,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayRouteTableArn": str,
        "OwnerId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayRouteTableVpcAssociationTypeDef = TypedDict(
    "LocalGatewayRouteTableVpcAssociationTypeDef",
    {
        "LocalGatewayRouteTableVpcAssociationId": str,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayRouteTableArn": str,
        "LocalGatewayId": str,
        "VpcId": str,
        "OwnerId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayRouteTypeDef = TypedDict(
    "LocalGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "Type": LocalGatewayRouteTypeType,
        "State": LocalGatewayRouteStateType,
        "LocalGatewayRouteTableId": str,
        "LocalGatewayRouteTableArn": str,
        "OwnerId": str,
        "SubnetId": str,
        "CoipPoolId": str,
        "NetworkInterfaceId": str,
        "DestinationPrefixListId": str,
    },
    total=False,
)

LocalGatewayTypeDef = TypedDict(
    "LocalGatewayTypeDef",
    {
        "LocalGatewayId": str,
        "OutpostArn": str,
        "OwnerId": str,
        "State": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayVirtualInterfaceGroupTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceGroupTypeDef",
    {
        "LocalGatewayVirtualInterfaceGroupId": str,
        "LocalGatewayVirtualInterfaceIds": List[str],
        "LocalGatewayId": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

LocalGatewayVirtualInterfaceTypeDef = TypedDict(
    "LocalGatewayVirtualInterfaceTypeDef",
    {
        "LocalGatewayVirtualInterfaceId": str,
        "LocalGatewayId": str,
        "Vlan": int,
        "LocalAddress": str,
        "PeerAddress": str,
        "LocalBgpAsn": int,
        "PeerBgpAsn": int,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

MaintenanceDetailsTypeDef = TypedDict(
    "MaintenanceDetailsTypeDef",
    {
        "PendingMaintenance": str,
        "MaintenanceAutoAppliedAfter": datetime,
        "LastMaintenanceApplied": datetime,
    },
    total=False,
)

ManagedPrefixListTypeDef = TypedDict(
    "ManagedPrefixListTypeDef",
    {
        "PrefixListId": str,
        "AddressFamily": str,
        "State": PrefixListStateType,
        "StateMessage": str,
        "PrefixListArn": str,
        "PrefixListName": str,
        "MaxEntries": int,
        "Version": int,
        "Tags": List["TagTypeDef"],
        "OwnerId": str,
    },
    total=False,
)

MemoryGiBPerVCpuRequestTypeDef = TypedDict(
    "MemoryGiBPerVCpuRequestTypeDef",
    {
        "Min": float,
        "Max": float,
    },
    total=False,
)

MemoryGiBPerVCpuTypeDef = TypedDict(
    "MemoryGiBPerVCpuTypeDef",
    {
        "Min": float,
        "Max": float,
    },
    total=False,
)

MemoryInfoTypeDef = TypedDict(
    "MemoryInfoTypeDef",
    {
        "SizeInMiB": int,
    },
    total=False,
)

_RequiredMemoryMiBRequestTypeDef = TypedDict(
    "_RequiredMemoryMiBRequestTypeDef",
    {
        "Min": int,
    },
)
_OptionalMemoryMiBRequestTypeDef = TypedDict(
    "_OptionalMemoryMiBRequestTypeDef",
    {
        "Max": int,
    },
    total=False,
)

class MemoryMiBRequestTypeDef(_RequiredMemoryMiBRequestTypeDef, _OptionalMemoryMiBRequestTypeDef):
    pass

MemoryMiBTypeDef = TypedDict(
    "MemoryMiBTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

MetricPointTypeDef = TypedDict(
    "MetricPointTypeDef",
    {
        "StartDate": datetime,
        "EndDate": datetime,
        "Value": float,
        "Status": str,
    },
    total=False,
)

_RequiredModifyAddressAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyAddressAttributeRequestRequestTypeDef",
    {
        "AllocationId": str,
    },
)
_OptionalModifyAddressAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyAddressAttributeRequestRequestTypeDef",
    {
        "DomainName": str,
        "DryRun": bool,
    },
    total=False,
)

class ModifyAddressAttributeRequestRequestTypeDef(
    _RequiredModifyAddressAttributeRequestRequestTypeDef,
    _OptionalModifyAddressAttributeRequestRequestTypeDef,
):
    pass

ModifyAddressAttributeResultTypeDef = TypedDict(
    "ModifyAddressAttributeResultTypeDef",
    {
        "Address": "AddressAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyAvailabilityZoneGroupRequestRequestTypeDef = TypedDict(
    "_RequiredModifyAvailabilityZoneGroupRequestRequestTypeDef",
    {
        "GroupName": str,
        "OptInStatus": ModifyAvailabilityZoneOptInStatusType,
    },
)
_OptionalModifyAvailabilityZoneGroupRequestRequestTypeDef = TypedDict(
    "_OptionalModifyAvailabilityZoneGroupRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ModifyAvailabilityZoneGroupRequestRequestTypeDef(
    _RequiredModifyAvailabilityZoneGroupRequestRequestTypeDef,
    _OptionalModifyAvailabilityZoneGroupRequestRequestTypeDef,
):
    pass

ModifyAvailabilityZoneGroupResultTypeDef = TypedDict(
    "ModifyAvailabilityZoneGroupResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyCapacityReservationFleetRequestRequestTypeDef = TypedDict(
    "_RequiredModifyCapacityReservationFleetRequestRequestTypeDef",
    {
        "CapacityReservationFleetId": str,
    },
)
_OptionalModifyCapacityReservationFleetRequestRequestTypeDef = TypedDict(
    "_OptionalModifyCapacityReservationFleetRequestRequestTypeDef",
    {
        "TotalTargetCapacity": int,
        "EndDate": Union[datetime, str],
        "DryRun": bool,
        "RemoveEndDate": bool,
    },
    total=False,
)

class ModifyCapacityReservationFleetRequestRequestTypeDef(
    _RequiredModifyCapacityReservationFleetRequestRequestTypeDef,
    _OptionalModifyCapacityReservationFleetRequestRequestTypeDef,
):
    pass

ModifyCapacityReservationFleetResultTypeDef = TypedDict(
    "ModifyCapacityReservationFleetResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyCapacityReservationRequestRequestTypeDef = TypedDict(
    "_RequiredModifyCapacityReservationRequestRequestTypeDef",
    {
        "CapacityReservationId": str,
    },
)
_OptionalModifyCapacityReservationRequestRequestTypeDef = TypedDict(
    "_OptionalModifyCapacityReservationRequestRequestTypeDef",
    {
        "InstanceCount": int,
        "EndDate": Union[datetime, str],
        "EndDateType": EndDateTypeType,
        "Accept": bool,
        "DryRun": bool,
        "AdditionalInfo": str,
    },
    total=False,
)

class ModifyCapacityReservationRequestRequestTypeDef(
    _RequiredModifyCapacityReservationRequestRequestTypeDef,
    _OptionalModifyCapacityReservationRequestRequestTypeDef,
):
    pass

ModifyCapacityReservationResultTypeDef = TypedDict(
    "ModifyCapacityReservationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredModifyClientVpnEndpointRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalModifyClientVpnEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalModifyClientVpnEndpointRequestRequestTypeDef",
    {
        "ServerCertificateArn": str,
        "ConnectionLogOptions": "ConnectionLogOptionsTypeDef",
        "DnsServers": "DnsServersOptionsModifyStructureTypeDef",
        "VpnPort": int,
        "Description": str,
        "SplitTunnel": bool,
        "DryRun": bool,
        "SecurityGroupIds": List[str],
        "VpcId": str,
        "SelfServicePortal": SelfServicePortalType,
        "ClientConnectOptions": "ClientConnectOptionsTypeDef",
        "SessionTimeoutHours": int,
        "ClientLoginBannerOptions": "ClientLoginBannerOptionsTypeDef",
    },
    total=False,
)

class ModifyClientVpnEndpointRequestRequestTypeDef(
    _RequiredModifyClientVpnEndpointRequestRequestTypeDef,
    _OptionalModifyClientVpnEndpointRequestRequestTypeDef,
):
    pass

ModifyClientVpnEndpointResultTypeDef = TypedDict(
    "ModifyClientVpnEndpointResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyDefaultCreditSpecificationRequestRequestTypeDef = TypedDict(
    "_RequiredModifyDefaultCreditSpecificationRequestRequestTypeDef",
    {
        "InstanceFamily": UnlimitedSupportedInstanceFamilyType,
        "CpuCredits": str,
    },
)
_OptionalModifyDefaultCreditSpecificationRequestRequestTypeDef = TypedDict(
    "_OptionalModifyDefaultCreditSpecificationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ModifyDefaultCreditSpecificationRequestRequestTypeDef(
    _RequiredModifyDefaultCreditSpecificationRequestRequestTypeDef,
    _OptionalModifyDefaultCreditSpecificationRequestRequestTypeDef,
):
    pass

ModifyDefaultCreditSpecificationResultTypeDef = TypedDict(
    "ModifyDefaultCreditSpecificationResultTypeDef",
    {
        "InstanceFamilyCreditSpecification": "InstanceFamilyCreditSpecificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "_RequiredModifyEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "KmsKeyId": str,
    },
)
_OptionalModifyEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "_OptionalModifyEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ModifyEbsDefaultKmsKeyIdRequestRequestTypeDef(
    _RequiredModifyEbsDefaultKmsKeyIdRequestRequestTypeDef,
    _OptionalModifyEbsDefaultKmsKeyIdRequestRequestTypeDef,
):
    pass

ModifyEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "ModifyEbsDefaultKmsKeyIdResultTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyFleetRequestRequestTypeDef = TypedDict(
    "_RequiredModifyFleetRequestRequestTypeDef",
    {
        "FleetId": str,
    },
)
_OptionalModifyFleetRequestRequestTypeDef = TypedDict(
    "_OptionalModifyFleetRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ExcessCapacityTerminationPolicy": FleetExcessCapacityTerminationPolicyType,
        "LaunchTemplateConfigs": List["FleetLaunchTemplateConfigRequestTypeDef"],
        "TargetCapacitySpecification": "TargetCapacitySpecificationRequestTypeDef",
        "Context": str,
    },
    total=False,
)

class ModifyFleetRequestRequestTypeDef(
    _RequiredModifyFleetRequestRequestTypeDef, _OptionalModifyFleetRequestRequestTypeDef
):
    pass

ModifyFleetResultTypeDef = TypedDict(
    "ModifyFleetResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyFpgaImageAttributeRequestRequestTypeDef",
    {
        "FpgaImageId": str,
    },
)
_OptionalModifyFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyFpgaImageAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Attribute": FpgaImageAttributeNameType,
        "OperationType": OperationTypeType,
        "UserIds": List[str],
        "UserGroups": List[str],
        "ProductCodes": List[str],
        "LoadPermission": "LoadPermissionModificationsTypeDef",
        "Description": str,
        "Name": str,
    },
    total=False,
)

class ModifyFpgaImageAttributeRequestRequestTypeDef(
    _RequiredModifyFpgaImageAttributeRequestRequestTypeDef,
    _OptionalModifyFpgaImageAttributeRequestRequestTypeDef,
):
    pass

ModifyFpgaImageAttributeResultTypeDef = TypedDict(
    "ModifyFpgaImageAttributeResultTypeDef",
    {
        "FpgaImageAttribute": "FpgaImageAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyHostsRequestRequestTypeDef = TypedDict(
    "_RequiredModifyHostsRequestRequestTypeDef",
    {
        "HostIds": List[str],
    },
)
_OptionalModifyHostsRequestRequestTypeDef = TypedDict(
    "_OptionalModifyHostsRequestRequestTypeDef",
    {
        "AutoPlacement": AutoPlacementType,
        "HostRecovery": HostRecoveryType,
        "InstanceType": str,
        "InstanceFamily": str,
        "HostMaintenance": HostMaintenanceType,
    },
    total=False,
)

class ModifyHostsRequestRequestTypeDef(
    _RequiredModifyHostsRequestRequestTypeDef, _OptionalModifyHostsRequestRequestTypeDef
):
    pass

ModifyHostsResultTypeDef = TypedDict(
    "ModifyHostsResultTypeDef",
    {
        "Successful": List[str],
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyIdFormatRequestRequestTypeDef = TypedDict(
    "ModifyIdFormatRequestRequestTypeDef",
    {
        "Resource": str,
        "UseLongIds": bool,
    },
)

ModifyIdentityIdFormatRequestRequestTypeDef = TypedDict(
    "ModifyIdentityIdFormatRequestRequestTypeDef",
    {
        "PrincipalArn": str,
        "Resource": str,
        "UseLongIds": bool,
    },
)

ModifyImageAttributeRequestImageTypeDef = TypedDict(
    "ModifyImageAttributeRequestImageTypeDef",
    {
        "Attribute": str,
        "Description": "AttributeValueTypeDef",
        "LaunchPermission": "LaunchPermissionModificationsTypeDef",
        "OperationType": OperationTypeType,
        "ProductCodes": List[str],
        "UserGroups": List[str],
        "UserIds": List[str],
        "Value": str,
        "DryRun": bool,
        "OrganizationArns": List[str],
        "OrganizationalUnitArns": List[str],
        "ImdsSupport": "AttributeValueTypeDef",
    },
    total=False,
)

_RequiredModifyImageAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyImageAttributeRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalModifyImageAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyImageAttributeRequestRequestTypeDef",
    {
        "Attribute": str,
        "Description": "AttributeValueTypeDef",
        "LaunchPermission": "LaunchPermissionModificationsTypeDef",
        "OperationType": OperationTypeType,
        "ProductCodes": List[str],
        "UserGroups": List[str],
        "UserIds": List[str],
        "Value": str,
        "DryRun": bool,
        "OrganizationArns": List[str],
        "OrganizationalUnitArns": List[str],
        "ImdsSupport": "AttributeValueTypeDef",
    },
    total=False,
)

class ModifyImageAttributeRequestRequestTypeDef(
    _RequiredModifyImageAttributeRequestRequestTypeDef,
    _OptionalModifyImageAttributeRequestRequestTypeDef,
):
    pass

ModifyInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "ModifyInstanceAttributeRequestInstanceTypeDef",
    {
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "Attribute": InstanceAttributeNameType,
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingSpecificationTypeDef"],
        "DisableApiTermination": "AttributeBooleanValueTypeDef",
        "DryRun": bool,
        "EbsOptimized": "AttributeBooleanValueTypeDef",
        "EnaSupport": "AttributeBooleanValueTypeDef",
        "Groups": List[str],
        "InstanceInitiatedShutdownBehavior": "AttributeValueTypeDef",
        "InstanceType": "AttributeValueTypeDef",
        "Kernel": "AttributeValueTypeDef",
        "Ramdisk": "AttributeValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "UserData": "BlobAttributeValueTypeDef",
        "Value": str,
        "DisableApiStop": "AttributeBooleanValueTypeDef",
    },
    total=False,
)

_RequiredModifyInstanceAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceAttributeRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalModifyInstanceAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceAttributeRequestRequestTypeDef",
    {
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "Attribute": InstanceAttributeNameType,
        "BlockDeviceMappings": List["InstanceBlockDeviceMappingSpecificationTypeDef"],
        "DisableApiTermination": "AttributeBooleanValueTypeDef",
        "DryRun": bool,
        "EbsOptimized": "AttributeBooleanValueTypeDef",
        "EnaSupport": "AttributeBooleanValueTypeDef",
        "Groups": List[str],
        "InstanceInitiatedShutdownBehavior": "AttributeValueTypeDef",
        "InstanceType": "AttributeValueTypeDef",
        "Kernel": "AttributeValueTypeDef",
        "Ramdisk": "AttributeValueTypeDef",
        "SriovNetSupport": "AttributeValueTypeDef",
        "UserData": "BlobAttributeValueTypeDef",
        "Value": str,
        "DisableApiStop": "AttributeBooleanValueTypeDef",
    },
    total=False,
)

class ModifyInstanceAttributeRequestRequestTypeDef(
    _RequiredModifyInstanceAttributeRequestRequestTypeDef,
    _OptionalModifyInstanceAttributeRequestRequestTypeDef,
):
    pass

_RequiredModifyInstanceCapacityReservationAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceCapacityReservationAttributesRequestRequestTypeDef",
    {
        "InstanceId": str,
        "CapacityReservationSpecification": "CapacityReservationSpecificationTypeDef",
    },
)
_OptionalModifyInstanceCapacityReservationAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceCapacityReservationAttributesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ModifyInstanceCapacityReservationAttributesRequestRequestTypeDef(
    _RequiredModifyInstanceCapacityReservationAttributesRequestRequestTypeDef,
    _OptionalModifyInstanceCapacityReservationAttributesRequestRequestTypeDef,
):
    pass

ModifyInstanceCapacityReservationAttributesResultTypeDef = TypedDict(
    "ModifyInstanceCapacityReservationAttributesResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstanceCreditSpecificationRequestRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceCreditSpecificationRequestRequestTypeDef",
    {
        "InstanceCreditSpecifications": List["InstanceCreditSpecificationRequestTypeDef"],
    },
)
_OptionalModifyInstanceCreditSpecificationRequestRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceCreditSpecificationRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

class ModifyInstanceCreditSpecificationRequestRequestTypeDef(
    _RequiredModifyInstanceCreditSpecificationRequestRequestTypeDef,
    _OptionalModifyInstanceCreditSpecificationRequestRequestTypeDef,
):
    pass

ModifyInstanceCreditSpecificationResultTypeDef = TypedDict(
    "ModifyInstanceCreditSpecificationResultTypeDef",
    {
        "SuccessfulInstanceCreditSpecifications": List[
            "SuccessfulInstanceCreditSpecificationItemTypeDef"
        ],
        "UnsuccessfulInstanceCreditSpecifications": List[
            "UnsuccessfulInstanceCreditSpecificationItemTypeDef"
        ],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstanceEventStartTimeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceEventStartTimeRequestRequestTypeDef",
    {
        "InstanceId": str,
        "InstanceEventId": str,
        "NotBefore": Union[datetime, str],
    },
)
_OptionalModifyInstanceEventStartTimeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceEventStartTimeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ModifyInstanceEventStartTimeRequestRequestTypeDef(
    _RequiredModifyInstanceEventStartTimeRequestRequestTypeDef,
    _OptionalModifyInstanceEventStartTimeRequestRequestTypeDef,
):
    pass

ModifyInstanceEventStartTimeResultTypeDef = TypedDict(
    "ModifyInstanceEventStartTimeResultTypeDef",
    {
        "Event": "InstanceStatusEventTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceEventWindowRequestRequestTypeDef",
    {
        "InstanceEventWindowId": str,
    },
)
_OptionalModifyInstanceEventWindowRequestRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceEventWindowRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Name": str,
        "TimeRanges": List["InstanceEventWindowTimeRangeRequestTypeDef"],
        "CronExpression": str,
    },
    total=False,
)

class ModifyInstanceEventWindowRequestRequestTypeDef(
    _RequiredModifyInstanceEventWindowRequestRequestTypeDef,
    _OptionalModifyInstanceEventWindowRequestRequestTypeDef,
):
    pass

ModifyInstanceEventWindowResultTypeDef = TypedDict(
    "ModifyInstanceEventWindowResultTypeDef",
    {
        "InstanceEventWindow": "InstanceEventWindowTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstanceMaintenanceOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceMaintenanceOptionsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalModifyInstanceMaintenanceOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceMaintenanceOptionsRequestRequestTypeDef",
    {
        "AutoRecovery": InstanceAutoRecoveryStateType,
        "DryRun": bool,
    },
    total=False,
)

class ModifyInstanceMaintenanceOptionsRequestRequestTypeDef(
    _RequiredModifyInstanceMaintenanceOptionsRequestRequestTypeDef,
    _OptionalModifyInstanceMaintenanceOptionsRequestRequestTypeDef,
):
    pass

ModifyInstanceMaintenanceOptionsResultTypeDef = TypedDict(
    "ModifyInstanceMaintenanceOptionsResultTypeDef",
    {
        "InstanceId": str,
        "AutoRecovery": InstanceAutoRecoveryStateType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstanceMetadataOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredModifyInstanceMetadataOptionsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalModifyInstanceMetadataOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalModifyInstanceMetadataOptionsRequestRequestTypeDef",
    {
        "HttpTokens": HttpTokensStateType,
        "HttpPutResponseHopLimit": int,
        "HttpEndpoint": InstanceMetadataEndpointStateType,
        "DryRun": bool,
        "HttpProtocolIpv6": InstanceMetadataProtocolStateType,
        "InstanceMetadataTags": InstanceMetadataTagsStateType,
    },
    total=False,
)

class ModifyInstanceMetadataOptionsRequestRequestTypeDef(
    _RequiredModifyInstanceMetadataOptionsRequestRequestTypeDef,
    _OptionalModifyInstanceMetadataOptionsRequestRequestTypeDef,
):
    pass

ModifyInstanceMetadataOptionsResultTypeDef = TypedDict(
    "ModifyInstanceMetadataOptionsResultTypeDef",
    {
        "InstanceId": str,
        "InstanceMetadataOptions": "InstanceMetadataOptionsResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyInstancePlacementRequestRequestTypeDef = TypedDict(
    "_RequiredModifyInstancePlacementRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalModifyInstancePlacementRequestRequestTypeDef = TypedDict(
    "_OptionalModifyInstancePlacementRequestRequestTypeDef",
    {
        "Affinity": AffinityType,
        "GroupName": str,
        "HostId": str,
        "Tenancy": HostTenancyType,
        "PartitionNumber": int,
        "HostResourceGroupArn": str,
        "GroupId": str,
    },
    total=False,
)

class ModifyInstancePlacementRequestRequestTypeDef(
    _RequiredModifyInstancePlacementRequestRequestTypeDef,
    _OptionalModifyInstancePlacementRequestRequestTypeDef,
):
    pass

ModifyInstancePlacementResultTypeDef = TypedDict(
    "ModifyInstancePlacementResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyIpamPoolRequestRequestTypeDef = TypedDict(
    "_RequiredModifyIpamPoolRequestRequestTypeDef",
    {
        "IpamPoolId": str,
    },
)
_OptionalModifyIpamPoolRequestRequestTypeDef = TypedDict(
    "_OptionalModifyIpamPoolRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Description": str,
        "AutoImport": bool,
        "AllocationMinNetmaskLength": int,
        "AllocationMaxNetmaskLength": int,
        "AllocationDefaultNetmaskLength": int,
        "ClearAllocationDefaultNetmaskLength": bool,
        "AddAllocationResourceTags": List["RequestIpamResourceTagTypeDef"],
        "RemoveAllocationResourceTags": List["RequestIpamResourceTagTypeDef"],
    },
    total=False,
)

class ModifyIpamPoolRequestRequestTypeDef(
    _RequiredModifyIpamPoolRequestRequestTypeDef, _OptionalModifyIpamPoolRequestRequestTypeDef
):
    pass

ModifyIpamPoolResultTypeDef = TypedDict(
    "ModifyIpamPoolResultTypeDef",
    {
        "IpamPool": "IpamPoolTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyIpamRequestRequestTypeDef = TypedDict(
    "_RequiredModifyIpamRequestRequestTypeDef",
    {
        "IpamId": str,
    },
)
_OptionalModifyIpamRequestRequestTypeDef = TypedDict(
    "_OptionalModifyIpamRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Description": str,
        "AddOperatingRegions": List["AddIpamOperatingRegionTypeDef"],
        "RemoveOperatingRegions": List["RemoveIpamOperatingRegionTypeDef"],
    },
    total=False,
)

class ModifyIpamRequestRequestTypeDef(
    _RequiredModifyIpamRequestRequestTypeDef, _OptionalModifyIpamRequestRequestTypeDef
):
    pass

_RequiredModifyIpamResourceCidrRequestRequestTypeDef = TypedDict(
    "_RequiredModifyIpamResourceCidrRequestRequestTypeDef",
    {
        "ResourceId": str,
        "ResourceCidr": str,
        "ResourceRegion": str,
        "CurrentIpamScopeId": str,
        "Monitored": bool,
    },
)
_OptionalModifyIpamResourceCidrRequestRequestTypeDef = TypedDict(
    "_OptionalModifyIpamResourceCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
        "DestinationIpamScopeId": str,
    },
    total=False,
)

class ModifyIpamResourceCidrRequestRequestTypeDef(
    _RequiredModifyIpamResourceCidrRequestRequestTypeDef,
    _OptionalModifyIpamResourceCidrRequestRequestTypeDef,
):
    pass

ModifyIpamResourceCidrResultTypeDef = TypedDict(
    "ModifyIpamResourceCidrResultTypeDef",
    {
        "IpamResourceCidr": "IpamResourceCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "_RequiredModifyIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "IpamResourceDiscoveryId": str,
    },
)
_OptionalModifyIpamResourceDiscoveryRequestRequestTypeDef = TypedDict(
    "_OptionalModifyIpamResourceDiscoveryRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Description": str,
        "AddOperatingRegions": List["AddIpamOperatingRegionTypeDef"],
        "RemoveOperatingRegions": List["RemoveIpamOperatingRegionTypeDef"],
    },
    total=False,
)

class ModifyIpamResourceDiscoveryRequestRequestTypeDef(
    _RequiredModifyIpamResourceDiscoveryRequestRequestTypeDef,
    _OptionalModifyIpamResourceDiscoveryRequestRequestTypeDef,
):
    pass

ModifyIpamResourceDiscoveryResultTypeDef = TypedDict(
    "ModifyIpamResourceDiscoveryResultTypeDef",
    {
        "IpamResourceDiscovery": "IpamResourceDiscoveryTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyIpamResultTypeDef = TypedDict(
    "ModifyIpamResultTypeDef",
    {
        "Ipam": "IpamTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyIpamScopeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyIpamScopeRequestRequestTypeDef",
    {
        "IpamScopeId": str,
    },
)
_OptionalModifyIpamScopeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyIpamScopeRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Description": str,
    },
    total=False,
)

class ModifyIpamScopeRequestRequestTypeDef(
    _RequiredModifyIpamScopeRequestRequestTypeDef, _OptionalModifyIpamScopeRequestRequestTypeDef
):
    pass

ModifyIpamScopeResultTypeDef = TypedDict(
    "ModifyIpamScopeResultTypeDef",
    {
        "IpamScope": "IpamScopeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyLaunchTemplateRequestRequestTypeDef = TypedDict(
    "ModifyLaunchTemplateRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
        "LaunchTemplateId": str,
        "LaunchTemplateName": str,
        "DefaultVersion": str,
    },
    total=False,
)

ModifyLaunchTemplateResultTypeDef = TypedDict(
    "ModifyLaunchTemplateResultTypeDef",
    {
        "LaunchTemplate": "LaunchTemplateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "_RequiredModifyLocalGatewayRouteRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
    },
)
_OptionalModifyLocalGatewayRouteRequestRequestTypeDef = TypedDict(
    "_OptionalModifyLocalGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "LocalGatewayVirtualInterfaceGroupId": str,
        "NetworkInterfaceId": str,
        "DryRun": bool,
        "DestinationPrefixListId": str,
    },
    total=False,
)

class ModifyLocalGatewayRouteRequestRequestTypeDef(
    _RequiredModifyLocalGatewayRouteRequestRequestTypeDef,
    _OptionalModifyLocalGatewayRouteRequestRequestTypeDef,
):
    pass

ModifyLocalGatewayRouteResultTypeDef = TypedDict(
    "ModifyLocalGatewayRouteResultTypeDef",
    {
        "Route": "LocalGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyManagedPrefixListRequestRequestTypeDef = TypedDict(
    "_RequiredModifyManagedPrefixListRequestRequestTypeDef",
    {
        "PrefixListId": str,
    },
)
_OptionalModifyManagedPrefixListRequestRequestTypeDef = TypedDict(
    "_OptionalModifyManagedPrefixListRequestRequestTypeDef",
    {
        "DryRun": bool,
        "CurrentVersion": int,
        "PrefixListName": str,
        "AddEntries": List["AddPrefixListEntryTypeDef"],
        "RemoveEntries": List["RemovePrefixListEntryTypeDef"],
        "MaxEntries": int,
    },
    total=False,
)

class ModifyManagedPrefixListRequestRequestTypeDef(
    _RequiredModifyManagedPrefixListRequestRequestTypeDef,
    _OptionalModifyManagedPrefixListRequestRequestTypeDef,
):
    pass

ModifyManagedPrefixListResultTypeDef = TypedDict(
    "ModifyManagedPrefixListResultTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef = TypedDict(
    "ModifyNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    {
        "Attachment": "NetworkInterfaceAttachmentChangesTypeDef",
        "Description": "AttributeValueTypeDef",
        "DryRun": bool,
        "Groups": List[str],
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "EnaSrdSpecification": "EnaSrdSpecificationTypeDef",
        "EnablePrimaryIpv6": bool,
    },
    total=False,
)

_RequiredModifyNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalModifyNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "Attachment": "NetworkInterfaceAttachmentChangesTypeDef",
        "Description": "AttributeValueTypeDef",
        "DryRun": bool,
        "Groups": List[str],
        "SourceDestCheck": "AttributeBooleanValueTypeDef",
        "EnaSrdSpecification": "EnaSrdSpecificationTypeDef",
        "EnablePrimaryIpv6": bool,
    },
    total=False,
)

class ModifyNetworkInterfaceAttributeRequestRequestTypeDef(
    _RequiredModifyNetworkInterfaceAttributeRequestRequestTypeDef,
    _OptionalModifyNetworkInterfaceAttributeRequestRequestTypeDef,
):
    pass

_RequiredModifyPrivateDnsNameOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredModifyPrivateDnsNameOptionsRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalModifyPrivateDnsNameOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalModifyPrivateDnsNameOptionsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "PrivateDnsHostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
    },
    total=False,
)

class ModifyPrivateDnsNameOptionsRequestRequestTypeDef(
    _RequiredModifyPrivateDnsNameOptionsRequestRequestTypeDef,
    _OptionalModifyPrivateDnsNameOptionsRequestRequestTypeDef,
):
    pass

ModifyPrivateDnsNameOptionsResultTypeDef = TypedDict(
    "ModifyPrivateDnsNameOptionsResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyReservedInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredModifyReservedInstancesRequestRequestTypeDef",
    {
        "ReservedInstancesIds": List[str],
        "TargetConfigurations": List["ReservedInstancesConfigurationTypeDef"],
    },
)
_OptionalModifyReservedInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalModifyReservedInstancesRequestRequestTypeDef",
    {
        "ClientToken": str,
    },
    total=False,
)

class ModifyReservedInstancesRequestRequestTypeDef(
    _RequiredModifyReservedInstancesRequestRequestTypeDef,
    _OptionalModifyReservedInstancesRequestRequestTypeDef,
):
    pass

ModifyReservedInstancesResultTypeDef = TypedDict(
    "ModifyReservedInstancesResultTypeDef",
    {
        "ReservedInstancesModificationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifySecurityGroupRulesRequestRequestTypeDef = TypedDict(
    "_RequiredModifySecurityGroupRulesRequestRequestTypeDef",
    {
        "GroupId": str,
        "SecurityGroupRules": List["SecurityGroupRuleUpdateTypeDef"],
    },
)
_OptionalModifySecurityGroupRulesRequestRequestTypeDef = TypedDict(
    "_OptionalModifySecurityGroupRulesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ModifySecurityGroupRulesRequestRequestTypeDef(
    _RequiredModifySecurityGroupRulesRequestRequestTypeDef,
    _OptionalModifySecurityGroupRulesRequestRequestTypeDef,
):
    pass

ModifySecurityGroupRulesResultTypeDef = TypedDict(
    "ModifySecurityGroupRulesResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifySnapshotAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredModifySnapshotAttributeRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalModifySnapshotAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalModifySnapshotAttributeRequestRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "CreateVolumePermission": "CreateVolumePermissionModificationsTypeDef",
        "GroupNames": List[str],
        "OperationType": OperationTypeType,
        "UserIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

class ModifySnapshotAttributeRequestRequestTypeDef(
    _RequiredModifySnapshotAttributeRequestRequestTypeDef,
    _OptionalModifySnapshotAttributeRequestRequestTypeDef,
):
    pass

ModifySnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "ModifySnapshotAttributeRequestSnapshotTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "CreateVolumePermission": "CreateVolumePermissionModificationsTypeDef",
        "GroupNames": List[str],
        "OperationType": OperationTypeType,
        "UserIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

_RequiredModifySnapshotTierRequestRequestTypeDef = TypedDict(
    "_RequiredModifySnapshotTierRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalModifySnapshotTierRequestRequestTypeDef = TypedDict(
    "_OptionalModifySnapshotTierRequestRequestTypeDef",
    {
        "StorageTier": Literal["archive"],
        "DryRun": bool,
    },
    total=False,
)

class ModifySnapshotTierRequestRequestTypeDef(
    _RequiredModifySnapshotTierRequestRequestTypeDef,
    _OptionalModifySnapshotTierRequestRequestTypeDef,
):
    pass

ModifySnapshotTierResultTypeDef = TypedDict(
    "ModifySnapshotTierResultTypeDef",
    {
        "SnapshotId": str,
        "TieringStartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifySpotFleetRequestRequestRequestTypeDef = TypedDict(
    "_RequiredModifySpotFleetRequestRequestRequestTypeDef",
    {
        "SpotFleetRequestId": str,
    },
)
_OptionalModifySpotFleetRequestRequestRequestTypeDef = TypedDict(
    "_OptionalModifySpotFleetRequestRequestRequestTypeDef",
    {
        "ExcessCapacityTerminationPolicy": ExcessCapacityTerminationPolicyType,
        "LaunchTemplateConfigs": List["LaunchTemplateConfigTypeDef"],
        "TargetCapacity": int,
        "OnDemandTargetCapacity": int,
        "Context": str,
    },
    total=False,
)

class ModifySpotFleetRequestRequestRequestTypeDef(
    _RequiredModifySpotFleetRequestRequestRequestTypeDef,
    _OptionalModifySpotFleetRequestRequestRequestTypeDef,
):
    pass

ModifySpotFleetRequestResponseTypeDef = TypedDict(
    "ModifySpotFleetRequestResponseTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifySubnetAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredModifySubnetAttributeRequestRequestTypeDef",
    {
        "SubnetId": str,
    },
)
_OptionalModifySubnetAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalModifySubnetAttributeRequestRequestTypeDef",
    {
        "AssignIpv6AddressOnCreation": "AttributeBooleanValueTypeDef",
        "MapPublicIpOnLaunch": "AttributeBooleanValueTypeDef",
        "MapCustomerOwnedIpOnLaunch": "AttributeBooleanValueTypeDef",
        "CustomerOwnedIpv4Pool": str,
        "EnableDns64": "AttributeBooleanValueTypeDef",
        "PrivateDnsHostnameTypeOnLaunch": HostnameTypeType,
        "EnableResourceNameDnsARecordOnLaunch": "AttributeBooleanValueTypeDef",
        "EnableResourceNameDnsAAAARecordOnLaunch": "AttributeBooleanValueTypeDef",
        "EnableLniAtDeviceIndex": int,
        "DisableLniAtDeviceIndex": "AttributeBooleanValueTypeDef",
    },
    total=False,
)

class ModifySubnetAttributeRequestRequestTypeDef(
    _RequiredModifySubnetAttributeRequestRequestTypeDef,
    _OptionalModifySubnetAttributeRequestRequestTypeDef,
):
    pass

_RequiredModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef = TypedDict(
    "_RequiredModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef",
    {
        "TrafficMirrorFilterId": str,
    },
)
_OptionalModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef = TypedDict(
    "_OptionalModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef",
    {
        "AddNetworkServices": List[Literal["amazon-dns"]],
        "RemoveNetworkServices": List[Literal["amazon-dns"]],
        "DryRun": bool,
    },
    total=False,
)

class ModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef(
    _RequiredModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef,
    _OptionalModifyTrafficMirrorFilterNetworkServicesRequestRequestTypeDef,
):
    pass

ModifyTrafficMirrorFilterNetworkServicesResultTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterNetworkServicesResultTypeDef",
    {
        "TrafficMirrorFilter": "TrafficMirrorFilterTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "_RequiredModifyTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
    },
)
_OptionalModifyTrafficMirrorFilterRuleRequestRequestTypeDef = TypedDict(
    "_OptionalModifyTrafficMirrorFilterRuleRequestRequestTypeDef",
    {
        "TrafficDirection": TrafficDirectionType,
        "RuleNumber": int,
        "RuleAction": TrafficMirrorRuleActionType,
        "DestinationPortRange": "TrafficMirrorPortRangeRequestTypeDef",
        "SourcePortRange": "TrafficMirrorPortRangeRequestTypeDef",
        "Protocol": int,
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
        "Description": str,
        "RemoveFields": List[TrafficMirrorFilterRuleFieldType],
        "DryRun": bool,
    },
    total=False,
)

class ModifyTrafficMirrorFilterRuleRequestRequestTypeDef(
    _RequiredModifyTrafficMirrorFilterRuleRequestRequestTypeDef,
    _OptionalModifyTrafficMirrorFilterRuleRequestRequestTypeDef,
):
    pass

ModifyTrafficMirrorFilterRuleResultTypeDef = TypedDict(
    "ModifyTrafficMirrorFilterRuleResultTypeDef",
    {
        "TrafficMirrorFilterRule": "TrafficMirrorFilterRuleTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "_RequiredModifyTrafficMirrorSessionRequestRequestTypeDef",
    {
        "TrafficMirrorSessionId": str,
    },
)
_OptionalModifyTrafficMirrorSessionRequestRequestTypeDef = TypedDict(
    "_OptionalModifyTrafficMirrorSessionRequestRequestTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "TrafficMirrorFilterId": str,
        "PacketLength": int,
        "SessionNumber": int,
        "VirtualNetworkId": int,
        "Description": str,
        "RemoveFields": List[TrafficMirrorSessionFieldType],
        "DryRun": bool,
    },
    total=False,
)

class ModifyTrafficMirrorSessionRequestRequestTypeDef(
    _RequiredModifyTrafficMirrorSessionRequestRequestTypeDef,
    _OptionalModifyTrafficMirrorSessionRequestRequestTypeDef,
):
    pass

ModifyTrafficMirrorSessionResultTypeDef = TypedDict(
    "ModifyTrafficMirrorSessionResultTypeDef",
    {
        "TrafficMirrorSession": "TrafficMirrorSessionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTransitGatewayOptionsTypeDef = TypedDict(
    "ModifyTransitGatewayOptionsTypeDef",
    {
        "AddTransitGatewayCidrBlocks": List[str],
        "RemoveTransitGatewayCidrBlocks": List[str],
        "VpnEcmpSupport": VpnEcmpSupportValueType,
        "DnsSupport": DnsSupportValueType,
        "AutoAcceptSharedAttachments": AutoAcceptSharedAttachmentsValueType,
        "DefaultRouteTableAssociation": DefaultRouteTableAssociationValueType,
        "AssociationDefaultRouteTableId": str,
        "DefaultRouteTablePropagation": DefaultRouteTablePropagationValueType,
        "PropagationDefaultRouteTableId": str,
        "AmazonSideAsn": int,
    },
    total=False,
)

_RequiredModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "_RequiredModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
    },
)
_OptionalModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef = TypedDict(
    "_OptionalModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Blackhole": bool,
        "DryRun": bool,
    },
    total=False,
)

class ModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef(
    _RequiredModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef,
    _OptionalModifyTransitGatewayPrefixListReferenceRequestRequestTypeDef,
):
    pass

ModifyTransitGatewayPrefixListReferenceResultTypeDef = TypedDict(
    "ModifyTransitGatewayPrefixListReferenceResultTypeDef",
    {
        "TransitGatewayPrefixListReference": "TransitGatewayPrefixListReferenceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyTransitGatewayRequestRequestTypeDef = TypedDict(
    "_RequiredModifyTransitGatewayRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
    },
)
_OptionalModifyTransitGatewayRequestRequestTypeDef = TypedDict(
    "_OptionalModifyTransitGatewayRequestRequestTypeDef",
    {
        "Description": str,
        "Options": "ModifyTransitGatewayOptionsTypeDef",
        "DryRun": bool,
    },
    total=False,
)

class ModifyTransitGatewayRequestRequestTypeDef(
    _RequiredModifyTransitGatewayRequestRequestTypeDef,
    _OptionalModifyTransitGatewayRequestRequestTypeDef,
):
    pass

ModifyTransitGatewayResultTypeDef = TypedDict(
    "ModifyTransitGatewayResultTypeDef",
    {
        "TransitGateway": "TransitGatewayTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
    {
        "DnsSupport": DnsSupportValueType,
        "Ipv6Support": Ipv6SupportValueType,
        "ApplianceModeSupport": ApplianceModeSupportValueType,
    },
    total=False,
)

_RequiredModifyTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredModifyTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalModifyTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalModifyTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "AddSubnetIds": List[str],
        "RemoveSubnetIds": List[str],
        "Options": "ModifyTransitGatewayVpcAttachmentRequestOptionsTypeDef",
        "DryRun": bool,
    },
    total=False,
)

class ModifyTransitGatewayVpcAttachmentRequestRequestTypeDef(
    _RequiredModifyTransitGatewayVpcAttachmentRequestRequestTypeDef,
    _OptionalModifyTransitGatewayVpcAttachmentRequestRequestTypeDef,
):
    pass

ModifyTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "ModifyTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVerifiedAccessEndpointEniOptionsTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointEniOptionsTypeDef",
    {
        "Protocol": VerifiedAccessEndpointProtocolType,
        "Port": int,
    },
    total=False,
)

ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    {
        "SubnetIds": List[str],
        "Protocol": VerifiedAccessEndpointProtocolType,
        "Port": int,
    },
    total=False,
)

_RequiredModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointId": str,
    },
)
_OptionalModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "ClientToken": str,
        "DryRun": bool,
        "SseSpecification": "VerifiedAccessSseSpecificationRequestTypeDef",
    },
    total=False,
)

class ModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef(
    _RequiredModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef,
    _OptionalModifyVerifiedAccessEndpointPolicyRequestRequestTypeDef,
):
    pass

ModifyVerifiedAccessEndpointPolicyResultTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointPolicyResultTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "SseSpecification": "VerifiedAccessSseSpecificationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVerifiedAccessEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVerifiedAccessEndpointRequestRequestTypeDef",
    {
        "VerifiedAccessEndpointId": str,
    },
)
_OptionalModifyVerifiedAccessEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVerifiedAccessEndpointRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
        "LoadBalancerOptions": "ModifyVerifiedAccessEndpointLoadBalancerOptionsTypeDef",
        "NetworkInterfaceOptions": "ModifyVerifiedAccessEndpointEniOptionsTypeDef",
        "Description": str,
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class ModifyVerifiedAccessEndpointRequestRequestTypeDef(
    _RequiredModifyVerifiedAccessEndpointRequestRequestTypeDef,
    _OptionalModifyVerifiedAccessEndpointRequestRequestTypeDef,
):
    pass

ModifyVerifiedAccessEndpointResultTypeDef = TypedDict(
    "ModifyVerifiedAccessEndpointResultTypeDef",
    {
        "VerifiedAccessEndpoint": "VerifiedAccessEndpointTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVerifiedAccessGroupPolicyRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVerifiedAccessGroupPolicyRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
    },
)
_OptionalModifyVerifiedAccessGroupPolicyRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVerifiedAccessGroupPolicyRequestRequestTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "ClientToken": str,
        "DryRun": bool,
        "SseSpecification": "VerifiedAccessSseSpecificationRequestTypeDef",
    },
    total=False,
)

class ModifyVerifiedAccessGroupPolicyRequestRequestTypeDef(
    _RequiredModifyVerifiedAccessGroupPolicyRequestRequestTypeDef,
    _OptionalModifyVerifiedAccessGroupPolicyRequestRequestTypeDef,
):
    pass

ModifyVerifiedAccessGroupPolicyResultTypeDef = TypedDict(
    "ModifyVerifiedAccessGroupPolicyResultTypeDef",
    {
        "PolicyEnabled": bool,
        "PolicyDocument": str,
        "SseSpecification": "VerifiedAccessSseSpecificationResponseTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVerifiedAccessGroupRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVerifiedAccessGroupRequestRequestTypeDef",
    {
        "VerifiedAccessGroupId": str,
    },
)
_OptionalModifyVerifiedAccessGroupRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVerifiedAccessGroupRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "Description": str,
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class ModifyVerifiedAccessGroupRequestRequestTypeDef(
    _RequiredModifyVerifiedAccessGroupRequestRequestTypeDef,
    _OptionalModifyVerifiedAccessGroupRequestRequestTypeDef,
):
    pass

ModifyVerifiedAccessGroupResultTypeDef = TypedDict(
    "ModifyVerifiedAccessGroupResultTypeDef",
    {
        "VerifiedAccessGroup": "VerifiedAccessGroupTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "AccessLogs": "VerifiedAccessLogOptionsTypeDef",
    },
)
_OptionalModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

class ModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef(
    _RequiredModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef,
    _OptionalModifyVerifiedAccessInstanceLoggingConfigurationRequestRequestTypeDef,
):
    pass

ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef = TypedDict(
    "ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef",
    {
        "LoggingConfiguration": "VerifiedAccessInstanceLoggingConfigurationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVerifiedAccessInstanceRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVerifiedAccessInstanceRequestRequestTypeDef",
    {
        "VerifiedAccessInstanceId": str,
    },
)
_OptionalModifyVerifiedAccessInstanceRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVerifiedAccessInstanceRequestRequestTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "ClientToken": str,
    },
    total=False,
)

class ModifyVerifiedAccessInstanceRequestRequestTypeDef(
    _RequiredModifyVerifiedAccessInstanceRequestRequestTypeDef,
    _OptionalModifyVerifiedAccessInstanceRequestRequestTypeDef,
):
    pass

ModifyVerifiedAccessInstanceResultTypeDef = TypedDict(
    "ModifyVerifiedAccessInstanceResultTypeDef",
    {
        "VerifiedAccessInstance": "VerifiedAccessInstanceTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef = TypedDict(
    "ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "Scope": str,
    },
    total=False,
)

_RequiredModifyVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "VerifiedAccessTrustProviderId": str,
    },
)
_OptionalModifyVerifiedAccessTrustProviderRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVerifiedAccessTrustProviderRequestRequestTypeDef",
    {
        "OidcOptions": "ModifyVerifiedAccessTrustProviderOidcOptionsTypeDef",
        "Description": str,
        "DryRun": bool,
        "ClientToken": str,
        "SseSpecification": "VerifiedAccessSseSpecificationRequestTypeDef",
    },
    total=False,
)

class ModifyVerifiedAccessTrustProviderRequestRequestTypeDef(
    _RequiredModifyVerifiedAccessTrustProviderRequestRequestTypeDef,
    _OptionalModifyVerifiedAccessTrustProviderRequestRequestTypeDef,
):
    pass

ModifyVerifiedAccessTrustProviderResultTypeDef = TypedDict(
    "ModifyVerifiedAccessTrustProviderResultTypeDef",
    {
        "VerifiedAccessTrustProvider": "VerifiedAccessTrustProviderTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVolumeAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVolumeAttributeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalModifyVolumeAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVolumeAttributeRequestRequestTypeDef",
    {
        "AutoEnableIO": "AttributeBooleanValueTypeDef",
        "DryRun": bool,
    },
    total=False,
)

class ModifyVolumeAttributeRequestRequestTypeDef(
    _RequiredModifyVolumeAttributeRequestRequestTypeDef,
    _OptionalModifyVolumeAttributeRequestRequestTypeDef,
):
    pass

ModifyVolumeAttributeRequestVolumeTypeDef = TypedDict(
    "ModifyVolumeAttributeRequestVolumeTypeDef",
    {
        "AutoEnableIO": "AttributeBooleanValueTypeDef",
        "DryRun": bool,
    },
    total=False,
)

_RequiredModifyVolumeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVolumeRequestRequestTypeDef",
    {
        "VolumeId": str,
    },
)
_OptionalModifyVolumeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVolumeRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Size": int,
        "VolumeType": VolumeTypeType,
        "Iops": int,
        "Throughput": int,
        "MultiAttachEnabled": bool,
    },
    total=False,
)

class ModifyVolumeRequestRequestTypeDef(
    _RequiredModifyVolumeRequestRequestTypeDef, _OptionalModifyVolumeRequestRequestTypeDef
):
    pass

ModifyVolumeResultTypeDef = TypedDict(
    "ModifyVolumeResultTypeDef",
    {
        "VolumeModification": "VolumeModificationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpcAttributeRequestRequestTypeDef",
    {
        "VpcId": str,
    },
)
_OptionalModifyVpcAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpcAttributeRequestRequestTypeDef",
    {
        "EnableDnsHostnames": "AttributeBooleanValueTypeDef",
        "EnableDnsSupport": "AttributeBooleanValueTypeDef",
        "EnableNetworkAddressUsageMetrics": "AttributeBooleanValueTypeDef",
    },
    total=False,
)

class ModifyVpcAttributeRequestRequestTypeDef(
    _RequiredModifyVpcAttributeRequestRequestTypeDef,
    _OptionalModifyVpcAttributeRequestRequestTypeDef,
):
    pass

ModifyVpcAttributeRequestVpcTypeDef = TypedDict(
    "ModifyVpcAttributeRequestVpcTypeDef",
    {
        "EnableDnsHostnames": "AttributeBooleanValueTypeDef",
        "EnableDnsSupport": "AttributeBooleanValueTypeDef",
        "EnableNetworkAddressUsageMetrics": "AttributeBooleanValueTypeDef",
    },
    total=False,
)

_RequiredModifyVpcEndpointConnectionNotificationRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpcEndpointConnectionNotificationRequestRequestTypeDef",
    {
        "ConnectionNotificationId": str,
    },
)
_OptionalModifyVpcEndpointConnectionNotificationRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpcEndpointConnectionNotificationRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ConnectionNotificationArn": str,
        "ConnectionEvents": List[str],
    },
    total=False,
)

class ModifyVpcEndpointConnectionNotificationRequestRequestTypeDef(
    _RequiredModifyVpcEndpointConnectionNotificationRequestRequestTypeDef,
    _OptionalModifyVpcEndpointConnectionNotificationRequestRequestTypeDef,
):
    pass

ModifyVpcEndpointConnectionNotificationResultTypeDef = TypedDict(
    "ModifyVpcEndpointConnectionNotificationResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcEndpointRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpcEndpointRequestRequestTypeDef",
    {
        "VpcEndpointId": str,
    },
)
_OptionalModifyVpcEndpointRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpcEndpointRequestRequestTypeDef",
    {
        "DryRun": bool,
        "ResetPolicy": bool,
        "PolicyDocument": str,
        "AddRouteTableIds": List[str],
        "RemoveRouteTableIds": List[str],
        "AddSubnetIds": List[str],
        "RemoveSubnetIds": List[str],
        "AddSecurityGroupIds": List[str],
        "RemoveSecurityGroupIds": List[str],
        "IpAddressType": IpAddressTypeType,
        "DnsOptions": "DnsOptionsSpecificationTypeDef",
        "PrivateDnsEnabled": bool,
        "SubnetConfigurations": List["SubnetConfigurationTypeDef"],
    },
    total=False,
)

class ModifyVpcEndpointRequestRequestTypeDef(
    _RequiredModifyVpcEndpointRequestRequestTypeDef, _OptionalModifyVpcEndpointRequestRequestTypeDef
):
    pass

ModifyVpcEndpointResultTypeDef = TypedDict(
    "ModifyVpcEndpointResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcEndpointServiceConfigurationRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpcEndpointServiceConfigurationRequestRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalModifyVpcEndpointServiceConfigurationRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpcEndpointServiceConfigurationRequestRequestTypeDef",
    {
        "DryRun": bool,
        "PrivateDnsName": str,
        "RemovePrivateDnsName": bool,
        "AcceptanceRequired": bool,
        "AddNetworkLoadBalancerArns": List[str],
        "RemoveNetworkLoadBalancerArns": List[str],
        "AddGatewayLoadBalancerArns": List[str],
        "RemoveGatewayLoadBalancerArns": List[str],
        "AddSupportedIpAddressTypes": List[str],
        "RemoveSupportedIpAddressTypes": List[str],
    },
    total=False,
)

class ModifyVpcEndpointServiceConfigurationRequestRequestTypeDef(
    _RequiredModifyVpcEndpointServiceConfigurationRequestRequestTypeDef,
    _OptionalModifyVpcEndpointServiceConfigurationRequestRequestTypeDef,
):
    pass

ModifyVpcEndpointServiceConfigurationResultTypeDef = TypedDict(
    "ModifyVpcEndpointServiceConfigurationResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef",
    {
        "ServiceId": str,
        "PayerResponsibility": Literal["ServiceOwner"],
    },
)
_OptionalModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef(
    _RequiredModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef,
    _OptionalModifyVpcEndpointServicePayerResponsibilityRequestRequestTypeDef,
):
    pass

ModifyVpcEndpointServicePayerResponsibilityResultTypeDef = TypedDict(
    "ModifyVpcEndpointServicePayerResponsibilityResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcEndpointServicePermissionsRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpcEndpointServicePermissionsRequestRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalModifyVpcEndpointServicePermissionsRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpcEndpointServicePermissionsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "AddAllowedPrincipals": List[str],
        "RemoveAllowedPrincipals": List[str],
    },
    total=False,
)

class ModifyVpcEndpointServicePermissionsRequestRequestTypeDef(
    _RequiredModifyVpcEndpointServicePermissionsRequestRequestTypeDef,
    _OptionalModifyVpcEndpointServicePermissionsRequestRequestTypeDef,
):
    pass

ModifyVpcEndpointServicePermissionsResultTypeDef = TypedDict(
    "ModifyVpcEndpointServicePermissionsResultTypeDef",
    {
        "AddedPrincipals": List["AddedPrincipalTypeDef"],
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcPeeringConnectionOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpcPeeringConnectionOptionsRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
    },
)
_OptionalModifyVpcPeeringConnectionOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpcPeeringConnectionOptionsRequestRequestTypeDef",
    {
        "AccepterPeeringConnectionOptions": "PeeringConnectionOptionsRequestTypeDef",
        "DryRun": bool,
        "RequesterPeeringConnectionOptions": "PeeringConnectionOptionsRequestTypeDef",
    },
    total=False,
)

class ModifyVpcPeeringConnectionOptionsRequestRequestTypeDef(
    _RequiredModifyVpcPeeringConnectionOptionsRequestRequestTypeDef,
    _OptionalModifyVpcPeeringConnectionOptionsRequestRequestTypeDef,
):
    pass

ModifyVpcPeeringConnectionOptionsResultTypeDef = TypedDict(
    "ModifyVpcPeeringConnectionOptionsResultTypeDef",
    {
        "AccepterPeeringConnectionOptions": "PeeringConnectionOptionsTypeDef",
        "RequesterPeeringConnectionOptions": "PeeringConnectionOptionsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpcTenancyRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpcTenancyRequestRequestTypeDef",
    {
        "VpcId": str,
        "InstanceTenancy": Literal["default"],
    },
)
_OptionalModifyVpcTenancyRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpcTenancyRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ModifyVpcTenancyRequestRequestTypeDef(
    _RequiredModifyVpcTenancyRequestRequestTypeDef, _OptionalModifyVpcTenancyRequestRequestTypeDef
):
    pass

ModifyVpcTenancyResultTypeDef = TypedDict(
    "ModifyVpcTenancyResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpnConnectionOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpnConnectionOptionsRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
    },
)
_OptionalModifyVpnConnectionOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpnConnectionOptionsRequestRequestTypeDef",
    {
        "LocalIpv4NetworkCidr": str,
        "RemoteIpv4NetworkCidr": str,
        "LocalIpv6NetworkCidr": str,
        "RemoteIpv6NetworkCidr": str,
        "DryRun": bool,
    },
    total=False,
)

class ModifyVpnConnectionOptionsRequestRequestTypeDef(
    _RequiredModifyVpnConnectionOptionsRequestRequestTypeDef,
    _OptionalModifyVpnConnectionOptionsRequestRequestTypeDef,
):
    pass

ModifyVpnConnectionOptionsResultTypeDef = TypedDict(
    "ModifyVpnConnectionOptionsResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpnConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpnConnectionRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
    },
)
_OptionalModifyVpnConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpnConnectionRequestRequestTypeDef",
    {
        "TransitGatewayId": str,
        "CustomerGatewayId": str,
        "VpnGatewayId": str,
        "DryRun": bool,
    },
    total=False,
)

class ModifyVpnConnectionRequestRequestTypeDef(
    _RequiredModifyVpnConnectionRequestRequestTypeDef,
    _OptionalModifyVpnConnectionRequestRequestTypeDef,
):
    pass

ModifyVpnConnectionResultTypeDef = TypedDict(
    "ModifyVpnConnectionResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpnTunnelCertificateRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpnTunnelCertificateRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
    },
)
_OptionalModifyVpnTunnelCertificateRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpnTunnelCertificateRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ModifyVpnTunnelCertificateRequestRequestTypeDef(
    _RequiredModifyVpnTunnelCertificateRequestRequestTypeDef,
    _OptionalModifyVpnTunnelCertificateRequestRequestTypeDef,
):
    pass

ModifyVpnTunnelCertificateResultTypeDef = TypedDict(
    "ModifyVpnTunnelCertificateResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredModifyVpnTunnelOptionsRequestRequestTypeDef = TypedDict(
    "_RequiredModifyVpnTunnelOptionsRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
        "TunnelOptions": "ModifyVpnTunnelOptionsSpecificationTypeDef",
    },
)
_OptionalModifyVpnTunnelOptionsRequestRequestTypeDef = TypedDict(
    "_OptionalModifyVpnTunnelOptionsRequestRequestTypeDef",
    {
        "DryRun": bool,
        "SkipTunnelReplacement": bool,
    },
    total=False,
)

class ModifyVpnTunnelOptionsRequestRequestTypeDef(
    _RequiredModifyVpnTunnelOptionsRequestRequestTypeDef,
    _OptionalModifyVpnTunnelOptionsRequestRequestTypeDef,
):
    pass

ModifyVpnTunnelOptionsResultTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsResultTypeDef",
    {
        "VpnConnection": "VpnConnectionTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ModifyVpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "ModifyVpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": str,
        "TunnelInsideIpv6Cidr": str,
        "PreSharedKey": str,
        "Phase1LifetimeSeconds": int,
        "Phase2LifetimeSeconds": int,
        "RekeyMarginTimeSeconds": int,
        "RekeyFuzzPercentage": int,
        "ReplayWindowSize": int,
        "DPDTimeoutSeconds": int,
        "DPDTimeoutAction": str,
        "Phase1EncryptionAlgorithms": List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase2EncryptionAlgorithms": List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase1IntegrityAlgorithms": List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase2IntegrityAlgorithms": List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase1DHGroupNumbers": List["Phase1DHGroupNumbersRequestListValueTypeDef"],
        "Phase2DHGroupNumbers": List["Phase2DHGroupNumbersRequestListValueTypeDef"],
        "IKEVersions": List["IKEVersionsRequestListValueTypeDef"],
        "StartupAction": str,
        "LogOptions": "VpnTunnelLogOptionsSpecificationTypeDef",
        "EnableTunnelLifecycleControl": bool,
    },
    total=False,
)

MonitorInstancesRequestInstanceTypeDef = TypedDict(
    "MonitorInstancesRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredMonitorInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredMonitorInstancesRequestRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalMonitorInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalMonitorInstancesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class MonitorInstancesRequestRequestTypeDef(
    _RequiredMonitorInstancesRequestRequestTypeDef, _OptionalMonitorInstancesRequestRequestTypeDef
):
    pass

MonitorInstancesResultTypeDef = TypedDict(
    "MonitorInstancesResultTypeDef",
    {
        "InstanceMonitorings": List["InstanceMonitoringTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MonitoringTypeDef = TypedDict(
    "MonitoringTypeDef",
    {
        "State": MonitoringStateType,
    },
    total=False,
)

_RequiredMoveAddressToVpcRequestRequestTypeDef = TypedDict(
    "_RequiredMoveAddressToVpcRequestRequestTypeDef",
    {
        "PublicIp": str,
    },
)
_OptionalMoveAddressToVpcRequestRequestTypeDef = TypedDict(
    "_OptionalMoveAddressToVpcRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class MoveAddressToVpcRequestRequestTypeDef(
    _RequiredMoveAddressToVpcRequestRequestTypeDef, _OptionalMoveAddressToVpcRequestRequestTypeDef
):
    pass

MoveAddressToVpcResultTypeDef = TypedDict(
    "MoveAddressToVpcResultTypeDef",
    {
        "AllocationId": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredMoveByoipCidrToIpamRequestRequestTypeDef = TypedDict(
    "_RequiredMoveByoipCidrToIpamRequestRequestTypeDef",
    {
        "Cidr": str,
        "IpamPoolId": str,
        "IpamPoolOwner": str,
    },
)
_OptionalMoveByoipCidrToIpamRequestRequestTypeDef = TypedDict(
    "_OptionalMoveByoipCidrToIpamRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class MoveByoipCidrToIpamRequestRequestTypeDef(
    _RequiredMoveByoipCidrToIpamRequestRequestTypeDef,
    _OptionalMoveByoipCidrToIpamRequestRequestTypeDef,
):
    pass

MoveByoipCidrToIpamResultTypeDef = TypedDict(
    "MoveByoipCidrToIpamResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

MovingAddressStatusTypeDef = TypedDict(
    "MovingAddressStatusTypeDef",
    {
        "MoveStatus": MoveStatusType,
        "PublicIp": str,
    },
    total=False,
)

NatGatewayAddressTypeDef = TypedDict(
    "NatGatewayAddressTypeDef",
    {
        "AllocationId": str,
        "NetworkInterfaceId": str,
        "PrivateIp": str,
        "PublicIp": str,
        "AssociationId": str,
        "IsPrimary": bool,
        "FailureMessage": str,
        "Status": NatGatewayAddressStatusType,
    },
    total=False,
)

NatGatewayTypeDef = TypedDict(
    "NatGatewayTypeDef",
    {
        "CreateTime": datetime,
        "DeleteTime": datetime,
        "FailureCode": str,
        "FailureMessage": str,
        "NatGatewayAddresses": List["NatGatewayAddressTypeDef"],
        "NatGatewayId": str,
        "ProvisionedBandwidth": "ProvisionedBandwidthTypeDef",
        "State": NatGatewayStateType,
        "SubnetId": str,
        "VpcId": str,
        "Tags": List["TagTypeDef"],
        "ConnectivityType": ConnectivityTypeType,
    },
    total=False,
)

NetworkAclAssociationTypeDef = TypedDict(
    "NetworkAclAssociationTypeDef",
    {
        "NetworkAclAssociationId": str,
        "NetworkAclId": str,
        "SubnetId": str,
    },
    total=False,
)

NetworkAclEntryTypeDef = TypedDict(
    "NetworkAclEntryTypeDef",
    {
        "CidrBlock": str,
        "Egress": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
    total=False,
)

NetworkAclTypeDef = TypedDict(
    "NetworkAclTypeDef",
    {
        "Associations": List["NetworkAclAssociationTypeDef"],
        "Entries": List["NetworkAclEntryTypeDef"],
        "IsDefault": bool,
        "NetworkAclId": str,
        "Tags": List["TagTypeDef"],
        "VpcId": str,
        "OwnerId": str,
    },
    total=False,
)

NetworkBandwidthGbpsRequestTypeDef = TypedDict(
    "NetworkBandwidthGbpsRequestTypeDef",
    {
        "Min": float,
        "Max": float,
    },
    total=False,
)

NetworkBandwidthGbpsTypeDef = TypedDict(
    "NetworkBandwidthGbpsTypeDef",
    {
        "Min": float,
        "Max": float,
    },
    total=False,
)

NetworkCardInfoTypeDef = TypedDict(
    "NetworkCardInfoTypeDef",
    {
        "NetworkCardIndex": int,
        "NetworkPerformance": str,
        "MaximumNetworkInterfaces": int,
        "BaselineBandwidthInGbps": float,
        "PeakBandwidthInGbps": float,
    },
    total=False,
)

NetworkInfoTypeDef = TypedDict(
    "NetworkInfoTypeDef",
    {
        "NetworkPerformance": str,
        "MaximumNetworkInterfaces": int,
        "MaximumNetworkCards": int,
        "DefaultNetworkCardIndex": int,
        "NetworkCards": List["NetworkCardInfoTypeDef"],
        "Ipv4AddressesPerInterface": int,
        "Ipv6AddressesPerInterface": int,
        "Ipv6Supported": bool,
        "EnaSupport": EnaSupportType,
        "EfaSupported": bool,
        "EfaInfo": "EfaInfoTypeDef",
        "EncryptionInTransitSupported": bool,
        "EnaSrdSupported": bool,
    },
    total=False,
)

NetworkInsightsAccessScopeAnalysisTypeDef = TypedDict(
    "NetworkInsightsAccessScopeAnalysisTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysisId": str,
        "NetworkInsightsAccessScopeAnalysisArn": str,
        "NetworkInsightsAccessScopeId": str,
        "Status": AnalysisStatusType,
        "StatusMessage": str,
        "WarningMessage": str,
        "StartDate": datetime,
        "EndDate": datetime,
        "FindingsFound": FindingsFoundType,
        "AnalyzedEniCount": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

NetworkInsightsAccessScopeContentTypeDef = TypedDict(
    "NetworkInsightsAccessScopeContentTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "MatchPaths": List["AccessScopePathTypeDef"],
        "ExcludePaths": List["AccessScopePathTypeDef"],
    },
    total=False,
)

NetworkInsightsAccessScopeTypeDef = TypedDict(
    "NetworkInsightsAccessScopeTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "NetworkInsightsAccessScopeArn": str,
        "CreatedDate": datetime,
        "UpdatedDate": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

NetworkInsightsAnalysisTypeDef = TypedDict(
    "NetworkInsightsAnalysisTypeDef",
    {
        "NetworkInsightsAnalysisId": str,
        "NetworkInsightsAnalysisArn": str,
        "NetworkInsightsPathId": str,
        "AdditionalAccounts": List[str],
        "FilterInArns": List[str],
        "StartDate": datetime,
        "Status": AnalysisStatusType,
        "StatusMessage": str,
        "WarningMessage": str,
        "NetworkPathFound": bool,
        "ForwardPathComponents": List["PathComponentTypeDef"],
        "ReturnPathComponents": List["PathComponentTypeDef"],
        "Explanations": List["ExplanationTypeDef"],
        "AlternatePathHints": List["AlternatePathHintTypeDef"],
        "SuggestedAccounts": List[str],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

NetworkInsightsPathTypeDef = TypedDict(
    "NetworkInsightsPathTypeDef",
    {
        "NetworkInsightsPathId": str,
        "NetworkInsightsPathArn": str,
        "CreatedDate": datetime,
        "Source": str,
        "Destination": str,
        "SourceArn": str,
        "DestinationArn": str,
        "SourceIp": str,
        "DestinationIp": str,
        "Protocol": ProtocolType,
        "DestinationPort": int,
        "Tags": List["TagTypeDef"],
        "FilterAtSource": "PathFilterTypeDef",
        "FilterAtDestination": "PathFilterTypeDef",
    },
    total=False,
)

NetworkInterfaceAssociationTypeDef = TypedDict(
    "NetworkInterfaceAssociationTypeDef",
    {
        "AllocationId": str,
        "AssociationId": str,
        "IpOwnerId": str,
        "PublicDnsName": str,
        "PublicIp": str,
        "CustomerOwnedIp": str,
        "CarrierIp": str,
    },
    total=False,
)

NetworkInterfaceAttachmentChangesTypeDef = TypedDict(
    "NetworkInterfaceAttachmentChangesTypeDef",
    {
        "AttachmentId": str,
        "DeleteOnTermination": bool,
    },
    total=False,
)

NetworkInterfaceAttachmentTypeDef = TypedDict(
    "NetworkInterfaceAttachmentTypeDef",
    {
        "AttachTime": datetime,
        "AttachmentId": str,
        "DeleteOnTermination": bool,
        "DeviceIndex": int,
        "NetworkCardIndex": int,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "Status": AttachmentStatusType,
        "EnaSrdSpecification": "AttachmentEnaSrdSpecificationTypeDef",
    },
    total=False,
)

NetworkInterfaceCountRequestTypeDef = TypedDict(
    "NetworkInterfaceCountRequestTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

NetworkInterfaceCountTypeDef = TypedDict(
    "NetworkInterfaceCountTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

NetworkInterfaceIpv6AddressTypeDef = TypedDict(
    "NetworkInterfaceIpv6AddressTypeDef",
    {
        "Ipv6Address": str,
        "IsPrimaryIpv6": bool,
    },
    total=False,
)

NetworkInterfacePermissionStateTypeDef = TypedDict(
    "NetworkInterfacePermissionStateTypeDef",
    {
        "State": NetworkInterfacePermissionStateCodeType,
        "StatusMessage": str,
    },
    total=False,
)

NetworkInterfacePermissionTypeDef = TypedDict(
    "NetworkInterfacePermissionTypeDef",
    {
        "NetworkInterfacePermissionId": str,
        "NetworkInterfaceId": str,
        "AwsAccountId": str,
        "AwsService": str,
        "Permission": InterfacePermissionTypeType,
        "PermissionState": "NetworkInterfacePermissionStateTypeDef",
    },
    total=False,
)

NetworkInterfacePrivateIpAddressTypeDef = TypedDict(
    "NetworkInterfacePrivateIpAddressTypeDef",
    {
        "Association": "NetworkInterfaceAssociationTypeDef",
        "Primary": bool,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Association": "NetworkInterfaceAssociationTypeDef",
        "Attachment": "NetworkInterfaceAttachmentTypeDef",
        "AvailabilityZone": str,
        "Description": str,
        "Groups": List["GroupIdentifierTypeDef"],
        "InterfaceType": NetworkInterfaceTypeType,
        "Ipv6Addresses": List["NetworkInterfaceIpv6AddressTypeDef"],
        "MacAddress": str,
        "NetworkInterfaceId": str,
        "OutpostArn": str,
        "OwnerId": str,
        "PrivateDnsName": str,
        "PrivateIpAddress": str,
        "PrivateIpAddresses": List["NetworkInterfacePrivateIpAddressTypeDef"],
        "Ipv4Prefixes": List["Ipv4PrefixSpecificationTypeDef"],
        "Ipv6Prefixes": List["Ipv6PrefixSpecificationTypeDef"],
        "RequesterId": str,
        "RequesterManaged": bool,
        "SourceDestCheck": bool,
        "Status": NetworkInterfaceStatusType,
        "SubnetId": str,
        "TagSet": List["TagTypeDef"],
        "VpcId": str,
        "DenyAllIgwTraffic": bool,
        "Ipv6Native": bool,
        "Ipv6Address": str,
    },
    total=False,
)

NewDhcpConfigurationTypeDef = TypedDict(
    "NewDhcpConfigurationTypeDef",
    {
        "Key": str,
        "Values": List[str],
    },
    total=False,
)

NitroTpmInfoTypeDef = TypedDict(
    "NitroTpmInfoTypeDef",
    {
        "SupportedVersions": List[str],
    },
    total=False,
)

OidcOptionsTypeDef = TypedDict(
    "OidcOptionsTypeDef",
    {
        "Issuer": str,
        "AuthorizationEndpoint": str,
        "TokenEndpoint": str,
        "UserInfoEndpoint": str,
        "ClientId": str,
        "ClientSecret": str,
        "Scope": str,
    },
    total=False,
)

OnDemandOptionsRequestTypeDef = TypedDict(
    "OnDemandOptionsRequestTypeDef",
    {
        "AllocationStrategy": FleetOnDemandAllocationStrategyType,
        "CapacityReservationOptions": "CapacityReservationOptionsRequestTypeDef",
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

OnDemandOptionsTypeDef = TypedDict(
    "OnDemandOptionsTypeDef",
    {
        "AllocationStrategy": FleetOnDemandAllocationStrategyType,
        "CapacityReservationOptions": "CapacityReservationOptionsTypeDef",
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

PacketHeaderStatementRequestTypeDef = TypedDict(
    "PacketHeaderStatementRequestTypeDef",
    {
        "SourceAddresses": List[str],
        "DestinationAddresses": List[str],
        "SourcePorts": List[str],
        "DestinationPorts": List[str],
        "SourcePrefixLists": List[str],
        "DestinationPrefixLists": List[str],
        "Protocols": List[ProtocolType],
    },
    total=False,
)

PacketHeaderStatementTypeDef = TypedDict(
    "PacketHeaderStatementTypeDef",
    {
        "SourceAddresses": List[str],
        "DestinationAddresses": List[str],
        "SourcePorts": List[str],
        "DestinationPorts": List[str],
        "SourcePrefixLists": List[str],
        "DestinationPrefixLists": List[str],
        "Protocols": List[ProtocolType],
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

PathComponentTypeDef = TypedDict(
    "PathComponentTypeDef",
    {
        "SequenceNumber": int,
        "AclRule": "AnalysisAclRuleTypeDef",
        "AttachedTo": "AnalysisComponentTypeDef",
        "Component": "AnalysisComponentTypeDef",
        "DestinationVpc": "AnalysisComponentTypeDef",
        "OutboundHeader": "AnalysisPacketHeaderTypeDef",
        "InboundHeader": "AnalysisPacketHeaderTypeDef",
        "RouteTableRoute": "AnalysisRouteTableRouteTypeDef",
        "SecurityGroupRule": "AnalysisSecurityGroupRuleTypeDef",
        "SourceVpc": "AnalysisComponentTypeDef",
        "Subnet": "AnalysisComponentTypeDef",
        "Vpc": "AnalysisComponentTypeDef",
        "AdditionalDetails": List["AdditionalDetailTypeDef"],
        "TransitGateway": "AnalysisComponentTypeDef",
        "TransitGatewayRouteTableRoute": "TransitGatewayRouteTableRouteTypeDef",
        "Explanations": List["ExplanationTypeDef"],
        "ElasticLoadBalancerListener": "AnalysisComponentTypeDef",
        "FirewallStatelessRule": "FirewallStatelessRuleTypeDef",
        "FirewallStatefulRule": "FirewallStatefulRuleTypeDef",
        "ServiceName": str,
    },
    total=False,
)

PathFilterTypeDef = TypedDict(
    "PathFilterTypeDef",
    {
        "SourceAddress": str,
        "SourcePortRange": "FilterPortRangeTypeDef",
        "DestinationAddress": str,
        "DestinationPortRange": "FilterPortRangeTypeDef",
    },
    total=False,
)

PathRequestFilterTypeDef = TypedDict(
    "PathRequestFilterTypeDef",
    {
        "SourceAddress": str,
        "SourcePortRange": "RequestFilterPortRangeTypeDef",
        "DestinationAddress": str,
        "DestinationPortRange": "RequestFilterPortRangeTypeDef",
    },
    total=False,
)

PathStatementRequestTypeDef = TypedDict(
    "PathStatementRequestTypeDef",
    {
        "PacketHeaderStatement": "PacketHeaderStatementRequestTypeDef",
        "ResourceStatement": "ResourceStatementRequestTypeDef",
    },
    total=False,
)

PathStatementTypeDef = TypedDict(
    "PathStatementTypeDef",
    {
        "PacketHeaderStatement": "PacketHeaderStatementTypeDef",
        "ResourceStatement": "ResourceStatementTypeDef",
    },
    total=False,
)

PciIdTypeDef = TypedDict(
    "PciIdTypeDef",
    {
        "DeviceId": str,
        "VendorId": str,
        "SubsystemId": str,
        "SubsystemVendorId": str,
    },
    total=False,
)

PeeringAttachmentStatusTypeDef = TypedDict(
    "PeeringAttachmentStatusTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

PeeringConnectionOptionsRequestTypeDef = TypedDict(
    "PeeringConnectionOptionsRequestTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

PeeringConnectionOptionsTypeDef = TypedDict(
    "PeeringConnectionOptionsTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

PeeringTgwInfoTypeDef = TypedDict(
    "PeeringTgwInfoTypeDef",
    {
        "TransitGatewayId": str,
        "CoreNetworkId": str,
        "OwnerId": str,
        "Region": str,
    },
    total=False,
)

Phase1DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersListValueTypeDef",
    {
        "Value": int,
    },
    total=False,
)

Phase1DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase1DHGroupNumbersRequestListValueTypeDef",
    {
        "Value": int,
    },
    total=False,
)

Phase1EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase1EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1EncryptionAlgorithmsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase1IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase1IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase1IntegrityAlgorithmsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase2DHGroupNumbersListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersListValueTypeDef",
    {
        "Value": int,
    },
    total=False,
)

Phase2DHGroupNumbersRequestListValueTypeDef = TypedDict(
    "Phase2DHGroupNumbersRequestListValueTypeDef",
    {
        "Value": int,
    },
    total=False,
)

Phase2EncryptionAlgorithmsListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase2EncryptionAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2EncryptionAlgorithmsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase2IntegrityAlgorithmsListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

Phase2IntegrityAlgorithmsRequestListValueTypeDef = TypedDict(
    "Phase2IntegrityAlgorithmsRequestListValueTypeDef",
    {
        "Value": str,
    },
    total=False,
)

PlacementGroupInfoTypeDef = TypedDict(
    "PlacementGroupInfoTypeDef",
    {
        "SupportedStrategies": List[PlacementGroupStrategyType],
    },
    total=False,
)

PlacementGroupTypeDef = TypedDict(
    "PlacementGroupTypeDef",
    {
        "GroupName": str,
        "State": PlacementGroupStateType,
        "Strategy": PlacementStrategyType,
        "PartitionCount": int,
        "GroupId": str,
        "Tags": List["TagTypeDef"],
        "GroupArn": str,
        "SpreadLevel": SpreadLevelType,
    },
    total=False,
)

PlacementResponseTypeDef = TypedDict(
    "PlacementResponseTypeDef",
    {
        "GroupName": str,
    },
    total=False,
)

PlacementTypeDef = TypedDict(
    "PlacementTypeDef",
    {
        "AvailabilityZone": str,
        "Affinity": str,
        "GroupName": str,
        "PartitionNumber": int,
        "HostId": str,
        "Tenancy": TenancyType,
        "SpreadDomain": str,
        "HostResourceGroupArn": str,
        "GroupId": str,
    },
    total=False,
)

PoolCidrBlockTypeDef = TypedDict(
    "PoolCidrBlockTypeDef",
    {
        "Cidr": str,
    },
    total=False,
)

PortRangeTypeDef = TypedDict(
    "PortRangeTypeDef",
    {
        "From": int,
        "To": int,
    },
    total=False,
)

PrefixListAssociationTypeDef = TypedDict(
    "PrefixListAssociationTypeDef",
    {
        "ResourceId": str,
        "ResourceOwner": str,
    },
    total=False,
)

PrefixListEntryTypeDef = TypedDict(
    "PrefixListEntryTypeDef",
    {
        "Cidr": str,
        "Description": str,
    },
    total=False,
)

PrefixListIdTypeDef = TypedDict(
    "PrefixListIdTypeDef",
    {
        "Description": str,
        "PrefixListId": str,
    },
    total=False,
)

PrefixListTypeDef = TypedDict(
    "PrefixListTypeDef",
    {
        "Cidrs": List[str],
        "PrefixListId": str,
        "PrefixListName": str,
    },
    total=False,
)

PriceScheduleSpecificationTypeDef = TypedDict(
    "PriceScheduleSpecificationTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Price": float,
        "Term": int,
    },
    total=False,
)

PriceScheduleTypeDef = TypedDict(
    "PriceScheduleTypeDef",
    {
        "Active": bool,
        "CurrencyCode": Literal["USD"],
        "Price": float,
        "Term": int,
    },
    total=False,
)

PricingDetailTypeDef = TypedDict(
    "PricingDetailTypeDef",
    {
        "Count": int,
        "Price": float,
    },
    total=False,
)

PrincipalIdFormatTypeDef = TypedDict(
    "PrincipalIdFormatTypeDef",
    {
        "Arn": str,
        "Statuses": List["IdFormatTypeDef"],
    },
    total=False,
)

PrivateDnsDetailsTypeDef = TypedDict(
    "PrivateDnsDetailsTypeDef",
    {
        "PrivateDnsName": str,
    },
    total=False,
)

PrivateDnsNameConfigurationTypeDef = TypedDict(
    "PrivateDnsNameConfigurationTypeDef",
    {
        "State": DnsNameStateType,
        "Type": str,
        "Value": str,
        "Name": str,
    },
    total=False,
)

PrivateDnsNameOptionsOnLaunchTypeDef = TypedDict(
    "PrivateDnsNameOptionsOnLaunchTypeDef",
    {
        "HostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
    },
    total=False,
)

PrivateDnsNameOptionsRequestTypeDef = TypedDict(
    "PrivateDnsNameOptionsRequestTypeDef",
    {
        "HostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
    },
    total=False,
)

PrivateDnsNameOptionsResponseTypeDef = TypedDict(
    "PrivateDnsNameOptionsResponseTypeDef",
    {
        "HostnameType": HostnameTypeType,
        "EnableResourceNameDnsARecord": bool,
        "EnableResourceNameDnsAAAARecord": bool,
    },
    total=False,
)

PrivateIpAddressSpecificationTypeDef = TypedDict(
    "PrivateIpAddressSpecificationTypeDef",
    {
        "Primary": bool,
        "PrivateIpAddress": str,
    },
    total=False,
)

ProcessorInfoTypeDef = TypedDict(
    "ProcessorInfoTypeDef",
    {
        "SupportedArchitectures": List[ArchitectureTypeType],
        "SustainedClockSpeedInGhz": float,
        "SupportedFeatures": List[Literal["amd-sev-snp"]],
    },
    total=False,
)

ProductCodeTypeDef = TypedDict(
    "ProductCodeTypeDef",
    {
        "ProductCodeId": str,
        "ProductCodeType": ProductCodeValuesType,
    },
    total=False,
)

PropagatingVgwTypeDef = TypedDict(
    "PropagatingVgwTypeDef",
    {
        "GatewayId": str,
    },
    total=False,
)

_RequiredProvisionByoipCidrRequestRequestTypeDef = TypedDict(
    "_RequiredProvisionByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalProvisionByoipCidrRequestRequestTypeDef = TypedDict(
    "_OptionalProvisionByoipCidrRequestRequestTypeDef",
    {
        "CidrAuthorizationContext": "CidrAuthorizationContextTypeDef",
        "PubliclyAdvertisable": bool,
        "Description": str,
        "DryRun": bool,
        "PoolTagSpecifications": List["TagSpecificationTypeDef"],
        "MultiRegion": bool,
    },
    total=False,
)

class ProvisionByoipCidrRequestRequestTypeDef(
    _RequiredProvisionByoipCidrRequestRequestTypeDef,
    _OptionalProvisionByoipCidrRequestRequestTypeDef,
):
    pass

ProvisionByoipCidrResultTypeDef = TypedDict(
    "ProvisionByoipCidrResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredProvisionIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "_RequiredProvisionIpamPoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
    },
)
_OptionalProvisionIpamPoolCidrRequestRequestTypeDef = TypedDict(
    "_OptionalProvisionIpamPoolCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Cidr": str,
        "CidrAuthorizationContext": "IpamCidrAuthorizationContextTypeDef",
        "NetmaskLength": int,
        "ClientToken": str,
    },
    total=False,
)

class ProvisionIpamPoolCidrRequestRequestTypeDef(
    _RequiredProvisionIpamPoolCidrRequestRequestTypeDef,
    _OptionalProvisionIpamPoolCidrRequestRequestTypeDef,
):
    pass

ProvisionIpamPoolCidrResultTypeDef = TypedDict(
    "ProvisionIpamPoolCidrResultTypeDef",
    {
        "IpamPoolCidr": "IpamPoolCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredProvisionPublicIpv4PoolCidrRequestRequestTypeDef = TypedDict(
    "_RequiredProvisionPublicIpv4PoolCidrRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "PoolId": str,
        "NetmaskLength": int,
    },
)
_OptionalProvisionPublicIpv4PoolCidrRequestRequestTypeDef = TypedDict(
    "_OptionalProvisionPublicIpv4PoolCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ProvisionPublicIpv4PoolCidrRequestRequestTypeDef(
    _RequiredProvisionPublicIpv4PoolCidrRequestRequestTypeDef,
    _OptionalProvisionPublicIpv4PoolCidrRequestRequestTypeDef,
):
    pass

ProvisionPublicIpv4PoolCidrResultTypeDef = TypedDict(
    "ProvisionPublicIpv4PoolCidrResultTypeDef",
    {
        "PoolId": str,
        "PoolAddressRange": "PublicIpv4PoolRangeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ProvisionedBandwidthTypeDef = TypedDict(
    "ProvisionedBandwidthTypeDef",
    {
        "ProvisionTime": datetime,
        "Provisioned": str,
        "RequestTime": datetime,
        "Requested": str,
        "Status": str,
    },
    total=False,
)

PtrUpdateStatusTypeDef = TypedDict(
    "PtrUpdateStatusTypeDef",
    {
        "Value": str,
        "Status": str,
        "Reason": str,
    },
    total=False,
)

PublicIpv4PoolRangeTypeDef = TypedDict(
    "PublicIpv4PoolRangeTypeDef",
    {
        "FirstAddress": str,
        "LastAddress": str,
        "AddressCount": int,
        "AvailableAddressCount": int,
    },
    total=False,
)

PublicIpv4PoolTypeDef = TypedDict(
    "PublicIpv4PoolTypeDef",
    {
        "PoolId": str,
        "Description": str,
        "PoolAddressRanges": List["PublicIpv4PoolRangeTypeDef"],
        "TotalAddressCount": int,
        "TotalAvailableAddressCount": int,
        "NetworkBorderGroup": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredPurchaseCapacityBlockRequestRequestTypeDef = TypedDict(
    "_RequiredPurchaseCapacityBlockRequestRequestTypeDef",
    {
        "CapacityBlockOfferingId": str,
        "InstancePlatform": CapacityReservationInstancePlatformType,
    },
)
_OptionalPurchaseCapacityBlockRequestRequestTypeDef = TypedDict(
    "_OptionalPurchaseCapacityBlockRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class PurchaseCapacityBlockRequestRequestTypeDef(
    _RequiredPurchaseCapacityBlockRequestRequestTypeDef,
    _OptionalPurchaseCapacityBlockRequestRequestTypeDef,
):
    pass

PurchaseCapacityBlockResultTypeDef = TypedDict(
    "PurchaseCapacityBlockResultTypeDef",
    {
        "CapacityReservation": "CapacityReservationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPurchaseHostReservationRequestRequestTypeDef = TypedDict(
    "_RequiredPurchaseHostReservationRequestRequestTypeDef",
    {
        "HostIdSet": List[str],
        "OfferingId": str,
    },
)
_OptionalPurchaseHostReservationRequestRequestTypeDef = TypedDict(
    "_OptionalPurchaseHostReservationRequestRequestTypeDef",
    {
        "ClientToken": str,
        "CurrencyCode": Literal["USD"],
        "LimitPrice": str,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class PurchaseHostReservationRequestRequestTypeDef(
    _RequiredPurchaseHostReservationRequestRequestTypeDef,
    _OptionalPurchaseHostReservationRequestRequestTypeDef,
):
    pass

PurchaseHostReservationResultTypeDef = TypedDict(
    "PurchaseHostReservationResultTypeDef",
    {
        "ClientToken": str,
        "CurrencyCode": Literal["USD"],
        "Purchase": List["PurchaseTypeDef"],
        "TotalHourlyPrice": str,
        "TotalUpfrontPrice": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PurchaseRequestTypeDef = TypedDict(
    "PurchaseRequestTypeDef",
    {
        "InstanceCount": int,
        "PurchaseToken": str,
    },
)

_RequiredPurchaseReservedInstancesOfferingRequestRequestTypeDef = TypedDict(
    "_RequiredPurchaseReservedInstancesOfferingRequestRequestTypeDef",
    {
        "InstanceCount": int,
        "ReservedInstancesOfferingId": str,
    },
)
_OptionalPurchaseReservedInstancesOfferingRequestRequestTypeDef = TypedDict(
    "_OptionalPurchaseReservedInstancesOfferingRequestRequestTypeDef",
    {
        "DryRun": bool,
        "LimitPrice": "ReservedInstanceLimitPriceTypeDef",
        "PurchaseTime": Union[datetime, str],
    },
    total=False,
)

class PurchaseReservedInstancesOfferingRequestRequestTypeDef(
    _RequiredPurchaseReservedInstancesOfferingRequestRequestTypeDef,
    _OptionalPurchaseReservedInstancesOfferingRequestRequestTypeDef,
):
    pass

PurchaseReservedInstancesOfferingResultTypeDef = TypedDict(
    "PurchaseReservedInstancesOfferingResultTypeDef",
    {
        "ReservedInstancesId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredPurchaseScheduledInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredPurchaseScheduledInstancesRequestRequestTypeDef",
    {
        "PurchaseRequests": List["PurchaseRequestTypeDef"],
    },
)
_OptionalPurchaseScheduledInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalPurchaseScheduledInstancesRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
    },
    total=False,
)

class PurchaseScheduledInstancesRequestRequestTypeDef(
    _RequiredPurchaseScheduledInstancesRequestRequestTypeDef,
    _OptionalPurchaseScheduledInstancesRequestRequestTypeDef,
):
    pass

PurchaseScheduledInstancesResultTypeDef = TypedDict(
    "PurchaseScheduledInstancesResultTypeDef",
    {
        "ScheduledInstanceSet": List["ScheduledInstanceTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

PurchaseTypeDef = TypedDict(
    "PurchaseTypeDef",
    {
        "CurrencyCode": Literal["USD"],
        "Duration": int,
        "HostIdSet": List[str],
        "HostReservationId": str,
        "HourlyPrice": str,
        "InstanceFamily": str,
        "PaymentOption": PaymentOptionType,
        "UpfrontPrice": str,
    },
    total=False,
)

RebootInstancesRequestInstanceTypeDef = TypedDict(
    "RebootInstancesRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredRebootInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredRebootInstancesRequestRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalRebootInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalRebootInstancesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RebootInstancesRequestRequestTypeDef(
    _RequiredRebootInstancesRequestRequestTypeDef, _OptionalRebootInstancesRequestRequestTypeDef
):
    pass

RecurringChargeTypeDef = TypedDict(
    "RecurringChargeTypeDef",
    {
        "Amount": float,
        "Frequency": Literal["Hourly"],
    },
    total=False,
)

ReferencedSecurityGroupTypeDef = TypedDict(
    "ReferencedSecurityGroupTypeDef",
    {
        "GroupId": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

RegionTypeDef = TypedDict(
    "RegionTypeDef",
    {
        "Endpoint": str,
        "RegionName": str,
        "OptInStatus": str,
    },
    total=False,
)

_RequiredRegisterImageRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterImageRequestRequestTypeDef",
    {
        "Name": str,
    },
)
_OptionalRegisterImageRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterImageRequestRequestTypeDef",
    {
        "ImageLocation": str,
        "Architecture": ArchitectureValuesType,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "DryRun": bool,
        "EnaSupport": bool,
        "KernelId": str,
        "BillingProducts": List[str],
        "RamdiskId": str,
        "RootDeviceName": str,
        "SriovNetSupport": str,
        "VirtualizationType": str,
        "BootMode": BootModeValuesType,
        "TpmSupport": Literal["v2.0"],
        "UefiData": str,
        "ImdsSupport": Literal["v2.0"],
    },
    total=False,
)

class RegisterImageRequestRequestTypeDef(
    _RequiredRegisterImageRequestRequestTypeDef, _OptionalRegisterImageRequestRequestTypeDef
):
    pass

_RequiredRegisterImageRequestServiceResourceTypeDef = TypedDict(
    "_RequiredRegisterImageRequestServiceResourceTypeDef",
    {
        "Name": str,
    },
)
_OptionalRegisterImageRequestServiceResourceTypeDef = TypedDict(
    "_OptionalRegisterImageRequestServiceResourceTypeDef",
    {
        "ImageLocation": str,
        "Architecture": ArchitectureValuesType,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "Description": str,
        "DryRun": bool,
        "EnaSupport": bool,
        "KernelId": str,
        "BillingProducts": List[str],
        "RamdiskId": str,
        "RootDeviceName": str,
        "SriovNetSupport": str,
        "VirtualizationType": str,
        "BootMode": BootModeValuesType,
        "TpmSupport": Literal["v2.0"],
        "UefiData": str,
        "ImdsSupport": Literal["v2.0"],
    },
    total=False,
)

class RegisterImageRequestServiceResourceTypeDef(
    _RequiredRegisterImageRequestServiceResourceTypeDef,
    _OptionalRegisterImageRequestServiceResourceTypeDef,
):
    pass

RegisterImageResultTypeDef = TypedDict(
    "RegisterImageResultTypeDef",
    {
        "ImageId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "InstanceTagAttribute": "RegisterInstanceTagAttributeRequestTypeDef",
    },
)
_OptionalRegisterInstanceEventNotificationAttributesRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterInstanceEventNotificationAttributesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RegisterInstanceEventNotificationAttributesRequestRequestTypeDef(
    _RequiredRegisterInstanceEventNotificationAttributesRequestRequestTypeDef,
    _OptionalRegisterInstanceEventNotificationAttributesRequestRequestTypeDef,
):
    pass

RegisterInstanceEventNotificationAttributesResultTypeDef = TypedDict(
    "RegisterInstanceEventNotificationAttributesResultTypeDef",
    {
        "InstanceTagAttribute": "InstanceTagNotificationAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RegisterInstanceTagAttributeRequestTypeDef = TypedDict(
    "RegisterInstanceTagAttributeRequestTypeDef",
    {
        "IncludeAllTagsOfInstance": bool,
        "InstanceTagKeys": List[str],
    },
    total=False,
)

_RequiredRegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "NetworkInterfaceIds": List[str],
    },
)
_OptionalRegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef",
    {
        "GroupIpAddress": str,
        "DryRun": bool,
    },
    total=False,
)

class RegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef(
    _RequiredRegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef,
    _OptionalRegisterTransitGatewayMulticastGroupMembersRequestRequestTypeDef,
):
    pass

RegisterTransitGatewayMulticastGroupMembersResultTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupMembersResultTypeDef",
    {
        "RegisteredMulticastGroupMembers": "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef = TypedDict(
    "_RequiredRegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "NetworkInterfaceIds": List[str],
    },
)
_OptionalRegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef = TypedDict(
    "_OptionalRegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef",
    {
        "GroupIpAddress": str,
        "DryRun": bool,
    },
    total=False,
)

class RegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef(
    _RequiredRegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef,
    _OptionalRegisterTransitGatewayMulticastGroupSourcesRequestRequestTypeDef,
):
    pass

RegisterTransitGatewayMulticastGroupSourcesResultTypeDef = TypedDict(
    "RegisterTransitGatewayMulticastGroupSourcesResultTypeDef",
    {
        "RegisteredMulticastGroupSources": "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef = TypedDict(
    "RejectTransitGatewayMulticastDomainAssociationsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "SubnetIds": List[str],
        "DryRun": bool,
    },
    total=False,
)

RejectTransitGatewayMulticastDomainAssociationsResultTypeDef = TypedDict(
    "RejectTransitGatewayMulticastDomainAssociationsResultTypeDef",
    {
        "Associations": "TransitGatewayMulticastDomainAssociationsTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredRejectTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalRejectTransitGatewayPeeringAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalRejectTransitGatewayPeeringAttachmentRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RejectTransitGatewayPeeringAttachmentRequestRequestTypeDef(
    _RequiredRejectTransitGatewayPeeringAttachmentRequestRequestTypeDef,
    _OptionalRejectTransitGatewayPeeringAttachmentRequestRequestTypeDef,
):
    pass

RejectTransitGatewayPeeringAttachmentResultTypeDef = TypedDict(
    "RejectTransitGatewayPeeringAttachmentResultTypeDef",
    {
        "TransitGatewayPeeringAttachment": "TransitGatewayPeeringAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_RequiredRejectTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
    },
)
_OptionalRejectTransitGatewayVpcAttachmentRequestRequestTypeDef = TypedDict(
    "_OptionalRejectTransitGatewayVpcAttachmentRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RejectTransitGatewayVpcAttachmentRequestRequestTypeDef(
    _RequiredRejectTransitGatewayVpcAttachmentRequestRequestTypeDef,
    _OptionalRejectTransitGatewayVpcAttachmentRequestRequestTypeDef,
):
    pass

RejectTransitGatewayVpcAttachmentResultTypeDef = TypedDict(
    "RejectTransitGatewayVpcAttachmentResultTypeDef",
    {
        "TransitGatewayVpcAttachment": "TransitGatewayVpcAttachmentTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "_RequiredRejectVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointIds": List[str],
    },
)
_OptionalRejectVpcEndpointConnectionsRequestRequestTypeDef = TypedDict(
    "_OptionalRejectVpcEndpointConnectionsRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RejectVpcEndpointConnectionsRequestRequestTypeDef(
    _RequiredRejectVpcEndpointConnectionsRequestRequestTypeDef,
    _OptionalRejectVpcEndpointConnectionsRequestRequestTypeDef,
):
    pass

RejectVpcEndpointConnectionsResultTypeDef = TypedDict(
    "RejectVpcEndpointConnectionsResultTypeDef",
    {
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRejectVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "_RequiredRejectVpcPeeringConnectionRequestRequestTypeDef",
    {
        "VpcPeeringConnectionId": str,
    },
)
_OptionalRejectVpcPeeringConnectionRequestRequestTypeDef = TypedDict(
    "_OptionalRejectVpcPeeringConnectionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RejectVpcPeeringConnectionRequestRequestTypeDef(
    _RequiredRejectVpcPeeringConnectionRequestRequestTypeDef,
    _OptionalRejectVpcPeeringConnectionRequestRequestTypeDef,
):
    pass

RejectVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef = TypedDict(
    "RejectVpcPeeringConnectionRequestVpcPeeringConnectionTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

RejectVpcPeeringConnectionResultTypeDef = TypedDict(
    "RejectVpcPeeringConnectionResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReleaseAddressRequestClassicAddressTypeDef = TypedDict(
    "ReleaseAddressRequestClassicAddressTypeDef",
    {
        "AllocationId": str,
        "PublicIp": str,
        "NetworkBorderGroup": str,
        "DryRun": bool,
    },
    total=False,
)

ReleaseAddressRequestRequestTypeDef = TypedDict(
    "ReleaseAddressRequestRequestTypeDef",
    {
        "AllocationId": str,
        "PublicIp": str,
        "NetworkBorderGroup": str,
        "DryRun": bool,
    },
    total=False,
)

ReleaseAddressRequestVpcAddressTypeDef = TypedDict(
    "ReleaseAddressRequestVpcAddressTypeDef",
    {
        "AllocationId": str,
        "PublicIp": str,
        "NetworkBorderGroup": str,
        "DryRun": bool,
    },
    total=False,
)

ReleaseHostsRequestRequestTypeDef = TypedDict(
    "ReleaseHostsRequestRequestTypeDef",
    {
        "HostIds": List[str],
    },
)

ReleaseHostsResultTypeDef = TypedDict(
    "ReleaseHostsResultTypeDef",
    {
        "Successful": List[str],
        "Unsuccessful": List["UnsuccessfulItemTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReleaseIpamPoolAllocationRequestRequestTypeDef = TypedDict(
    "_RequiredReleaseIpamPoolAllocationRequestRequestTypeDef",
    {
        "IpamPoolId": str,
        "Cidr": str,
        "IpamPoolAllocationId": str,
    },
)
_OptionalReleaseIpamPoolAllocationRequestRequestTypeDef = TypedDict(
    "_OptionalReleaseIpamPoolAllocationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ReleaseIpamPoolAllocationRequestRequestTypeDef(
    _RequiredReleaseIpamPoolAllocationRequestRequestTypeDef,
    _OptionalReleaseIpamPoolAllocationRequestRequestTypeDef,
):
    pass

ReleaseIpamPoolAllocationResultTypeDef = TypedDict(
    "ReleaseIpamPoolAllocationResultTypeDef",
    {
        "Success": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveIpamOperatingRegionTypeDef = TypedDict(
    "RemoveIpamOperatingRegionTypeDef",
    {
        "RegionName": str,
    },
    total=False,
)

RemovePrefixListEntryTypeDef = TypedDict(
    "RemovePrefixListEntryTypeDef",
    {
        "Cidr": str,
    },
)

ReplaceIamInstanceProfileAssociationRequestRequestTypeDef = TypedDict(
    "ReplaceIamInstanceProfileAssociationRequestRequestTypeDef",
    {
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "AssociationId": str,
    },
)

ReplaceIamInstanceProfileAssociationResultTypeDef = TypedDict(
    "ReplaceIamInstanceProfileAssociationResultTypeDef",
    {
        "IamInstanceProfileAssociation": "IamInstanceProfileAssociationTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplaceNetworkAclAssociationRequestNetworkAclTypeDef = TypedDict(
    "_RequiredReplaceNetworkAclAssociationRequestNetworkAclTypeDef",
    {
        "AssociationId": str,
    },
)
_OptionalReplaceNetworkAclAssociationRequestNetworkAclTypeDef = TypedDict(
    "_OptionalReplaceNetworkAclAssociationRequestNetworkAclTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ReplaceNetworkAclAssociationRequestNetworkAclTypeDef(
    _RequiredReplaceNetworkAclAssociationRequestNetworkAclTypeDef,
    _OptionalReplaceNetworkAclAssociationRequestNetworkAclTypeDef,
):
    pass

_RequiredReplaceNetworkAclAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredReplaceNetworkAclAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "NetworkAclId": str,
    },
)
_OptionalReplaceNetworkAclAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalReplaceNetworkAclAssociationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ReplaceNetworkAclAssociationRequestRequestTypeDef(
    _RequiredReplaceNetworkAclAssociationRequestRequestTypeDef,
    _OptionalReplaceNetworkAclAssociationRequestRequestTypeDef,
):
    pass

ReplaceNetworkAclAssociationResultTypeDef = TypedDict(
    "ReplaceNetworkAclAssociationResultTypeDef",
    {
        "NewAssociationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplaceNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_RequiredReplaceNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "Egress": bool,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
)
_OptionalReplaceNetworkAclEntryRequestNetworkAclTypeDef = TypedDict(
    "_OptionalReplaceNetworkAclEntryRequestNetworkAclTypeDef",
    {
        "CidrBlock": str,
        "DryRun": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
    },
    total=False,
)

class ReplaceNetworkAclEntryRequestNetworkAclTypeDef(
    _RequiredReplaceNetworkAclEntryRequestNetworkAclTypeDef,
    _OptionalReplaceNetworkAclEntryRequestNetworkAclTypeDef,
):
    pass

_RequiredReplaceNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "_RequiredReplaceNetworkAclEntryRequestRequestTypeDef",
    {
        "Egress": bool,
        "NetworkAclId": str,
        "Protocol": str,
        "RuleAction": RuleActionType,
        "RuleNumber": int,
    },
)
_OptionalReplaceNetworkAclEntryRequestRequestTypeDef = TypedDict(
    "_OptionalReplaceNetworkAclEntryRequestRequestTypeDef",
    {
        "CidrBlock": str,
        "DryRun": bool,
        "IcmpTypeCode": "IcmpTypeCodeTypeDef",
        "Ipv6CidrBlock": str,
        "PortRange": "PortRangeTypeDef",
    },
    total=False,
)

class ReplaceNetworkAclEntryRequestRequestTypeDef(
    _RequiredReplaceNetworkAclEntryRequestRequestTypeDef,
    _OptionalReplaceNetworkAclEntryRequestRequestTypeDef,
):
    pass

ReplaceRootVolumeTaskTypeDef = TypedDict(
    "ReplaceRootVolumeTaskTypeDef",
    {
        "ReplaceRootVolumeTaskId": str,
        "InstanceId": str,
        "TaskState": ReplaceRootVolumeTaskStateType,
        "StartTime": str,
        "CompleteTime": str,
        "Tags": List["TagTypeDef"],
        "ImageId": str,
        "SnapshotId": str,
        "DeleteReplacedRootVolume": bool,
    },
    total=False,
)

_RequiredReplaceRouteRequestRequestTypeDef = TypedDict(
    "_RequiredReplaceRouteRequestRequestTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalReplaceRouteRequestRequestTypeDef = TypedDict(
    "_OptionalReplaceRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
        "VpcEndpointId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "LocalTarget": bool,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "VpcPeeringConnectionId": str,
        "CoreNetworkArn": str,
    },
    total=False,
)

class ReplaceRouteRequestRequestTypeDef(
    _RequiredReplaceRouteRequestRequestTypeDef, _OptionalReplaceRouteRequestRequestTypeDef
):
    pass

ReplaceRouteRequestRouteTypeDef = TypedDict(
    "ReplaceRouteRequestRouteTypeDef",
    {
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "DryRun": bool,
        "VpcEndpointId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "LocalTarget": bool,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "VpcPeeringConnectionId": str,
        "CoreNetworkArn": str,
    },
    total=False,
)

_RequiredReplaceRouteTableAssociationRequestRequestTypeDef = TypedDict(
    "_RequiredReplaceRouteTableAssociationRequestRequestTypeDef",
    {
        "AssociationId": str,
        "RouteTableId": str,
    },
)
_OptionalReplaceRouteTableAssociationRequestRequestTypeDef = TypedDict(
    "_OptionalReplaceRouteTableAssociationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ReplaceRouteTableAssociationRequestRequestTypeDef(
    _RequiredReplaceRouteTableAssociationRequestRequestTypeDef,
    _OptionalReplaceRouteTableAssociationRequestRequestTypeDef,
):
    pass

_RequiredReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef = TypedDict(
    "_RequiredReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef",
    {
        "RouteTableId": str,
    },
)
_OptionalReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef = TypedDict(
    "_OptionalReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef(
    _RequiredReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef,
    _OptionalReplaceRouteTableAssociationRequestRouteTableAssociationTypeDef,
):
    pass

ReplaceRouteTableAssociationResultTypeDef = TypedDict(
    "ReplaceRouteTableAssociationResultTypeDef",
    {
        "NewAssociationId": str,
        "AssociationState": "RouteTableAssociationStateTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplaceTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "_RequiredReplaceTransitGatewayRouteRequestRequestTypeDef",
    {
        "DestinationCidrBlock": str,
        "TransitGatewayRouteTableId": str,
    },
)
_OptionalReplaceTransitGatewayRouteRequestRequestTypeDef = TypedDict(
    "_OptionalReplaceTransitGatewayRouteRequestRequestTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "Blackhole": bool,
        "DryRun": bool,
    },
    total=False,
)

class ReplaceTransitGatewayRouteRequestRequestTypeDef(
    _RequiredReplaceTransitGatewayRouteRequestRequestTypeDef,
    _OptionalReplaceTransitGatewayRouteRequestRequestTypeDef,
):
    pass

ReplaceTransitGatewayRouteResultTypeDef = TypedDict(
    "ReplaceTransitGatewayRouteResultTypeDef",
    {
        "Route": "TransitGatewayRouteTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReplaceVpnTunnelRequestRequestTypeDef = TypedDict(
    "_RequiredReplaceVpnTunnelRequestRequestTypeDef",
    {
        "VpnConnectionId": str,
        "VpnTunnelOutsideIpAddress": str,
    },
)
_OptionalReplaceVpnTunnelRequestRequestTypeDef = TypedDict(
    "_OptionalReplaceVpnTunnelRequestRequestTypeDef",
    {
        "ApplyPendingMaintenance": bool,
        "DryRun": bool,
    },
    total=False,
)

class ReplaceVpnTunnelRequestRequestTypeDef(
    _RequiredReplaceVpnTunnelRequestRequestTypeDef, _OptionalReplaceVpnTunnelRequestRequestTypeDef
):
    pass

ReplaceVpnTunnelResultTypeDef = TypedDict(
    "ReplaceVpnTunnelResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredReportInstanceStatusRequestInstanceTypeDef = TypedDict(
    "_RequiredReportInstanceStatusRequestInstanceTypeDef",
    {
        "ReasonCodes": List[ReportInstanceReasonCodesType],
        "Status": ReportStatusTypeType,
    },
)
_OptionalReportInstanceStatusRequestInstanceTypeDef = TypedDict(
    "_OptionalReportInstanceStatusRequestInstanceTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "EndTime": Union[datetime, str],
        "StartTime": Union[datetime, str],
    },
    total=False,
)

class ReportInstanceStatusRequestInstanceTypeDef(
    _RequiredReportInstanceStatusRequestInstanceTypeDef,
    _OptionalReportInstanceStatusRequestInstanceTypeDef,
):
    pass

_RequiredReportInstanceStatusRequestRequestTypeDef = TypedDict(
    "_RequiredReportInstanceStatusRequestRequestTypeDef",
    {
        "Instances": List[str],
        "ReasonCodes": List[ReportInstanceReasonCodesType],
        "Status": ReportStatusTypeType,
    },
)
_OptionalReportInstanceStatusRequestRequestTypeDef = TypedDict(
    "_OptionalReportInstanceStatusRequestRequestTypeDef",
    {
        "Description": str,
        "DryRun": bool,
        "EndTime": Union[datetime, str],
        "StartTime": Union[datetime, str],
    },
    total=False,
)

class ReportInstanceStatusRequestRequestTypeDef(
    _RequiredReportInstanceStatusRequestRequestTypeDef,
    _OptionalReportInstanceStatusRequestRequestTypeDef,
):
    pass

RequestFilterPortRangeTypeDef = TypedDict(
    "RequestFilterPortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

RequestIpamResourceTagTypeDef = TypedDict(
    "RequestIpamResourceTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

RequestLaunchTemplateDataTypeDef = TypedDict(
    "RequestLaunchTemplateDataTypeDef",
    {
        "KernelId": str,
        "EbsOptimized": bool,
        "IamInstanceProfile": "LaunchTemplateIamInstanceProfileSpecificationRequestTypeDef",
        "BlockDeviceMappings": List["LaunchTemplateBlockDeviceMappingRequestTypeDef"],
        "NetworkInterfaces": List[
            "LaunchTemplateInstanceNetworkInterfaceSpecificationRequestTypeDef"
        ],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KeyName": str,
        "Monitoring": "LaunchTemplatesMonitoringRequestTypeDef",
        "Placement": "LaunchTemplatePlacementRequestTypeDef",
        "RamDiskId": str,
        "DisableApiTermination": bool,
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "UserData": str,
        "TagSpecifications": List["LaunchTemplateTagSpecificationRequestTypeDef"],
        "ElasticGpuSpecifications": List["ElasticGpuSpecificationTypeDef"],
        "ElasticInferenceAccelerators": List["LaunchTemplateElasticInferenceAcceleratorTypeDef"],
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "InstanceMarketOptions": "LaunchTemplateInstanceMarketOptionsRequestTypeDef",
        "CreditSpecification": "CreditSpecificationRequestTypeDef",
        "CpuOptions": "LaunchTemplateCpuOptionsRequestTypeDef",
        "CapacityReservationSpecification": "LaunchTemplateCapacityReservationSpecificationRequestTypeDef",
        "LicenseSpecifications": List["LaunchTemplateLicenseConfigurationRequestTypeDef"],
        "HibernationOptions": "LaunchTemplateHibernationOptionsRequestTypeDef",
        "MetadataOptions": "LaunchTemplateInstanceMetadataOptionsRequestTypeDef",
        "EnclaveOptions": "LaunchTemplateEnclaveOptionsRequestTypeDef",
        "InstanceRequirements": "InstanceRequirementsRequestTypeDef",
        "PrivateDnsNameOptions": "LaunchTemplatePrivateDnsNameOptionsRequestTypeDef",
        "MaintenanceOptions": "LaunchTemplateInstanceMaintenanceOptionsRequestTypeDef",
        "DisableApiStop": bool,
    },
    total=False,
)

_RequiredRequestSpotFleetRequestRequestTypeDef = TypedDict(
    "_RequiredRequestSpotFleetRequestRequestTypeDef",
    {
        "SpotFleetRequestConfig": "SpotFleetRequestConfigDataTypeDef",
    },
)
_OptionalRequestSpotFleetRequestRequestTypeDef = TypedDict(
    "_OptionalRequestSpotFleetRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RequestSpotFleetRequestRequestTypeDef(
    _RequiredRequestSpotFleetRequestRequestTypeDef, _OptionalRequestSpotFleetRequestRequestTypeDef
):
    pass

RequestSpotFleetResponseTypeDef = TypedDict(
    "RequestSpotFleetResponseTypeDef",
    {
        "SpotFleetRequestId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestSpotInstancesRequestRequestTypeDef = TypedDict(
    "RequestSpotInstancesRequestRequestTypeDef",
    {
        "AvailabilityZoneGroup": str,
        "BlockDurationMinutes": int,
        "ClientToken": str,
        "DryRun": bool,
        "InstanceCount": int,
        "LaunchGroup": str,
        "LaunchSpecification": "RequestSpotLaunchSpecificationTypeDef",
        "SpotPrice": str,
        "Type": SpotInstanceTypeType,
        "ValidFrom": Union[datetime, str],
        "ValidUntil": Union[datetime, str],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

RequestSpotInstancesResultTypeDef = TypedDict(
    "RequestSpotInstancesResultTypeDef",
    {
        "SpotInstanceRequests": List["SpotInstanceRequestTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RequestSpotLaunchSpecificationTypeDef = TypedDict(
    "RequestSpotLaunchSpecificationTypeDef",
    {
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "AddressingType": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "Placement": "SpotPlacementTypeDef",
        "RamdiskId": str,
        "SubnetId": str,
        "UserData": str,
    },
    total=False,
)

ReservationFleetInstanceSpecificationTypeDef = TypedDict(
    "ReservationFleetInstanceSpecificationTypeDef",
    {
        "InstanceType": InstanceTypeType,
        "InstancePlatform": CapacityReservationInstancePlatformType,
        "Weight": float,
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "EbsOptimized": bool,
        "Priority": int,
    },
    total=False,
)

ReservationResponseMetadataTypeDef = TypedDict(
    "ReservationResponseMetadataTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "Instances": List["InstanceTypeDef"],
        "OwnerId": str,
        "RequesterId": str,
        "ReservationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ReservationTypeDef = TypedDict(
    "ReservationTypeDef",
    {
        "Groups": List["GroupIdentifierTypeDef"],
        "Instances": List["InstanceTypeDef"],
        "OwnerId": str,
        "RequesterId": str,
        "ReservationId": str,
    },
    total=False,
)

ReservationValueTypeDef = TypedDict(
    "ReservationValueTypeDef",
    {
        "HourlyPrice": str,
        "RemainingTotalValue": str,
        "RemainingUpfrontValue": str,
    },
    total=False,
)

ReservedInstanceLimitPriceTypeDef = TypedDict(
    "ReservedInstanceLimitPriceTypeDef",
    {
        "Amount": float,
        "CurrencyCode": Literal["USD"],
    },
    total=False,
)

ReservedInstanceReservationValueTypeDef = TypedDict(
    "ReservedInstanceReservationValueTypeDef",
    {
        "ReservationValue": "ReservationValueTypeDef",
        "ReservedInstanceId": str,
    },
    total=False,
)

ReservedInstancesConfigurationTypeDef = TypedDict(
    "ReservedInstancesConfigurationTypeDef",
    {
        "AvailabilityZone": str,
        "InstanceCount": int,
        "InstanceType": InstanceTypeType,
        "Platform": str,
        "Scope": scopeType,
    },
    total=False,
)

ReservedInstancesIdTypeDef = TypedDict(
    "ReservedInstancesIdTypeDef",
    {
        "ReservedInstancesId": str,
    },
    total=False,
)

ReservedInstancesListingTypeDef = TypedDict(
    "ReservedInstancesListingTypeDef",
    {
        "ClientToken": str,
        "CreateDate": datetime,
        "InstanceCounts": List["InstanceCountTypeDef"],
        "PriceSchedules": List["PriceScheduleTypeDef"],
        "ReservedInstancesId": str,
        "ReservedInstancesListingId": str,
        "Status": ListingStatusType,
        "StatusMessage": str,
        "Tags": List["TagTypeDef"],
        "UpdateDate": datetime,
    },
    total=False,
)

ReservedInstancesModificationResultTypeDef = TypedDict(
    "ReservedInstancesModificationResultTypeDef",
    {
        "ReservedInstancesId": str,
        "TargetConfiguration": "ReservedInstancesConfigurationTypeDef",
    },
    total=False,
)

ReservedInstancesModificationTypeDef = TypedDict(
    "ReservedInstancesModificationTypeDef",
    {
        "ClientToken": str,
        "CreateDate": datetime,
        "EffectiveDate": datetime,
        "ModificationResults": List["ReservedInstancesModificationResultTypeDef"],
        "ReservedInstancesIds": List["ReservedInstancesIdTypeDef"],
        "ReservedInstancesModificationId": str,
        "Status": str,
        "StatusMessage": str,
        "UpdateDate": datetime,
    },
    total=False,
)

ReservedInstancesOfferingTypeDef = TypedDict(
    "ReservedInstancesOfferingTypeDef",
    {
        "AvailabilityZone": str,
        "Duration": int,
        "FixedPrice": float,
        "InstanceType": InstanceTypeType,
        "ProductDescription": RIProductDescriptionType,
        "ReservedInstancesOfferingId": str,
        "UsagePrice": float,
        "CurrencyCode": Literal["USD"],
        "InstanceTenancy": TenancyType,
        "Marketplace": bool,
        "OfferingClass": OfferingClassTypeType,
        "OfferingType": OfferingTypeValuesType,
        "PricingDetails": List["PricingDetailTypeDef"],
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "Scope": scopeType,
    },
    total=False,
)

ReservedInstancesTypeDef = TypedDict(
    "ReservedInstancesTypeDef",
    {
        "AvailabilityZone": str,
        "Duration": int,
        "End": datetime,
        "FixedPrice": float,
        "InstanceCount": int,
        "InstanceType": InstanceTypeType,
        "ProductDescription": RIProductDescriptionType,
        "ReservedInstancesId": str,
        "Start": datetime,
        "State": ReservedInstanceStateType,
        "UsagePrice": float,
        "CurrencyCode": Literal["USD"],
        "InstanceTenancy": TenancyType,
        "OfferingClass": OfferingClassTypeType,
        "OfferingType": OfferingTypeValuesType,
        "RecurringCharges": List["RecurringChargeTypeDef"],
        "Scope": scopeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredResetAddressAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredResetAddressAttributeRequestRequestTypeDef",
    {
        "AllocationId": str,
        "Attribute": Literal["domain-name"],
    },
)
_OptionalResetAddressAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalResetAddressAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ResetAddressAttributeRequestRequestTypeDef(
    _RequiredResetAddressAttributeRequestRequestTypeDef,
    _OptionalResetAddressAttributeRequestRequestTypeDef,
):
    pass

ResetAddressAttributeResultTypeDef = TypedDict(
    "ResetAddressAttributeResultTypeDef",
    {
        "Address": "AddressAttributeTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetEbsDefaultKmsKeyIdRequestRequestTypeDef = TypedDict(
    "ResetEbsDefaultKmsKeyIdRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

ResetEbsDefaultKmsKeyIdResultTypeDef = TypedDict(
    "ResetEbsDefaultKmsKeyIdResultTypeDef",
    {
        "KmsKeyId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResetFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredResetFpgaImageAttributeRequestRequestTypeDef",
    {
        "FpgaImageId": str,
    },
)
_OptionalResetFpgaImageAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalResetFpgaImageAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
        "Attribute": Literal["loadPermission"],
    },
    total=False,
)

class ResetFpgaImageAttributeRequestRequestTypeDef(
    _RequiredResetFpgaImageAttributeRequestRequestTypeDef,
    _OptionalResetFpgaImageAttributeRequestRequestTypeDef,
):
    pass

ResetFpgaImageAttributeResultTypeDef = TypedDict(
    "ResetFpgaImageAttributeResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredResetImageAttributeRequestImageTypeDef = TypedDict(
    "_RequiredResetImageAttributeRequestImageTypeDef",
    {
        "Attribute": Literal["launchPermission"],
    },
)
_OptionalResetImageAttributeRequestImageTypeDef = TypedDict(
    "_OptionalResetImageAttributeRequestImageTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ResetImageAttributeRequestImageTypeDef(
    _RequiredResetImageAttributeRequestImageTypeDef, _OptionalResetImageAttributeRequestImageTypeDef
):
    pass

_RequiredResetImageAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredResetImageAttributeRequestRequestTypeDef",
    {
        "Attribute": Literal["launchPermission"],
        "ImageId": str,
    },
)
_OptionalResetImageAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalResetImageAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ResetImageAttributeRequestRequestTypeDef(
    _RequiredResetImageAttributeRequestRequestTypeDef,
    _OptionalResetImageAttributeRequestRequestTypeDef,
):
    pass

_RequiredResetInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "_RequiredResetInstanceAttributeRequestInstanceTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
    },
)
_OptionalResetInstanceAttributeRequestInstanceTypeDef = TypedDict(
    "_OptionalResetInstanceAttributeRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ResetInstanceAttributeRequestInstanceTypeDef(
    _RequiredResetInstanceAttributeRequestInstanceTypeDef,
    _OptionalResetInstanceAttributeRequestInstanceTypeDef,
):
    pass

_RequiredResetInstanceAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredResetInstanceAttributeRequestRequestTypeDef",
    {
        "Attribute": InstanceAttributeNameType,
        "InstanceId": str,
    },
)
_OptionalResetInstanceAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalResetInstanceAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ResetInstanceAttributeRequestRequestTypeDef(
    _RequiredResetInstanceAttributeRequestRequestTypeDef,
    _OptionalResetInstanceAttributeRequestRequestTypeDef,
):
    pass

ResetNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef = TypedDict(
    "ResetNetworkInterfaceAttributeRequestNetworkInterfaceTypeDef",
    {
        "DryRun": bool,
        "SourceDestCheck": str,
    },
    total=False,
)

_RequiredResetNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredResetNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalResetNetworkInterfaceAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalResetNetworkInterfaceAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
        "SourceDestCheck": str,
    },
    total=False,
)

class ResetNetworkInterfaceAttributeRequestRequestTypeDef(
    _RequiredResetNetworkInterfaceAttributeRequestRequestTypeDef,
    _OptionalResetNetworkInterfaceAttributeRequestRequestTypeDef,
):
    pass

_RequiredResetSnapshotAttributeRequestRequestTypeDef = TypedDict(
    "_RequiredResetSnapshotAttributeRequestRequestTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
        "SnapshotId": str,
    },
)
_OptionalResetSnapshotAttributeRequestRequestTypeDef = TypedDict(
    "_OptionalResetSnapshotAttributeRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ResetSnapshotAttributeRequestRequestTypeDef(
    _RequiredResetSnapshotAttributeRequestRequestTypeDef,
    _OptionalResetSnapshotAttributeRequestRequestTypeDef,
):
    pass

_RequiredResetSnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "_RequiredResetSnapshotAttributeRequestSnapshotTypeDef",
    {
        "Attribute": SnapshotAttributeNameType,
    },
)
_OptionalResetSnapshotAttributeRequestSnapshotTypeDef = TypedDict(
    "_OptionalResetSnapshotAttributeRequestSnapshotTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class ResetSnapshotAttributeRequestSnapshotTypeDef(
    _RequiredResetSnapshotAttributeRequestSnapshotTypeDef,
    _OptionalResetSnapshotAttributeRequestSnapshotTypeDef,
):
    pass

ResourceStatementRequestTypeDef = TypedDict(
    "ResourceStatementRequestTypeDef",
    {
        "Resources": List[str],
        "ResourceTypes": List[str],
    },
    total=False,
)

ResourceStatementTypeDef = TypedDict(
    "ResourceStatementTypeDef",
    {
        "Resources": List[str],
        "ResourceTypes": List[str],
    },
    total=False,
)

ResponseErrorTypeDef = TypedDict(
    "ResponseErrorTypeDef",
    {
        "Code": LaunchTemplateErrorCodeType,
        "Message": str,
    },
    total=False,
)

ResponseLaunchTemplateDataTypeDef = TypedDict(
    "ResponseLaunchTemplateDataTypeDef",
    {
        "KernelId": str,
        "EbsOptimized": bool,
        "IamInstanceProfile": "LaunchTemplateIamInstanceProfileSpecificationTypeDef",
        "BlockDeviceMappings": List["LaunchTemplateBlockDeviceMappingTypeDef"],
        "NetworkInterfaces": List["LaunchTemplateInstanceNetworkInterfaceSpecificationTypeDef"],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KeyName": str,
        "Monitoring": "LaunchTemplatesMonitoringTypeDef",
        "Placement": "LaunchTemplatePlacementTypeDef",
        "RamDiskId": str,
        "DisableApiTermination": bool,
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "UserData": str,
        "TagSpecifications": List["LaunchTemplateTagSpecificationTypeDef"],
        "ElasticGpuSpecifications": List["ElasticGpuSpecificationResponseTypeDef"],
        "ElasticInferenceAccelerators": List[
            "LaunchTemplateElasticInferenceAcceleratorResponseTypeDef"
        ],
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "InstanceMarketOptions": "LaunchTemplateInstanceMarketOptionsTypeDef",
        "CreditSpecification": "CreditSpecificationTypeDef",
        "CpuOptions": "LaunchTemplateCpuOptionsTypeDef",
        "CapacityReservationSpecification": "LaunchTemplateCapacityReservationSpecificationResponseTypeDef",
        "LicenseSpecifications": List["LaunchTemplateLicenseConfigurationTypeDef"],
        "HibernationOptions": "LaunchTemplateHibernationOptionsTypeDef",
        "MetadataOptions": "LaunchTemplateInstanceMetadataOptionsTypeDef",
        "EnclaveOptions": "LaunchTemplateEnclaveOptionsTypeDef",
        "InstanceRequirements": "InstanceRequirementsTypeDef",
        "PrivateDnsNameOptions": "LaunchTemplatePrivateDnsNameOptionsTypeDef",
        "MaintenanceOptions": "LaunchTemplateInstanceMaintenanceOptionsTypeDef",
        "DisableApiStop": bool,
    },
    total=False,
)

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

_RequiredRestoreAddressToClassicRequestRequestTypeDef = TypedDict(
    "_RequiredRestoreAddressToClassicRequestRequestTypeDef",
    {
        "PublicIp": str,
    },
)
_OptionalRestoreAddressToClassicRequestRequestTypeDef = TypedDict(
    "_OptionalRestoreAddressToClassicRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RestoreAddressToClassicRequestRequestTypeDef(
    _RequiredRestoreAddressToClassicRequestRequestTypeDef,
    _OptionalRestoreAddressToClassicRequestRequestTypeDef,
):
    pass

RestoreAddressToClassicResultTypeDef = TypedDict(
    "RestoreAddressToClassicResultTypeDef",
    {
        "PublicIp": str,
        "Status": StatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreImageFromRecycleBinRequestRequestTypeDef = TypedDict(
    "_RequiredRestoreImageFromRecycleBinRequestRequestTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalRestoreImageFromRecycleBinRequestRequestTypeDef = TypedDict(
    "_OptionalRestoreImageFromRecycleBinRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RestoreImageFromRecycleBinRequestRequestTypeDef(
    _RequiredRestoreImageFromRecycleBinRequestRequestTypeDef,
    _OptionalRestoreImageFromRecycleBinRequestRequestTypeDef,
):
    pass

RestoreImageFromRecycleBinResultTypeDef = TypedDict(
    "RestoreImageFromRecycleBinResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreManagedPrefixListVersionRequestRequestTypeDef = TypedDict(
    "_RequiredRestoreManagedPrefixListVersionRequestRequestTypeDef",
    {
        "PrefixListId": str,
        "PreviousVersion": int,
        "CurrentVersion": int,
    },
)
_OptionalRestoreManagedPrefixListVersionRequestRequestTypeDef = TypedDict(
    "_OptionalRestoreManagedPrefixListVersionRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RestoreManagedPrefixListVersionRequestRequestTypeDef(
    _RequiredRestoreManagedPrefixListVersionRequestRequestTypeDef,
    _OptionalRestoreManagedPrefixListVersionRequestRequestTypeDef,
):
    pass

RestoreManagedPrefixListVersionResultTypeDef = TypedDict(
    "RestoreManagedPrefixListVersionResultTypeDef",
    {
        "PrefixList": "ManagedPrefixListTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreSnapshotFromRecycleBinRequestRequestTypeDef = TypedDict(
    "_RequiredRestoreSnapshotFromRecycleBinRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalRestoreSnapshotFromRecycleBinRequestRequestTypeDef = TypedDict(
    "_OptionalRestoreSnapshotFromRecycleBinRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class RestoreSnapshotFromRecycleBinRequestRequestTypeDef(
    _RequiredRestoreSnapshotFromRecycleBinRequestRequestTypeDef,
    _OptionalRestoreSnapshotFromRecycleBinRequestRequestTypeDef,
):
    pass

RestoreSnapshotFromRecycleBinResultTypeDef = TypedDict(
    "RestoreSnapshotFromRecycleBinResultTypeDef",
    {
        "SnapshotId": str,
        "OutpostArn": str,
        "Description": str,
        "Encrypted": bool,
        "OwnerId": str,
        "Progress": str,
        "StartTime": datetime,
        "State": SnapshotStateType,
        "VolumeId": str,
        "VolumeSize": int,
        "SseType": SSETypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRestoreSnapshotTierRequestRequestTypeDef = TypedDict(
    "_RequiredRestoreSnapshotTierRequestRequestTypeDef",
    {
        "SnapshotId": str,
    },
)
_OptionalRestoreSnapshotTierRequestRequestTypeDef = TypedDict(
    "_OptionalRestoreSnapshotTierRequestRequestTypeDef",
    {
        "TemporaryRestoreDays": int,
        "PermanentRestore": bool,
        "DryRun": bool,
    },
    total=False,
)

class RestoreSnapshotTierRequestRequestTypeDef(
    _RequiredRestoreSnapshotTierRequestRequestTypeDef,
    _OptionalRestoreSnapshotTierRequestRequestTypeDef,
):
    pass

RestoreSnapshotTierResultTypeDef = TypedDict(
    "RestoreSnapshotTierResultTypeDef",
    {
        "SnapshotId": str,
        "RestoreStartTime": datetime,
        "RestoreDuration": int,
        "IsPermanentRestore": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRevokeClientVpnIngressRequestRequestTypeDef = TypedDict(
    "_RequiredRevokeClientVpnIngressRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
        "TargetNetworkCidr": str,
    },
)
_OptionalRevokeClientVpnIngressRequestRequestTypeDef = TypedDict(
    "_OptionalRevokeClientVpnIngressRequestRequestTypeDef",
    {
        "AccessGroupId": str,
        "RevokeAllGroups": bool,
        "DryRun": bool,
    },
    total=False,
)

class RevokeClientVpnIngressRequestRequestTypeDef(
    _RequiredRevokeClientVpnIngressRequestRequestTypeDef,
    _OptionalRevokeClientVpnIngressRequestRequestTypeDef,
):
    pass

RevokeClientVpnIngressResultTypeDef = TypedDict(
    "RevokeClientVpnIngressResultTypeDef",
    {
        "Status": "ClientVpnAuthorizationRuleStatusTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredRevokeSecurityGroupEgressRequestRequestTypeDef = TypedDict(
    "_RequiredRevokeSecurityGroupEgressRequestRequestTypeDef",
    {
        "GroupId": str,
    },
)
_OptionalRevokeSecurityGroupEgressRequestRequestTypeDef = TypedDict(
    "_OptionalRevokeSecurityGroupEgressRequestRequestTypeDef",
    {
        "DryRun": bool,
        "IpPermissions": List["IpPermissionTypeDef"],
        "SecurityGroupRuleIds": List[str],
        "CidrIp": str,
        "FromPort": int,
        "IpProtocol": str,
        "ToPort": int,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
    },
    total=False,
)

class RevokeSecurityGroupEgressRequestRequestTypeDef(
    _RequiredRevokeSecurityGroupEgressRequestRequestTypeDef,
    _OptionalRevokeSecurityGroupEgressRequestRequestTypeDef,
):
    pass

RevokeSecurityGroupEgressRequestSecurityGroupTypeDef = TypedDict(
    "RevokeSecurityGroupEgressRequestSecurityGroupTypeDef",
    {
        "DryRun": bool,
        "IpPermissions": List["IpPermissionTypeDef"],
        "SecurityGroupRuleIds": List[str],
        "CidrIp": str,
        "FromPort": int,
        "IpProtocol": str,
        "ToPort": int,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
    },
    total=False,
)

RevokeSecurityGroupEgressResultTypeDef = TypedDict(
    "RevokeSecurityGroupEgressResultTypeDef",
    {
        "Return": bool,
        "UnknownIpPermissions": List["IpPermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RevokeSecurityGroupIngressRequestRequestTypeDef = TypedDict(
    "RevokeSecurityGroupIngressRequestRequestTypeDef",
    {
        "CidrIp": str,
        "FromPort": int,
        "GroupId": str,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "IpProtocol": str,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
        "ToPort": int,
        "DryRun": bool,
        "SecurityGroupRuleIds": List[str],
    },
    total=False,
)

RevokeSecurityGroupIngressRequestSecurityGroupTypeDef = TypedDict(
    "RevokeSecurityGroupIngressRequestSecurityGroupTypeDef",
    {
        "CidrIp": str,
        "FromPort": int,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "IpProtocol": str,
        "SourceSecurityGroupName": str,
        "SourceSecurityGroupOwnerId": str,
        "ToPort": int,
        "DryRun": bool,
        "SecurityGroupRuleIds": List[str],
    },
    total=False,
)

RevokeSecurityGroupIngressResultTypeDef = TypedDict(
    "RevokeSecurityGroupIngressResultTypeDef",
    {
        "Return": bool,
        "UnknownIpPermissions": List["IpPermissionTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RouteTableAssociationStateTypeDef = TypedDict(
    "RouteTableAssociationStateTypeDef",
    {
        "State": RouteTableAssociationStateCodeType,
        "StatusMessage": str,
    },
    total=False,
)

RouteTableAssociationTypeDef = TypedDict(
    "RouteTableAssociationTypeDef",
    {
        "Main": bool,
        "RouteTableAssociationId": str,
        "RouteTableId": str,
        "SubnetId": str,
        "GatewayId": str,
        "AssociationState": "RouteTableAssociationStateTypeDef",
    },
    total=False,
)

RouteTableTypeDef = TypedDict(
    "RouteTableTypeDef",
    {
        "Associations": List["RouteTableAssociationTypeDef"],
        "PropagatingVgws": List["PropagatingVgwTypeDef"],
        "RouteTableId": str,
        "Routes": List["RouteTypeDef"],
        "Tags": List["TagTypeDef"],
        "VpcId": str,
        "OwnerId": str,
    },
    total=False,
)

RouteTypeDef = TypedDict(
    "RouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "DestinationIpv6CidrBlock": str,
        "DestinationPrefixListId": str,
        "EgressOnlyInternetGatewayId": str,
        "GatewayId": str,
        "InstanceId": str,
        "InstanceOwnerId": str,
        "NatGatewayId": str,
        "TransitGatewayId": str,
        "LocalGatewayId": str,
        "CarrierGatewayId": str,
        "NetworkInterfaceId": str,
        "Origin": RouteOriginType,
        "State": RouteStateType,
        "VpcPeeringConnectionId": str,
        "CoreNetworkArn": str,
    },
    total=False,
)

RuleGroupRuleOptionsPairTypeDef = TypedDict(
    "RuleGroupRuleOptionsPairTypeDef",
    {
        "RuleGroupArn": str,
        "RuleOptions": List["RuleOptionTypeDef"],
    },
    total=False,
)

RuleGroupTypePairTypeDef = TypedDict(
    "RuleGroupTypePairTypeDef",
    {
        "RuleGroupArn": str,
        "RuleGroupType": str,
    },
    total=False,
)

RuleOptionTypeDef = TypedDict(
    "RuleOptionTypeDef",
    {
        "Keyword": str,
        "Settings": List[str],
    },
    total=False,
)

RunInstancesMonitoringEnabledTypeDef = TypedDict(
    "RunInstancesMonitoringEnabledTypeDef",
    {
        "Enabled": bool,
    },
)

_RequiredRunInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredRunInstancesRequestRequestTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
    },
)
_OptionalRunInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalRunInstancesRequestRequestTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
        "Placement": "PlacementTypeDef",
        "RamdiskId": str,
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "SubnetId": str,
        "UserData": str,
        "AdditionalInfo": str,
        "ClientToken": str,
        "DisableApiTermination": bool,
        "DryRun": bool,
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "PrivateIpAddress": str,
        "ElasticGpuSpecification": List["ElasticGpuSpecificationTypeDef"],
        "ElasticInferenceAccelerators": List["ElasticInferenceAcceleratorTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "InstanceMarketOptions": "InstanceMarketOptionsRequestTypeDef",
        "CreditSpecification": "CreditSpecificationRequestTypeDef",
        "CpuOptions": "CpuOptionsRequestTypeDef",
        "CapacityReservationSpecification": "CapacityReservationSpecificationTypeDef",
        "HibernationOptions": "HibernationOptionsRequestTypeDef",
        "LicenseSpecifications": List["LicenseConfigurationRequestTypeDef"],
        "MetadataOptions": "InstanceMetadataOptionsRequestTypeDef",
        "EnclaveOptions": "EnclaveOptionsRequestTypeDef",
        "PrivateDnsNameOptions": "PrivateDnsNameOptionsRequestTypeDef",
        "MaintenanceOptions": "InstanceMaintenanceOptionsRequestTypeDef",
        "DisableApiStop": bool,
        "EnablePrimaryIpv6": bool,
    },
    total=False,
)

class RunInstancesRequestRequestTypeDef(
    _RequiredRunInstancesRequestRequestTypeDef, _OptionalRunInstancesRequestRequestTypeDef
):
    pass

_RequiredRunInstancesRequestServiceResourceTypeDef = TypedDict(
    "_RequiredRunInstancesRequestServiceResourceTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
    },
)
_OptionalRunInstancesRequestServiceResourceTypeDef = TypedDict(
    "_OptionalRunInstancesRequestServiceResourceTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
        "Placement": "PlacementTypeDef",
        "RamdiskId": str,
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "SubnetId": str,
        "UserData": str,
        "AdditionalInfo": str,
        "ClientToken": str,
        "DisableApiTermination": bool,
        "DryRun": bool,
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "PrivateIpAddress": str,
        "ElasticGpuSpecification": List["ElasticGpuSpecificationTypeDef"],
        "ElasticInferenceAccelerators": List["ElasticInferenceAcceleratorTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "InstanceMarketOptions": "InstanceMarketOptionsRequestTypeDef",
        "CreditSpecification": "CreditSpecificationRequestTypeDef",
        "CpuOptions": "CpuOptionsRequestTypeDef",
        "CapacityReservationSpecification": "CapacityReservationSpecificationTypeDef",
        "HibernationOptions": "HibernationOptionsRequestTypeDef",
        "LicenseSpecifications": List["LicenseConfigurationRequestTypeDef"],
        "MetadataOptions": "InstanceMetadataOptionsRequestTypeDef",
        "EnclaveOptions": "EnclaveOptionsRequestTypeDef",
        "PrivateDnsNameOptions": "PrivateDnsNameOptionsRequestTypeDef",
        "MaintenanceOptions": "InstanceMaintenanceOptionsRequestTypeDef",
        "DisableApiStop": bool,
        "EnablePrimaryIpv6": bool,
    },
    total=False,
)

class RunInstancesRequestServiceResourceTypeDef(
    _RequiredRunInstancesRequestServiceResourceTypeDef,
    _OptionalRunInstancesRequestServiceResourceTypeDef,
):
    pass

_RequiredRunInstancesRequestSubnetTypeDef = TypedDict(
    "_RequiredRunInstancesRequestSubnetTypeDef",
    {
        "MaxCount": int,
        "MinCount": int,
    },
)
_OptionalRunInstancesRequestSubnetTypeDef = TypedDict(
    "_OptionalRunInstancesRequestSubnetTypeDef",
    {
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["InstanceIpv6AddressTypeDef"],
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "RunInstancesMonitoringEnabledTypeDef",
        "Placement": "PlacementTypeDef",
        "RamdiskId": str,
        "SecurityGroupIds": List[str],
        "SecurityGroups": List[str],
        "UserData": str,
        "AdditionalInfo": str,
        "ClientToken": str,
        "DisableApiTermination": bool,
        "DryRun": bool,
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "InstanceInitiatedShutdownBehavior": ShutdownBehaviorType,
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "PrivateIpAddress": str,
        "ElasticGpuSpecification": List["ElasticGpuSpecificationTypeDef"],
        "ElasticInferenceAccelerators": List["ElasticInferenceAcceleratorTypeDef"],
        "TagSpecifications": List["TagSpecificationTypeDef"],
        "LaunchTemplate": "LaunchTemplateSpecificationTypeDef",
        "InstanceMarketOptions": "InstanceMarketOptionsRequestTypeDef",
        "CreditSpecification": "CreditSpecificationRequestTypeDef",
        "CpuOptions": "CpuOptionsRequestTypeDef",
        "CapacityReservationSpecification": "CapacityReservationSpecificationTypeDef",
        "HibernationOptions": "HibernationOptionsRequestTypeDef",
        "LicenseSpecifications": List["LicenseConfigurationRequestTypeDef"],
        "MetadataOptions": "InstanceMetadataOptionsRequestTypeDef",
        "EnclaveOptions": "EnclaveOptionsRequestTypeDef",
        "PrivateDnsNameOptions": "PrivateDnsNameOptionsRequestTypeDef",
        "MaintenanceOptions": "InstanceMaintenanceOptionsRequestTypeDef",
        "DisableApiStop": bool,
        "EnablePrimaryIpv6": bool,
    },
    total=False,
)

class RunInstancesRequestSubnetTypeDef(
    _RequiredRunInstancesRequestSubnetTypeDef, _OptionalRunInstancesRequestSubnetTypeDef
):
    pass

_RequiredRunScheduledInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredRunScheduledInstancesRequestRequestTypeDef",
    {
        "LaunchSpecification": "ScheduledInstancesLaunchSpecificationTypeDef",
        "ScheduledInstanceId": str,
    },
)
_OptionalRunScheduledInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalRunScheduledInstancesRequestRequestTypeDef",
    {
        "ClientToken": str,
        "DryRun": bool,
        "InstanceCount": int,
    },
    total=False,
)

class RunScheduledInstancesRequestRequestTypeDef(
    _RequiredRunScheduledInstancesRequestRequestTypeDef,
    _OptionalRunScheduledInstancesRequestRequestTypeDef,
):
    pass

RunScheduledInstancesResultTypeDef = TypedDict(
    "RunScheduledInstancesResultTypeDef",
    {
        "InstanceIdSet": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

S3ObjectTagTypeDef = TypedDict(
    "S3ObjectTagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
    total=False,
)

S3StorageTypeDef = TypedDict(
    "S3StorageTypeDef",
    {
        "AWSAccessKeyId": str,
        "Bucket": str,
        "Prefix": str,
        "UploadPolicy": Union[bytes, IO[bytes], StreamingBody],
        "UploadPolicySignature": str,
    },
    total=False,
)

ScheduledInstanceAvailabilityTypeDef = TypedDict(
    "ScheduledInstanceAvailabilityTypeDef",
    {
        "AvailabilityZone": str,
        "AvailableInstanceCount": int,
        "FirstSlotStartTime": datetime,
        "HourlyPrice": str,
        "InstanceType": str,
        "MaxTermDurationInDays": int,
        "MinTermDurationInDays": int,
        "NetworkPlatform": str,
        "Platform": str,
        "PurchaseToken": str,
        "Recurrence": "ScheduledInstanceRecurrenceTypeDef",
        "SlotDurationInHours": int,
        "TotalScheduledInstanceHours": int,
    },
    total=False,
)

ScheduledInstanceRecurrenceRequestTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceRequestTypeDef",
    {
        "Frequency": str,
        "Interval": int,
        "OccurrenceDays": List[int],
        "OccurrenceRelativeToEnd": bool,
        "OccurrenceUnit": str,
    },
    total=False,
)

ScheduledInstanceRecurrenceTypeDef = TypedDict(
    "ScheduledInstanceRecurrenceTypeDef",
    {
        "Frequency": str,
        "Interval": int,
        "OccurrenceDaySet": List[int],
        "OccurrenceRelativeToEnd": bool,
        "OccurrenceUnit": str,
    },
    total=False,
)

ScheduledInstanceTypeDef = TypedDict(
    "ScheduledInstanceTypeDef",
    {
        "AvailabilityZone": str,
        "CreateDate": datetime,
        "HourlyPrice": str,
        "InstanceCount": int,
        "InstanceType": str,
        "NetworkPlatform": str,
        "NextSlotStartTime": datetime,
        "Platform": str,
        "PreviousSlotEndTime": datetime,
        "Recurrence": "ScheduledInstanceRecurrenceTypeDef",
        "ScheduledInstanceId": str,
        "SlotDurationInHours": int,
        "TermEndDate": datetime,
        "TermStartDate": datetime,
        "TotalScheduledInstanceHours": int,
    },
    total=False,
)

ScheduledInstancesBlockDeviceMappingTypeDef = TypedDict(
    "ScheduledInstancesBlockDeviceMappingTypeDef",
    {
        "DeviceName": str,
        "Ebs": "ScheduledInstancesEbsTypeDef",
        "NoDevice": str,
        "VirtualName": str,
    },
    total=False,
)

ScheduledInstancesEbsTypeDef = TypedDict(
    "ScheduledInstancesEbsTypeDef",
    {
        "DeleteOnTermination": bool,
        "Encrypted": bool,
        "Iops": int,
        "SnapshotId": str,
        "VolumeSize": int,
        "VolumeType": str,
    },
    total=False,
)

ScheduledInstancesIamInstanceProfileTypeDef = TypedDict(
    "ScheduledInstancesIamInstanceProfileTypeDef",
    {
        "Arn": str,
        "Name": str,
    },
    total=False,
)

ScheduledInstancesIpv6AddressTypeDef = TypedDict(
    "ScheduledInstancesIpv6AddressTypeDef",
    {
        "Ipv6Address": str,
    },
    total=False,
)

_RequiredScheduledInstancesLaunchSpecificationTypeDef = TypedDict(
    "_RequiredScheduledInstancesLaunchSpecificationTypeDef",
    {
        "ImageId": str,
    },
)
_OptionalScheduledInstancesLaunchSpecificationTypeDef = TypedDict(
    "_OptionalScheduledInstancesLaunchSpecificationTypeDef",
    {
        "BlockDeviceMappings": List["ScheduledInstancesBlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "ScheduledInstancesIamInstanceProfileTypeDef",
        "InstanceType": str,
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "ScheduledInstancesMonitoringTypeDef",
        "NetworkInterfaces": List["ScheduledInstancesNetworkInterfaceTypeDef"],
        "Placement": "ScheduledInstancesPlacementTypeDef",
        "RamdiskId": str,
        "SecurityGroupIds": List[str],
        "SubnetId": str,
        "UserData": str,
    },
    total=False,
)

class ScheduledInstancesLaunchSpecificationTypeDef(
    _RequiredScheduledInstancesLaunchSpecificationTypeDef,
    _OptionalScheduledInstancesLaunchSpecificationTypeDef,
):
    pass

ScheduledInstancesMonitoringTypeDef = TypedDict(
    "ScheduledInstancesMonitoringTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

ScheduledInstancesNetworkInterfaceTypeDef = TypedDict(
    "ScheduledInstancesNetworkInterfaceTypeDef",
    {
        "AssociatePublicIpAddress": bool,
        "DeleteOnTermination": bool,
        "Description": str,
        "DeviceIndex": int,
        "Groups": List[str],
        "Ipv6AddressCount": int,
        "Ipv6Addresses": List["ScheduledInstancesIpv6AddressTypeDef"],
        "NetworkInterfaceId": str,
        "PrivateIpAddress": str,
        "PrivateIpAddressConfigs": List["ScheduledInstancesPrivateIpAddressConfigTypeDef"],
        "SecondaryPrivateIpAddressCount": int,
        "SubnetId": str,
    },
    total=False,
)

ScheduledInstancesPlacementTypeDef = TypedDict(
    "ScheduledInstancesPlacementTypeDef",
    {
        "AvailabilityZone": str,
        "GroupName": str,
    },
    total=False,
)

ScheduledInstancesPrivateIpAddressConfigTypeDef = TypedDict(
    "ScheduledInstancesPrivateIpAddressConfigTypeDef",
    {
        "Primary": bool,
        "PrivateIpAddress": str,
    },
    total=False,
)

_RequiredSearchLocalGatewayRoutesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchLocalGatewayRoutesRequestRequestTypeDef",
    {
        "LocalGatewayRouteTableId": str,
    },
)
_OptionalSearchLocalGatewayRoutesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchLocalGatewayRoutesRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class SearchLocalGatewayRoutesRequestRequestTypeDef(
    _RequiredSearchLocalGatewayRoutesRequestRequestTypeDef,
    _OptionalSearchLocalGatewayRoutesRequestRequestTypeDef,
):
    pass

SearchLocalGatewayRoutesResultTypeDef = TypedDict(
    "SearchLocalGatewayRoutesResultTypeDef",
    {
        "Routes": List["LocalGatewayRouteTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchTransitGatewayMulticastGroupsRequestRequestTypeDef = TypedDict(
    "_RequiredSearchTransitGatewayMulticastGroupsRequestRequestTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
    },
)
_OptionalSearchTransitGatewayMulticastGroupsRequestRequestTypeDef = TypedDict(
    "_OptionalSearchTransitGatewayMulticastGroupsRequestRequestTypeDef",
    {
        "Filters": List["FilterTypeDef"],
        "MaxResults": int,
        "NextToken": str,
        "DryRun": bool,
    },
    total=False,
)

class SearchTransitGatewayMulticastGroupsRequestRequestTypeDef(
    _RequiredSearchTransitGatewayMulticastGroupsRequestRequestTypeDef,
    _OptionalSearchTransitGatewayMulticastGroupsRequestRequestTypeDef,
):
    pass

SearchTransitGatewayMulticastGroupsResultTypeDef = TypedDict(
    "SearchTransitGatewayMulticastGroupsResultTypeDef",
    {
        "MulticastGroups": List["TransitGatewayMulticastGroupTypeDef"],
        "NextToken": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredSearchTransitGatewayRoutesRequestRequestTypeDef = TypedDict(
    "_RequiredSearchTransitGatewayRoutesRequestRequestTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "Filters": List["FilterTypeDef"],
    },
)
_OptionalSearchTransitGatewayRoutesRequestRequestTypeDef = TypedDict(
    "_OptionalSearchTransitGatewayRoutesRequestRequestTypeDef",
    {
        "MaxResults": int,
        "DryRun": bool,
    },
    total=False,
)

class SearchTransitGatewayRoutesRequestRequestTypeDef(
    _RequiredSearchTransitGatewayRoutesRequestRequestTypeDef,
    _OptionalSearchTransitGatewayRoutesRequestRequestTypeDef,
):
    pass

SearchTransitGatewayRoutesResultTypeDef = TypedDict(
    "SearchTransitGatewayRoutesResultTypeDef",
    {
        "Routes": List["TransitGatewayRouteTypeDef"],
        "AdditionalRoutesAvailable": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SecurityGroupForVpcTypeDef = TypedDict(
    "SecurityGroupForVpcTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "OwnerId": str,
        "GroupId": str,
        "Tags": List["TagTypeDef"],
        "PrimaryVpcId": str,
    },
    total=False,
)

SecurityGroupIdentifierTypeDef = TypedDict(
    "SecurityGroupIdentifierTypeDef",
    {
        "GroupId": str,
        "GroupName": str,
    },
    total=False,
)

SecurityGroupReferenceTypeDef = TypedDict(
    "SecurityGroupReferenceTypeDef",
    {
        "GroupId": str,
        "ReferencingVpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

SecurityGroupRuleDescriptionTypeDef = TypedDict(
    "SecurityGroupRuleDescriptionTypeDef",
    {
        "SecurityGroupRuleId": str,
        "Description": str,
    },
    total=False,
)

SecurityGroupRuleRequestTypeDef = TypedDict(
    "SecurityGroupRuleRequestTypeDef",
    {
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "CidrIpv4": str,
        "CidrIpv6": str,
        "PrefixListId": str,
        "ReferencedGroupId": str,
        "Description": str,
    },
    total=False,
)

SecurityGroupRuleTypeDef = TypedDict(
    "SecurityGroupRuleTypeDef",
    {
        "SecurityGroupRuleId": str,
        "GroupId": str,
        "GroupOwnerId": str,
        "IsEgress": bool,
        "IpProtocol": str,
        "FromPort": int,
        "ToPort": int,
        "CidrIpv4": str,
        "CidrIpv6": str,
        "PrefixListId": str,
        "ReferencedGroupInfo": "ReferencedSecurityGroupTypeDef",
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredSecurityGroupRuleUpdateTypeDef = TypedDict(
    "_RequiredSecurityGroupRuleUpdateTypeDef",
    {
        "SecurityGroupRuleId": str,
    },
)
_OptionalSecurityGroupRuleUpdateTypeDef = TypedDict(
    "_OptionalSecurityGroupRuleUpdateTypeDef",
    {
        "SecurityGroupRule": "SecurityGroupRuleRequestTypeDef",
    },
    total=False,
)

class SecurityGroupRuleUpdateTypeDef(
    _RequiredSecurityGroupRuleUpdateTypeDef, _OptionalSecurityGroupRuleUpdateTypeDef
):
    pass

SecurityGroupTypeDef = TypedDict(
    "SecurityGroupTypeDef",
    {
        "Description": str,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "OwnerId": str,
        "GroupId": str,
        "IpPermissionsEgress": List["IpPermissionTypeDef"],
        "Tags": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

_RequiredSendDiagnosticInterruptRequestRequestTypeDef = TypedDict(
    "_RequiredSendDiagnosticInterruptRequestRequestTypeDef",
    {
        "InstanceId": str,
    },
)
_OptionalSendDiagnosticInterruptRequestRequestTypeDef = TypedDict(
    "_OptionalSendDiagnosticInterruptRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class SendDiagnosticInterruptRequestRequestTypeDef(
    _RequiredSendDiagnosticInterruptRequestRequestTypeDef,
    _OptionalSendDiagnosticInterruptRequestRequestTypeDef,
):
    pass

ServiceConfigurationTypeDef = TypedDict(
    "ServiceConfigurationTypeDef",
    {
        "ServiceType": List["ServiceTypeDetailTypeDef"],
        "ServiceId": str,
        "ServiceName": str,
        "ServiceState": ServiceStateType,
        "AvailabilityZones": List[str],
        "AcceptanceRequired": bool,
        "ManagesVpcEndpoints": bool,
        "NetworkLoadBalancerArns": List[str],
        "GatewayLoadBalancerArns": List[str],
        "SupportedIpAddressTypes": List[ServiceConnectivityTypeType],
        "BaseEndpointDnsNames": List[str],
        "PrivateDnsName": str,
        "PrivateDnsNameConfiguration": "PrivateDnsNameConfigurationTypeDef",
        "PayerResponsibility": Literal["ServiceOwner"],
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

ServiceDetailTypeDef = TypedDict(
    "ServiceDetailTypeDef",
    {
        "ServiceName": str,
        "ServiceId": str,
        "ServiceType": List["ServiceTypeDetailTypeDef"],
        "AvailabilityZones": List[str],
        "Owner": str,
        "BaseEndpointDnsNames": List[str],
        "PrivateDnsName": str,
        "PrivateDnsNames": List["PrivateDnsDetailsTypeDef"],
        "VpcEndpointPolicySupported": bool,
        "AcceptanceRequired": bool,
        "ManagesVpcEndpoints": bool,
        "PayerResponsibility": Literal["ServiceOwner"],
        "Tags": List["TagTypeDef"],
        "PrivateDnsNameVerificationState": DnsNameStateType,
        "SupportedIpAddressTypes": List[ServiceConnectivityTypeType],
    },
    total=False,
)

ServiceResourceClassicAddressRequestTypeDef = TypedDict(
    "ServiceResourceClassicAddressRequestTypeDef",
    {
        "public_ip": str,
    },
)

ServiceResourceDhcpOptionsRequestTypeDef = TypedDict(
    "ServiceResourceDhcpOptionsRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceImageRequestTypeDef = TypedDict(
    "ServiceResourceImageRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceInstanceRequestTypeDef = TypedDict(
    "ServiceResourceInstanceRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceInternetGatewayRequestTypeDef = TypedDict(
    "ServiceResourceInternetGatewayRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceKeyPairRequestTypeDef = TypedDict(
    "ServiceResourceKeyPairRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceNetworkAclRequestTypeDef = TypedDict(
    "ServiceResourceNetworkAclRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceNetworkInterfaceAssociationRequestTypeDef = TypedDict(
    "ServiceResourceNetworkInterfaceAssociationRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceNetworkInterfaceRequestTypeDef = TypedDict(
    "ServiceResourceNetworkInterfaceRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourcePlacementGroupRequestTypeDef = TypedDict(
    "ServiceResourcePlacementGroupRequestTypeDef",
    {
        "name": str,
    },
)

ServiceResourceRouteRequestTypeDef = TypedDict(
    "ServiceResourceRouteRequestTypeDef",
    {
        "route_table_id": str,
        "destination_cidr_block": str,
    },
)

ServiceResourceRouteTableAssociationRequestTypeDef = TypedDict(
    "ServiceResourceRouteTableAssociationRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceRouteTableRequestTypeDef = TypedDict(
    "ServiceResourceRouteTableRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceSecurityGroupRequestTypeDef = TypedDict(
    "ServiceResourceSecurityGroupRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceSnapshotRequestTypeDef = TypedDict(
    "ServiceResourceSnapshotRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceSubnetRequestTypeDef = TypedDict(
    "ServiceResourceSubnetRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceTagRequestTypeDef = TypedDict(
    "ServiceResourceTagRequestTypeDef",
    {
        "resource_id": str,
        "key": str,
        "value": str,
    },
)

ServiceResourceVolumeRequestTypeDef = TypedDict(
    "ServiceResourceVolumeRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceVpcAddressRequestTypeDef = TypedDict(
    "ServiceResourceVpcAddressRequestTypeDef",
    {
        "allocation_id": str,
    },
)

ServiceResourceVpcPeeringConnectionRequestTypeDef = TypedDict(
    "ServiceResourceVpcPeeringConnectionRequestTypeDef",
    {
        "id": str,
    },
)

ServiceResourceVpcRequestTypeDef = TypedDict(
    "ServiceResourceVpcRequestTypeDef",
    {
        "id": str,
    },
)

ServiceTypeDetailTypeDef = TypedDict(
    "ServiceTypeDetailTypeDef",
    {
        "ServiceType": ServiceTypeType,
    },
    total=False,
)

SlotDateTimeRangeRequestTypeDef = TypedDict(
    "SlotDateTimeRangeRequestTypeDef",
    {
        "EarliestTime": Union[datetime, str],
        "LatestTime": Union[datetime, str],
    },
)

SlotStartTimeRangeRequestTypeDef = TypedDict(
    "SlotStartTimeRangeRequestTypeDef",
    {
        "EarliestTime": Union[datetime, str],
        "LatestTime": Union[datetime, str],
    },
    total=False,
)

SnapshotDetailTypeDef = TypedDict(
    "SnapshotDetailTypeDef",
    {
        "Description": str,
        "DeviceName": str,
        "DiskImageSize": float,
        "Format": str,
        "Progress": str,
        "SnapshotId": str,
        "Status": str,
        "StatusMessage": str,
        "Url": str,
        "UserBucket": "UserBucketDetailsTypeDef",
    },
    total=False,
)

SnapshotDiskContainerTypeDef = TypedDict(
    "SnapshotDiskContainerTypeDef",
    {
        "Description": str,
        "Format": str,
        "Url": str,
        "UserBucket": "UserBucketTypeDef",
    },
    total=False,
)

SnapshotInfoTypeDef = TypedDict(
    "SnapshotInfoTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
        "Encrypted": bool,
        "VolumeId": str,
        "State": SnapshotStateType,
        "VolumeSize": int,
        "StartTime": datetime,
        "Progress": str,
        "OwnerId": str,
        "SnapshotId": str,
        "OutpostArn": str,
        "SseType": SSETypeType,
    },
    total=False,
)

SnapshotRecycleBinInfoTypeDef = TypedDict(
    "SnapshotRecycleBinInfoTypeDef",
    {
        "SnapshotId": str,
        "RecycleBinEnterTime": datetime,
        "RecycleBinExitTime": datetime,
        "Description": str,
        "VolumeId": str,
    },
    total=False,
)

SnapshotResponseMetadataTypeDef = TypedDict(
    "SnapshotResponseMetadataTypeDef",
    {
        "DataEncryptionKeyId": str,
        "Description": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OwnerId": str,
        "Progress": str,
        "SnapshotId": str,
        "StartTime": datetime,
        "State": SnapshotStateType,
        "StateMessage": str,
        "VolumeId": str,
        "VolumeSize": int,
        "OwnerAlias": str,
        "OutpostArn": str,
        "Tags": List["TagTypeDef"],
        "StorageTier": StorageTierType,
        "RestoreExpiryTime": datetime,
        "SseType": SSETypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SnapshotTaskDetailTypeDef = TypedDict(
    "SnapshotTaskDetailTypeDef",
    {
        "Description": str,
        "DiskImageSize": float,
        "Encrypted": bool,
        "Format": str,
        "KmsKeyId": str,
        "Progress": str,
        "SnapshotId": str,
        "Status": str,
        "StatusMessage": str,
        "Url": str,
        "UserBucket": "UserBucketDetailsTypeDef",
    },
    total=False,
)

SnapshotTierStatusTypeDef = TypedDict(
    "SnapshotTierStatusTypeDef",
    {
        "SnapshotId": str,
        "VolumeId": str,
        "Status": SnapshotStateType,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
        "StorageTier": StorageTierType,
        "LastTieringStartTime": datetime,
        "LastTieringProgress": int,
        "LastTieringOperationStatus": TieringOperationStatusType,
        "LastTieringOperationStatusDetail": str,
        "ArchivalCompleteTime": datetime,
        "RestoreExpiryTime": datetime,
    },
    total=False,
)

SnapshotTypeDef = TypedDict(
    "SnapshotTypeDef",
    {
        "DataEncryptionKeyId": str,
        "Description": str,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OwnerId": str,
        "Progress": str,
        "SnapshotId": str,
        "StartTime": datetime,
        "State": SnapshotStateType,
        "StateMessage": str,
        "VolumeId": str,
        "VolumeSize": int,
        "OwnerAlias": str,
        "OutpostArn": str,
        "Tags": List["TagTypeDef"],
        "StorageTier": StorageTierType,
        "RestoreExpiryTime": datetime,
        "SseType": SSETypeType,
    },
    total=False,
)

SpotCapacityRebalanceTypeDef = TypedDict(
    "SpotCapacityRebalanceTypeDef",
    {
        "ReplacementStrategy": ReplacementStrategyType,
        "TerminationDelay": int,
    },
    total=False,
)

SpotDatafeedSubscriptionTypeDef = TypedDict(
    "SpotDatafeedSubscriptionTypeDef",
    {
        "Bucket": str,
        "Fault": "SpotInstanceStateFaultTypeDef",
        "OwnerId": str,
        "Prefix": str,
        "State": DatafeedSubscriptionStateType,
    },
    total=False,
)

SpotFleetLaunchSpecificationTypeDef = TypedDict(
    "SpotFleetLaunchSpecificationTypeDef",
    {
        "SecurityGroups": List["GroupIdentifierTypeDef"],
        "AddressingType": str,
        "BlockDeviceMappings": List["BlockDeviceMappingTypeDef"],
        "EbsOptimized": bool,
        "IamInstanceProfile": "IamInstanceProfileSpecificationTypeDef",
        "ImageId": str,
        "InstanceType": InstanceTypeType,
        "KernelId": str,
        "KeyName": str,
        "Monitoring": "SpotFleetMonitoringTypeDef",
        "NetworkInterfaces": List["InstanceNetworkInterfaceSpecificationTypeDef"],
        "Placement": "SpotPlacementTypeDef",
        "RamdiskId": str,
        "SpotPrice": str,
        "SubnetId": str,
        "UserData": str,
        "WeightedCapacity": float,
        "TagSpecifications": List["SpotFleetTagSpecificationTypeDef"],
        "InstanceRequirements": "InstanceRequirementsTypeDef",
    },
    total=False,
)

SpotFleetMonitoringTypeDef = TypedDict(
    "SpotFleetMonitoringTypeDef",
    {
        "Enabled": bool,
    },
    total=False,
)

_RequiredSpotFleetRequestConfigDataTypeDef = TypedDict(
    "_RequiredSpotFleetRequestConfigDataTypeDef",
    {
        "IamFleetRole": str,
        "TargetCapacity": int,
    },
)
_OptionalSpotFleetRequestConfigDataTypeDef = TypedDict(
    "_OptionalSpotFleetRequestConfigDataTypeDef",
    {
        "AllocationStrategy": AllocationStrategyType,
        "OnDemandAllocationStrategy": OnDemandAllocationStrategyType,
        "SpotMaintenanceStrategies": "SpotMaintenanceStrategiesTypeDef",
        "ClientToken": str,
        "ExcessCapacityTerminationPolicy": ExcessCapacityTerminationPolicyType,
        "FulfilledCapacity": float,
        "OnDemandFulfilledCapacity": float,
        "LaunchSpecifications": List["SpotFleetLaunchSpecificationTypeDef"],
        "LaunchTemplateConfigs": List["LaunchTemplateConfigTypeDef"],
        "SpotPrice": str,
        "OnDemandTargetCapacity": int,
        "OnDemandMaxTotalPrice": str,
        "SpotMaxTotalPrice": str,
        "TerminateInstancesWithExpiration": bool,
        "Type": FleetTypeType,
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "ReplaceUnhealthyInstances": bool,
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
        "LoadBalancersConfig": "LoadBalancersConfigTypeDef",
        "InstancePoolsToUseCount": int,
        "Context": str,
        "TargetCapacityUnitType": TargetCapacityUnitTypeType,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class SpotFleetRequestConfigDataTypeDef(
    _RequiredSpotFleetRequestConfigDataTypeDef, _OptionalSpotFleetRequestConfigDataTypeDef
):
    pass

SpotFleetRequestConfigTypeDef = TypedDict(
    "SpotFleetRequestConfigTypeDef",
    {
        "ActivityStatus": ActivityStatusType,
        "CreateTime": datetime,
        "SpotFleetRequestConfig": "SpotFleetRequestConfigDataTypeDef",
        "SpotFleetRequestId": str,
        "SpotFleetRequestState": BatchStateType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SpotFleetTagSpecificationTypeDef = TypedDict(
    "SpotFleetTagSpecificationTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SpotInstanceRequestTypeDef = TypedDict(
    "SpotInstanceRequestTypeDef",
    {
        "ActualBlockHourlyPrice": str,
        "AvailabilityZoneGroup": str,
        "BlockDurationMinutes": int,
        "CreateTime": datetime,
        "Fault": "SpotInstanceStateFaultTypeDef",
        "InstanceId": str,
        "LaunchGroup": str,
        "LaunchSpecification": "LaunchSpecificationTypeDef",
        "LaunchedAvailabilityZone": str,
        "ProductDescription": RIProductDescriptionType,
        "SpotInstanceRequestId": str,
        "SpotPrice": str,
        "State": SpotInstanceStateType,
        "Status": "SpotInstanceStatusTypeDef",
        "Tags": List["TagTypeDef"],
        "Type": SpotInstanceTypeType,
        "ValidFrom": datetime,
        "ValidUntil": datetime,
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

SpotInstanceStateFaultTypeDef = TypedDict(
    "SpotInstanceStateFaultTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

SpotInstanceStatusTypeDef = TypedDict(
    "SpotInstanceStatusTypeDef",
    {
        "Code": str,
        "Message": str,
        "UpdateTime": datetime,
    },
    total=False,
)

SpotMaintenanceStrategiesTypeDef = TypedDict(
    "SpotMaintenanceStrategiesTypeDef",
    {
        "CapacityRebalance": "SpotCapacityRebalanceTypeDef",
    },
    total=False,
)

SpotMarketOptionsTypeDef = TypedDict(
    "SpotMarketOptionsTypeDef",
    {
        "MaxPrice": str,
        "SpotInstanceType": SpotInstanceTypeType,
        "BlockDurationMinutes": int,
        "ValidUntil": Union[datetime, str],
        "InstanceInterruptionBehavior": InstanceInterruptionBehaviorType,
    },
    total=False,
)

SpotOptionsRequestTypeDef = TypedDict(
    "SpotOptionsRequestTypeDef",
    {
        "AllocationStrategy": SpotAllocationStrategyType,
        "MaintenanceStrategies": "FleetSpotMaintenanceStrategiesRequestTypeDef",
        "InstanceInterruptionBehavior": SpotInstanceInterruptionBehaviorType,
        "InstancePoolsToUseCount": int,
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

SpotOptionsTypeDef = TypedDict(
    "SpotOptionsTypeDef",
    {
        "AllocationStrategy": SpotAllocationStrategyType,
        "MaintenanceStrategies": "FleetSpotMaintenanceStrategiesTypeDef",
        "InstanceInterruptionBehavior": SpotInstanceInterruptionBehaviorType,
        "InstancePoolsToUseCount": int,
        "SingleInstanceType": bool,
        "SingleAvailabilityZone": bool,
        "MinTargetCapacity": int,
        "MaxTotalPrice": str,
    },
    total=False,
)

SpotPlacementScoreTypeDef = TypedDict(
    "SpotPlacementScoreTypeDef",
    {
        "Region": str,
        "AvailabilityZoneId": str,
        "Score": int,
    },
    total=False,
)

SpotPlacementTypeDef = TypedDict(
    "SpotPlacementTypeDef",
    {
        "AvailabilityZone": str,
        "GroupName": str,
        "Tenancy": TenancyType,
    },
    total=False,
)

SpotPriceTypeDef = TypedDict(
    "SpotPriceTypeDef",
    {
        "AvailabilityZone": str,
        "InstanceType": InstanceTypeType,
        "ProductDescription": RIProductDescriptionType,
        "SpotPrice": str,
        "Timestamp": datetime,
    },
    total=False,
)

StaleIpPermissionTypeDef = TypedDict(
    "StaleIpPermissionTypeDef",
    {
        "FromPort": int,
        "IpProtocol": str,
        "IpRanges": List[str],
        "PrefixListIds": List[str],
        "ToPort": int,
        "UserIdGroupPairs": List["UserIdGroupPairTypeDef"],
    },
    total=False,
)

StaleSecurityGroupTypeDef = TypedDict(
    "StaleSecurityGroupTypeDef",
    {
        "Description": str,
        "GroupId": str,
        "GroupName": str,
        "StaleIpPermissions": List["StaleIpPermissionTypeDef"],
        "StaleIpPermissionsEgress": List["StaleIpPermissionTypeDef"],
        "VpcId": str,
    },
    total=False,
)

StartInstancesRequestInstanceTypeDef = TypedDict(
    "StartInstancesRequestInstanceTypeDef",
    {
        "AdditionalInfo": str,
        "DryRun": bool,
    },
    total=False,
)

_RequiredStartInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredStartInstancesRequestRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalStartInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalStartInstancesRequestRequestTypeDef",
    {
        "AdditionalInfo": str,
        "DryRun": bool,
    },
    total=False,
)

class StartInstancesRequestRequestTypeDef(
    _RequiredStartInstancesRequestRequestTypeDef, _OptionalStartInstancesRequestRequestTypeDef
):
    pass

StartInstancesResultTypeDef = TypedDict(
    "StartInstancesResultTypeDef",
    {
        "StartingInstances": List["InstanceStateChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredStartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsAccessScopeId": str,
        "ClientToken": str,
    },
)
_OptionalStartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalStartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef",
    {
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class StartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef(
    _RequiredStartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef,
    _OptionalStartNetworkInsightsAccessScopeAnalysisRequestRequestTypeDef,
):
    pass

StartNetworkInsightsAccessScopeAnalysisResultTypeDef = TypedDict(
    "StartNetworkInsightsAccessScopeAnalysisResultTypeDef",
    {
        "NetworkInsightsAccessScopeAnalysis": "NetworkInsightsAccessScopeAnalysisTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartNetworkInsightsAnalysisRequestRequestTypeDef = TypedDict(
    "_RequiredStartNetworkInsightsAnalysisRequestRequestTypeDef",
    {
        "NetworkInsightsPathId": str,
        "ClientToken": str,
    },
)
_OptionalStartNetworkInsightsAnalysisRequestRequestTypeDef = TypedDict(
    "_OptionalStartNetworkInsightsAnalysisRequestRequestTypeDef",
    {
        "AdditionalAccounts": List[str],
        "FilterInArns": List[str],
        "DryRun": bool,
        "TagSpecifications": List["TagSpecificationTypeDef"],
    },
    total=False,
)

class StartNetworkInsightsAnalysisRequestRequestTypeDef(
    _RequiredStartNetworkInsightsAnalysisRequestRequestTypeDef,
    _OptionalStartNetworkInsightsAnalysisRequestRequestTypeDef,
):
    pass

StartNetworkInsightsAnalysisResultTypeDef = TypedDict(
    "StartNetworkInsightsAnalysisResultTypeDef",
    {
        "NetworkInsightsAnalysis": "NetworkInsightsAnalysisTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredStartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef = TypedDict(
    "_RequiredStartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef",
    {
        "ServiceId": str,
    },
)
_OptionalStartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef = TypedDict(
    "_OptionalStartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class StartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef(
    _RequiredStartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef,
    _OptionalStartVpcEndpointServicePrivateDnsVerificationRequestRequestTypeDef,
):
    pass

StartVpcEndpointServicePrivateDnsVerificationResultTypeDef = TypedDict(
    "StartVpcEndpointServicePrivateDnsVerificationResultTypeDef",
    {
        "ReturnValue": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StateReasonTypeDef = TypedDict(
    "StateReasonTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

StopInstancesRequestInstanceTypeDef = TypedDict(
    "StopInstancesRequestInstanceTypeDef",
    {
        "Hibernate": bool,
        "DryRun": bool,
        "Force": bool,
    },
    total=False,
)

_RequiredStopInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredStopInstancesRequestRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalStopInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalStopInstancesRequestRequestTypeDef",
    {
        "Hibernate": bool,
        "DryRun": bool,
        "Force": bool,
    },
    total=False,
)

class StopInstancesRequestRequestTypeDef(
    _RequiredStopInstancesRequestRequestTypeDef, _OptionalStopInstancesRequestRequestTypeDef
):
    pass

StopInstancesResultTypeDef = TypedDict(
    "StopInstancesResultTypeDef",
    {
        "StoppingInstances": List["InstanceStateChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorageLocationTypeDef = TypedDict(
    "StorageLocationTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
    total=False,
)

StorageTypeDef = TypedDict(
    "StorageTypeDef",
    {
        "S3": "S3StorageTypeDef",
    },
    total=False,
)

StoreImageTaskResultTypeDef = TypedDict(
    "StoreImageTaskResultTypeDef",
    {
        "AmiId": str,
        "TaskStartTime": datetime,
        "Bucket": str,
        "S3objectKey": str,
        "ProgressPercentage": int,
        "StoreTaskState": str,
        "StoreTaskFailureReason": str,
    },
    total=False,
)

SubnetAssociationTypeDef = TypedDict(
    "SubnetAssociationTypeDef",
    {
        "SubnetId": str,
        "State": TransitGatewayMulitcastDomainAssociationStateType,
    },
    total=False,
)

SubnetCidrBlockStateTypeDef = TypedDict(
    "SubnetCidrBlockStateTypeDef",
    {
        "State": SubnetCidrBlockStateCodeType,
        "StatusMessage": str,
    },
    total=False,
)

SubnetCidrReservationTypeDef = TypedDict(
    "SubnetCidrReservationTypeDef",
    {
        "SubnetCidrReservationId": str,
        "SubnetId": str,
        "Cidr": str,
        "ReservationType": SubnetCidrReservationTypeType,
        "OwnerId": str,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

SubnetConfigurationTypeDef = TypedDict(
    "SubnetConfigurationTypeDef",
    {
        "SubnetId": str,
        "Ipv4": str,
        "Ipv6": str,
    },
    total=False,
)

SubnetIpv6CidrBlockAssociationTypeDef = TypedDict(
    "SubnetIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "Ipv6CidrBlock": str,
        "Ipv6CidrBlockState": "SubnetCidrBlockStateTypeDef",
    },
    total=False,
)

SubnetTypeDef = TypedDict(
    "SubnetTypeDef",
    {
        "AvailabilityZone": str,
        "AvailabilityZoneId": str,
        "AvailableIpAddressCount": int,
        "CidrBlock": str,
        "DefaultForAz": bool,
        "EnableLniAtDeviceIndex": int,
        "MapPublicIpOnLaunch": bool,
        "MapCustomerOwnedIpOnLaunch": bool,
        "CustomerOwnedIpv4Pool": str,
        "State": SubnetStateType,
        "SubnetId": str,
        "VpcId": str,
        "OwnerId": str,
        "AssignIpv6AddressOnCreation": bool,
        "Ipv6CidrBlockAssociationSet": List["SubnetIpv6CidrBlockAssociationTypeDef"],
        "Tags": List["TagTypeDef"],
        "SubnetArn": str,
        "OutpostArn": str,
        "EnableDns64": bool,
        "Ipv6Native": bool,
        "PrivateDnsNameOptionsOnLaunch": "PrivateDnsNameOptionsOnLaunchTypeDef",
    },
    total=False,
)

SubscriptionTypeDef = TypedDict(
    "SubscriptionTypeDef",
    {
        "Source": str,
        "Destination": str,
        "Metric": Literal["aggregate-latency"],
        "Statistic": Literal["p50"],
        "Period": PeriodTypeType,
    },
    total=False,
)

SuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "SuccessfulInstanceCreditSpecificationItemTypeDef",
    {
        "InstanceId": str,
    },
    total=False,
)

SuccessfulQueuedPurchaseDeletionTypeDef = TypedDict(
    "SuccessfulQueuedPurchaseDeletionTypeDef",
    {
        "ReservedInstancesId": str,
    },
    total=False,
)

TagDescriptionTypeDef = TypedDict(
    "TagDescriptionTypeDef",
    {
        "Key": str,
        "ResourceId": str,
        "ResourceType": ResourceTypeType,
        "Value": str,
    },
    total=False,
)

TagSpecificationTypeDef = TypedDict(
    "TagSpecificationTypeDef",
    {
        "ResourceType": ResourceTypeType,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

_RequiredTagTypeDef = TypedDict(
    "_RequiredTagTypeDef",
    {
        "Key": str,
    },
)
_OptionalTagTypeDef = TypedDict(
    "_OptionalTagTypeDef",
    {
        "Value": str,
    },
    total=False,
)

class TagTypeDef(_RequiredTagTypeDef, _OptionalTagTypeDef):
    pass

_RequiredTargetCapacitySpecificationRequestTypeDef = TypedDict(
    "_RequiredTargetCapacitySpecificationRequestTypeDef",
    {
        "TotalTargetCapacity": int,
    },
)
_OptionalTargetCapacitySpecificationRequestTypeDef = TypedDict(
    "_OptionalTargetCapacitySpecificationRequestTypeDef",
    {
        "OnDemandTargetCapacity": int,
        "SpotTargetCapacity": int,
        "DefaultTargetCapacityType": DefaultTargetCapacityTypeType,
        "TargetCapacityUnitType": TargetCapacityUnitTypeType,
    },
    total=False,
)

class TargetCapacitySpecificationRequestTypeDef(
    _RequiredTargetCapacitySpecificationRequestTypeDef,
    _OptionalTargetCapacitySpecificationRequestTypeDef,
):
    pass

TargetCapacitySpecificationTypeDef = TypedDict(
    "TargetCapacitySpecificationTypeDef",
    {
        "TotalTargetCapacity": int,
        "OnDemandTargetCapacity": int,
        "SpotTargetCapacity": int,
        "DefaultTargetCapacityType": DefaultTargetCapacityTypeType,
        "TargetCapacityUnitType": TargetCapacityUnitTypeType,
    },
    total=False,
)

_RequiredTargetConfigurationRequestTypeDef = TypedDict(
    "_RequiredTargetConfigurationRequestTypeDef",
    {
        "OfferingId": str,
    },
)
_OptionalTargetConfigurationRequestTypeDef = TypedDict(
    "_OptionalTargetConfigurationRequestTypeDef",
    {
        "InstanceCount": int,
    },
    total=False,
)

class TargetConfigurationRequestTypeDef(
    _RequiredTargetConfigurationRequestTypeDef, _OptionalTargetConfigurationRequestTypeDef
):
    pass

TargetConfigurationTypeDef = TypedDict(
    "TargetConfigurationTypeDef",
    {
        "InstanceCount": int,
        "OfferingId": str,
    },
    total=False,
)

TargetGroupTypeDef = TypedDict(
    "TargetGroupTypeDef",
    {
        "Arn": str,
    },
    total=False,
)

TargetGroupsConfigTypeDef = TypedDict(
    "TargetGroupsConfigTypeDef",
    {
        "TargetGroups": List["TargetGroupTypeDef"],
    },
    total=False,
)

TargetNetworkTypeDef = TypedDict(
    "TargetNetworkTypeDef",
    {
        "AssociationId": str,
        "VpcId": str,
        "TargetNetworkId": str,
        "ClientVpnEndpointId": str,
        "Status": "AssociationStatusTypeDef",
        "SecurityGroups": List[str],
    },
    total=False,
)

TargetReservationValueTypeDef = TypedDict(
    "TargetReservationValueTypeDef",
    {
        "ReservationValue": "ReservationValueTypeDef",
        "TargetConfiguration": "TargetConfigurationTypeDef",
    },
    total=False,
)

_RequiredTerminateClientVpnConnectionsRequestRequestTypeDef = TypedDict(
    "_RequiredTerminateClientVpnConnectionsRequestRequestTypeDef",
    {
        "ClientVpnEndpointId": str,
    },
)
_OptionalTerminateClientVpnConnectionsRequestRequestTypeDef = TypedDict(
    "_OptionalTerminateClientVpnConnectionsRequestRequestTypeDef",
    {
        "ConnectionId": str,
        "Username": str,
        "DryRun": bool,
    },
    total=False,
)

class TerminateClientVpnConnectionsRequestRequestTypeDef(
    _RequiredTerminateClientVpnConnectionsRequestRequestTypeDef,
    _OptionalTerminateClientVpnConnectionsRequestRequestTypeDef,
):
    pass

TerminateClientVpnConnectionsResultTypeDef = TypedDict(
    "TerminateClientVpnConnectionsResultTypeDef",
    {
        "ClientVpnEndpointId": str,
        "Username": str,
        "ConnectionStatuses": List["TerminateConnectionStatusTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

TerminateConnectionStatusTypeDef = TypedDict(
    "TerminateConnectionStatusTypeDef",
    {
        "ConnectionId": str,
        "PreviousStatus": "ClientVpnConnectionStatusTypeDef",
        "CurrentStatus": "ClientVpnConnectionStatusTypeDef",
    },
    total=False,
)

TerminateInstancesRequestInstanceTypeDef = TypedDict(
    "TerminateInstancesRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredTerminateInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredTerminateInstancesRequestRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalTerminateInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalTerminateInstancesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class TerminateInstancesRequestRequestTypeDef(
    _RequiredTerminateInstancesRequestRequestTypeDef,
    _OptionalTerminateInstancesRequestRequestTypeDef,
):
    pass

TerminateInstancesResultTypeDef = TypedDict(
    "TerminateInstancesResultTypeDef",
    {
        "TerminatingInstances": List["InstanceStateChangeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ThroughResourcesStatementRequestTypeDef = TypedDict(
    "ThroughResourcesStatementRequestTypeDef",
    {
        "ResourceStatement": "ResourceStatementRequestTypeDef",
    },
    total=False,
)

ThroughResourcesStatementTypeDef = TypedDict(
    "ThroughResourcesStatementTypeDef",
    {
        "ResourceStatement": "ResourceStatementTypeDef",
    },
    total=False,
)

TotalLocalStorageGBRequestTypeDef = TypedDict(
    "TotalLocalStorageGBRequestTypeDef",
    {
        "Min": float,
        "Max": float,
    },
    total=False,
)

TotalLocalStorageGBTypeDef = TypedDict(
    "TotalLocalStorageGBTypeDef",
    {
        "Min": float,
        "Max": float,
    },
    total=False,
)

TrafficMirrorFilterRuleTypeDef = TypedDict(
    "TrafficMirrorFilterRuleTypeDef",
    {
        "TrafficMirrorFilterRuleId": str,
        "TrafficMirrorFilterId": str,
        "TrafficDirection": TrafficDirectionType,
        "RuleNumber": int,
        "RuleAction": TrafficMirrorRuleActionType,
        "Protocol": int,
        "DestinationPortRange": "TrafficMirrorPortRangeTypeDef",
        "SourcePortRange": "TrafficMirrorPortRangeTypeDef",
        "DestinationCidrBlock": str,
        "SourceCidrBlock": str,
        "Description": str,
    },
    total=False,
)

TrafficMirrorFilterTypeDef = TypedDict(
    "TrafficMirrorFilterTypeDef",
    {
        "TrafficMirrorFilterId": str,
        "IngressFilterRules": List["TrafficMirrorFilterRuleTypeDef"],
        "EgressFilterRules": List["TrafficMirrorFilterRuleTypeDef"],
        "NetworkServices": List[Literal["amazon-dns"]],
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TrafficMirrorPortRangeRequestTypeDef = TypedDict(
    "TrafficMirrorPortRangeRequestTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

TrafficMirrorPortRangeTypeDef = TypedDict(
    "TrafficMirrorPortRangeTypeDef",
    {
        "FromPort": int,
        "ToPort": int,
    },
    total=False,
)

TrafficMirrorSessionTypeDef = TypedDict(
    "TrafficMirrorSessionTypeDef",
    {
        "TrafficMirrorSessionId": str,
        "TrafficMirrorTargetId": str,
        "TrafficMirrorFilterId": str,
        "NetworkInterfaceId": str,
        "OwnerId": str,
        "PacketLength": int,
        "SessionNumber": int,
        "VirtualNetworkId": int,
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TrafficMirrorTargetTypeDef = TypedDict(
    "TrafficMirrorTargetTypeDef",
    {
        "TrafficMirrorTargetId": str,
        "NetworkInterfaceId": str,
        "NetworkLoadBalancerArn": str,
        "Type": TrafficMirrorTargetTypeType,
        "Description": str,
        "OwnerId": str,
        "Tags": List["TagTypeDef"],
        "GatewayLoadBalancerEndpointId": str,
    },
    total=False,
)

TransitGatewayAssociationTypeDef = TypedDict(
    "TransitGatewayAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "State": TransitGatewayAssociationStateType,
    },
    total=False,
)

TransitGatewayAttachmentAssociationTypeDef = TypedDict(
    "TransitGatewayAttachmentAssociationTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "State": TransitGatewayAssociationStateType,
    },
    total=False,
)

TransitGatewayAttachmentBgpConfigurationTypeDef = TypedDict(
    "TransitGatewayAttachmentBgpConfigurationTypeDef",
    {
        "TransitGatewayAsn": int,
        "PeerAsn": int,
        "TransitGatewayAddress": str,
        "PeerAddress": str,
        "BgpStatus": BgpStatusType,
    },
    total=False,
)

TransitGatewayAttachmentPropagationTypeDef = TypedDict(
    "TransitGatewayAttachmentPropagationTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "State": TransitGatewayPropagationStateType,
    },
    total=False,
)

TransitGatewayAttachmentTypeDef = TypedDict(
    "TransitGatewayAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransitGatewayId": str,
        "TransitGatewayOwnerId": str,
        "ResourceOwnerId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceId": str,
        "State": TransitGatewayAttachmentStateType,
        "Association": "TransitGatewayAttachmentAssociationTypeDef",
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayConnectOptionsTypeDef = TypedDict(
    "TransitGatewayConnectOptionsTypeDef",
    {
        "Protocol": Literal["gre"],
    },
    total=False,
)

TransitGatewayConnectPeerConfigurationTypeDef = TypedDict(
    "TransitGatewayConnectPeerConfigurationTypeDef",
    {
        "TransitGatewayAddress": str,
        "PeerAddress": str,
        "InsideCidrBlocks": List[str],
        "Protocol": Literal["gre"],
        "BgpConfigurations": List["TransitGatewayAttachmentBgpConfigurationTypeDef"],
    },
    total=False,
)

TransitGatewayConnectPeerTypeDef = TypedDict(
    "TransitGatewayConnectPeerTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransitGatewayConnectPeerId": str,
        "State": TransitGatewayConnectPeerStateType,
        "CreationTime": datetime,
        "ConnectPeerConfiguration": "TransitGatewayConnectPeerConfigurationTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayConnectRequestBgpOptionsTypeDef = TypedDict(
    "TransitGatewayConnectRequestBgpOptionsTypeDef",
    {
        "PeerAsn": int,
    },
    total=False,
)

TransitGatewayConnectTypeDef = TypedDict(
    "TransitGatewayConnectTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransportTransitGatewayAttachmentId": str,
        "TransitGatewayId": str,
        "State": TransitGatewayAttachmentStateType,
        "CreationTime": datetime,
        "Options": "TransitGatewayConnectOptionsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayMulticastDeregisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "DeregisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayMulticastDeregisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastDeregisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "DeregisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayMulticastDomainAssociationTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceOwnerId": str,
        "Subnet": "SubnetAssociationTypeDef",
    },
    total=False,
)

TransitGatewayMulticastDomainAssociationsTypeDef = TypedDict(
    "TransitGatewayMulticastDomainAssociationsTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceOwnerId": str,
        "Subnets": List["SubnetAssociationTypeDef"],
    },
    total=False,
)

TransitGatewayMulticastDomainOptionsTypeDef = TypedDict(
    "TransitGatewayMulticastDomainOptionsTypeDef",
    {
        "Igmpv2Support": Igmpv2SupportValueType,
        "StaticSourcesSupport": StaticSourcesSupportValueType,
        "AutoAcceptSharedAssociations": AutoAcceptSharedAssociationsValueType,
    },
    total=False,
)

TransitGatewayMulticastDomainTypeDef = TypedDict(
    "TransitGatewayMulticastDomainTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "TransitGatewayId": str,
        "TransitGatewayMulticastDomainArn": str,
        "OwnerId": str,
        "Options": "TransitGatewayMulticastDomainOptionsTypeDef",
        "State": TransitGatewayMulticastDomainStateType,
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayMulticastGroupTypeDef = TypedDict(
    "TransitGatewayMulticastGroupTypeDef",
    {
        "GroupIpAddress": str,
        "TransitGatewayAttachmentId": str,
        "SubnetId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceOwnerId": str,
        "NetworkInterfaceId": str,
        "GroupMember": bool,
        "GroupSource": bool,
        "MemberType": MembershipTypeType,
        "SourceType": MembershipTypeType,
    },
    total=False,
)

TransitGatewayMulticastRegisteredGroupMembersTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupMembersTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "RegisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayMulticastRegisteredGroupSourcesTypeDef = TypedDict(
    "TransitGatewayMulticastRegisteredGroupSourcesTypeDef",
    {
        "TransitGatewayMulticastDomainId": str,
        "RegisteredNetworkInterfaceIds": List[str],
        "GroupIpAddress": str,
    },
    total=False,
)

TransitGatewayOptionsTypeDef = TypedDict(
    "TransitGatewayOptionsTypeDef",
    {
        "AmazonSideAsn": int,
        "TransitGatewayCidrBlocks": List[str],
        "AutoAcceptSharedAttachments": AutoAcceptSharedAttachmentsValueType,
        "DefaultRouteTableAssociation": DefaultRouteTableAssociationValueType,
        "AssociationDefaultRouteTableId": str,
        "DefaultRouteTablePropagation": DefaultRouteTablePropagationValueType,
        "PropagationDefaultRouteTableId": str,
        "VpnEcmpSupport": VpnEcmpSupportValueType,
        "DnsSupport": DnsSupportValueType,
        "MulticastSupport": MulticastSupportValueType,
    },
    total=False,
)

TransitGatewayPeeringAttachmentOptionsTypeDef = TypedDict(
    "TransitGatewayPeeringAttachmentOptionsTypeDef",
    {
        "DynamicRouting": DynamicRoutingValueType,
    },
    total=False,
)

TransitGatewayPeeringAttachmentTypeDef = TypedDict(
    "TransitGatewayPeeringAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "AccepterTransitGatewayAttachmentId": str,
        "RequesterTgwInfo": "PeeringTgwInfoTypeDef",
        "AccepterTgwInfo": "PeeringTgwInfoTypeDef",
        "Options": "TransitGatewayPeeringAttachmentOptionsTypeDef",
        "Status": "PeeringAttachmentStatusTypeDef",
        "State": TransitGatewayAttachmentStateType,
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayPolicyRuleMetaDataTypeDef = TypedDict(
    "TransitGatewayPolicyRuleMetaDataTypeDef",
    {
        "MetaDataKey": str,
        "MetaDataValue": str,
    },
    total=False,
)

TransitGatewayPolicyRuleTypeDef = TypedDict(
    "TransitGatewayPolicyRuleTypeDef",
    {
        "SourceCidrBlock": str,
        "SourcePortRange": str,
        "DestinationCidrBlock": str,
        "DestinationPortRange": str,
        "Protocol": str,
        "MetaData": "TransitGatewayPolicyRuleMetaDataTypeDef",
    },
    total=False,
)

TransitGatewayPolicyTableAssociationTypeDef = TypedDict(
    "TransitGatewayPolicyTableAssociationTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "State": TransitGatewayAssociationStateType,
    },
    total=False,
)

TransitGatewayPolicyTableEntryTypeDef = TypedDict(
    "TransitGatewayPolicyTableEntryTypeDef",
    {
        "PolicyRuleNumber": str,
        "PolicyRule": "TransitGatewayPolicyRuleTypeDef",
        "TargetRouteTableId": str,
    },
    total=False,
)

TransitGatewayPolicyTableTypeDef = TypedDict(
    "TransitGatewayPolicyTableTypeDef",
    {
        "TransitGatewayPolicyTableId": str,
        "TransitGatewayId": str,
        "State": TransitGatewayPolicyTableStateType,
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayPrefixListAttachmentTypeDef = TypedDict(
    "TransitGatewayPrefixListAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "ResourceId": str,
    },
    total=False,
)

TransitGatewayPrefixListReferenceTypeDef = TypedDict(
    "TransitGatewayPrefixListReferenceTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "PrefixListId": str,
        "PrefixListOwnerId": str,
        "State": TransitGatewayPrefixListReferenceStateType,
        "Blackhole": bool,
        "TransitGatewayAttachment": "TransitGatewayPrefixListAttachmentTypeDef",
    },
    total=False,
)

TransitGatewayPropagationTypeDef = TypedDict(
    "TransitGatewayPropagationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "TransitGatewayRouteTableId": str,
        "State": TransitGatewayPropagationStateType,
        "TransitGatewayRouteTableAnnouncementId": str,
    },
    total=False,
)

TransitGatewayRequestOptionsTypeDef = TypedDict(
    "TransitGatewayRequestOptionsTypeDef",
    {
        "AmazonSideAsn": int,
        "AutoAcceptSharedAttachments": AutoAcceptSharedAttachmentsValueType,
        "DefaultRouteTableAssociation": DefaultRouteTableAssociationValueType,
        "DefaultRouteTablePropagation": DefaultRouteTablePropagationValueType,
        "VpnEcmpSupport": VpnEcmpSupportValueType,
        "DnsSupport": DnsSupportValueType,
        "MulticastSupport": MulticastSupportValueType,
        "TransitGatewayCidrBlocks": List[str],
    },
    total=False,
)

TransitGatewayRouteAttachmentTypeDef = TypedDict(
    "TransitGatewayRouteAttachmentTypeDef",
    {
        "ResourceId": str,
        "TransitGatewayAttachmentId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
    },
    total=False,
)

TransitGatewayRouteTableAnnouncementTypeDef = TypedDict(
    "TransitGatewayRouteTableAnnouncementTypeDef",
    {
        "TransitGatewayRouteTableAnnouncementId": str,
        "TransitGatewayId": str,
        "CoreNetworkId": str,
        "PeerTransitGatewayId": str,
        "PeerCoreNetworkId": str,
        "PeeringAttachmentId": str,
        "AnnouncementDirection": TransitGatewayRouteTableAnnouncementDirectionType,
        "TransitGatewayRouteTableId": str,
        "State": TransitGatewayRouteTableAnnouncementStateType,
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayRouteTableAssociationTypeDef = TypedDict(
    "TransitGatewayRouteTableAssociationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "State": TransitGatewayAssociationStateType,
    },
    total=False,
)

TransitGatewayRouteTablePropagationTypeDef = TypedDict(
    "TransitGatewayRouteTablePropagationTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "ResourceId": str,
        "ResourceType": TransitGatewayAttachmentResourceTypeType,
        "State": TransitGatewayPropagationStateType,
        "TransitGatewayRouteTableAnnouncementId": str,
    },
    total=False,
)

TransitGatewayRouteTableRouteTypeDef = TypedDict(
    "TransitGatewayRouteTableRouteTypeDef",
    {
        "DestinationCidr": str,
        "State": str,
        "RouteOrigin": str,
        "PrefixListId": str,
        "AttachmentId": str,
        "ResourceId": str,
        "ResourceType": str,
    },
    total=False,
)

TransitGatewayRouteTableTypeDef = TypedDict(
    "TransitGatewayRouteTableTypeDef",
    {
        "TransitGatewayRouteTableId": str,
        "TransitGatewayId": str,
        "State": TransitGatewayRouteTableStateType,
        "DefaultAssociationRouteTable": bool,
        "DefaultPropagationRouteTable": bool,
        "CreationTime": datetime,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayRouteTypeDef = TypedDict(
    "TransitGatewayRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "PrefixListId": str,
        "TransitGatewayRouteTableAnnouncementId": str,
        "TransitGatewayAttachments": List["TransitGatewayRouteAttachmentTypeDef"],
        "Type": TransitGatewayRouteTypeType,
        "State": TransitGatewayRouteStateType,
    },
    total=False,
)

TransitGatewayTypeDef = TypedDict(
    "TransitGatewayTypeDef",
    {
        "TransitGatewayId": str,
        "TransitGatewayArn": str,
        "State": TransitGatewayStateType,
        "OwnerId": str,
        "Description": str,
        "CreationTime": datetime,
        "Options": "TransitGatewayOptionsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TransitGatewayVpcAttachmentOptionsTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentOptionsTypeDef",
    {
        "DnsSupport": DnsSupportValueType,
        "Ipv6Support": Ipv6SupportValueType,
        "ApplianceModeSupport": ApplianceModeSupportValueType,
    },
    total=False,
)

TransitGatewayVpcAttachmentTypeDef = TypedDict(
    "TransitGatewayVpcAttachmentTypeDef",
    {
        "TransitGatewayAttachmentId": str,
        "TransitGatewayId": str,
        "VpcId": str,
        "VpcOwnerId": str,
        "State": TransitGatewayAttachmentStateType,
        "SubnetIds": List[str],
        "CreationTime": datetime,
        "Options": "TransitGatewayVpcAttachmentOptionsTypeDef",
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TrunkInterfaceAssociationTypeDef = TypedDict(
    "TrunkInterfaceAssociationTypeDef",
    {
        "AssociationId": str,
        "BranchInterfaceId": str,
        "TrunkInterfaceId": str,
        "InterfaceProtocol": InterfaceProtocolTypeType,
        "VlanId": int,
        "GreKey": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

TunnelOptionTypeDef = TypedDict(
    "TunnelOptionTypeDef",
    {
        "OutsideIpAddress": str,
        "TunnelInsideCidr": str,
        "TunnelInsideIpv6Cidr": str,
        "PreSharedKey": str,
        "Phase1LifetimeSeconds": int,
        "Phase2LifetimeSeconds": int,
        "RekeyMarginTimeSeconds": int,
        "RekeyFuzzPercentage": int,
        "ReplayWindowSize": int,
        "DpdTimeoutSeconds": int,
        "DpdTimeoutAction": str,
        "Phase1EncryptionAlgorithms": List["Phase1EncryptionAlgorithmsListValueTypeDef"],
        "Phase2EncryptionAlgorithms": List["Phase2EncryptionAlgorithmsListValueTypeDef"],
        "Phase1IntegrityAlgorithms": List["Phase1IntegrityAlgorithmsListValueTypeDef"],
        "Phase2IntegrityAlgorithms": List["Phase2IntegrityAlgorithmsListValueTypeDef"],
        "Phase1DHGroupNumbers": List["Phase1DHGroupNumbersListValueTypeDef"],
        "Phase2DHGroupNumbers": List["Phase2DHGroupNumbersListValueTypeDef"],
        "IkeVersions": List["IKEVersionsListValueTypeDef"],
        "StartupAction": str,
        "LogOptions": "VpnTunnelLogOptionsTypeDef",
        "EnableTunnelLifecycleControl": bool,
    },
    total=False,
)

_RequiredUnassignIpv6AddressesRequestRequestTypeDef = TypedDict(
    "_RequiredUnassignIpv6AddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalUnassignIpv6AddressesRequestRequestTypeDef = TypedDict(
    "_OptionalUnassignIpv6AddressesRequestRequestTypeDef",
    {
        "Ipv6Addresses": List[str],
        "Ipv6Prefixes": List[str],
    },
    total=False,
)

class UnassignIpv6AddressesRequestRequestTypeDef(
    _RequiredUnassignIpv6AddressesRequestRequestTypeDef,
    _OptionalUnassignIpv6AddressesRequestRequestTypeDef,
):
    pass

UnassignIpv6AddressesResultTypeDef = TypedDict(
    "UnassignIpv6AddressesResultTypeDef",
    {
        "NetworkInterfaceId": str,
        "UnassignedIpv6Addresses": List[str],
        "UnassignedIpv6Prefixes": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnassignPrivateIpAddressesRequestNetworkInterfaceTypeDef = TypedDict(
    "UnassignPrivateIpAddressesRequestNetworkInterfaceTypeDef",
    {
        "PrivateIpAddresses": List[str],
        "Ipv4Prefixes": List[str],
    },
    total=False,
)

_RequiredUnassignPrivateIpAddressesRequestRequestTypeDef = TypedDict(
    "_RequiredUnassignPrivateIpAddressesRequestRequestTypeDef",
    {
        "NetworkInterfaceId": str,
    },
)
_OptionalUnassignPrivateIpAddressesRequestRequestTypeDef = TypedDict(
    "_OptionalUnassignPrivateIpAddressesRequestRequestTypeDef",
    {
        "PrivateIpAddresses": List[str],
        "Ipv4Prefixes": List[str],
    },
    total=False,
)

class UnassignPrivateIpAddressesRequestRequestTypeDef(
    _RequiredUnassignPrivateIpAddressesRequestRequestTypeDef,
    _OptionalUnassignPrivateIpAddressesRequestRequestTypeDef,
):
    pass

_RequiredUnassignPrivateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "_RequiredUnassignPrivateNatGatewayAddressRequestRequestTypeDef",
    {
        "NatGatewayId": str,
        "PrivateIpAddresses": List[str],
    },
)
_OptionalUnassignPrivateNatGatewayAddressRequestRequestTypeDef = TypedDict(
    "_OptionalUnassignPrivateNatGatewayAddressRequestRequestTypeDef",
    {
        "MaxDrainDurationSeconds": int,
        "DryRun": bool,
    },
    total=False,
)

class UnassignPrivateNatGatewayAddressRequestRequestTypeDef(
    _RequiredUnassignPrivateNatGatewayAddressRequestRequestTypeDef,
    _OptionalUnassignPrivateNatGatewayAddressRequestRequestTypeDef,
):
    pass

UnassignPrivateNatGatewayAddressResultTypeDef = TypedDict(
    "UnassignPrivateNatGatewayAddressResultTypeDef",
    {
        "NatGatewayId": str,
        "NatGatewayAddresses": List["NatGatewayAddressTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnmonitorInstancesRequestInstanceTypeDef = TypedDict(
    "UnmonitorInstancesRequestInstanceTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

_RequiredUnmonitorInstancesRequestRequestTypeDef = TypedDict(
    "_RequiredUnmonitorInstancesRequestRequestTypeDef",
    {
        "InstanceIds": List[str],
    },
)
_OptionalUnmonitorInstancesRequestRequestTypeDef = TypedDict(
    "_OptionalUnmonitorInstancesRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class UnmonitorInstancesRequestRequestTypeDef(
    _RequiredUnmonitorInstancesRequestRequestTypeDef,
    _OptionalUnmonitorInstancesRequestRequestTypeDef,
):
    pass

UnmonitorInstancesResultTypeDef = TypedDict(
    "UnmonitorInstancesResultTypeDef",
    {
        "InstanceMonitorings": List["InstanceMonitoringTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    {
        "Code": UnsuccessfulInstanceCreditSpecificationErrorCodeType,
        "Message": str,
    },
    total=False,
)

UnsuccessfulInstanceCreditSpecificationItemTypeDef = TypedDict(
    "UnsuccessfulInstanceCreditSpecificationItemTypeDef",
    {
        "InstanceId": str,
        "Error": "UnsuccessfulInstanceCreditSpecificationItemErrorTypeDef",
    },
    total=False,
)

UnsuccessfulItemErrorTypeDef = TypedDict(
    "UnsuccessfulItemErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

UnsuccessfulItemTypeDef = TypedDict(
    "UnsuccessfulItemTypeDef",
    {
        "Error": "UnsuccessfulItemErrorTypeDef",
        "ResourceId": str,
    },
    total=False,
)

UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsEgressRequestRequestTypeDef",
    {
        "DryRun": bool,
        "GroupId": str,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "SecurityGroupRuleDescriptions": List["SecurityGroupRuleDescriptionTypeDef"],
    },
    total=False,
)

UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsIngressRequestRequestTypeDef",
    {
        "DryRun": bool,
        "GroupId": str,
        "GroupName": str,
        "IpPermissions": List["IpPermissionTypeDef"],
        "SecurityGroupRuleDescriptions": List["SecurityGroupRuleDescriptionTypeDef"],
    },
    total=False,
)

UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef = TypedDict(
    "UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef",
    {
        "Return": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UserBucketDetailsTypeDef = TypedDict(
    "UserBucketDetailsTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
    },
    total=False,
)

UserBucketTypeDef = TypedDict(
    "UserBucketTypeDef",
    {
        "S3Bucket": str,
        "S3Key": str,
    },
    total=False,
)

UserDataTypeDef = TypedDict(
    "UserDataTypeDef",
    {
        "Data": str,
    },
    total=False,
)

UserIdGroupPairTypeDef = TypedDict(
    "UserIdGroupPairTypeDef",
    {
        "Description": str,
        "GroupId": str,
        "GroupName": str,
        "PeeringStatus": str,
        "UserId": str,
        "VpcId": str,
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

_RequiredVCpuCountRangeRequestTypeDef = TypedDict(
    "_RequiredVCpuCountRangeRequestTypeDef",
    {
        "Min": int,
    },
)
_OptionalVCpuCountRangeRequestTypeDef = TypedDict(
    "_OptionalVCpuCountRangeRequestTypeDef",
    {
        "Max": int,
    },
    total=False,
)

class VCpuCountRangeRequestTypeDef(
    _RequiredVCpuCountRangeRequestTypeDef, _OptionalVCpuCountRangeRequestTypeDef
):
    pass

VCpuCountRangeTypeDef = TypedDict(
    "VCpuCountRangeTypeDef",
    {
        "Min": int,
        "Max": int,
    },
    total=False,
)

VCpuInfoTypeDef = TypedDict(
    "VCpuInfoTypeDef",
    {
        "DefaultVCpus": int,
        "DefaultCores": int,
        "DefaultThreadsPerCore": int,
        "ValidCores": List[int],
        "ValidThreadsPerCore": List[int],
    },
    total=False,
)

ValidationErrorTypeDef = TypedDict(
    "ValidationErrorTypeDef",
    {
        "Code": str,
        "Message": str,
    },
    total=False,
)

ValidationWarningTypeDef = TypedDict(
    "ValidationWarningTypeDef",
    {
        "Errors": List["ValidationErrorTypeDef"],
    },
    total=False,
)

VerifiedAccessEndpointEniOptionsTypeDef = TypedDict(
    "VerifiedAccessEndpointEniOptionsTypeDef",
    {
        "NetworkInterfaceId": str,
        "Protocol": VerifiedAccessEndpointProtocolType,
        "Port": int,
    },
    total=False,
)

VerifiedAccessEndpointLoadBalancerOptionsTypeDef = TypedDict(
    "VerifiedAccessEndpointLoadBalancerOptionsTypeDef",
    {
        "Protocol": VerifiedAccessEndpointProtocolType,
        "Port": int,
        "LoadBalancerArn": str,
        "SubnetIds": List[str],
    },
    total=False,
)

VerifiedAccessEndpointStatusTypeDef = TypedDict(
    "VerifiedAccessEndpointStatusTypeDef",
    {
        "Code": VerifiedAccessEndpointStatusCodeType,
        "Message": str,
    },
    total=False,
)

VerifiedAccessEndpointTypeDef = TypedDict(
    "VerifiedAccessEndpointTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "VerifiedAccessGroupId": str,
        "VerifiedAccessEndpointId": str,
        "ApplicationDomain": str,
        "EndpointType": VerifiedAccessEndpointTypeType,
        "AttachmentType": Literal["vpc"],
        "DomainCertificateArn": str,
        "EndpointDomain": str,
        "DeviceValidationDomain": str,
        "SecurityGroupIds": List[str],
        "LoadBalancerOptions": "VerifiedAccessEndpointLoadBalancerOptionsTypeDef",
        "NetworkInterfaceOptions": "VerifiedAccessEndpointEniOptionsTypeDef",
        "Status": "VerifiedAccessEndpointStatusTypeDef",
        "Description": str,
        "CreationTime": str,
        "LastUpdatedTime": str,
        "DeletionTime": str,
        "Tags": List["TagTypeDef"],
        "SseSpecification": "VerifiedAccessSseSpecificationResponseTypeDef",
    },
    total=False,
)

VerifiedAccessGroupTypeDef = TypedDict(
    "VerifiedAccessGroupTypeDef",
    {
        "VerifiedAccessGroupId": str,
        "VerifiedAccessInstanceId": str,
        "Description": str,
        "Owner": str,
        "VerifiedAccessGroupArn": str,
        "CreationTime": str,
        "LastUpdatedTime": str,
        "DeletionTime": str,
        "Tags": List["TagTypeDef"],
        "SseSpecification": "VerifiedAccessSseSpecificationResponseTypeDef",
    },
    total=False,
)

VerifiedAccessInstanceLoggingConfigurationTypeDef = TypedDict(
    "VerifiedAccessInstanceLoggingConfigurationTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "AccessLogs": "VerifiedAccessLogsTypeDef",
    },
    total=False,
)

VerifiedAccessInstanceTypeDef = TypedDict(
    "VerifiedAccessInstanceTypeDef",
    {
        "VerifiedAccessInstanceId": str,
        "Description": str,
        "VerifiedAccessTrustProviders": List["VerifiedAccessTrustProviderCondensedTypeDef"],
        "CreationTime": str,
        "LastUpdatedTime": str,
        "Tags": List["TagTypeDef"],
        "FipsEnabled": bool,
    },
    total=False,
)

_RequiredVerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef = TypedDict(
    "_RequiredVerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalVerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef = TypedDict(
    "_OptionalVerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef",
    {
        "LogGroup": str,
    },
    total=False,
)

class VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef(
    _RequiredVerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef,
    _OptionalVerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef,
):
    pass

VerifiedAccessLogCloudWatchLogsDestinationTypeDef = TypedDict(
    "VerifiedAccessLogCloudWatchLogsDestinationTypeDef",
    {
        "Enabled": bool,
        "DeliveryStatus": "VerifiedAccessLogDeliveryStatusTypeDef",
        "LogGroup": str,
    },
    total=False,
)

VerifiedAccessLogDeliveryStatusTypeDef = TypedDict(
    "VerifiedAccessLogDeliveryStatusTypeDef",
    {
        "Code": VerifiedAccessLogDeliveryStatusCodeType,
        "Message": str,
    },
    total=False,
)

_RequiredVerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef = TypedDict(
    "_RequiredVerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalVerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef = TypedDict(
    "_OptionalVerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef",
    {
        "DeliveryStream": str,
    },
    total=False,
)

class VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef(
    _RequiredVerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef,
    _OptionalVerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef,
):
    pass

VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef = TypedDict(
    "VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef",
    {
        "Enabled": bool,
        "DeliveryStatus": "VerifiedAccessLogDeliveryStatusTypeDef",
        "DeliveryStream": str,
    },
    total=False,
)

VerifiedAccessLogOptionsTypeDef = TypedDict(
    "VerifiedAccessLogOptionsTypeDef",
    {
        "S3": "VerifiedAccessLogS3DestinationOptionsTypeDef",
        "CloudWatchLogs": "VerifiedAccessLogCloudWatchLogsDestinationOptionsTypeDef",
        "KinesisDataFirehose": "VerifiedAccessLogKinesisDataFirehoseDestinationOptionsTypeDef",
        "LogVersion": str,
        "IncludeTrustContext": bool,
    },
    total=False,
)

_RequiredVerifiedAccessLogS3DestinationOptionsTypeDef = TypedDict(
    "_RequiredVerifiedAccessLogS3DestinationOptionsTypeDef",
    {
        "Enabled": bool,
    },
)
_OptionalVerifiedAccessLogS3DestinationOptionsTypeDef = TypedDict(
    "_OptionalVerifiedAccessLogS3DestinationOptionsTypeDef",
    {
        "BucketName": str,
        "Prefix": str,
        "BucketOwner": str,
    },
    total=False,
)

class VerifiedAccessLogS3DestinationOptionsTypeDef(
    _RequiredVerifiedAccessLogS3DestinationOptionsTypeDef,
    _OptionalVerifiedAccessLogS3DestinationOptionsTypeDef,
):
    pass

VerifiedAccessLogS3DestinationTypeDef = TypedDict(
    "VerifiedAccessLogS3DestinationTypeDef",
    {
        "Enabled": bool,
        "DeliveryStatus": "VerifiedAccessLogDeliveryStatusTypeDef",
        "BucketName": str,
        "Prefix": str,
        "BucketOwner": str,
    },
    total=False,
)

VerifiedAccessLogsTypeDef = TypedDict(
    "VerifiedAccessLogsTypeDef",
    {
        "S3": "VerifiedAccessLogS3DestinationTypeDef",
        "CloudWatchLogs": "VerifiedAccessLogCloudWatchLogsDestinationTypeDef",
        "KinesisDataFirehose": "VerifiedAccessLogKinesisDataFirehoseDestinationTypeDef",
        "LogVersion": str,
        "IncludeTrustContext": bool,
    },
    total=False,
)

VerifiedAccessSseSpecificationRequestTypeDef = TypedDict(
    "VerifiedAccessSseSpecificationRequestTypeDef",
    {
        "CustomerManagedKeyEnabled": bool,
        "KmsKeyArn": str,
    },
    total=False,
)

VerifiedAccessSseSpecificationResponseTypeDef = TypedDict(
    "VerifiedAccessSseSpecificationResponseTypeDef",
    {
        "CustomerManagedKeyEnabled": bool,
        "KmsKeyArn": str,
    },
    total=False,
)

VerifiedAccessTrustProviderCondensedTypeDef = TypedDict(
    "VerifiedAccessTrustProviderCondensedTypeDef",
    {
        "VerifiedAccessTrustProviderId": str,
        "Description": str,
        "TrustProviderType": TrustProviderTypeType,
        "UserTrustProviderType": UserTrustProviderTypeType,
        "DeviceTrustProviderType": DeviceTrustProviderTypeType,
    },
    total=False,
)

VerifiedAccessTrustProviderTypeDef = TypedDict(
    "VerifiedAccessTrustProviderTypeDef",
    {
        "VerifiedAccessTrustProviderId": str,
        "Description": str,
        "TrustProviderType": TrustProviderTypeType,
        "UserTrustProviderType": UserTrustProviderTypeType,
        "DeviceTrustProviderType": DeviceTrustProviderTypeType,
        "OidcOptions": "OidcOptionsTypeDef",
        "DeviceOptions": "DeviceOptionsTypeDef",
        "PolicyReferenceName": str,
        "CreationTime": str,
        "LastUpdatedTime": str,
        "Tags": List["TagTypeDef"],
        "SseSpecification": "VerifiedAccessSseSpecificationResponseTypeDef",
    },
    total=False,
)

VgwTelemetryTypeDef = TypedDict(
    "VgwTelemetryTypeDef",
    {
        "AcceptedRouteCount": int,
        "LastStatusChange": datetime,
        "OutsideIpAddress": str,
        "Status": TelemetryStatusType,
        "StatusMessage": str,
        "CertificateArn": str,
    },
    total=False,
)

VolumeAttachmentResponseMetadataTypeDef = TypedDict(
    "VolumeAttachmentResponseMetadataTypeDef",
    {
        "AttachTime": datetime,
        "Device": str,
        "InstanceId": str,
        "State": VolumeAttachmentStateType,
        "VolumeId": str,
        "DeleteOnTermination": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeAttachmentTypeDef = TypedDict(
    "VolumeAttachmentTypeDef",
    {
        "AttachTime": datetime,
        "Device": str,
        "InstanceId": str,
        "State": VolumeAttachmentStateType,
        "VolumeId": str,
        "DeleteOnTermination": bool,
    },
    total=False,
)

VolumeDetailTypeDef = TypedDict(
    "VolumeDetailTypeDef",
    {
        "Size": int,
    },
)

VolumeModificationTypeDef = TypedDict(
    "VolumeModificationTypeDef",
    {
        "VolumeId": str,
        "ModificationState": VolumeModificationStateType,
        "StatusMessage": str,
        "TargetSize": int,
        "TargetIops": int,
        "TargetVolumeType": VolumeTypeType,
        "TargetThroughput": int,
        "TargetMultiAttachEnabled": bool,
        "OriginalSize": int,
        "OriginalIops": int,
        "OriginalVolumeType": VolumeTypeType,
        "OriginalThroughput": int,
        "OriginalMultiAttachEnabled": bool,
        "Progress": int,
        "StartTime": datetime,
        "EndTime": datetime,
    },
    total=False,
)

VolumeResponseMetadataTypeDef = TypedDict(
    "VolumeResponseMetadataTypeDef",
    {
        "Attachments": List["VolumeAttachmentTypeDef"],
        "AvailabilityZone": str,
        "CreateTime": datetime,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "State": VolumeStateType,
        "VolumeId": str,
        "Iops": int,
        "Tags": List["TagTypeDef"],
        "VolumeType": VolumeTypeType,
        "FastRestored": bool,
        "MultiAttachEnabled": bool,
        "Throughput": int,
        "SseType": SSETypeType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VolumeStatusActionTypeDef = TypedDict(
    "VolumeStatusActionTypeDef",
    {
        "Code": str,
        "Description": str,
        "EventId": str,
        "EventType": str,
    },
    total=False,
)

VolumeStatusAttachmentStatusTypeDef = TypedDict(
    "VolumeStatusAttachmentStatusTypeDef",
    {
        "IoPerformance": str,
        "InstanceId": str,
    },
    total=False,
)

VolumeStatusDetailsTypeDef = TypedDict(
    "VolumeStatusDetailsTypeDef",
    {
        "Name": VolumeStatusNameType,
        "Status": str,
    },
    total=False,
)

VolumeStatusEventTypeDef = TypedDict(
    "VolumeStatusEventTypeDef",
    {
        "Description": str,
        "EventId": str,
        "EventType": str,
        "NotAfter": datetime,
        "NotBefore": datetime,
        "InstanceId": str,
    },
    total=False,
)

VolumeStatusInfoTypeDef = TypedDict(
    "VolumeStatusInfoTypeDef",
    {
        "Details": List["VolumeStatusDetailsTypeDef"],
        "Status": VolumeStatusInfoStatusType,
    },
    total=False,
)

VolumeStatusItemTypeDef = TypedDict(
    "VolumeStatusItemTypeDef",
    {
        "Actions": List["VolumeStatusActionTypeDef"],
        "AvailabilityZone": str,
        "OutpostArn": str,
        "Events": List["VolumeStatusEventTypeDef"],
        "VolumeId": str,
        "VolumeStatus": "VolumeStatusInfoTypeDef",
        "AttachmentStatuses": List["VolumeStatusAttachmentStatusTypeDef"],
    },
    total=False,
)

VolumeTypeDef = TypedDict(
    "VolumeTypeDef",
    {
        "Attachments": List["VolumeAttachmentTypeDef"],
        "AvailabilityZone": str,
        "CreateTime": datetime,
        "Encrypted": bool,
        "KmsKeyId": str,
        "OutpostArn": str,
        "Size": int,
        "SnapshotId": str,
        "State": VolumeStateType,
        "VolumeId": str,
        "Iops": int,
        "Tags": List["TagTypeDef"],
        "VolumeType": VolumeTypeType,
        "FastRestored": bool,
        "MultiAttachEnabled": bool,
        "Throughput": int,
        "SseType": SSETypeType,
    },
    total=False,
)

VpcAttachmentTypeDef = TypedDict(
    "VpcAttachmentTypeDef",
    {
        "State": AttachmentStatusType,
        "VpcId": str,
    },
    total=False,
)

VpcCidrBlockAssociationTypeDef = TypedDict(
    "VpcCidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "CidrBlock": str,
        "CidrBlockState": "VpcCidrBlockStateTypeDef",
    },
    total=False,
)

VpcCidrBlockStateTypeDef = TypedDict(
    "VpcCidrBlockStateTypeDef",
    {
        "State": VpcCidrBlockStateCodeType,
        "StatusMessage": str,
    },
    total=False,
)

VpcClassicLinkTypeDef = TypedDict(
    "VpcClassicLinkTypeDef",
    {
        "ClassicLinkEnabled": bool,
        "Tags": List["TagTypeDef"],
        "VpcId": str,
    },
    total=False,
)

VpcEndpointConnectionTypeDef = TypedDict(
    "VpcEndpointConnectionTypeDef",
    {
        "ServiceId": str,
        "VpcEndpointId": str,
        "VpcEndpointOwner": str,
        "VpcEndpointState": StateType,
        "CreationTimestamp": datetime,
        "DnsEntries": List["DnsEntryTypeDef"],
        "NetworkLoadBalancerArns": List[str],
        "GatewayLoadBalancerArns": List[str],
        "IpAddressType": IpAddressTypeType,
        "VpcEndpointConnectionId": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpcEndpointTypeDef = TypedDict(
    "VpcEndpointTypeDef",
    {
        "VpcEndpointId": str,
        "VpcEndpointType": VpcEndpointTypeType,
        "VpcId": str,
        "ServiceName": str,
        "State": StateType,
        "PolicyDocument": str,
        "RouteTableIds": List[str],
        "SubnetIds": List[str],
        "Groups": List["SecurityGroupIdentifierTypeDef"],
        "IpAddressType": IpAddressTypeType,
        "DnsOptions": "DnsOptionsTypeDef",
        "PrivateDnsEnabled": bool,
        "RequesterManaged": bool,
        "NetworkInterfaceIds": List[str],
        "DnsEntries": List["DnsEntryTypeDef"],
        "CreationTimestamp": datetime,
        "Tags": List["TagTypeDef"],
        "OwnerId": str,
        "LastError": "LastErrorTypeDef",
    },
    total=False,
)

VpcIpv6CidrBlockAssociationTypeDef = TypedDict(
    "VpcIpv6CidrBlockAssociationTypeDef",
    {
        "AssociationId": str,
        "Ipv6CidrBlock": str,
        "Ipv6CidrBlockState": "VpcCidrBlockStateTypeDef",
        "NetworkBorderGroup": str,
        "Ipv6Pool": str,
    },
    total=False,
)

VpcPeeringConnectionOptionsDescriptionTypeDef = TypedDict(
    "VpcPeeringConnectionOptionsDescriptionTypeDef",
    {
        "AllowDnsResolutionFromRemoteVpc": bool,
        "AllowEgressFromLocalClassicLinkToRemoteVpc": bool,
        "AllowEgressFromLocalVpcToRemoteClassicLink": bool,
    },
    total=False,
)

VpcPeeringConnectionStateReasonTypeDef = TypedDict(
    "VpcPeeringConnectionStateReasonTypeDef",
    {
        "Code": VpcPeeringConnectionStateReasonCodeType,
        "Message": str,
    },
    total=False,
)

VpcPeeringConnectionTypeDef = TypedDict(
    "VpcPeeringConnectionTypeDef",
    {
        "AccepterVpcInfo": "VpcPeeringConnectionVpcInfoTypeDef",
        "ExpirationTime": datetime,
        "RequesterVpcInfo": "VpcPeeringConnectionVpcInfoTypeDef",
        "Status": "VpcPeeringConnectionStateReasonTypeDef",
        "Tags": List["TagTypeDef"],
        "VpcPeeringConnectionId": str,
    },
    total=False,
)

VpcPeeringConnectionVpcInfoTypeDef = TypedDict(
    "VpcPeeringConnectionVpcInfoTypeDef",
    {
        "CidrBlock": str,
        "Ipv6CidrBlockSet": List["Ipv6CidrBlockTypeDef"],
        "CidrBlockSet": List["CidrBlockTypeDef"],
        "OwnerId": str,
        "PeeringOptions": "VpcPeeringConnectionOptionsDescriptionTypeDef",
        "VpcId": str,
        "Region": str,
    },
    total=False,
)

VpcTypeDef = TypedDict(
    "VpcTypeDef",
    {
        "CidrBlock": str,
        "DhcpOptionsId": str,
        "State": VpcStateType,
        "VpcId": str,
        "OwnerId": str,
        "InstanceTenancy": TenancyType,
        "Ipv6CidrBlockAssociationSet": List["VpcIpv6CidrBlockAssociationTypeDef"],
        "CidrBlockAssociationSet": List["VpcCidrBlockAssociationTypeDef"],
        "IsDefault": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpnConnectionDeviceTypeTypeDef = TypedDict(
    "VpnConnectionDeviceTypeTypeDef",
    {
        "VpnConnectionDeviceTypeId": str,
        "Vendor": str,
        "Platform": str,
        "Software": str,
    },
    total=False,
)

VpnConnectionOptionsSpecificationTypeDef = TypedDict(
    "VpnConnectionOptionsSpecificationTypeDef",
    {
        "EnableAcceleration": bool,
        "StaticRoutesOnly": bool,
        "TunnelInsideIpVersion": TunnelInsideIpVersionType,
        "TunnelOptions": List["VpnTunnelOptionsSpecificationTypeDef"],
        "LocalIpv4NetworkCidr": str,
        "RemoteIpv4NetworkCidr": str,
        "LocalIpv6NetworkCidr": str,
        "RemoteIpv6NetworkCidr": str,
        "OutsideIpAddressType": str,
        "TransportTransitGatewayAttachmentId": str,
    },
    total=False,
)

VpnConnectionOptionsTypeDef = TypedDict(
    "VpnConnectionOptionsTypeDef",
    {
        "EnableAcceleration": bool,
        "StaticRoutesOnly": bool,
        "LocalIpv4NetworkCidr": str,
        "RemoteIpv4NetworkCidr": str,
        "LocalIpv6NetworkCidr": str,
        "RemoteIpv6NetworkCidr": str,
        "OutsideIpAddressType": str,
        "TransportTransitGatewayAttachmentId": str,
        "TunnelInsideIpVersion": TunnelInsideIpVersionType,
        "TunnelOptions": List["TunnelOptionTypeDef"],
    },
    total=False,
)

VpnConnectionTypeDef = TypedDict(
    "VpnConnectionTypeDef",
    {
        "CustomerGatewayConfiguration": str,
        "CustomerGatewayId": str,
        "Category": str,
        "State": VpnStateType,
        "Type": Literal["ipsec.1"],
        "VpnConnectionId": str,
        "VpnGatewayId": str,
        "TransitGatewayId": str,
        "CoreNetworkArn": str,
        "CoreNetworkAttachmentArn": str,
        "GatewayAssociationState": GatewayAssociationStateType,
        "Options": "VpnConnectionOptionsTypeDef",
        "Routes": List["VpnStaticRouteTypeDef"],
        "Tags": List["TagTypeDef"],
        "VgwTelemetry": List["VgwTelemetryTypeDef"],
    },
    total=False,
)

VpnGatewayTypeDef = TypedDict(
    "VpnGatewayTypeDef",
    {
        "AvailabilityZone": str,
        "State": VpnStateType,
        "Type": Literal["ipsec.1"],
        "VpcAttachments": List["VpcAttachmentTypeDef"],
        "VpnGatewayId": str,
        "AmazonSideAsn": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

VpnStaticRouteTypeDef = TypedDict(
    "VpnStaticRouteTypeDef",
    {
        "DestinationCidrBlock": str,
        "Source": Literal["Static"],
        "State": VpnStateType,
    },
    total=False,
)

VpnTunnelLogOptionsSpecificationTypeDef = TypedDict(
    "VpnTunnelLogOptionsSpecificationTypeDef",
    {
        "CloudWatchLogOptions": "CloudWatchLogOptionsSpecificationTypeDef",
    },
    total=False,
)

VpnTunnelLogOptionsTypeDef = TypedDict(
    "VpnTunnelLogOptionsTypeDef",
    {
        "CloudWatchLogOptions": "CloudWatchLogOptionsTypeDef",
    },
    total=False,
)

VpnTunnelOptionsSpecificationTypeDef = TypedDict(
    "VpnTunnelOptionsSpecificationTypeDef",
    {
        "TunnelInsideCidr": str,
        "TunnelInsideIpv6Cidr": str,
        "PreSharedKey": str,
        "Phase1LifetimeSeconds": int,
        "Phase2LifetimeSeconds": int,
        "RekeyMarginTimeSeconds": int,
        "RekeyFuzzPercentage": int,
        "ReplayWindowSize": int,
        "DPDTimeoutSeconds": int,
        "DPDTimeoutAction": str,
        "Phase1EncryptionAlgorithms": List["Phase1EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase2EncryptionAlgorithms": List["Phase2EncryptionAlgorithmsRequestListValueTypeDef"],
        "Phase1IntegrityAlgorithms": List["Phase1IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase2IntegrityAlgorithms": List["Phase2IntegrityAlgorithmsRequestListValueTypeDef"],
        "Phase1DHGroupNumbers": List["Phase1DHGroupNumbersRequestListValueTypeDef"],
        "Phase2DHGroupNumbers": List["Phase2DHGroupNumbersRequestListValueTypeDef"],
        "IKEVersions": List["IKEVersionsRequestListValueTypeDef"],
        "StartupAction": str,
        "LogOptions": "VpnTunnelLogOptionsSpecificationTypeDef",
        "EnableTunnelLifecycleControl": bool,
    },
    total=False,
)

WaiterConfigTypeDef = TypedDict(
    "WaiterConfigTypeDef",
    {
        "Delay": int,
        "MaxAttempts": int,
    },
    total=False,
)

_RequiredWithdrawByoipCidrRequestRequestTypeDef = TypedDict(
    "_RequiredWithdrawByoipCidrRequestRequestTypeDef",
    {
        "Cidr": str,
    },
)
_OptionalWithdrawByoipCidrRequestRequestTypeDef = TypedDict(
    "_OptionalWithdrawByoipCidrRequestRequestTypeDef",
    {
        "DryRun": bool,
    },
    total=False,
)

class WithdrawByoipCidrRequestRequestTypeDef(
    _RequiredWithdrawByoipCidrRequestRequestTypeDef, _OptionalWithdrawByoipCidrRequestRequestTypeDef
):
    pass

WithdrawByoipCidrResultTypeDef = TypedDict(
    "WithdrawByoipCidrResultTypeDef",
    {
        "ByoipCidr": "ByoipCidrTypeDef",
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)
