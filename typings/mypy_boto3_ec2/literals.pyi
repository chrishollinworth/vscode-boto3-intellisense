"""
Type annotations for ec2 service literal definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/literals.html)

Usage::

    ```python
    from mypy_boto3_ec2.literals import AccountAttributeNameType

    data: AccountAttributeNameType = "default-vpc"
    ```
"""
import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "AccountAttributeNameType",
    "ActivityStatusType",
    "AddressAttributeNameType",
    "AffinityType",
    "AllocationStateType",
    "AllocationStrategyType",
    "AllowsMultipleInstanceTypesType",
    "AnalysisStatusType",
    "ApplianceModeSupportValueType",
    "ArchitectureTypeType",
    "ArchitectureValuesType",
    "AssociatedNetworkTypeType",
    "AssociationStatusCodeType",
    "AttachmentStatusType",
    "AutoAcceptSharedAssociationsValueType",
    "AutoAcceptSharedAttachmentsValueType",
    "AutoPlacementType",
    "AvailabilityZoneOptInStatusType",
    "AvailabilityZoneStateType",
    "BatchStateType",
    "BgpStatusType",
    "BootModeTypeType",
    "BootModeValuesType",
    "BundleTaskCompleteWaiterName",
    "BundleTaskStateType",
    "ByoipCidrStateType",
    "CancelBatchErrorCodeType",
    "CancelSpotInstanceRequestStateType",
    "CapacityReservationInstancePlatformType",
    "CapacityReservationPreferenceType",
    "CapacityReservationStateType",
    "CapacityReservationTenancyType",
    "CarrierGatewayStateType",
    "ClientCertificateRevocationListStatusCodeType",
    "ClientVpnAuthenticationTypeType",
    "ClientVpnAuthorizationRuleStatusCodeType",
    "ClientVpnConnectionStatusCodeType",
    "ClientVpnEndpointAttributeStatusCodeType",
    "ClientVpnEndpointStatusCodeType",
    "ClientVpnRouteStatusCodeType",
    "ConnectionNotificationStateType",
    "ConnectionNotificationTypeType",
    "ConnectivityTypeType",
    "ContainerFormatType",
    "ConversionTaskCancelledWaiterName",
    "ConversionTaskCompletedWaiterName",
    "ConversionTaskDeletedWaiterName",
    "ConversionTaskStateType",
    "CopyTagsFromSourceType",
    "CurrencyCodeValuesType",
    "CustomerGatewayAvailableWaiterName",
    "DatafeedSubscriptionStateType",
    "DefaultRouteTableAssociationValueType",
    "DefaultRouteTablePropagationValueType",
    "DefaultTargetCapacityTypeType",
    "DeleteFleetErrorCodeType",
    "DeleteQueuedReservedInstancesErrorCodeType",
    "DescribeAddressesAttributePaginatorName",
    "DescribeByoipCidrsPaginatorName",
    "DescribeCapacityReservationsPaginatorName",
    "DescribeCarrierGatewaysPaginatorName",
    "DescribeClassicLinkInstancesPaginatorName",
    "DescribeClientVpnAuthorizationRulesPaginatorName",
    "DescribeClientVpnConnectionsPaginatorName",
    "DescribeClientVpnEndpointsPaginatorName",
    "DescribeClientVpnRoutesPaginatorName",
    "DescribeClientVpnTargetNetworksPaginatorName",
    "DescribeCoipPoolsPaginatorName",
    "DescribeDhcpOptionsPaginatorName",
    "DescribeEgressOnlyInternetGatewaysPaginatorName",
    "DescribeExportImageTasksPaginatorName",
    "DescribeFastSnapshotRestoresPaginatorName",
    "DescribeFleetsPaginatorName",
    "DescribeFlowLogsPaginatorName",
    "DescribeFpgaImagesPaginatorName",
    "DescribeHostReservationOfferingsPaginatorName",
    "DescribeHostReservationsPaginatorName",
    "DescribeHostsPaginatorName",
    "DescribeIamInstanceProfileAssociationsPaginatorName",
    "DescribeImportImageTasksPaginatorName",
    "DescribeImportSnapshotTasksPaginatorName",
    "DescribeInstanceCreditSpecificationsPaginatorName",
    "DescribeInstanceEventWindowsPaginatorName",
    "DescribeInstanceStatusPaginatorName",
    "DescribeInstanceTypeOfferingsPaginatorName",
    "DescribeInstanceTypesPaginatorName",
    "DescribeInstancesPaginatorName",
    "DescribeInternetGatewaysPaginatorName",
    "DescribeIpv6PoolsPaginatorName",
    "DescribeLaunchTemplateVersionsPaginatorName",
    "DescribeLaunchTemplatesPaginatorName",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginatorName",
    "DescribeLocalGatewayRouteTableVpcAssociationsPaginatorName",
    "DescribeLocalGatewayRouteTablesPaginatorName",
    "DescribeLocalGatewayVirtualInterfaceGroupsPaginatorName",
    "DescribeLocalGatewayVirtualInterfacesPaginatorName",
    "DescribeLocalGatewaysPaginatorName",
    "DescribeManagedPrefixListsPaginatorName",
    "DescribeMovingAddressesPaginatorName",
    "DescribeNatGatewaysPaginatorName",
    "DescribeNetworkAclsPaginatorName",
    "DescribeNetworkInsightsAnalysesPaginatorName",
    "DescribeNetworkInsightsPathsPaginatorName",
    "DescribeNetworkInterfacePermissionsPaginatorName",
    "DescribeNetworkInterfacesPaginatorName",
    "DescribePrefixListsPaginatorName",
    "DescribePrincipalIdFormatPaginatorName",
    "DescribePublicIpv4PoolsPaginatorName",
    "DescribeReplaceRootVolumeTasksPaginatorName",
    "DescribeReservedInstancesModificationsPaginatorName",
    "DescribeReservedInstancesOfferingsPaginatorName",
    "DescribeRouteTablesPaginatorName",
    "DescribeScheduledInstanceAvailabilityPaginatorName",
    "DescribeScheduledInstancesPaginatorName",
    "DescribeSecurityGroupRulesPaginatorName",
    "DescribeSecurityGroupsPaginatorName",
    "DescribeSnapshotsPaginatorName",
    "DescribeSpotFleetInstancesPaginatorName",
    "DescribeSpotFleetRequestsPaginatorName",
    "DescribeSpotInstanceRequestsPaginatorName",
    "DescribeSpotPriceHistoryPaginatorName",
    "DescribeStaleSecurityGroupsPaginatorName",
    "DescribeStoreImageTasksPaginatorName",
    "DescribeSubnetsPaginatorName",
    "DescribeTagsPaginatorName",
    "DescribeTrafficMirrorFiltersPaginatorName",
    "DescribeTrafficMirrorSessionsPaginatorName",
    "DescribeTrafficMirrorTargetsPaginatorName",
    "DescribeTransitGatewayAttachmentsPaginatorName",
    "DescribeTransitGatewayConnectPeersPaginatorName",
    "DescribeTransitGatewayConnectsPaginatorName",
    "DescribeTransitGatewayMulticastDomainsPaginatorName",
    "DescribeTransitGatewayPeeringAttachmentsPaginatorName",
    "DescribeTransitGatewayRouteTablesPaginatorName",
    "DescribeTransitGatewayVpcAttachmentsPaginatorName",
    "DescribeTransitGatewaysPaginatorName",
    "DescribeVolumeStatusPaginatorName",
    "DescribeVolumesModificationsPaginatorName",
    "DescribeVolumesPaginatorName",
    "DescribeVpcClassicLinkDnsSupportPaginatorName",
    "DescribeVpcEndpointConnectionNotificationsPaginatorName",
    "DescribeVpcEndpointConnectionsPaginatorName",
    "DescribeVpcEndpointServiceConfigurationsPaginatorName",
    "DescribeVpcEndpointServicePermissionsPaginatorName",
    "DescribeVpcEndpointServicesPaginatorName",
    "DescribeVpcEndpointsPaginatorName",
    "DescribeVpcPeeringConnectionsPaginatorName",
    "DescribeVpcsPaginatorName",
    "DeviceTypeType",
    "DiskImageFormatType",
    "DiskTypeType",
    "DnsNameStateType",
    "DnsSupportValueType",
    "DomainTypeType",
    "EbsEncryptionSupportType",
    "EbsNvmeSupportType",
    "EbsOptimizedSupportType",
    "ElasticGpuStateType",
    "ElasticGpuStatusType",
    "EnaSupportType",
    "EndDateTypeType",
    "EphemeralNvmeSupportType",
    "EventCodeType",
    "EventTypeType",
    "ExcessCapacityTerminationPolicyType",
    "ExportEnvironmentType",
    "ExportTaskCancelledWaiterName",
    "ExportTaskCompletedWaiterName",
    "ExportTaskStateType",
    "FastSnapshotRestoreStateCodeType",
    "FleetActivityStatusType",
    "FleetCapacityReservationUsageStrategyType",
    "FleetEventTypeType",
    "FleetExcessCapacityTerminationPolicyType",
    "FleetOnDemandAllocationStrategyType",
    "FleetReplacementStrategyType",
    "FleetStateCodeType",
    "FleetTypeType",
    "FlowLogsResourceTypeType",
    "FpgaImageAttributeNameType",
    "FpgaImageStateCodeType",
    "GatewayTypeType",
    "GetAssociatedIpv6PoolCidrsPaginatorName",
    "GetGroupsForCapacityReservationPaginatorName",
    "GetManagedPrefixListAssociationsPaginatorName",
    "GetManagedPrefixListEntriesPaginatorName",
    "GetTransitGatewayAttachmentPropagationsPaginatorName",
    "GetTransitGatewayMulticastDomainAssociationsPaginatorName",
    "GetTransitGatewayPrefixListReferencesPaginatorName",
    "GetTransitGatewayRouteTableAssociationsPaginatorName",
    "GetTransitGatewayRouteTablePropagationsPaginatorName",
    "HostRecoveryType",
    "HostTenancyType",
    "HttpTokensStateType",
    "HypervisorTypeType",
    "IamInstanceProfileAssociationStateType",
    "Igmpv2SupportValueType",
    "ImageAttributeNameType",
    "ImageAvailableWaiterName",
    "ImageExistsWaiterName",
    "ImageStateType",
    "ImageTypeValuesType",
    "InstanceAttributeNameType",
    "InstanceEventWindowStateType",
    "InstanceExistsWaiterName",
    "InstanceHealthStatusType",
    "InstanceInterruptionBehaviorType",
    "InstanceLifecycleType",
    "InstanceLifecycleTypeType",
    "InstanceMatchCriteriaType",
    "InstanceMetadataEndpointStateType",
    "InstanceMetadataOptionsStateType",
    "InstanceRunningWaiterName",
    "InstanceStateNameType",
    "InstanceStatusOkWaiterName",
    "InstanceStoppedWaiterName",
    "InstanceTerminatedWaiterName",
    "InstanceTypeHypervisorType",
    "InstanceTypeType",
    "InterfacePermissionTypeType",
    "InterfaceProtocolTypeType",
    "Ipv6SupportValueType",
    "KeyPairExistsWaiterName",
    "LaunchTemplateErrorCodeType",
    "LaunchTemplateHttpTokensStateType",
    "LaunchTemplateInstanceMetadataEndpointStateType",
    "LaunchTemplateInstanceMetadataOptionsStateType",
    "ListingStateType",
    "ListingStatusType",
    "LocalGatewayRouteStateType",
    "LocalGatewayRouteTypeType",
    "LocationTypeType",
    "LogDestinationTypeType",
    "MarketTypeType",
    "MembershipTypeType",
    "ModifyAvailabilityZoneOptInStatusType",
    "MonitoringStateType",
    "MoveStatusType",
    "MulticastSupportValueType",
    "NatGatewayAvailableWaiterName",
    "NatGatewayStateType",
    "NetworkInterfaceAttributeType",
    "NetworkInterfaceAvailableWaiterName",
    "NetworkInterfaceCreationTypeType",
    "NetworkInterfacePermissionStateCodeType",
    "NetworkInterfaceStatusType",
    "NetworkInterfaceTypeType",
    "OfferingClassTypeType",
    "OfferingTypeValuesType",
    "OnDemandAllocationStrategyType",
    "OperationTypeType",
    "PartitionLoadFrequencyType",
    "PasswordDataAvailableWaiterName",
    "PaymentOptionType",
    "PermissionGroupType",
    "PlacementGroupStateType",
    "PlacementGroupStrategyType",
    "PlacementStrategyType",
    "PlatformValuesType",
    "PrefixListStateType",
    "PrincipalTypeType",
    "ProductCodeValuesType",
    "ProtocolType",
    "ProtocolValueType",
    "RIProductDescriptionType",
    "RecurringChargeFrequencyType",
    "ReplaceRootVolumeTaskStateType",
    "ReplacementStrategyType",
    "ReportInstanceReasonCodesType",
    "ReportStatusTypeType",
    "ReservationStateType",
    "ReservedInstanceStateType",
    "ResetFpgaImageAttributeNameType",
    "ResetImageAttributeNameType",
    "ResourceTypeType",
    "RootDeviceTypeType",
    "RouteOriginType",
    "RouteStateType",
    "RouteTableAssociationStateCodeType",
    "RuleActionType",
    "SearchLocalGatewayRoutesPaginatorName",
    "SearchTransitGatewayMulticastGroupsPaginatorName",
    "SecurityGroupExistsWaiterName",
    "SelfServicePortalType",
    "ServiceStateType",
    "ServiceTypeType",
    "ShutdownBehaviorType",
    "SnapshotAttributeNameType",
    "SnapshotCompletedWaiterName",
    "SnapshotStateType",
    "SpotAllocationStrategyType",
    "SpotInstanceInterruptionBehaviorType",
    "SpotInstanceRequestFulfilledWaiterName",
    "SpotInstanceStateType",
    "SpotInstanceTypeType",
    "StateType",
    "StaticSourcesSupportValueType",
    "StatusNameType",
    "StatusType",
    "StatusTypeType",
    "SubnetAvailableWaiterName",
    "SubnetCidrBlockStateCodeType",
    "SubnetCidrReservationTypeType",
    "SubnetStateType",
    "SummaryStatusType",
    "SystemStatusOkWaiterName",
    "TelemetryStatusType",
    "TenancyType",
    "TrafficDirectionType",
    "TrafficMirrorFilterRuleFieldType",
    "TrafficMirrorNetworkServiceType",
    "TrafficMirrorRuleActionType",
    "TrafficMirrorSessionFieldType",
    "TrafficMirrorTargetTypeType",
    "TrafficTypeType",
    "TransitGatewayAssociationStateType",
    "TransitGatewayAttachmentResourceTypeType",
    "TransitGatewayAttachmentStateType",
    "TransitGatewayConnectPeerStateType",
    "TransitGatewayMulitcastDomainAssociationStateType",
    "TransitGatewayMulticastDomainStateType",
    "TransitGatewayPrefixListReferenceStateType",
    "TransitGatewayPropagationStateType",
    "TransitGatewayRouteStateType",
    "TransitGatewayRouteTableStateType",
    "TransitGatewayRouteTypeType",
    "TransitGatewayStateType",
    "TransportProtocolType",
    "TunnelInsideIpVersionType",
    "UnlimitedSupportedInstanceFamilyType",
    "UnsuccessfulInstanceCreditSpecificationErrorCodeType",
    "UsageClassTypeType",
    "VirtualizationTypeType",
    "VolumeAttachmentStateType",
    "VolumeAttributeNameType",
    "VolumeAvailableWaiterName",
    "VolumeDeletedWaiterName",
    "VolumeInUseWaiterName",
    "VolumeModificationStateType",
    "VolumeStateType",
    "VolumeStatusInfoStatusType",
    "VolumeStatusNameType",
    "VolumeTypeType",
    "VpcAttributeNameType",
    "VpcAvailableWaiterName",
    "VpcCidrBlockStateCodeType",
    "VpcEndpointTypeType",
    "VpcExistsWaiterName",
    "VpcPeeringConnectionDeletedWaiterName",
    "VpcPeeringConnectionExistsWaiterName",
    "VpcPeeringConnectionStateReasonCodeType",
    "VpcStateType",
    "VpcTenancyType",
    "VpnConnectionAvailableWaiterName",
    "VpnConnectionDeletedWaiterName",
    "VpnEcmpSupportValueType",
    "VpnProtocolType",
    "VpnStateType",
    "VpnStaticRouteSourceType",
    "WeekDayType",
    "scopeType",
)

AccountAttributeNameType = Literal["default-vpc", "supported-platforms"]
ActivityStatusType = Literal["error", "fulfilled", "pending_fulfillment", "pending_termination"]
AddressAttributeNameType = Literal["domain-name"]
AffinityType = Literal["default", "host"]
AllocationStateType = Literal[
    "available",
    "pending",
    "permanent-failure",
    "released",
    "released-permanent-failure",
    "under-assessment",
]
AllocationStrategyType = Literal[
    "capacityOptimized", "capacityOptimizedPrioritized", "diversified", "lowestPrice"
]
AllowsMultipleInstanceTypesType = Literal["off", "on"]
AnalysisStatusType = Literal["failed", "running", "succeeded"]
ApplianceModeSupportValueType = Literal["disable", "enable"]
ArchitectureTypeType = Literal["arm64", "i386", "x86_64"]
ArchitectureValuesType = Literal["arm64", "i386", "x86_64"]
AssociatedNetworkTypeType = Literal["vpc"]
AssociationStatusCodeType = Literal[
    "associated", "associating", "association-failed", "disassociated", "disassociating"
]
AttachmentStatusType = Literal["attached", "attaching", "detached", "detaching"]
AutoAcceptSharedAssociationsValueType = Literal["disable", "enable"]
AutoAcceptSharedAttachmentsValueType = Literal["disable", "enable"]
AutoPlacementType = Literal["off", "on"]
AvailabilityZoneOptInStatusType = Literal["not-opted-in", "opt-in-not-required", "opted-in"]
AvailabilityZoneStateType = Literal["available", "impaired", "information", "unavailable"]
BatchStateType = Literal[
    "active",
    "cancelled",
    "cancelled_running",
    "cancelled_terminating",
    "failed",
    "modifying",
    "submitted",
]
BgpStatusType = Literal["down", "up"]
BootModeTypeType = Literal["legacy-bios", "uefi"]
BootModeValuesType = Literal["legacy-bios", "uefi"]
BundleTaskCompleteWaiterName = Literal["bundle_task_complete"]
BundleTaskStateType = Literal[
    "bundling", "cancelling", "complete", "failed", "pending", "storing", "waiting-for-shutdown"
]
ByoipCidrStateType = Literal[
    "advertised",
    "deprovisioned",
    "failed-deprovision",
    "failed-provision",
    "pending-deprovision",
    "pending-provision",
    "provisioned",
    "provisioned-not-publicly-advertisable",
]
CancelBatchErrorCodeType = Literal[
    "fleetRequestIdDoesNotExist",
    "fleetRequestIdMalformed",
    "fleetRequestNotInCancellableState",
    "unexpectedError",
]
CancelSpotInstanceRequestStateType = Literal["active", "cancelled", "closed", "completed", "open"]
CapacityReservationInstancePlatformType = Literal[
    "Linux with SQL Server Enterprise",
    "Linux with SQL Server Standard",
    "Linux with SQL Server Web",
    "Linux/UNIX",
    "Red Hat Enterprise Linux",
    "SUSE Linux",
    "Windows",
    "Windows with SQL Server",
    "Windows with SQL Server Enterprise",
    "Windows with SQL Server Standard",
    "Windows with SQL Server Web",
]
CapacityReservationPreferenceType = Literal["none", "open"]
CapacityReservationStateType = Literal["active", "cancelled", "expired", "failed", "pending"]
CapacityReservationTenancyType = Literal["dedicated", "default"]
CarrierGatewayStateType = Literal["available", "deleted", "deleting", "pending"]
ClientCertificateRevocationListStatusCodeType = Literal["active", "pending"]
ClientVpnAuthenticationTypeType = Literal[
    "certificate-authentication", "directory-service-authentication", "federated-authentication"
]
ClientVpnAuthorizationRuleStatusCodeType = Literal["active", "authorizing", "failed", "revoking"]
ClientVpnConnectionStatusCodeType = Literal[
    "active", "failed-to-terminate", "terminated", "terminating"
]
ClientVpnEndpointAttributeStatusCodeType = Literal["applied", "applying"]
ClientVpnEndpointStatusCodeType = Literal["available", "deleted", "deleting", "pending-associate"]
ClientVpnRouteStatusCodeType = Literal["active", "creating", "deleting", "failed"]
ConnectionNotificationStateType = Literal["Disabled", "Enabled"]
ConnectionNotificationTypeType = Literal["Topic"]
ConnectivityTypeType = Literal["private", "public"]
ContainerFormatType = Literal["ova"]
ConversionTaskCancelledWaiterName = Literal["conversion_task_cancelled"]
ConversionTaskCompletedWaiterName = Literal["conversion_task_completed"]
ConversionTaskDeletedWaiterName = Literal["conversion_task_deleted"]
ConversionTaskStateType = Literal["active", "cancelled", "cancelling", "completed"]
CopyTagsFromSourceType = Literal["volume"]
CurrencyCodeValuesType = Literal["USD"]
CustomerGatewayAvailableWaiterName = Literal["customer_gateway_available"]
DatafeedSubscriptionStateType = Literal["Active", "Inactive"]
DefaultRouteTableAssociationValueType = Literal["disable", "enable"]
DefaultRouteTablePropagationValueType = Literal["disable", "enable"]
DefaultTargetCapacityTypeType = Literal["on-demand", "spot"]
DeleteFleetErrorCodeType = Literal[
    "fleetIdDoesNotExist", "fleetIdMalformed", "fleetNotInDeletableState", "unexpectedError"
]
DeleteQueuedReservedInstancesErrorCodeType = Literal[
    "reserved-instances-id-invalid", "reserved-instances-not-in-queued-state", "unexpected-error"
]
DescribeAddressesAttributePaginatorName = Literal["describe_addresses_attribute"]
DescribeByoipCidrsPaginatorName = Literal["describe_byoip_cidrs"]
DescribeCapacityReservationsPaginatorName = Literal["describe_capacity_reservations"]
DescribeCarrierGatewaysPaginatorName = Literal["describe_carrier_gateways"]
DescribeClassicLinkInstancesPaginatorName = Literal["describe_classic_link_instances"]
DescribeClientVpnAuthorizationRulesPaginatorName = Literal[
    "describe_client_vpn_authorization_rules"
]
DescribeClientVpnConnectionsPaginatorName = Literal["describe_client_vpn_connections"]
DescribeClientVpnEndpointsPaginatorName = Literal["describe_client_vpn_endpoints"]
DescribeClientVpnRoutesPaginatorName = Literal["describe_client_vpn_routes"]
DescribeClientVpnTargetNetworksPaginatorName = Literal["describe_client_vpn_target_networks"]
DescribeCoipPoolsPaginatorName = Literal["describe_coip_pools"]
DescribeDhcpOptionsPaginatorName = Literal["describe_dhcp_options"]
DescribeEgressOnlyInternetGatewaysPaginatorName = Literal["describe_egress_only_internet_gateways"]
DescribeExportImageTasksPaginatorName = Literal["describe_export_image_tasks"]
DescribeFastSnapshotRestoresPaginatorName = Literal["describe_fast_snapshot_restores"]
DescribeFleetsPaginatorName = Literal["describe_fleets"]
DescribeFlowLogsPaginatorName = Literal["describe_flow_logs"]
DescribeFpgaImagesPaginatorName = Literal["describe_fpga_images"]
DescribeHostReservationOfferingsPaginatorName = Literal["describe_host_reservation_offerings"]
DescribeHostReservationsPaginatorName = Literal["describe_host_reservations"]
DescribeHostsPaginatorName = Literal["describe_hosts"]
DescribeIamInstanceProfileAssociationsPaginatorName = Literal[
    "describe_iam_instance_profile_associations"
]
DescribeImportImageTasksPaginatorName = Literal["describe_import_image_tasks"]
DescribeImportSnapshotTasksPaginatorName = Literal["describe_import_snapshot_tasks"]
DescribeInstanceCreditSpecificationsPaginatorName = Literal[
    "describe_instance_credit_specifications"
]
DescribeInstanceEventWindowsPaginatorName = Literal["describe_instance_event_windows"]
DescribeInstanceStatusPaginatorName = Literal["describe_instance_status"]
DescribeInstanceTypeOfferingsPaginatorName = Literal["describe_instance_type_offerings"]
DescribeInstanceTypesPaginatorName = Literal["describe_instance_types"]
DescribeInstancesPaginatorName = Literal["describe_instances"]
DescribeInternetGatewaysPaginatorName = Literal["describe_internet_gateways"]
DescribeIpv6PoolsPaginatorName = Literal["describe_ipv6_pools"]
DescribeLaunchTemplateVersionsPaginatorName = Literal["describe_launch_template_versions"]
DescribeLaunchTemplatesPaginatorName = Literal["describe_launch_templates"]
DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginatorName = Literal[
    "describe_local_gateway_route_table_virtual_interface_group_associations"
]
DescribeLocalGatewayRouteTableVpcAssociationsPaginatorName = Literal[
    "describe_local_gateway_route_table_vpc_associations"
]
DescribeLocalGatewayRouteTablesPaginatorName = Literal["describe_local_gateway_route_tables"]
DescribeLocalGatewayVirtualInterfaceGroupsPaginatorName = Literal[
    "describe_local_gateway_virtual_interface_groups"
]
DescribeLocalGatewayVirtualInterfacesPaginatorName = Literal[
    "describe_local_gateway_virtual_interfaces"
]
DescribeLocalGatewaysPaginatorName = Literal["describe_local_gateways"]
DescribeManagedPrefixListsPaginatorName = Literal["describe_managed_prefix_lists"]
DescribeMovingAddressesPaginatorName = Literal["describe_moving_addresses"]
DescribeNatGatewaysPaginatorName = Literal["describe_nat_gateways"]
DescribeNetworkAclsPaginatorName = Literal["describe_network_acls"]
DescribeNetworkInsightsAnalysesPaginatorName = Literal["describe_network_insights_analyses"]
DescribeNetworkInsightsPathsPaginatorName = Literal["describe_network_insights_paths"]
DescribeNetworkInterfacePermissionsPaginatorName = Literal["describe_network_interface_permissions"]
DescribeNetworkInterfacesPaginatorName = Literal["describe_network_interfaces"]
DescribePrefixListsPaginatorName = Literal["describe_prefix_lists"]
DescribePrincipalIdFormatPaginatorName = Literal["describe_principal_id_format"]
DescribePublicIpv4PoolsPaginatorName = Literal["describe_public_ipv4_pools"]
DescribeReplaceRootVolumeTasksPaginatorName = Literal["describe_replace_root_volume_tasks"]
DescribeReservedInstancesModificationsPaginatorName = Literal[
    "describe_reserved_instances_modifications"
]
DescribeReservedInstancesOfferingsPaginatorName = Literal["describe_reserved_instances_offerings"]
DescribeRouteTablesPaginatorName = Literal["describe_route_tables"]
DescribeScheduledInstanceAvailabilityPaginatorName = Literal[
    "describe_scheduled_instance_availability"
]
DescribeScheduledInstancesPaginatorName = Literal["describe_scheduled_instances"]
DescribeSecurityGroupRulesPaginatorName = Literal["describe_security_group_rules"]
DescribeSecurityGroupsPaginatorName = Literal["describe_security_groups"]
DescribeSnapshotsPaginatorName = Literal["describe_snapshots"]
DescribeSpotFleetInstancesPaginatorName = Literal["describe_spot_fleet_instances"]
DescribeSpotFleetRequestsPaginatorName = Literal["describe_spot_fleet_requests"]
DescribeSpotInstanceRequestsPaginatorName = Literal["describe_spot_instance_requests"]
DescribeSpotPriceHistoryPaginatorName = Literal["describe_spot_price_history"]
DescribeStaleSecurityGroupsPaginatorName = Literal["describe_stale_security_groups"]
DescribeStoreImageTasksPaginatorName = Literal["describe_store_image_tasks"]
DescribeSubnetsPaginatorName = Literal["describe_subnets"]
DescribeTagsPaginatorName = Literal["describe_tags"]
DescribeTrafficMirrorFiltersPaginatorName = Literal["describe_traffic_mirror_filters"]
DescribeTrafficMirrorSessionsPaginatorName = Literal["describe_traffic_mirror_sessions"]
DescribeTrafficMirrorTargetsPaginatorName = Literal["describe_traffic_mirror_targets"]
DescribeTransitGatewayAttachmentsPaginatorName = Literal["describe_transit_gateway_attachments"]
DescribeTransitGatewayConnectPeersPaginatorName = Literal["describe_transit_gateway_connect_peers"]
DescribeTransitGatewayConnectsPaginatorName = Literal["describe_transit_gateway_connects"]
DescribeTransitGatewayMulticastDomainsPaginatorName = Literal[
    "describe_transit_gateway_multicast_domains"
]
DescribeTransitGatewayPeeringAttachmentsPaginatorName = Literal[
    "describe_transit_gateway_peering_attachments"
]
DescribeTransitGatewayRouteTablesPaginatorName = Literal["describe_transit_gateway_route_tables"]
DescribeTransitGatewayVpcAttachmentsPaginatorName = Literal[
    "describe_transit_gateway_vpc_attachments"
]
DescribeTransitGatewaysPaginatorName = Literal["describe_transit_gateways"]
DescribeVolumeStatusPaginatorName = Literal["describe_volume_status"]
DescribeVolumesModificationsPaginatorName = Literal["describe_volumes_modifications"]
DescribeVolumesPaginatorName = Literal["describe_volumes"]
DescribeVpcClassicLinkDnsSupportPaginatorName = Literal["describe_vpc_classic_link_dns_support"]
DescribeVpcEndpointConnectionNotificationsPaginatorName = Literal[
    "describe_vpc_endpoint_connection_notifications"
]
DescribeVpcEndpointConnectionsPaginatorName = Literal["describe_vpc_endpoint_connections"]
DescribeVpcEndpointServiceConfigurationsPaginatorName = Literal[
    "describe_vpc_endpoint_service_configurations"
]
DescribeVpcEndpointServicePermissionsPaginatorName = Literal[
    "describe_vpc_endpoint_service_permissions"
]
DescribeVpcEndpointServicesPaginatorName = Literal["describe_vpc_endpoint_services"]
DescribeVpcEndpointsPaginatorName = Literal["describe_vpc_endpoints"]
DescribeVpcPeeringConnectionsPaginatorName = Literal["describe_vpc_peering_connections"]
DescribeVpcsPaginatorName = Literal["describe_vpcs"]
DeviceTypeType = Literal["ebs", "instance-store"]
DiskImageFormatType = Literal["RAW", "VHD", "VMDK"]
DiskTypeType = Literal["hdd", "ssd"]
DnsNameStateType = Literal["failed", "pendingVerification", "verified"]
DnsSupportValueType = Literal["disable", "enable"]
DomainTypeType = Literal["standard", "vpc"]
EbsEncryptionSupportType = Literal["supported", "unsupported"]
EbsNvmeSupportType = Literal["required", "supported", "unsupported"]
EbsOptimizedSupportType = Literal["default", "supported", "unsupported"]
ElasticGpuStateType = Literal["ATTACHED"]
ElasticGpuStatusType = Literal["IMPAIRED", "OK"]
EnaSupportType = Literal["required", "supported", "unsupported"]
EndDateTypeType = Literal["limited", "unlimited"]
EphemeralNvmeSupportType = Literal["required", "supported", "unsupported"]
EventCodeType = Literal[
    "instance-reboot", "instance-retirement", "instance-stop", "system-maintenance", "system-reboot"
]
EventTypeType = Literal["error", "fleetRequestChange", "information", "instanceChange"]
ExcessCapacityTerminationPolicyType = Literal["default", "noTermination"]
ExportEnvironmentType = Literal["citrix", "microsoft", "vmware"]
ExportTaskCancelledWaiterName = Literal["export_task_cancelled"]
ExportTaskCompletedWaiterName = Literal["export_task_completed"]
ExportTaskStateType = Literal["active", "cancelled", "cancelling", "completed"]
FastSnapshotRestoreStateCodeType = Literal[
    "disabled", "disabling", "enabled", "enabling", "optimizing"
]
FleetActivityStatusType = Literal[
    "error", "fulfilled", "pending_fulfillment", "pending_termination"
]
FleetCapacityReservationUsageStrategyType = Literal["use-capacity-reservations-first"]
FleetEventTypeType = Literal["fleet-change", "instance-change", "service-error"]
FleetExcessCapacityTerminationPolicyType = Literal["no-termination", "termination"]
FleetOnDemandAllocationStrategyType = Literal["lowest-price", "prioritized"]
FleetReplacementStrategyType = Literal["launch"]
FleetStateCodeType = Literal[
    "active",
    "deleted",
    "deleted_running",
    "deleted_terminating",
    "failed",
    "modifying",
    "submitted",
]
FleetTypeType = Literal["instant", "maintain", "request"]
FlowLogsResourceTypeType = Literal["NetworkInterface", "Subnet", "VPC"]
FpgaImageAttributeNameType = Literal["description", "loadPermission", "name", "productCodes"]
FpgaImageStateCodeType = Literal["available", "failed", "pending", "unavailable"]
GatewayTypeType = Literal["ipsec.1"]
GetAssociatedIpv6PoolCidrsPaginatorName = Literal["get_associated_ipv6_pool_cidrs"]
GetGroupsForCapacityReservationPaginatorName = Literal["get_groups_for_capacity_reservation"]
GetManagedPrefixListAssociationsPaginatorName = Literal["get_managed_prefix_list_associations"]
GetManagedPrefixListEntriesPaginatorName = Literal["get_managed_prefix_list_entries"]
GetTransitGatewayAttachmentPropagationsPaginatorName = Literal[
    "get_transit_gateway_attachment_propagations"
]
GetTransitGatewayMulticastDomainAssociationsPaginatorName = Literal[
    "get_transit_gateway_multicast_domain_associations"
]
GetTransitGatewayPrefixListReferencesPaginatorName = Literal[
    "get_transit_gateway_prefix_list_references"
]
GetTransitGatewayRouteTableAssociationsPaginatorName = Literal[
    "get_transit_gateway_route_table_associations"
]
GetTransitGatewayRouteTablePropagationsPaginatorName = Literal[
    "get_transit_gateway_route_table_propagations"
]
HostRecoveryType = Literal["off", "on"]
HostTenancyType = Literal["dedicated", "host"]
HttpTokensStateType = Literal["optional", "required"]
HypervisorTypeType = Literal["ovm", "xen"]
IamInstanceProfileAssociationStateType = Literal[
    "associated", "associating", "disassociated", "disassociating"
]
Igmpv2SupportValueType = Literal["disable", "enable"]
ImageAttributeNameType = Literal[
    "blockDeviceMapping",
    "bootMode",
    "description",
    "kernel",
    "launchPermission",
    "productCodes",
    "ramdisk",
    "sriovNetSupport",
]
ImageAvailableWaiterName = Literal["image_available"]
ImageExistsWaiterName = Literal["image_exists"]
ImageStateType = Literal[
    "available", "deregistered", "error", "failed", "invalid", "pending", "transient"
]
ImageTypeValuesType = Literal["kernel", "machine", "ramdisk"]
InstanceAttributeNameType = Literal[
    "blockDeviceMapping",
    "disableApiTermination",
    "ebsOptimized",
    "enaSupport",
    "enclaveOptions",
    "groupSet",
    "instanceInitiatedShutdownBehavior",
    "instanceType",
    "kernel",
    "productCodes",
    "ramdisk",
    "rootDeviceName",
    "sourceDestCheck",
    "sriovNetSupport",
    "userData",
]
InstanceEventWindowStateType = Literal["active", "creating", "deleted", "deleting"]
InstanceExistsWaiterName = Literal["instance_exists"]
InstanceHealthStatusType = Literal["healthy", "unhealthy"]
InstanceInterruptionBehaviorType = Literal["hibernate", "stop", "terminate"]
InstanceLifecycleType = Literal["on-demand", "spot"]
InstanceLifecycleTypeType = Literal["scheduled", "spot"]
InstanceMatchCriteriaType = Literal["open", "targeted"]
InstanceMetadataEndpointStateType = Literal["disabled", "enabled"]
InstanceMetadataOptionsStateType = Literal["applied", "pending"]
InstanceRunningWaiterName = Literal["instance_running"]
InstanceStateNameType = Literal[
    "pending", "running", "shutting-down", "stopped", "stopping", "terminated"
]
InstanceStatusOkWaiterName = Literal["instance_status_ok"]
InstanceStoppedWaiterName = Literal["instance_stopped"]
InstanceTerminatedWaiterName = Literal["instance_terminated"]
InstanceTypeHypervisorType = Literal["nitro", "xen"]
InstanceTypeType = Literal[
    "a1.2xlarge",
    "a1.4xlarge",
    "a1.large",
    "a1.medium",
    "a1.metal",
    "a1.xlarge",
    "c1.medium",
    "c1.xlarge",
    "c3.2xlarge",
    "c3.4xlarge",
    "c3.8xlarge",
    "c3.large",
    "c3.xlarge",
    "c4.2xlarge",
    "c4.4xlarge",
    "c4.8xlarge",
    "c4.large",
    "c4.xlarge",
    "c5.12xlarge",
    "c5.18xlarge",
    "c5.24xlarge",
    "c5.2xlarge",
    "c5.4xlarge",
    "c5.9xlarge",
    "c5.large",
    "c5.metal",
    "c5.xlarge",
    "c5a.12xlarge",
    "c5a.16xlarge",
    "c5a.24xlarge",
    "c5a.2xlarge",
    "c5a.4xlarge",
    "c5a.8xlarge",
    "c5a.large",
    "c5a.xlarge",
    "c5ad.12xlarge",
    "c5ad.16xlarge",
    "c5ad.24xlarge",
    "c5ad.2xlarge",
    "c5ad.4xlarge",
    "c5ad.8xlarge",
    "c5ad.large",
    "c5ad.xlarge",
    "c5d.12xlarge",
    "c5d.18xlarge",
    "c5d.24xlarge",
    "c5d.2xlarge",
    "c5d.4xlarge",
    "c5d.9xlarge",
    "c5d.large",
    "c5d.metal",
    "c5d.xlarge",
    "c5n.18xlarge",
    "c5n.2xlarge",
    "c5n.4xlarge",
    "c5n.9xlarge",
    "c5n.large",
    "c5n.metal",
    "c5n.xlarge",
    "c6g.12xlarge",
    "c6g.16xlarge",
    "c6g.2xlarge",
    "c6g.4xlarge",
    "c6g.8xlarge",
    "c6g.large",
    "c6g.medium",
    "c6g.metal",
    "c6g.xlarge",
    "c6gd.12xlarge",
    "c6gd.16xlarge",
    "c6gd.2xlarge",
    "c6gd.4xlarge",
    "c6gd.8xlarge",
    "c6gd.large",
    "c6gd.medium",
    "c6gd.metal",
    "c6gd.xlarge",
    "c6gn.12xlarge",
    "c6gn.16xlarge",
    "c6gn.2xlarge",
    "c6gn.4xlarge",
    "c6gn.8xlarge",
    "c6gn.large",
    "c6gn.medium",
    "c6gn.xlarge",
    "cc1.4xlarge",
    "cc2.8xlarge",
    "cg1.4xlarge",
    "cr1.8xlarge",
    "d2.2xlarge",
    "d2.4xlarge",
    "d2.8xlarge",
    "d2.xlarge",
    "d3.2xlarge",
    "d3.4xlarge",
    "d3.8xlarge",
    "d3.xlarge",
    "d3en.12xlarge",
    "d3en.2xlarge",
    "d3en.4xlarge",
    "d3en.6xlarge",
    "d3en.8xlarge",
    "d3en.xlarge",
    "f1.16xlarge",
    "f1.2xlarge",
    "f1.4xlarge",
    "g2.2xlarge",
    "g2.8xlarge",
    "g3.16xlarge",
    "g3.4xlarge",
    "g3.8xlarge",
    "g3s.xlarge",
    "g4ad.16xlarge",
    "g4ad.2xlarge",
    "g4ad.4xlarge",
    "g4ad.8xlarge",
    "g4ad.xlarge",
    "g4dn.12xlarge",
    "g4dn.16xlarge",
    "g4dn.2xlarge",
    "g4dn.4xlarge",
    "g4dn.8xlarge",
    "g4dn.metal",
    "g4dn.xlarge",
    "h1.16xlarge",
    "h1.2xlarge",
    "h1.4xlarge",
    "h1.8xlarge",
    "hi1.4xlarge",
    "hs1.8xlarge",
    "i2.2xlarge",
    "i2.4xlarge",
    "i2.8xlarge",
    "i2.xlarge",
    "i3.16xlarge",
    "i3.2xlarge",
    "i3.4xlarge",
    "i3.8xlarge",
    "i3.large",
    "i3.metal",
    "i3.xlarge",
    "i3en.12xlarge",
    "i3en.24xlarge",
    "i3en.2xlarge",
    "i3en.3xlarge",
    "i3en.6xlarge",
    "i3en.large",
    "i3en.metal",
    "i3en.xlarge",
    "inf1.24xlarge",
    "inf1.2xlarge",
    "inf1.6xlarge",
    "inf1.xlarge",
    "m1.large",
    "m1.medium",
    "m1.small",
    "m1.xlarge",
    "m2.2xlarge",
    "m2.4xlarge",
    "m2.xlarge",
    "m3.2xlarge",
    "m3.large",
    "m3.medium",
    "m3.xlarge",
    "m4.10xlarge",
    "m4.16xlarge",
    "m4.2xlarge",
    "m4.4xlarge",
    "m4.large",
    "m4.xlarge",
    "m5.12xlarge",
    "m5.16xlarge",
    "m5.24xlarge",
    "m5.2xlarge",
    "m5.4xlarge",
    "m5.8xlarge",
    "m5.large",
    "m5.metal",
    "m5.xlarge",
    "m5a.12xlarge",
    "m5a.16xlarge",
    "m5a.24xlarge",
    "m5a.2xlarge",
    "m5a.4xlarge",
    "m5a.8xlarge",
    "m5a.large",
    "m5a.xlarge",
    "m5ad.12xlarge",
    "m5ad.16xlarge",
    "m5ad.24xlarge",
    "m5ad.2xlarge",
    "m5ad.4xlarge",
    "m5ad.8xlarge",
    "m5ad.large",
    "m5ad.xlarge",
    "m5d.12xlarge",
    "m5d.16xlarge",
    "m5d.24xlarge",
    "m5d.2xlarge",
    "m5d.4xlarge",
    "m5d.8xlarge",
    "m5d.large",
    "m5d.metal",
    "m5d.xlarge",
    "m5dn.12xlarge",
    "m5dn.16xlarge",
    "m5dn.24xlarge",
    "m5dn.2xlarge",
    "m5dn.4xlarge",
    "m5dn.8xlarge",
    "m5dn.large",
    "m5dn.metal",
    "m5dn.xlarge",
    "m5n.12xlarge",
    "m5n.16xlarge",
    "m5n.24xlarge",
    "m5n.2xlarge",
    "m5n.4xlarge",
    "m5n.8xlarge",
    "m5n.large",
    "m5n.metal",
    "m5n.xlarge",
    "m5zn.12xlarge",
    "m5zn.2xlarge",
    "m5zn.3xlarge",
    "m5zn.6xlarge",
    "m5zn.large",
    "m5zn.metal",
    "m5zn.xlarge",
    "m6g.12xlarge",
    "m6g.16xlarge",
    "m6g.2xlarge",
    "m6g.4xlarge",
    "m6g.8xlarge",
    "m6g.large",
    "m6g.medium",
    "m6g.metal",
    "m6g.xlarge",
    "m6gd.12xlarge",
    "m6gd.16xlarge",
    "m6gd.2xlarge",
    "m6gd.4xlarge",
    "m6gd.8xlarge",
    "m6gd.large",
    "m6gd.medium",
    "m6gd.metal",
    "m6gd.xlarge",
    "mac1.metal",
    "p2.16xlarge",
    "p2.8xlarge",
    "p2.xlarge",
    "p3.16xlarge",
    "p3.2xlarge",
    "p3.8xlarge",
    "p3dn.24xlarge",
    "p4d.24xlarge",
    "r3.2xlarge",
    "r3.4xlarge",
    "r3.8xlarge",
    "r3.large",
    "r3.xlarge",
    "r4.16xlarge",
    "r4.2xlarge",
    "r4.4xlarge",
    "r4.8xlarge",
    "r4.large",
    "r4.xlarge",
    "r5.12xlarge",
    "r5.16xlarge",
    "r5.24xlarge",
    "r5.2xlarge",
    "r5.4xlarge",
    "r5.8xlarge",
    "r5.large",
    "r5.metal",
    "r5.xlarge",
    "r5a.12xlarge",
    "r5a.16xlarge",
    "r5a.24xlarge",
    "r5a.2xlarge",
    "r5a.4xlarge",
    "r5a.8xlarge",
    "r5a.large",
    "r5a.xlarge",
    "r5ad.12xlarge",
    "r5ad.16xlarge",
    "r5ad.24xlarge",
    "r5ad.2xlarge",
    "r5ad.4xlarge",
    "r5ad.8xlarge",
    "r5ad.large",
    "r5ad.xlarge",
    "r5b.12xlarge",
    "r5b.16xlarge",
    "r5b.24xlarge",
    "r5b.2xlarge",
    "r5b.4xlarge",
    "r5b.8xlarge",
    "r5b.large",
    "r5b.metal",
    "r5b.xlarge",
    "r5d.12xlarge",
    "r5d.16xlarge",
    "r5d.24xlarge",
    "r5d.2xlarge",
    "r5d.4xlarge",
    "r5d.8xlarge",
    "r5d.large",
    "r5d.metal",
    "r5d.xlarge",
    "r5dn.12xlarge",
    "r5dn.16xlarge",
    "r5dn.24xlarge",
    "r5dn.2xlarge",
    "r5dn.4xlarge",
    "r5dn.8xlarge",
    "r5dn.large",
    "r5dn.metal",
    "r5dn.xlarge",
    "r5n.12xlarge",
    "r5n.16xlarge",
    "r5n.24xlarge",
    "r5n.2xlarge",
    "r5n.4xlarge",
    "r5n.8xlarge",
    "r5n.large",
    "r5n.metal",
    "r5n.xlarge",
    "r6g.12xlarge",
    "r6g.16xlarge",
    "r6g.2xlarge",
    "r6g.4xlarge",
    "r6g.8xlarge",
    "r6g.large",
    "r6g.medium",
    "r6g.metal",
    "r6g.xlarge",
    "r6gd.12xlarge",
    "r6gd.16xlarge",
    "r6gd.2xlarge",
    "r6gd.4xlarge",
    "r6gd.8xlarge",
    "r6gd.large",
    "r6gd.medium",
    "r6gd.metal",
    "r6gd.xlarge",
    "t1.micro",
    "t2.2xlarge",
    "t2.large",
    "t2.medium",
    "t2.micro",
    "t2.nano",
    "t2.small",
    "t2.xlarge",
    "t3.2xlarge",
    "t3.large",
    "t3.medium",
    "t3.micro",
    "t3.nano",
    "t3.small",
    "t3.xlarge",
    "t3a.2xlarge",
    "t3a.large",
    "t3a.medium",
    "t3a.micro",
    "t3a.nano",
    "t3a.small",
    "t3a.xlarge",
    "t4g.2xlarge",
    "t4g.large",
    "t4g.medium",
    "t4g.micro",
    "t4g.nano",
    "t4g.small",
    "t4g.xlarge",
    "u-12tb1.112xlarge",
    "u-12tb1.metal",
    "u-18tb1.metal",
    "u-24tb1.metal",
    "u-6tb1.112xlarge",
    "u-6tb1.56xlarge",
    "u-6tb1.metal",
    "u-9tb1.112xlarge",
    "u-9tb1.metal",
    "x1.16xlarge",
    "x1.32xlarge",
    "x1e.16xlarge",
    "x1e.2xlarge",
    "x1e.32xlarge",
    "x1e.4xlarge",
    "x1e.8xlarge",
    "x1e.xlarge",
    "x2gd.12xlarge",
    "x2gd.16xlarge",
    "x2gd.2xlarge",
    "x2gd.4xlarge",
    "x2gd.8xlarge",
    "x2gd.large",
    "x2gd.medium",
    "x2gd.metal",
    "x2gd.xlarge",
    "z1d.12xlarge",
    "z1d.2xlarge",
    "z1d.3xlarge",
    "z1d.6xlarge",
    "z1d.large",
    "z1d.metal",
    "z1d.xlarge",
]
InterfacePermissionTypeType = Literal["EIP-ASSOCIATE", "INSTANCE-ATTACH"]
InterfaceProtocolTypeType = Literal["GRE", "VLAN"]
Ipv6SupportValueType = Literal["disable", "enable"]
KeyPairExistsWaiterName = Literal["key_pair_exists"]
LaunchTemplateErrorCodeType = Literal[
    "launchTemplateIdDoesNotExist",
    "launchTemplateIdMalformed",
    "launchTemplateNameDoesNotExist",
    "launchTemplateNameMalformed",
    "launchTemplateVersionDoesNotExist",
    "unexpectedError",
]
LaunchTemplateHttpTokensStateType = Literal["optional", "required"]
LaunchTemplateInstanceMetadataEndpointStateType = Literal["disabled", "enabled"]
LaunchTemplateInstanceMetadataOptionsStateType = Literal["applied", "pending"]
ListingStateType = Literal["available", "cancelled", "pending", "sold"]
ListingStatusType = Literal["active", "cancelled", "closed", "pending"]
LocalGatewayRouteStateType = Literal["active", "blackhole", "deleted", "deleting", "pending"]
LocalGatewayRouteTypeType = Literal["propagated", "static"]
LocationTypeType = Literal["availability-zone", "availability-zone-id", "region"]
LogDestinationTypeType = Literal["cloud-watch-logs", "s3"]
MarketTypeType = Literal["spot"]
MembershipTypeType = Literal["igmp", "static"]
ModifyAvailabilityZoneOptInStatusType = Literal["not-opted-in", "opted-in"]
MonitoringStateType = Literal["disabled", "disabling", "enabled", "pending"]
MoveStatusType = Literal["movingToVpc", "restoringToClassic"]
MulticastSupportValueType = Literal["disable", "enable"]
NatGatewayAvailableWaiterName = Literal["nat_gateway_available"]
NatGatewayStateType = Literal["available", "deleted", "deleting", "failed", "pending"]
NetworkInterfaceAttributeType = Literal["attachment", "description", "groupSet", "sourceDestCheck"]
NetworkInterfaceAvailableWaiterName = Literal["network_interface_available"]
NetworkInterfaceCreationTypeType = Literal["branch", "efa", "trunk"]
NetworkInterfacePermissionStateCodeType = Literal["granted", "pending", "revoked", "revoking"]
NetworkInterfaceStatusType = Literal["associated", "attaching", "available", "detaching", "in-use"]
NetworkInterfaceTypeType = Literal["efa", "interface", "natGateway", "trunk"]
OfferingClassTypeType = Literal["convertible", "standard"]
OfferingTypeValuesType = Literal[
    "All Upfront",
    "Heavy Utilization",
    "Light Utilization",
    "Medium Utilization",
    "No Upfront",
    "Partial Upfront",
]
OnDemandAllocationStrategyType = Literal["lowestPrice", "prioritized"]
OperationTypeType = Literal["add", "remove"]
PartitionLoadFrequencyType = Literal["daily", "monthly", "none", "weekly"]
PasswordDataAvailableWaiterName = Literal["password_data_available"]
PaymentOptionType = Literal["AllUpfront", "NoUpfront", "PartialUpfront"]
PermissionGroupType = Literal["all"]
PlacementGroupStateType = Literal["available", "deleted", "deleting", "pending"]
PlacementGroupStrategyType = Literal["cluster", "partition", "spread"]
PlacementStrategyType = Literal["cluster", "partition", "spread"]
PlatformValuesType = Literal["Windows"]
PrefixListStateType = Literal[
    "create-complete",
    "create-failed",
    "create-in-progress",
    "delete-complete",
    "delete-failed",
    "delete-in-progress",
    "modify-complete",
    "modify-failed",
    "modify-in-progress",
    "restore-complete",
    "restore-failed",
    "restore-in-progress",
]
PrincipalTypeType = Literal["Account", "All", "OrganizationUnit", "Role", "Service", "User"]
ProductCodeValuesType = Literal["devpay", "marketplace"]
ProtocolType = Literal["tcp", "udp"]
ProtocolValueType = Literal["gre"]
RIProductDescriptionType = Literal[
    "Linux/UNIX", "Linux/UNIX (Amazon VPC)", "Windows", "Windows (Amazon VPC)"
]
RecurringChargeFrequencyType = Literal["Hourly"]
ReplaceRootVolumeTaskStateType = Literal[
    "failed", "failed-detached", "failing", "in-progress", "pending", "succeeded"
]
ReplacementStrategyType = Literal["launch"]
ReportInstanceReasonCodesType = Literal[
    "instance-stuck-in-state",
    "not-accepting-credentials",
    "other",
    "password-not-available",
    "performance-ebs-volume",
    "performance-instance-store",
    "performance-network",
    "performance-other",
    "unresponsive",
]
ReportStatusTypeType = Literal["impaired", "ok"]
ReservationStateType = Literal["active", "payment-failed", "payment-pending", "retired"]
ReservedInstanceStateType = Literal[
    "active", "payment-failed", "payment-pending", "queued", "queued-deleted", "retired"
]
ResetFpgaImageAttributeNameType = Literal["loadPermission"]
ResetImageAttributeNameType = Literal["launchPermission"]
ResourceTypeType = Literal[
    "client-vpn-endpoint",
    "customer-gateway",
    "dedicated-host",
    "dhcp-options",
    "egress-only-internet-gateway",
    "elastic-gpu",
    "elastic-ip",
    "export-image-task",
    "export-instance-task",
    "fleet",
    "fpga-image",
    "host-reservation",
    "image",
    "import-image-task",
    "import-snapshot-task",
    "instance",
    "instance-event-window",
    "internet-gateway",
    "key-pair",
    "launch-template",
    "local-gateway-route-table-vpc-association",
    "natgateway",
    "network-acl",
    "network-insights-analysis",
    "network-insights-path",
    "network-interface",
    "placement-group",
    "reserved-instances",
    "route-table",
    "security-group",
    "security-group-rule",
    "snapshot",
    "spot-fleet-request",
    "spot-instances-request",
    "subnet",
    "traffic-mirror-filter",
    "traffic-mirror-session",
    "traffic-mirror-target",
    "transit-gateway",
    "transit-gateway-attachment",
    "transit-gateway-connect-peer",
    "transit-gateway-multicast-domain",
    "transit-gateway-route-table",
    "volume",
    "vpc",
    "vpc-flow-log",
    "vpc-peering-connection",
    "vpn-connection",
    "vpn-gateway",
]
RootDeviceTypeType = Literal["ebs", "instance-store"]
RouteOriginType = Literal["CreateRoute", "CreateRouteTable", "EnableVgwRoutePropagation"]
RouteStateType = Literal["active", "blackhole"]
RouteTableAssociationStateCodeType = Literal[
    "associated", "associating", "disassociated", "disassociating", "failed"
]
RuleActionType = Literal["allow", "deny"]
SearchLocalGatewayRoutesPaginatorName = Literal["search_local_gateway_routes"]
SearchTransitGatewayMulticastGroupsPaginatorName = Literal[
    "search_transit_gateway_multicast_groups"
]
SecurityGroupExistsWaiterName = Literal["security_group_exists"]
SelfServicePortalType = Literal["disabled", "enabled"]
ServiceStateType = Literal["Available", "Deleted", "Deleting", "Failed", "Pending"]
ServiceTypeType = Literal["Gateway", "GatewayLoadBalancer", "Interface"]
ShutdownBehaviorType = Literal["stop", "terminate"]
SnapshotAttributeNameType = Literal["createVolumePermission", "productCodes"]
SnapshotCompletedWaiterName = Literal["snapshot_completed"]
SnapshotStateType = Literal["completed", "error", "pending"]
SpotAllocationStrategyType = Literal[
    "capacity-optimized", "capacity-optimized-prioritized", "diversified", "lowest-price"
]
SpotInstanceInterruptionBehaviorType = Literal["hibernate", "stop", "terminate"]
SpotInstanceRequestFulfilledWaiterName = Literal["spot_instance_request_fulfilled"]
SpotInstanceStateType = Literal["active", "cancelled", "closed", "failed", "open"]
SpotInstanceTypeType = Literal["one-time", "persistent"]
StateType = Literal[
    "Available",
    "Deleted",
    "Deleting",
    "Expired",
    "Failed",
    "Pending",
    "PendingAcceptance",
    "Rejected",
]
StaticSourcesSupportValueType = Literal["disable", "enable"]
StatusNameType = Literal["reachability"]
StatusType = Literal["InClassic", "InVpc", "MoveInProgress"]
StatusTypeType = Literal["failed", "initializing", "insufficient-data", "passed"]
SubnetAvailableWaiterName = Literal["subnet_available"]
SubnetCidrBlockStateCodeType = Literal[
    "associated", "associating", "disassociated", "disassociating", "failed", "failing"
]
SubnetCidrReservationTypeType = Literal["explicit", "prefix"]
SubnetStateType = Literal["available", "pending"]
SummaryStatusType = Literal["impaired", "initializing", "insufficient-data", "not-applicable", "ok"]
SystemStatusOkWaiterName = Literal["system_status_ok"]
TelemetryStatusType = Literal["DOWN", "UP"]
TenancyType = Literal["dedicated", "default", "host"]
TrafficDirectionType = Literal["egress", "ingress"]
TrafficMirrorFilterRuleFieldType = Literal[
    "description", "destination-port-range", "protocol", "source-port-range"
]
TrafficMirrorNetworkServiceType = Literal["amazon-dns"]
TrafficMirrorRuleActionType = Literal["accept", "reject"]
TrafficMirrorSessionFieldType = Literal["description", "packet-length", "virtual-network-id"]
TrafficMirrorTargetTypeType = Literal["network-interface", "network-load-balancer"]
TrafficTypeType = Literal["ACCEPT", "ALL", "REJECT"]
TransitGatewayAssociationStateType = Literal[
    "associated", "associating", "disassociated", "disassociating"
]
TransitGatewayAttachmentResourceTypeType = Literal[
    "connect", "direct-connect-gateway", "peering", "tgw-peering", "vpc", "vpn"
]
TransitGatewayAttachmentStateType = Literal[
    "available",
    "deleted",
    "deleting",
    "failed",
    "failing",
    "initiating",
    "initiatingRequest",
    "modifying",
    "pending",
    "pendingAcceptance",
    "rejected",
    "rejecting",
    "rollingBack",
]
TransitGatewayConnectPeerStateType = Literal["available", "deleted", "deleting", "pending"]
TransitGatewayMulitcastDomainAssociationStateType = Literal[
    "associated",
    "associating",
    "disassociated",
    "disassociating",
    "failed",
    "pendingAcceptance",
    "rejected",
]
TransitGatewayMulticastDomainStateType = Literal["available", "deleted", "deleting", "pending"]
TransitGatewayPrefixListReferenceStateType = Literal[
    "available", "deleting", "modifying", "pending"
]
TransitGatewayPropagationStateType = Literal["disabled", "disabling", "enabled", "enabling"]
TransitGatewayRouteStateType = Literal["active", "blackhole", "deleted", "deleting", "pending"]
TransitGatewayRouteTableStateType = Literal["available", "deleted", "deleting", "pending"]
TransitGatewayRouteTypeType = Literal["propagated", "static"]
TransitGatewayStateType = Literal["available", "deleted", "deleting", "modifying", "pending"]
TransportProtocolType = Literal["tcp", "udp"]
TunnelInsideIpVersionType = Literal["ipv4", "ipv6"]
UnlimitedSupportedInstanceFamilyType = Literal["t2", "t3", "t3a", "t4g"]
UnsuccessfulInstanceCreditSpecificationErrorCodeType = Literal[
    "IncorrectInstanceState",
    "InstanceCreditSpecification.NotSupported",
    "InvalidInstanceID.Malformed",
    "InvalidInstanceID.NotFound",
]
UsageClassTypeType = Literal["on-demand", "spot"]
VirtualizationTypeType = Literal["hvm", "paravirtual"]
VolumeAttachmentStateType = Literal["attached", "attaching", "busy", "detached", "detaching"]
VolumeAttributeNameType = Literal["autoEnableIO", "productCodes"]
VolumeAvailableWaiterName = Literal["volume_available"]
VolumeDeletedWaiterName = Literal["volume_deleted"]
VolumeInUseWaiterName = Literal["volume_in_use"]
VolumeModificationStateType = Literal["completed", "failed", "modifying", "optimizing"]
VolumeStateType = Literal["available", "creating", "deleted", "deleting", "error", "in-use"]
VolumeStatusInfoStatusType = Literal["impaired", "insufficient-data", "ok"]
VolumeStatusNameType = Literal["io-enabled", "io-performance"]
VolumeTypeType = Literal["gp2", "gp3", "io1", "io2", "sc1", "st1", "standard"]
VpcAttributeNameType = Literal["enableDnsHostnames", "enableDnsSupport"]
VpcAvailableWaiterName = Literal["vpc_available"]
VpcCidrBlockStateCodeType = Literal[
    "associated", "associating", "disassociated", "disassociating", "failed", "failing"
]
VpcEndpointTypeType = Literal["Gateway", "GatewayLoadBalancer", "Interface"]
VpcExistsWaiterName = Literal["vpc_exists"]
VpcPeeringConnectionDeletedWaiterName = Literal["vpc_peering_connection_deleted"]
VpcPeeringConnectionExistsWaiterName = Literal["vpc_peering_connection_exists"]
VpcPeeringConnectionStateReasonCodeType = Literal[
    "active",
    "deleted",
    "deleting",
    "expired",
    "failed",
    "initiating-request",
    "pending-acceptance",
    "provisioning",
    "rejected",
]
VpcStateType = Literal["available", "pending"]
VpcTenancyType = Literal["default"]
VpnConnectionAvailableWaiterName = Literal["vpn_connection_available"]
VpnConnectionDeletedWaiterName = Literal["vpn_connection_deleted"]
VpnEcmpSupportValueType = Literal["disable", "enable"]
VpnProtocolType = Literal["openvpn"]
VpnStateType = Literal["available", "deleted", "deleting", "pending"]
VpnStaticRouteSourceType = Literal["Static"]
WeekDayType = Literal["friday", "monday", "saturday", "sunday", "thursday", "tuesday", "wednesday"]
scopeType = Literal["Availability Zone", "Region"]
