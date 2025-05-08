"""
Type annotations for ec2 service client paginators.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ec2.client import EC2Client
    from mypy_boto3_ec2.paginator import (
        DescribeAddressTransfersPaginator,
        DescribeAddressesAttributePaginator,
        DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator,
        DescribeByoipCidrsPaginator,
        DescribeCapacityBlockExtensionHistoryPaginator,
        DescribeCapacityBlockExtensionOfferingsPaginator,
        DescribeCapacityBlockOfferingsPaginator,
        DescribeCapacityReservationBillingRequestsPaginator,
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
        DescribeInstanceImageMetadataPaginator,
        DescribeInstanceStatusPaginator,
        DescribeInstanceTopologyPaginator,
        DescribeInstanceTypeOfferingsPaginator,
        DescribeInstanceTypesPaginator,
        DescribeInstancesPaginator,
        DescribeInternetGatewaysPaginator,
        DescribeIpamPoolsPaginator,
        DescribeIpamResourceDiscoveriesPaginator,
        DescribeIpamResourceDiscoveryAssociationsPaginator,
        DescribeIpamScopesPaginator,
        DescribeIpamsPaginator,
        DescribeIpv6PoolsPaginator,
        DescribeLaunchTemplateVersionsPaginator,
        DescribeLaunchTemplatesPaginator,
        DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator,
        DescribeLocalGatewayRouteTableVpcAssociationsPaginator,
        DescribeLocalGatewayRouteTablesPaginator,
        DescribeLocalGatewayVirtualInterfaceGroupsPaginator,
        DescribeLocalGatewayVirtualInterfacesPaginator,
        DescribeLocalGatewaysPaginator,
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
        DescribeRouteServerEndpointsPaginator,
        DescribeRouteServerPeersPaginator,
        DescribeRouteServersPaginator,
        DescribeRouteTablesPaginator,
        DescribeScheduledInstanceAvailabilityPaginator,
        DescribeScheduledInstancesPaginator,
        DescribeSecurityGroupRulesPaginator,
        DescribeSecurityGroupVpcAssociationsPaginator,
        DescribeSecurityGroupsPaginator,
        DescribeSnapshotTierStatusPaginator,
        DescribeSnapshotsPaginator,
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
        DescribeTransitGatewayVpcAttachmentsPaginator,
        DescribeTransitGatewaysPaginator,
        DescribeTrunkInterfaceAssociationsPaginator,
        DescribeVerifiedAccessEndpointsPaginator,
        DescribeVerifiedAccessGroupsPaginator,
        DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator,
        DescribeVerifiedAccessInstancesPaginator,
        DescribeVerifiedAccessTrustProvidersPaginator,
        DescribeVolumeStatusPaginator,
        DescribeVolumesModificationsPaginator,
        DescribeVolumesPaginator,
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

    session = Session()
    client: EC2Client = session.client("ec2")

    describe_address_transfers_paginator: DescribeAddressTransfersPaginator = client.get_paginator("describe_address_transfers")
    describe_addresses_attribute_paginator: DescribeAddressesAttributePaginator = client.get_paginator("describe_addresses_attribute")
    describe_aws_network_performance_metric_subscriptions_paginator: DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator = client.get_paginator("describe_aws_network_performance_metric_subscriptions")
    describe_byoip_cidrs_paginator: DescribeByoipCidrsPaginator = client.get_paginator("describe_byoip_cidrs")
    describe_capacity_block_extension_history_paginator: DescribeCapacityBlockExtensionHistoryPaginator = client.get_paginator("describe_capacity_block_extension_history")
    describe_capacity_block_extension_offerings_paginator: DescribeCapacityBlockExtensionOfferingsPaginator = client.get_paginator("describe_capacity_block_extension_offerings")
    describe_capacity_block_offerings_paginator: DescribeCapacityBlockOfferingsPaginator = client.get_paginator("describe_capacity_block_offerings")
    describe_capacity_reservation_billing_requests_paginator: DescribeCapacityReservationBillingRequestsPaginator = client.get_paginator("describe_capacity_reservation_billing_requests")
    describe_capacity_reservation_fleets_paginator: DescribeCapacityReservationFleetsPaginator = client.get_paginator("describe_capacity_reservation_fleets")
    describe_capacity_reservations_paginator: DescribeCapacityReservationsPaginator = client.get_paginator("describe_capacity_reservations")
    describe_carrier_gateways_paginator: DescribeCarrierGatewaysPaginator = client.get_paginator("describe_carrier_gateways")
    describe_classic_link_instances_paginator: DescribeClassicLinkInstancesPaginator = client.get_paginator("describe_classic_link_instances")
    describe_client_vpn_authorization_rules_paginator: DescribeClientVpnAuthorizationRulesPaginator = client.get_paginator("describe_client_vpn_authorization_rules")
    describe_client_vpn_connections_paginator: DescribeClientVpnConnectionsPaginator = client.get_paginator("describe_client_vpn_connections")
    describe_client_vpn_endpoints_paginator: DescribeClientVpnEndpointsPaginator = client.get_paginator("describe_client_vpn_endpoints")
    describe_client_vpn_routes_paginator: DescribeClientVpnRoutesPaginator = client.get_paginator("describe_client_vpn_routes")
    describe_client_vpn_target_networks_paginator: DescribeClientVpnTargetNetworksPaginator = client.get_paginator("describe_client_vpn_target_networks")
    describe_coip_pools_paginator: DescribeCoipPoolsPaginator = client.get_paginator("describe_coip_pools")
    describe_dhcp_options_paginator: DescribeDhcpOptionsPaginator = client.get_paginator("describe_dhcp_options")
    describe_egress_only_internet_gateways_paginator: DescribeEgressOnlyInternetGatewaysPaginator = client.get_paginator("describe_egress_only_internet_gateways")
    describe_export_image_tasks_paginator: DescribeExportImageTasksPaginator = client.get_paginator("describe_export_image_tasks")
    describe_fast_launch_images_paginator: DescribeFastLaunchImagesPaginator = client.get_paginator("describe_fast_launch_images")
    describe_fast_snapshot_restores_paginator: DescribeFastSnapshotRestoresPaginator = client.get_paginator("describe_fast_snapshot_restores")
    describe_fleets_paginator: DescribeFleetsPaginator = client.get_paginator("describe_fleets")
    describe_flow_logs_paginator: DescribeFlowLogsPaginator = client.get_paginator("describe_flow_logs")
    describe_fpga_images_paginator: DescribeFpgaImagesPaginator = client.get_paginator("describe_fpga_images")
    describe_host_reservation_offerings_paginator: DescribeHostReservationOfferingsPaginator = client.get_paginator("describe_host_reservation_offerings")
    describe_host_reservations_paginator: DescribeHostReservationsPaginator = client.get_paginator("describe_host_reservations")
    describe_hosts_paginator: DescribeHostsPaginator = client.get_paginator("describe_hosts")
    describe_iam_instance_profile_associations_paginator: DescribeIamInstanceProfileAssociationsPaginator = client.get_paginator("describe_iam_instance_profile_associations")
    describe_images_paginator: DescribeImagesPaginator = client.get_paginator("describe_images")
    describe_import_image_tasks_paginator: DescribeImportImageTasksPaginator = client.get_paginator("describe_import_image_tasks")
    describe_import_snapshot_tasks_paginator: DescribeImportSnapshotTasksPaginator = client.get_paginator("describe_import_snapshot_tasks")
    describe_instance_connect_endpoints_paginator: DescribeInstanceConnectEndpointsPaginator = client.get_paginator("describe_instance_connect_endpoints")
    describe_instance_credit_specifications_paginator: DescribeInstanceCreditSpecificationsPaginator = client.get_paginator("describe_instance_credit_specifications")
    describe_instance_event_windows_paginator: DescribeInstanceEventWindowsPaginator = client.get_paginator("describe_instance_event_windows")
    describe_instance_image_metadata_paginator: DescribeInstanceImageMetadataPaginator = client.get_paginator("describe_instance_image_metadata")
    describe_instance_status_paginator: DescribeInstanceStatusPaginator = client.get_paginator("describe_instance_status")
    describe_instance_topology_paginator: DescribeInstanceTopologyPaginator = client.get_paginator("describe_instance_topology")
    describe_instance_type_offerings_paginator: DescribeInstanceTypeOfferingsPaginator = client.get_paginator("describe_instance_type_offerings")
    describe_instance_types_paginator: DescribeInstanceTypesPaginator = client.get_paginator("describe_instance_types")
    describe_instances_paginator: DescribeInstancesPaginator = client.get_paginator("describe_instances")
    describe_internet_gateways_paginator: DescribeInternetGatewaysPaginator = client.get_paginator("describe_internet_gateways")
    describe_ipam_pools_paginator: DescribeIpamPoolsPaginator = client.get_paginator("describe_ipam_pools")
    describe_ipam_resource_discoveries_paginator: DescribeIpamResourceDiscoveriesPaginator = client.get_paginator("describe_ipam_resource_discoveries")
    describe_ipam_resource_discovery_associations_paginator: DescribeIpamResourceDiscoveryAssociationsPaginator = client.get_paginator("describe_ipam_resource_discovery_associations")
    describe_ipam_scopes_paginator: DescribeIpamScopesPaginator = client.get_paginator("describe_ipam_scopes")
    describe_ipams_paginator: DescribeIpamsPaginator = client.get_paginator("describe_ipams")
    describe_ipv6_pools_paginator: DescribeIpv6PoolsPaginator = client.get_paginator("describe_ipv6_pools")
    describe_launch_template_versions_paginator: DescribeLaunchTemplateVersionsPaginator = client.get_paginator("describe_launch_template_versions")
    describe_launch_templates_paginator: DescribeLaunchTemplatesPaginator = client.get_paginator("describe_launch_templates")
    describe_local_gateway_route_table_virtual_interface_group_associations_paginator: DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator = client.get_paginator("describe_local_gateway_route_table_virtual_interface_group_associations")
    describe_local_gateway_route_table_vpc_associations_paginator: DescribeLocalGatewayRouteTableVpcAssociationsPaginator = client.get_paginator("describe_local_gateway_route_table_vpc_associations")
    describe_local_gateway_route_tables_paginator: DescribeLocalGatewayRouteTablesPaginator = client.get_paginator("describe_local_gateway_route_tables")
    describe_local_gateway_virtual_interface_groups_paginator: DescribeLocalGatewayVirtualInterfaceGroupsPaginator = client.get_paginator("describe_local_gateway_virtual_interface_groups")
    describe_local_gateway_virtual_interfaces_paginator: DescribeLocalGatewayVirtualInterfacesPaginator = client.get_paginator("describe_local_gateway_virtual_interfaces")
    describe_local_gateways_paginator: DescribeLocalGatewaysPaginator = client.get_paginator("describe_local_gateways")
    describe_mac_hosts_paginator: DescribeMacHostsPaginator = client.get_paginator("describe_mac_hosts")
    describe_managed_prefix_lists_paginator: DescribeManagedPrefixListsPaginator = client.get_paginator("describe_managed_prefix_lists")
    describe_moving_addresses_paginator: DescribeMovingAddressesPaginator = client.get_paginator("describe_moving_addresses")
    describe_nat_gateways_paginator: DescribeNatGatewaysPaginator = client.get_paginator("describe_nat_gateways")
    describe_network_acls_paginator: DescribeNetworkAclsPaginator = client.get_paginator("describe_network_acls")
    describe_network_insights_access_scope_analyses_paginator: DescribeNetworkInsightsAccessScopeAnalysesPaginator = client.get_paginator("describe_network_insights_access_scope_analyses")
    describe_network_insights_access_scopes_paginator: DescribeNetworkInsightsAccessScopesPaginator = client.get_paginator("describe_network_insights_access_scopes")
    describe_network_insights_analyses_paginator: DescribeNetworkInsightsAnalysesPaginator = client.get_paginator("describe_network_insights_analyses")
    describe_network_insights_paths_paginator: DescribeNetworkInsightsPathsPaginator = client.get_paginator("describe_network_insights_paths")
    describe_network_interface_permissions_paginator: DescribeNetworkInterfacePermissionsPaginator = client.get_paginator("describe_network_interface_permissions")
    describe_network_interfaces_paginator: DescribeNetworkInterfacesPaginator = client.get_paginator("describe_network_interfaces")
    describe_prefix_lists_paginator: DescribePrefixListsPaginator = client.get_paginator("describe_prefix_lists")
    describe_principal_id_format_paginator: DescribePrincipalIdFormatPaginator = client.get_paginator("describe_principal_id_format")
    describe_public_ipv4_pools_paginator: DescribePublicIpv4PoolsPaginator = client.get_paginator("describe_public_ipv4_pools")
    describe_replace_root_volume_tasks_paginator: DescribeReplaceRootVolumeTasksPaginator = client.get_paginator("describe_replace_root_volume_tasks")
    describe_reserved_instances_modifications_paginator: DescribeReservedInstancesModificationsPaginator = client.get_paginator("describe_reserved_instances_modifications")
    describe_reserved_instances_offerings_paginator: DescribeReservedInstancesOfferingsPaginator = client.get_paginator("describe_reserved_instances_offerings")
    describe_route_server_endpoints_paginator: DescribeRouteServerEndpointsPaginator = client.get_paginator("describe_route_server_endpoints")
    describe_route_server_peers_paginator: DescribeRouteServerPeersPaginator = client.get_paginator("describe_route_server_peers")
    describe_route_servers_paginator: DescribeRouteServersPaginator = client.get_paginator("describe_route_servers")
    describe_route_tables_paginator: DescribeRouteTablesPaginator = client.get_paginator("describe_route_tables")
    describe_scheduled_instance_availability_paginator: DescribeScheduledInstanceAvailabilityPaginator = client.get_paginator("describe_scheduled_instance_availability")
    describe_scheduled_instances_paginator: DescribeScheduledInstancesPaginator = client.get_paginator("describe_scheduled_instances")
    describe_security_group_rules_paginator: DescribeSecurityGroupRulesPaginator = client.get_paginator("describe_security_group_rules")
    describe_security_group_vpc_associations_paginator: DescribeSecurityGroupVpcAssociationsPaginator = client.get_paginator("describe_security_group_vpc_associations")
    describe_security_groups_paginator: DescribeSecurityGroupsPaginator = client.get_paginator("describe_security_groups")
    describe_snapshot_tier_status_paginator: DescribeSnapshotTierStatusPaginator = client.get_paginator("describe_snapshot_tier_status")
    describe_snapshots_paginator: DescribeSnapshotsPaginator = client.get_paginator("describe_snapshots")
    describe_spot_fleet_instances_paginator: DescribeSpotFleetInstancesPaginator = client.get_paginator("describe_spot_fleet_instances")
    describe_spot_fleet_requests_paginator: DescribeSpotFleetRequestsPaginator = client.get_paginator("describe_spot_fleet_requests")
    describe_spot_instance_requests_paginator: DescribeSpotInstanceRequestsPaginator = client.get_paginator("describe_spot_instance_requests")
    describe_spot_price_history_paginator: DescribeSpotPriceHistoryPaginator = client.get_paginator("describe_spot_price_history")
    describe_stale_security_groups_paginator: DescribeStaleSecurityGroupsPaginator = client.get_paginator("describe_stale_security_groups")
    describe_store_image_tasks_paginator: DescribeStoreImageTasksPaginator = client.get_paginator("describe_store_image_tasks")
    describe_subnets_paginator: DescribeSubnetsPaginator = client.get_paginator("describe_subnets")
    describe_tags_paginator: DescribeTagsPaginator = client.get_paginator("describe_tags")
    describe_traffic_mirror_filters_paginator: DescribeTrafficMirrorFiltersPaginator = client.get_paginator("describe_traffic_mirror_filters")
    describe_traffic_mirror_sessions_paginator: DescribeTrafficMirrorSessionsPaginator = client.get_paginator("describe_traffic_mirror_sessions")
    describe_traffic_mirror_targets_paginator: DescribeTrafficMirrorTargetsPaginator = client.get_paginator("describe_traffic_mirror_targets")
    describe_transit_gateway_attachments_paginator: DescribeTransitGatewayAttachmentsPaginator = client.get_paginator("describe_transit_gateway_attachments")
    describe_transit_gateway_connect_peers_paginator: DescribeTransitGatewayConnectPeersPaginator = client.get_paginator("describe_transit_gateway_connect_peers")
    describe_transit_gateway_connects_paginator: DescribeTransitGatewayConnectsPaginator = client.get_paginator("describe_transit_gateway_connects")
    describe_transit_gateway_multicast_domains_paginator: DescribeTransitGatewayMulticastDomainsPaginator = client.get_paginator("describe_transit_gateway_multicast_domains")
    describe_transit_gateway_peering_attachments_paginator: DescribeTransitGatewayPeeringAttachmentsPaginator = client.get_paginator("describe_transit_gateway_peering_attachments")
    describe_transit_gateway_policy_tables_paginator: DescribeTransitGatewayPolicyTablesPaginator = client.get_paginator("describe_transit_gateway_policy_tables")
    describe_transit_gateway_route_table_announcements_paginator: DescribeTransitGatewayRouteTableAnnouncementsPaginator = client.get_paginator("describe_transit_gateway_route_table_announcements")
    describe_transit_gateway_route_tables_paginator: DescribeTransitGatewayRouteTablesPaginator = client.get_paginator("describe_transit_gateway_route_tables")
    describe_transit_gateway_vpc_attachments_paginator: DescribeTransitGatewayVpcAttachmentsPaginator = client.get_paginator("describe_transit_gateway_vpc_attachments")
    describe_transit_gateways_paginator: DescribeTransitGatewaysPaginator = client.get_paginator("describe_transit_gateways")
    describe_trunk_interface_associations_paginator: DescribeTrunkInterfaceAssociationsPaginator = client.get_paginator("describe_trunk_interface_associations")
    describe_verified_access_endpoints_paginator: DescribeVerifiedAccessEndpointsPaginator = client.get_paginator("describe_verified_access_endpoints")
    describe_verified_access_groups_paginator: DescribeVerifiedAccessGroupsPaginator = client.get_paginator("describe_verified_access_groups")
    describe_verified_access_instance_logging_configurations_paginator: DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator = client.get_paginator("describe_verified_access_instance_logging_configurations")
    describe_verified_access_instances_paginator: DescribeVerifiedAccessInstancesPaginator = client.get_paginator("describe_verified_access_instances")
    describe_verified_access_trust_providers_paginator: DescribeVerifiedAccessTrustProvidersPaginator = client.get_paginator("describe_verified_access_trust_providers")
    describe_volume_status_paginator: DescribeVolumeStatusPaginator = client.get_paginator("describe_volume_status")
    describe_volumes_modifications_paginator: DescribeVolumesModificationsPaginator = client.get_paginator("describe_volumes_modifications")
    describe_volumes_paginator: DescribeVolumesPaginator = client.get_paginator("describe_volumes")
    describe_vpc_classic_link_dns_support_paginator: DescribeVpcClassicLinkDnsSupportPaginator = client.get_paginator("describe_vpc_classic_link_dns_support")
    describe_vpc_endpoint_connection_notifications_paginator: DescribeVpcEndpointConnectionNotificationsPaginator = client.get_paginator("describe_vpc_endpoint_connection_notifications")
    describe_vpc_endpoint_connections_paginator: DescribeVpcEndpointConnectionsPaginator = client.get_paginator("describe_vpc_endpoint_connections")
    describe_vpc_endpoint_service_configurations_paginator: DescribeVpcEndpointServiceConfigurationsPaginator = client.get_paginator("describe_vpc_endpoint_service_configurations")
    describe_vpc_endpoint_service_permissions_paginator: DescribeVpcEndpointServicePermissionsPaginator = client.get_paginator("describe_vpc_endpoint_service_permissions")
    describe_vpc_endpoint_services_paginator: DescribeVpcEndpointServicesPaginator = client.get_paginator("describe_vpc_endpoint_services")
    describe_vpc_endpoints_paginator: DescribeVpcEndpointsPaginator = client.get_paginator("describe_vpc_endpoints")
    describe_vpc_peering_connections_paginator: DescribeVpcPeeringConnectionsPaginator = client.get_paginator("describe_vpc_peering_connections")
    describe_vpcs_paginator: DescribeVpcsPaginator = client.get_paginator("describe_vpcs")
    get_associated_ipv6_pool_cidrs_paginator: GetAssociatedIpv6PoolCidrsPaginator = client.get_paginator("get_associated_ipv6_pool_cidrs")
    get_aws_network_performance_data_paginator: GetAwsNetworkPerformanceDataPaginator = client.get_paginator("get_aws_network_performance_data")
    get_groups_for_capacity_reservation_paginator: GetGroupsForCapacityReservationPaginator = client.get_paginator("get_groups_for_capacity_reservation")
    get_instance_types_from_instance_requirements_paginator: GetInstanceTypesFromInstanceRequirementsPaginator = client.get_paginator("get_instance_types_from_instance_requirements")
    get_ipam_address_history_paginator: GetIpamAddressHistoryPaginator = client.get_paginator("get_ipam_address_history")
    get_ipam_discovered_accounts_paginator: GetIpamDiscoveredAccountsPaginator = client.get_paginator("get_ipam_discovered_accounts")
    get_ipam_discovered_resource_cidrs_paginator: GetIpamDiscoveredResourceCidrsPaginator = client.get_paginator("get_ipam_discovered_resource_cidrs")
    get_ipam_pool_allocations_paginator: GetIpamPoolAllocationsPaginator = client.get_paginator("get_ipam_pool_allocations")
    get_ipam_pool_cidrs_paginator: GetIpamPoolCidrsPaginator = client.get_paginator("get_ipam_pool_cidrs")
    get_ipam_resource_cidrs_paginator: GetIpamResourceCidrsPaginator = client.get_paginator("get_ipam_resource_cidrs")
    get_managed_prefix_list_associations_paginator: GetManagedPrefixListAssociationsPaginator = client.get_paginator("get_managed_prefix_list_associations")
    get_managed_prefix_list_entries_paginator: GetManagedPrefixListEntriesPaginator = client.get_paginator("get_managed_prefix_list_entries")
    get_network_insights_access_scope_analysis_findings_paginator: GetNetworkInsightsAccessScopeAnalysisFindingsPaginator = client.get_paginator("get_network_insights_access_scope_analysis_findings")
    get_security_groups_for_vpc_paginator: GetSecurityGroupsForVpcPaginator = client.get_paginator("get_security_groups_for_vpc")
    get_spot_placement_scores_paginator: GetSpotPlacementScoresPaginator = client.get_paginator("get_spot_placement_scores")
    get_transit_gateway_attachment_propagations_paginator: GetTransitGatewayAttachmentPropagationsPaginator = client.get_paginator("get_transit_gateway_attachment_propagations")
    get_transit_gateway_multicast_domain_associations_paginator: GetTransitGatewayMulticastDomainAssociationsPaginator = client.get_paginator("get_transit_gateway_multicast_domain_associations")
    get_transit_gateway_policy_table_associations_paginator: GetTransitGatewayPolicyTableAssociationsPaginator = client.get_paginator("get_transit_gateway_policy_table_associations")
    get_transit_gateway_prefix_list_references_paginator: GetTransitGatewayPrefixListReferencesPaginator = client.get_paginator("get_transit_gateway_prefix_list_references")
    get_transit_gateway_route_table_associations_paginator: GetTransitGatewayRouteTableAssociationsPaginator = client.get_paginator("get_transit_gateway_route_table_associations")
    get_transit_gateway_route_table_propagations_paginator: GetTransitGatewayRouteTablePropagationsPaginator = client.get_paginator("get_transit_gateway_route_table_propagations")
    get_vpn_connection_device_types_paginator: GetVpnConnectionDeviceTypesPaginator = client.get_paginator("get_vpn_connection_device_types")
    list_images_in_recycle_bin_paginator: ListImagesInRecycleBinPaginator = client.get_paginator("list_images_in_recycle_bin")
    list_snapshots_in_recycle_bin_paginator: ListSnapshotsInRecycleBinPaginator = client.get_paginator("list_snapshots_in_recycle_bin")
    search_local_gateway_routes_paginator: SearchLocalGatewayRoutesPaginator = client.get_paginator("search_local_gateway_routes")
    search_transit_gateway_multicast_groups_paginator: SearchTransitGatewayMulticastGroupsPaginator = client.get_paginator("search_transit_gateway_multicast_groups")
    ```
"""

from __future__ import annotations

import sys
from typing import TYPE_CHECKING

from botocore.paginate import PageIterator, Paginator

from .type_defs import (
    DescribeAddressesAttributeRequestPaginateTypeDef,
    DescribeAddressesAttributeResultTypeDef,
    DescribeAddressTransfersRequestPaginateTypeDef,
    DescribeAddressTransfersResultTypeDef,
    DescribeAwsNetworkPerformanceMetricSubscriptionsRequestPaginateTypeDef,
    DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef,
    DescribeByoipCidrsRequestPaginateTypeDef,
    DescribeByoipCidrsResultTypeDef,
    DescribeCapacityBlockExtensionHistoryRequestPaginateTypeDef,
    DescribeCapacityBlockExtensionHistoryResultTypeDef,
    DescribeCapacityBlockExtensionOfferingsRequestPaginateTypeDef,
    DescribeCapacityBlockExtensionOfferingsResultTypeDef,
    DescribeCapacityBlockOfferingsRequestPaginateTypeDef,
    DescribeCapacityBlockOfferingsResultTypeDef,
    DescribeCapacityReservationBillingRequestsRequestPaginateTypeDef,
    DescribeCapacityReservationBillingRequestsResultTypeDef,
    DescribeCapacityReservationFleetsRequestPaginateTypeDef,
    DescribeCapacityReservationFleetsResultTypeDef,
    DescribeCapacityReservationsRequestPaginateTypeDef,
    DescribeCapacityReservationsResultTypeDef,
    DescribeCarrierGatewaysRequestPaginateTypeDef,
    DescribeCarrierGatewaysResultTypeDef,
    DescribeClassicLinkInstancesRequestPaginateTypeDef,
    DescribeClassicLinkInstancesResultTypeDef,
    DescribeClientVpnAuthorizationRulesRequestPaginateTypeDef,
    DescribeClientVpnAuthorizationRulesResultTypeDef,
    DescribeClientVpnConnectionsRequestPaginateTypeDef,
    DescribeClientVpnConnectionsResultTypeDef,
    DescribeClientVpnEndpointsRequestPaginateTypeDef,
    DescribeClientVpnEndpointsResultTypeDef,
    DescribeClientVpnRoutesRequestPaginateTypeDef,
    DescribeClientVpnRoutesResultTypeDef,
    DescribeClientVpnTargetNetworksRequestPaginateTypeDef,
    DescribeClientVpnTargetNetworksResultTypeDef,
    DescribeCoipPoolsRequestPaginateTypeDef,
    DescribeCoipPoolsResultTypeDef,
    DescribeDhcpOptionsRequestPaginateTypeDef,
    DescribeDhcpOptionsResultTypeDef,
    DescribeEgressOnlyInternetGatewaysRequestPaginateTypeDef,
    DescribeEgressOnlyInternetGatewaysResultTypeDef,
    DescribeExportImageTasksRequestPaginateTypeDef,
    DescribeExportImageTasksResultTypeDef,
    DescribeFastLaunchImagesRequestPaginateTypeDef,
    DescribeFastLaunchImagesResultTypeDef,
    DescribeFastSnapshotRestoresRequestPaginateTypeDef,
    DescribeFastSnapshotRestoresResultTypeDef,
    DescribeFleetsRequestPaginateTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeFlowLogsRequestPaginateTypeDef,
    DescribeFlowLogsResultTypeDef,
    DescribeFpgaImagesRequestPaginateTypeDef,
    DescribeFpgaImagesResultTypeDef,
    DescribeHostReservationOfferingsRequestPaginateTypeDef,
    DescribeHostReservationOfferingsResultTypeDef,
    DescribeHostReservationsRequestPaginateTypeDef,
    DescribeHostReservationsResultTypeDef,
    DescribeHostsRequestPaginateTypeDef,
    DescribeHostsResultTypeDef,
    DescribeIamInstanceProfileAssociationsRequestPaginateTypeDef,
    DescribeIamInstanceProfileAssociationsResultTypeDef,
    DescribeImagesRequestPaginateTypeDef,
    DescribeImagesResultTypeDef,
    DescribeImportImageTasksRequestPaginateTypeDef,
    DescribeImportImageTasksResultTypeDef,
    DescribeImportSnapshotTasksRequestPaginateTypeDef,
    DescribeImportSnapshotTasksResultTypeDef,
    DescribeInstanceConnectEndpointsRequestPaginateTypeDef,
    DescribeInstanceConnectEndpointsResultTypeDef,
    DescribeInstanceCreditSpecificationsRequestPaginateTypeDef,
    DescribeInstanceCreditSpecificationsResultTypeDef,
    DescribeInstanceEventWindowsRequestPaginateTypeDef,
    DescribeInstanceEventWindowsResultTypeDef,
    DescribeInstanceImageMetadataRequestPaginateTypeDef,
    DescribeInstanceImageMetadataResultTypeDef,
    DescribeInstancesRequestPaginateTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeInstanceStatusRequestPaginateTypeDef,
    DescribeInstanceStatusResultTypeDef,
    DescribeInstanceTopologyRequestPaginateTypeDef,
    DescribeInstanceTopologyResultTypeDef,
    DescribeInstanceTypeOfferingsRequestPaginateTypeDef,
    DescribeInstanceTypeOfferingsResultTypeDef,
    DescribeInstanceTypesRequestPaginateTypeDef,
    DescribeInstanceTypesResultTypeDef,
    DescribeInternetGatewaysRequestPaginateTypeDef,
    DescribeInternetGatewaysResultTypeDef,
    DescribeIpamPoolsRequestPaginateTypeDef,
    DescribeIpamPoolsResultTypeDef,
    DescribeIpamResourceDiscoveriesRequestPaginateTypeDef,
    DescribeIpamResourceDiscoveriesResultTypeDef,
    DescribeIpamResourceDiscoveryAssociationsRequestPaginateTypeDef,
    DescribeIpamResourceDiscoveryAssociationsResultTypeDef,
    DescribeIpamScopesRequestPaginateTypeDef,
    DescribeIpamScopesResultTypeDef,
    DescribeIpamsRequestPaginateTypeDef,
    DescribeIpamsResultTypeDef,
    DescribeIpv6PoolsRequestPaginateTypeDef,
    DescribeIpv6PoolsResultTypeDef,
    DescribeLaunchTemplatesRequestPaginateTypeDef,
    DescribeLaunchTemplatesResultTypeDef,
    DescribeLaunchTemplateVersionsRequestPaginateTypeDef,
    DescribeLaunchTemplateVersionsResultTypeDef,
    DescribeLocalGatewayRouteTablesRequestPaginateTypeDef,
    DescribeLocalGatewayRouteTablesResultTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestPaginateTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsRequestPaginateTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef,
    DescribeLocalGatewaysRequestPaginateTypeDef,
    DescribeLocalGatewaysResultTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsRequestPaginateTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef,
    DescribeLocalGatewayVirtualInterfacesRequestPaginateTypeDef,
    DescribeLocalGatewayVirtualInterfacesResultTypeDef,
    DescribeMacHostsRequestPaginateTypeDef,
    DescribeMacHostsResultTypeDef,
    DescribeManagedPrefixListsRequestPaginateTypeDef,
    DescribeManagedPrefixListsResultTypeDef,
    DescribeMovingAddressesRequestPaginateTypeDef,
    DescribeMovingAddressesResultTypeDef,
    DescribeNatGatewaysRequestPaginateTypeDef,
    DescribeNatGatewaysResultTypeDef,
    DescribeNetworkAclsRequestPaginateTypeDef,
    DescribeNetworkAclsResultTypeDef,
    DescribeNetworkInsightsAccessScopeAnalysesRequestPaginateTypeDef,
    DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef,
    DescribeNetworkInsightsAccessScopesRequestPaginateTypeDef,
    DescribeNetworkInsightsAccessScopesResultTypeDef,
    DescribeNetworkInsightsAnalysesRequestPaginateTypeDef,
    DescribeNetworkInsightsAnalysesResultTypeDef,
    DescribeNetworkInsightsPathsRequestPaginateTypeDef,
    DescribeNetworkInsightsPathsResultTypeDef,
    DescribeNetworkInterfacePermissionsRequestPaginateTypeDef,
    DescribeNetworkInterfacePermissionsResultTypeDef,
    DescribeNetworkInterfacesRequestPaginateTypeDef,
    DescribeNetworkInterfacesResultTypeDef,
    DescribePrefixListsRequestPaginateTypeDef,
    DescribePrefixListsResultTypeDef,
    DescribePrincipalIdFormatRequestPaginateTypeDef,
    DescribePrincipalIdFormatResultTypeDef,
    DescribePublicIpv4PoolsRequestPaginateTypeDef,
    DescribePublicIpv4PoolsResultTypeDef,
    DescribeReplaceRootVolumeTasksRequestPaginateTypeDef,
    DescribeReplaceRootVolumeTasksResultTypeDef,
    DescribeReservedInstancesModificationsRequestPaginateTypeDef,
    DescribeReservedInstancesModificationsResultTypeDef,
    DescribeReservedInstancesOfferingsRequestPaginateTypeDef,
    DescribeReservedInstancesOfferingsResultTypeDef,
    DescribeRouteServerEndpointsRequestPaginateTypeDef,
    DescribeRouteServerEndpointsResultTypeDef,
    DescribeRouteServerPeersRequestPaginateTypeDef,
    DescribeRouteServerPeersResultTypeDef,
    DescribeRouteServersRequestPaginateTypeDef,
    DescribeRouteServersResultTypeDef,
    DescribeRouteTablesRequestPaginateTypeDef,
    DescribeRouteTablesResultTypeDef,
    DescribeScheduledInstanceAvailabilityRequestPaginateTypeDef,
    DescribeScheduledInstanceAvailabilityResultTypeDef,
    DescribeScheduledInstancesRequestPaginateTypeDef,
    DescribeScheduledInstancesResultTypeDef,
    DescribeSecurityGroupRulesRequestPaginateTypeDef,
    DescribeSecurityGroupRulesResultTypeDef,
    DescribeSecurityGroupsRequestPaginateTypeDef,
    DescribeSecurityGroupsResultTypeDef,
    DescribeSecurityGroupVpcAssociationsRequestPaginateTypeDef,
    DescribeSecurityGroupVpcAssociationsResultTypeDef,
    DescribeSnapshotsRequestPaginateTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeSnapshotTierStatusRequestPaginateTypeDef,
    DescribeSnapshotTierStatusResultTypeDef,
    DescribeSpotFleetInstancesRequestPaginateTypeDef,
    DescribeSpotFleetInstancesResponseTypeDef,
    DescribeSpotFleetRequestsRequestPaginateTypeDef,
    DescribeSpotFleetRequestsResponseTypeDef,
    DescribeSpotInstanceRequestsRequestPaginateTypeDef,
    DescribeSpotInstanceRequestsResultTypeDef,
    DescribeSpotPriceHistoryRequestPaginateTypeDef,
    DescribeSpotPriceHistoryResultTypeDef,
    DescribeStaleSecurityGroupsRequestPaginateTypeDef,
    DescribeStaleSecurityGroupsResultTypeDef,
    DescribeStoreImageTasksRequestPaginateTypeDef,
    DescribeStoreImageTasksResultTypeDef,
    DescribeSubnetsRequestPaginateTypeDef,
    DescribeSubnetsResultTypeDef,
    DescribeTagsRequestPaginateTypeDef,
    DescribeTagsResultTypeDef,
    DescribeTrafficMirrorFiltersRequestPaginateTypeDef,
    DescribeTrafficMirrorFiltersResultTypeDef,
    DescribeTrafficMirrorSessionsRequestPaginateTypeDef,
    DescribeTrafficMirrorSessionsResultTypeDef,
    DescribeTrafficMirrorTargetsRequestPaginateTypeDef,
    DescribeTrafficMirrorTargetsResultTypeDef,
    DescribeTransitGatewayAttachmentsRequestPaginateTypeDef,
    DescribeTransitGatewayAttachmentsResultTypeDef,
    DescribeTransitGatewayConnectPeersRequestPaginateTypeDef,
    DescribeTransitGatewayConnectPeersResultTypeDef,
    DescribeTransitGatewayConnectsRequestPaginateTypeDef,
    DescribeTransitGatewayConnectsResultTypeDef,
    DescribeTransitGatewayMulticastDomainsRequestPaginateTypeDef,
    DescribeTransitGatewayMulticastDomainsResultTypeDef,
    DescribeTransitGatewayPeeringAttachmentsRequestPaginateTypeDef,
    DescribeTransitGatewayPeeringAttachmentsResultTypeDef,
    DescribeTransitGatewayPolicyTablesRequestPaginateTypeDef,
    DescribeTransitGatewayPolicyTablesResultTypeDef,
    DescribeTransitGatewayRouteTableAnnouncementsRequestPaginateTypeDef,
    DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef,
    DescribeTransitGatewayRouteTablesRequestPaginateTypeDef,
    DescribeTransitGatewayRouteTablesResultTypeDef,
    DescribeTransitGatewaysRequestPaginateTypeDef,
    DescribeTransitGatewaysResultTypeDef,
    DescribeTransitGatewayVpcAttachmentsRequestPaginateTypeDef,
    DescribeTransitGatewayVpcAttachmentsResultTypeDef,
    DescribeTrunkInterfaceAssociationsRequestPaginateTypeDef,
    DescribeTrunkInterfaceAssociationsResultTypeDef,
    DescribeVerifiedAccessEndpointsRequestPaginateTypeDef,
    DescribeVerifiedAccessEndpointsResultTypeDef,
    DescribeVerifiedAccessGroupsRequestPaginateTypeDef,
    DescribeVerifiedAccessGroupsResultTypeDef,
    DescribeVerifiedAccessInstanceLoggingConfigurationsRequestPaginateTypeDef,
    DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef,
    DescribeVerifiedAccessInstancesRequestPaginateTypeDef,
    DescribeVerifiedAccessInstancesResultTypeDef,
    DescribeVerifiedAccessTrustProvidersRequestPaginateTypeDef,
    DescribeVerifiedAccessTrustProvidersResultTypeDef,
    DescribeVolumesModificationsRequestPaginateTypeDef,
    DescribeVolumesModificationsResultTypeDef,
    DescribeVolumesRequestPaginateTypeDef,
    DescribeVolumesResultTypeDef,
    DescribeVolumeStatusRequestPaginateTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcClassicLinkDnsSupportRequestPaginateTypeDef,
    DescribeVpcClassicLinkDnsSupportResultTypeDef,
    DescribeVpcEndpointConnectionNotificationsRequestPaginateTypeDef,
    DescribeVpcEndpointConnectionNotificationsResultTypeDef,
    DescribeVpcEndpointConnectionsRequestPaginateTypeDef,
    DescribeVpcEndpointConnectionsResultTypeDef,
    DescribeVpcEndpointServiceConfigurationsRequestPaginateTypeDef,
    DescribeVpcEndpointServiceConfigurationsResultTypeDef,
    DescribeVpcEndpointServicePermissionsRequestPaginateTypeDef,
    DescribeVpcEndpointServicePermissionsResultTypeDef,
    DescribeVpcEndpointServicesRequestPaginateTypeDef,
    DescribeVpcEndpointServicesResultTypeDef,
    DescribeVpcEndpointsRequestPaginateTypeDef,
    DescribeVpcEndpointsResultTypeDef,
    DescribeVpcPeeringConnectionsRequestPaginateTypeDef,
    DescribeVpcPeeringConnectionsResultTypeDef,
    DescribeVpcsRequestPaginateTypeDef,
    DescribeVpcsResultTypeDef,
    GetAssociatedIpv6PoolCidrsRequestPaginateTypeDef,
    GetAssociatedIpv6PoolCidrsResultTypeDef,
    GetAwsNetworkPerformanceDataRequestPaginateTypeDef,
    GetAwsNetworkPerformanceDataResultTypeDef,
    GetGroupsForCapacityReservationRequestPaginateTypeDef,
    GetGroupsForCapacityReservationResultTypeDef,
    GetInstanceTypesFromInstanceRequirementsRequestPaginateTypeDef,
    GetInstanceTypesFromInstanceRequirementsResultTypeDef,
    GetIpamAddressHistoryRequestPaginateTypeDef,
    GetIpamAddressHistoryResultTypeDef,
    GetIpamDiscoveredAccountsRequestPaginateTypeDef,
    GetIpamDiscoveredAccountsResultTypeDef,
    GetIpamDiscoveredResourceCidrsRequestPaginateTypeDef,
    GetIpamDiscoveredResourceCidrsResultTypeDef,
    GetIpamPoolAllocationsRequestPaginateTypeDef,
    GetIpamPoolAllocationsResultTypeDef,
    GetIpamPoolCidrsRequestPaginateTypeDef,
    GetIpamPoolCidrsResultTypeDef,
    GetIpamResourceCidrsRequestPaginateTypeDef,
    GetIpamResourceCidrsResultTypeDef,
    GetManagedPrefixListAssociationsRequestPaginateTypeDef,
    GetManagedPrefixListAssociationsResultTypeDef,
    GetManagedPrefixListEntriesRequestPaginateTypeDef,
    GetManagedPrefixListEntriesResultTypeDef,
    GetNetworkInsightsAccessScopeAnalysisFindingsRequestPaginateTypeDef,
    GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef,
    GetSecurityGroupsForVpcRequestPaginateTypeDef,
    GetSecurityGroupsForVpcResultTypeDef,
    GetSpotPlacementScoresRequestPaginateTypeDef,
    GetSpotPlacementScoresResultTypeDef,
    GetTransitGatewayAttachmentPropagationsRequestPaginateTypeDef,
    GetTransitGatewayAttachmentPropagationsResultTypeDef,
    GetTransitGatewayMulticastDomainAssociationsRequestPaginateTypeDef,
    GetTransitGatewayMulticastDomainAssociationsResultTypeDef,
    GetTransitGatewayPolicyTableAssociationsRequestPaginateTypeDef,
    GetTransitGatewayPolicyTableAssociationsResultTypeDef,
    GetTransitGatewayPrefixListReferencesRequestPaginateTypeDef,
    GetTransitGatewayPrefixListReferencesResultTypeDef,
    GetTransitGatewayRouteTableAssociationsRequestPaginateTypeDef,
    GetTransitGatewayRouteTableAssociationsResultTypeDef,
    GetTransitGatewayRouteTablePropagationsRequestPaginateTypeDef,
    GetTransitGatewayRouteTablePropagationsResultTypeDef,
    GetVpnConnectionDeviceTypesRequestPaginateTypeDef,
    GetVpnConnectionDeviceTypesResultTypeDef,
    ListImagesInRecycleBinRequestPaginateTypeDef,
    ListImagesInRecycleBinResultTypeDef,
    ListSnapshotsInRecycleBinRequestPaginateTypeDef,
    ListSnapshotsInRecycleBinResultTypeDef,
    SearchLocalGatewayRoutesRequestPaginateTypeDef,
    SearchLocalGatewayRoutesResultTypeDef,
    SearchTransitGatewayMulticastGroupsRequestPaginateTypeDef,
    SearchTransitGatewayMulticastGroupsResultTypeDef,
)

if sys.version_info >= (3, 12):
    from typing import Unpack
else:
    from typing_extensions import Unpack

__all__ = (
    "DescribeAddressTransfersPaginator",
    "DescribeAddressesAttributePaginator",
    "DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator",
    "DescribeByoipCidrsPaginator",
    "DescribeCapacityBlockExtensionHistoryPaginator",
    "DescribeCapacityBlockExtensionOfferingsPaginator",
    "DescribeCapacityBlockOfferingsPaginator",
    "DescribeCapacityReservationBillingRequestsPaginator",
    "DescribeCapacityReservationFleetsPaginator",
    "DescribeCapacityReservationsPaginator",
    "DescribeCarrierGatewaysPaginator",
    "DescribeClassicLinkInstancesPaginator",
    "DescribeClientVpnAuthorizationRulesPaginator",
    "DescribeClientVpnConnectionsPaginator",
    "DescribeClientVpnEndpointsPaginator",
    "DescribeClientVpnRoutesPaginator",
    "DescribeClientVpnTargetNetworksPaginator",
    "DescribeCoipPoolsPaginator",
    "DescribeDhcpOptionsPaginator",
    "DescribeEgressOnlyInternetGatewaysPaginator",
    "DescribeExportImageTasksPaginator",
    "DescribeFastLaunchImagesPaginator",
    "DescribeFastSnapshotRestoresPaginator",
    "DescribeFleetsPaginator",
    "DescribeFlowLogsPaginator",
    "DescribeFpgaImagesPaginator",
    "DescribeHostReservationOfferingsPaginator",
    "DescribeHostReservationsPaginator",
    "DescribeHostsPaginator",
    "DescribeIamInstanceProfileAssociationsPaginator",
    "DescribeImagesPaginator",
    "DescribeImportImageTasksPaginator",
    "DescribeImportSnapshotTasksPaginator",
    "DescribeInstanceConnectEndpointsPaginator",
    "DescribeInstanceCreditSpecificationsPaginator",
    "DescribeInstanceEventWindowsPaginator",
    "DescribeInstanceImageMetadataPaginator",
    "DescribeInstanceStatusPaginator",
    "DescribeInstanceTopologyPaginator",
    "DescribeInstanceTypeOfferingsPaginator",
    "DescribeInstanceTypesPaginator",
    "DescribeInstancesPaginator",
    "DescribeInternetGatewaysPaginator",
    "DescribeIpamPoolsPaginator",
    "DescribeIpamResourceDiscoveriesPaginator",
    "DescribeIpamResourceDiscoveryAssociationsPaginator",
    "DescribeIpamScopesPaginator",
    "DescribeIpamsPaginator",
    "DescribeIpv6PoolsPaginator",
    "DescribeLaunchTemplateVersionsPaginator",
    "DescribeLaunchTemplatesPaginator",
    "DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator",
    "DescribeLocalGatewayRouteTableVpcAssociationsPaginator",
    "DescribeLocalGatewayRouteTablesPaginator",
    "DescribeLocalGatewayVirtualInterfaceGroupsPaginator",
    "DescribeLocalGatewayVirtualInterfacesPaginator",
    "DescribeLocalGatewaysPaginator",
    "DescribeMacHostsPaginator",
    "DescribeManagedPrefixListsPaginator",
    "DescribeMovingAddressesPaginator",
    "DescribeNatGatewaysPaginator",
    "DescribeNetworkAclsPaginator",
    "DescribeNetworkInsightsAccessScopeAnalysesPaginator",
    "DescribeNetworkInsightsAccessScopesPaginator",
    "DescribeNetworkInsightsAnalysesPaginator",
    "DescribeNetworkInsightsPathsPaginator",
    "DescribeNetworkInterfacePermissionsPaginator",
    "DescribeNetworkInterfacesPaginator",
    "DescribePrefixListsPaginator",
    "DescribePrincipalIdFormatPaginator",
    "DescribePublicIpv4PoolsPaginator",
    "DescribeReplaceRootVolumeTasksPaginator",
    "DescribeReservedInstancesModificationsPaginator",
    "DescribeReservedInstancesOfferingsPaginator",
    "DescribeRouteServerEndpointsPaginator",
    "DescribeRouteServerPeersPaginator",
    "DescribeRouteServersPaginator",
    "DescribeRouteTablesPaginator",
    "DescribeScheduledInstanceAvailabilityPaginator",
    "DescribeScheduledInstancesPaginator",
    "DescribeSecurityGroupRulesPaginator",
    "DescribeSecurityGroupVpcAssociationsPaginator",
    "DescribeSecurityGroupsPaginator",
    "DescribeSnapshotTierStatusPaginator",
    "DescribeSnapshotsPaginator",
    "DescribeSpotFleetInstancesPaginator",
    "DescribeSpotFleetRequestsPaginator",
    "DescribeSpotInstanceRequestsPaginator",
    "DescribeSpotPriceHistoryPaginator",
    "DescribeStaleSecurityGroupsPaginator",
    "DescribeStoreImageTasksPaginator",
    "DescribeSubnetsPaginator",
    "DescribeTagsPaginator",
    "DescribeTrafficMirrorFiltersPaginator",
    "DescribeTrafficMirrorSessionsPaginator",
    "DescribeTrafficMirrorTargetsPaginator",
    "DescribeTransitGatewayAttachmentsPaginator",
    "DescribeTransitGatewayConnectPeersPaginator",
    "DescribeTransitGatewayConnectsPaginator",
    "DescribeTransitGatewayMulticastDomainsPaginator",
    "DescribeTransitGatewayPeeringAttachmentsPaginator",
    "DescribeTransitGatewayPolicyTablesPaginator",
    "DescribeTransitGatewayRouteTableAnnouncementsPaginator",
    "DescribeTransitGatewayRouteTablesPaginator",
    "DescribeTransitGatewayVpcAttachmentsPaginator",
    "DescribeTransitGatewaysPaginator",
    "DescribeTrunkInterfaceAssociationsPaginator",
    "DescribeVerifiedAccessEndpointsPaginator",
    "DescribeVerifiedAccessGroupsPaginator",
    "DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator",
    "DescribeVerifiedAccessInstancesPaginator",
    "DescribeVerifiedAccessTrustProvidersPaginator",
    "DescribeVolumeStatusPaginator",
    "DescribeVolumesModificationsPaginator",
    "DescribeVolumesPaginator",
    "DescribeVpcClassicLinkDnsSupportPaginator",
    "DescribeVpcEndpointConnectionNotificationsPaginator",
    "DescribeVpcEndpointConnectionsPaginator",
    "DescribeVpcEndpointServiceConfigurationsPaginator",
    "DescribeVpcEndpointServicePermissionsPaginator",
    "DescribeVpcEndpointServicesPaginator",
    "DescribeVpcEndpointsPaginator",
    "DescribeVpcPeeringConnectionsPaginator",
    "DescribeVpcsPaginator",
    "GetAssociatedIpv6PoolCidrsPaginator",
    "GetAwsNetworkPerformanceDataPaginator",
    "GetGroupsForCapacityReservationPaginator",
    "GetInstanceTypesFromInstanceRequirementsPaginator",
    "GetIpamAddressHistoryPaginator",
    "GetIpamDiscoveredAccountsPaginator",
    "GetIpamDiscoveredResourceCidrsPaginator",
    "GetIpamPoolAllocationsPaginator",
    "GetIpamPoolCidrsPaginator",
    "GetIpamResourceCidrsPaginator",
    "GetManagedPrefixListAssociationsPaginator",
    "GetManagedPrefixListEntriesPaginator",
    "GetNetworkInsightsAccessScopeAnalysisFindingsPaginator",
    "GetSecurityGroupsForVpcPaginator",
    "GetSpotPlacementScoresPaginator",
    "GetTransitGatewayAttachmentPropagationsPaginator",
    "GetTransitGatewayMulticastDomainAssociationsPaginator",
    "GetTransitGatewayPolicyTableAssociationsPaginator",
    "GetTransitGatewayPrefixListReferencesPaginator",
    "GetTransitGatewayRouteTableAssociationsPaginator",
    "GetTransitGatewayRouteTablePropagationsPaginator",
    "GetVpnConnectionDeviceTypesPaginator",
    "ListImagesInRecycleBinPaginator",
    "ListSnapshotsInRecycleBinPaginator",
    "SearchLocalGatewayRoutesPaginator",
    "SearchTransitGatewayMulticastGroupsPaginator",
)

if TYPE_CHECKING:
    _DescribeAddressTransfersPaginatorBase = Paginator[DescribeAddressTransfersResultTypeDef]
else:
    _DescribeAddressTransfersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAddressTransfersPaginator(_DescribeAddressTransfersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeAddressTransfers.html#EC2.Paginator.DescribeAddressTransfers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeaddresstransferspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAddressTransfersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAddressTransfersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeAddressTransfers.html#EC2.Paginator.DescribeAddressTransfers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeaddresstransferspaginator)
        """

if TYPE_CHECKING:
    _DescribeAddressesAttributePaginatorBase = Paginator[DescribeAddressesAttributeResultTypeDef]
else:
    _DescribeAddressesAttributePaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAddressesAttributePaginator(_DescribeAddressesAttributePaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeAddressesAttribute.html#EC2.Paginator.DescribeAddressesAttribute)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeaddressesattributepaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeAddressesAttributeRequestPaginateTypeDef]
    ) -> PageIterator[DescribeAddressesAttributeResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeAddressesAttribute.html#EC2.Paginator.DescribeAddressesAttribute.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeaddressesattributepaginator)
        """

if TYPE_CHECKING:
    _DescribeAwsNetworkPerformanceMetricSubscriptionsPaginatorBase = Paginator[
        DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef
    ]
else:
    _DescribeAwsNetworkPerformanceMetricSubscriptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator(
    _DescribeAwsNetworkPerformanceMetricSubscriptionsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeAwsNetworkPerformanceMetricSubscriptions.html#EC2.Paginator.DescribeAwsNetworkPerformanceMetricSubscriptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeawsnetworkperformancemetricsubscriptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self,
        **kwargs: Unpack[DescribeAwsNetworkPerformanceMetricSubscriptionsRequestPaginateTypeDef],
    ) -> PageIterator[DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeAwsNetworkPerformanceMetricSubscriptions.html#EC2.Paginator.DescribeAwsNetworkPerformanceMetricSubscriptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeawsnetworkperformancemetricsubscriptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeByoipCidrsPaginatorBase = Paginator[DescribeByoipCidrsResultTypeDef]
else:
    _DescribeByoipCidrsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeByoipCidrsPaginator(_DescribeByoipCidrsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeByoipCidrs.html#EC2.Paginator.DescribeByoipCidrs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describebyoipcidrspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeByoipCidrsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeByoipCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeByoipCidrs.html#EC2.Paginator.DescribeByoipCidrs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describebyoipcidrspaginator)
        """

if TYPE_CHECKING:
    _DescribeCapacityBlockExtensionHistoryPaginatorBase = Paginator[
        DescribeCapacityBlockExtensionHistoryResultTypeDef
    ]
else:
    _DescribeCapacityBlockExtensionHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCapacityBlockExtensionHistoryPaginator(
    _DescribeCapacityBlockExtensionHistoryPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityBlockExtensionHistory.html#EC2.Paginator.DescribeCapacityBlockExtensionHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityblockextensionhistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCapacityBlockExtensionHistoryRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCapacityBlockExtensionHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityBlockExtensionHistory.html#EC2.Paginator.DescribeCapacityBlockExtensionHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityblockextensionhistorypaginator)
        """

if TYPE_CHECKING:
    _DescribeCapacityBlockExtensionOfferingsPaginatorBase = Paginator[
        DescribeCapacityBlockExtensionOfferingsResultTypeDef
    ]
else:
    _DescribeCapacityBlockExtensionOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCapacityBlockExtensionOfferingsPaginator(
    _DescribeCapacityBlockExtensionOfferingsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityBlockExtensionOfferings.html#EC2.Paginator.DescribeCapacityBlockExtensionOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityblockextensionofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCapacityBlockExtensionOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCapacityBlockExtensionOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityBlockExtensionOfferings.html#EC2.Paginator.DescribeCapacityBlockExtensionOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityblockextensionofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeCapacityBlockOfferingsPaginatorBase = Paginator[
        DescribeCapacityBlockOfferingsResultTypeDef
    ]
else:
    _DescribeCapacityBlockOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCapacityBlockOfferingsPaginator(_DescribeCapacityBlockOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityBlockOfferings.html#EC2.Paginator.DescribeCapacityBlockOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityblockofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCapacityBlockOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCapacityBlockOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityBlockOfferings.html#EC2.Paginator.DescribeCapacityBlockOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityblockofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeCapacityReservationBillingRequestsPaginatorBase = Paginator[
        DescribeCapacityReservationBillingRequestsResultTypeDef
    ]
else:
    _DescribeCapacityReservationBillingRequestsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCapacityReservationBillingRequestsPaginator(
    _DescribeCapacityReservationBillingRequestsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityReservationBillingRequests.html#EC2.Paginator.DescribeCapacityReservationBillingRequests)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityreservationbillingrequestspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCapacityReservationBillingRequestsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCapacityReservationBillingRequestsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityReservationBillingRequests.html#EC2.Paginator.DescribeCapacityReservationBillingRequests.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityreservationbillingrequestspaginator)
        """

if TYPE_CHECKING:
    _DescribeCapacityReservationFleetsPaginatorBase = Paginator[
        DescribeCapacityReservationFleetsResultTypeDef
    ]
else:
    _DescribeCapacityReservationFleetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCapacityReservationFleetsPaginator(_DescribeCapacityReservationFleetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityReservationFleets.html#EC2.Paginator.DescribeCapacityReservationFleets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityreservationfleetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCapacityReservationFleetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCapacityReservationFleetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityReservationFleets.html#EC2.Paginator.DescribeCapacityReservationFleets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityreservationfleetspaginator)
        """

if TYPE_CHECKING:
    _DescribeCapacityReservationsPaginatorBase = Paginator[
        DescribeCapacityReservationsResultTypeDef
    ]
else:
    _DescribeCapacityReservationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCapacityReservationsPaginator(_DescribeCapacityReservationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityReservations.html#EC2.Paginator.DescribeCapacityReservations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityreservationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCapacityReservationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCapacityReservationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCapacityReservations.html#EC2.Paginator.DescribeCapacityReservations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecapacityreservationspaginator)
        """

if TYPE_CHECKING:
    _DescribeCarrierGatewaysPaginatorBase = Paginator[DescribeCarrierGatewaysResultTypeDef]
else:
    _DescribeCarrierGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCarrierGatewaysPaginator(_DescribeCarrierGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCarrierGateways.html#EC2.Paginator.DescribeCarrierGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecarriergatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCarrierGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCarrierGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCarrierGateways.html#EC2.Paginator.DescribeCarrierGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecarriergatewayspaginator)
        """

if TYPE_CHECKING:
    _DescribeClassicLinkInstancesPaginatorBase = Paginator[
        DescribeClassicLinkInstancesResultTypeDef
    ]
else:
    _DescribeClassicLinkInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClassicLinkInstancesPaginator(_DescribeClassicLinkInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClassicLinkInstances.html#EC2.Paginator.DescribeClassicLinkInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclassiclinkinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClassicLinkInstancesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClassicLinkInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClassicLinkInstances.html#EC2.Paginator.DescribeClassicLinkInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclassiclinkinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeClientVpnAuthorizationRulesPaginatorBase = Paginator[
        DescribeClientVpnAuthorizationRulesResultTypeDef
    ]
else:
    _DescribeClientVpnAuthorizationRulesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClientVpnAuthorizationRulesPaginator(
    _DescribeClientVpnAuthorizationRulesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnAuthorizationRules.html#EC2.Paginator.DescribeClientVpnAuthorizationRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpnauthorizationrulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClientVpnAuthorizationRulesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClientVpnAuthorizationRulesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnAuthorizationRules.html#EC2.Paginator.DescribeClientVpnAuthorizationRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpnauthorizationrulespaginator)
        """

if TYPE_CHECKING:
    _DescribeClientVpnConnectionsPaginatorBase = Paginator[
        DescribeClientVpnConnectionsResultTypeDef
    ]
else:
    _DescribeClientVpnConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClientVpnConnectionsPaginator(_DescribeClientVpnConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnConnections.html#EC2.Paginator.DescribeClientVpnConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpnconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClientVpnConnectionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClientVpnConnectionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnConnections.html#EC2.Paginator.DescribeClientVpnConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpnconnectionspaginator)
        """

if TYPE_CHECKING:
    _DescribeClientVpnEndpointsPaginatorBase = Paginator[DescribeClientVpnEndpointsResultTypeDef]
else:
    _DescribeClientVpnEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClientVpnEndpointsPaginator(_DescribeClientVpnEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnEndpoints.html#EC2.Paginator.DescribeClientVpnEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpnendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClientVpnEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClientVpnEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnEndpoints.html#EC2.Paginator.DescribeClientVpnEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpnendpointspaginator)
        """

if TYPE_CHECKING:
    _DescribeClientVpnRoutesPaginatorBase = Paginator[DescribeClientVpnRoutesResultTypeDef]
else:
    _DescribeClientVpnRoutesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClientVpnRoutesPaginator(_DescribeClientVpnRoutesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnRoutes.html#EC2.Paginator.DescribeClientVpnRoutes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpnroutespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClientVpnRoutesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClientVpnRoutesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnRoutes.html#EC2.Paginator.DescribeClientVpnRoutes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpnroutespaginator)
        """

if TYPE_CHECKING:
    _DescribeClientVpnTargetNetworksPaginatorBase = Paginator[
        DescribeClientVpnTargetNetworksResultTypeDef
    ]
else:
    _DescribeClientVpnTargetNetworksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeClientVpnTargetNetworksPaginator(_DescribeClientVpnTargetNetworksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnTargetNetworks.html#EC2.Paginator.DescribeClientVpnTargetNetworks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpntargetnetworkspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeClientVpnTargetNetworksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeClientVpnTargetNetworksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeClientVpnTargetNetworks.html#EC2.Paginator.DescribeClientVpnTargetNetworks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeclientvpntargetnetworkspaginator)
        """

if TYPE_CHECKING:
    _DescribeCoipPoolsPaginatorBase = Paginator[DescribeCoipPoolsResultTypeDef]
else:
    _DescribeCoipPoolsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeCoipPoolsPaginator(_DescribeCoipPoolsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCoipPools.html#EC2.Paginator.DescribeCoipPools)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecoippoolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeCoipPoolsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeCoipPoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeCoipPools.html#EC2.Paginator.DescribeCoipPools.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describecoippoolspaginator)
        """

if TYPE_CHECKING:
    _DescribeDhcpOptionsPaginatorBase = Paginator[DescribeDhcpOptionsResultTypeDef]
else:
    _DescribeDhcpOptionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeDhcpOptionsPaginator(_DescribeDhcpOptionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeDhcpOptions.html#EC2.Paginator.DescribeDhcpOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describedhcpoptionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeDhcpOptionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeDhcpOptionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeDhcpOptions.html#EC2.Paginator.DescribeDhcpOptions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describedhcpoptionspaginator)
        """

if TYPE_CHECKING:
    _DescribeEgressOnlyInternetGatewaysPaginatorBase = Paginator[
        DescribeEgressOnlyInternetGatewaysResultTypeDef
    ]
else:
    _DescribeEgressOnlyInternetGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeEgressOnlyInternetGatewaysPaginator(_DescribeEgressOnlyInternetGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeEgressOnlyInternetGateways.html#EC2.Paginator.DescribeEgressOnlyInternetGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeegressonlyinternetgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeEgressOnlyInternetGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[DescribeEgressOnlyInternetGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeEgressOnlyInternetGateways.html#EC2.Paginator.DescribeEgressOnlyInternetGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeegressonlyinternetgatewayspaginator)
        """

if TYPE_CHECKING:
    _DescribeExportImageTasksPaginatorBase = Paginator[DescribeExportImageTasksResultTypeDef]
else:
    _DescribeExportImageTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeExportImageTasksPaginator(_DescribeExportImageTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeExportImageTasks.html#EC2.Paginator.DescribeExportImageTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeexportimagetaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeExportImageTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeExportImageTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeExportImageTasks.html#EC2.Paginator.DescribeExportImageTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeexportimagetaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeFastLaunchImagesPaginatorBase = Paginator[DescribeFastLaunchImagesResultTypeDef]
else:
    _DescribeFastLaunchImagesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeFastLaunchImagesPaginator(_DescribeFastLaunchImagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFastLaunchImages.html#EC2.Paginator.DescribeFastLaunchImages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describefastlaunchimagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFastLaunchImagesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeFastLaunchImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFastLaunchImages.html#EC2.Paginator.DescribeFastLaunchImages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describefastlaunchimagespaginator)
        """

if TYPE_CHECKING:
    _DescribeFastSnapshotRestoresPaginatorBase = Paginator[
        DescribeFastSnapshotRestoresResultTypeDef
    ]
else:
    _DescribeFastSnapshotRestoresPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeFastSnapshotRestoresPaginator(_DescribeFastSnapshotRestoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFastSnapshotRestores.html#EC2.Paginator.DescribeFastSnapshotRestores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describefastsnapshotrestorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFastSnapshotRestoresRequestPaginateTypeDef]
    ) -> PageIterator[DescribeFastSnapshotRestoresResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFastSnapshotRestores.html#EC2.Paginator.DescribeFastSnapshotRestores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describefastsnapshotrestorespaginator)
        """

if TYPE_CHECKING:
    _DescribeFleetsPaginatorBase = Paginator[DescribeFleetsResultTypeDef]
else:
    _DescribeFleetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeFleetsPaginator(_DescribeFleetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFleets.html#EC2.Paginator.DescribeFleets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describefleetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFleetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeFleetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFleets.html#EC2.Paginator.DescribeFleets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describefleetspaginator)
        """

if TYPE_CHECKING:
    _DescribeFlowLogsPaginatorBase = Paginator[DescribeFlowLogsResultTypeDef]
else:
    _DescribeFlowLogsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeFlowLogsPaginator(_DescribeFlowLogsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFlowLogs.html#EC2.Paginator.DescribeFlowLogs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeflowlogspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFlowLogsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeFlowLogsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFlowLogs.html#EC2.Paginator.DescribeFlowLogs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeflowlogspaginator)
        """

if TYPE_CHECKING:
    _DescribeFpgaImagesPaginatorBase = Paginator[DescribeFpgaImagesResultTypeDef]
else:
    _DescribeFpgaImagesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeFpgaImagesPaginator(_DescribeFpgaImagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFpgaImages.html#EC2.Paginator.DescribeFpgaImages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describefpgaimagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeFpgaImagesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeFpgaImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeFpgaImages.html#EC2.Paginator.DescribeFpgaImages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describefpgaimagespaginator)
        """

if TYPE_CHECKING:
    _DescribeHostReservationOfferingsPaginatorBase = Paginator[
        DescribeHostReservationOfferingsResultTypeDef
    ]
else:
    _DescribeHostReservationOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeHostReservationOfferingsPaginator(_DescribeHostReservationOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeHostReservationOfferings.html#EC2.Paginator.DescribeHostReservationOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describehostreservationofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeHostReservationOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeHostReservationOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeHostReservationOfferings.html#EC2.Paginator.DescribeHostReservationOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describehostreservationofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeHostReservationsPaginatorBase = Paginator[DescribeHostReservationsResultTypeDef]
else:
    _DescribeHostReservationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeHostReservationsPaginator(_DescribeHostReservationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeHostReservations.html#EC2.Paginator.DescribeHostReservations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describehostreservationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeHostReservationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeHostReservationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeHostReservations.html#EC2.Paginator.DescribeHostReservations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describehostreservationspaginator)
        """

if TYPE_CHECKING:
    _DescribeHostsPaginatorBase = Paginator[DescribeHostsResultTypeDef]
else:
    _DescribeHostsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeHostsPaginator(_DescribeHostsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeHosts.html#EC2.Paginator.DescribeHosts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describehostspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeHostsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeHostsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeHosts.html#EC2.Paginator.DescribeHosts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describehostspaginator)
        """

if TYPE_CHECKING:
    _DescribeIamInstanceProfileAssociationsPaginatorBase = Paginator[
        DescribeIamInstanceProfileAssociationsResultTypeDef
    ]
else:
    _DescribeIamInstanceProfileAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIamInstanceProfileAssociationsPaginator(
    _DescribeIamInstanceProfileAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIamInstanceProfileAssociations.html#EC2.Paginator.DescribeIamInstanceProfileAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeiaminstanceprofileassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIamInstanceProfileAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeIamInstanceProfileAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIamInstanceProfileAssociations.html#EC2.Paginator.DescribeIamInstanceProfileAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeiaminstanceprofileassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeImagesPaginatorBase = Paginator[DescribeImagesResultTypeDef]
else:
    _DescribeImagesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeImagesPaginator(_DescribeImagesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeImages.html#EC2.Paginator.DescribeImages)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeimagespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImagesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeImages.html#EC2.Paginator.DescribeImages.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeimagespaginator)
        """

if TYPE_CHECKING:
    _DescribeImportImageTasksPaginatorBase = Paginator[DescribeImportImageTasksResultTypeDef]
else:
    _DescribeImportImageTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeImportImageTasksPaginator(_DescribeImportImageTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeImportImageTasks.html#EC2.Paginator.DescribeImportImageTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeimportimagetaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImportImageTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeImportImageTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeImportImageTasks.html#EC2.Paginator.DescribeImportImageTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeimportimagetaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeImportSnapshotTasksPaginatorBase = Paginator[DescribeImportSnapshotTasksResultTypeDef]
else:
    _DescribeImportSnapshotTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeImportSnapshotTasksPaginator(_DescribeImportSnapshotTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeImportSnapshotTasks.html#EC2.Paginator.DescribeImportSnapshotTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeimportsnapshottaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeImportSnapshotTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeImportSnapshotTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeImportSnapshotTasks.html#EC2.Paginator.DescribeImportSnapshotTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeimportsnapshottaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceConnectEndpointsPaginatorBase = Paginator[
        DescribeInstanceConnectEndpointsResultTypeDef
    ]
else:
    _DescribeInstanceConnectEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceConnectEndpointsPaginator(_DescribeInstanceConnectEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceConnectEndpoints.html#EC2.Paginator.DescribeInstanceConnectEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstanceconnectendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceConnectEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceConnectEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceConnectEndpoints.html#EC2.Paginator.DescribeInstanceConnectEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstanceconnectendpointspaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceCreditSpecificationsPaginatorBase = Paginator[
        DescribeInstanceCreditSpecificationsResultTypeDef
    ]
else:
    _DescribeInstanceCreditSpecificationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceCreditSpecificationsPaginator(
    _DescribeInstanceCreditSpecificationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceCreditSpecifications.html#EC2.Paginator.DescribeInstanceCreditSpecifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancecreditspecificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceCreditSpecificationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceCreditSpecificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceCreditSpecifications.html#EC2.Paginator.DescribeInstanceCreditSpecifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancecreditspecificationspaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceEventWindowsPaginatorBase = Paginator[
        DescribeInstanceEventWindowsResultTypeDef
    ]
else:
    _DescribeInstanceEventWindowsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceEventWindowsPaginator(_DescribeInstanceEventWindowsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceEventWindows.html#EC2.Paginator.DescribeInstanceEventWindows)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstanceeventwindowspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceEventWindowsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceEventWindowsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceEventWindows.html#EC2.Paginator.DescribeInstanceEventWindows.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstanceeventwindowspaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceImageMetadataPaginatorBase = Paginator[
        DescribeInstanceImageMetadataResultTypeDef
    ]
else:
    _DescribeInstanceImageMetadataPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceImageMetadataPaginator(_DescribeInstanceImageMetadataPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceImageMetadata.html#EC2.Paginator.DescribeInstanceImageMetadata)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstanceimagemetadatapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceImageMetadataRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceImageMetadataResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceImageMetadata.html#EC2.Paginator.DescribeInstanceImageMetadata.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstanceimagemetadatapaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceStatusPaginatorBase = Paginator[DescribeInstanceStatusResultTypeDef]
else:
    _DescribeInstanceStatusPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceStatusPaginator(_DescribeInstanceStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceStatus.html#EC2.Paginator.DescribeInstanceStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancestatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceStatusRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceStatus.html#EC2.Paginator.DescribeInstanceStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancestatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceTopologyPaginatorBase = Paginator[DescribeInstanceTopologyResultTypeDef]
else:
    _DescribeInstanceTopologyPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceTopologyPaginator(_DescribeInstanceTopologyPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceTopology.html#EC2.Paginator.DescribeInstanceTopology)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancetopologypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceTopologyRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceTopologyResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceTopology.html#EC2.Paginator.DescribeInstanceTopology.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancetopologypaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceTypeOfferingsPaginatorBase = Paginator[
        DescribeInstanceTypeOfferingsResultTypeDef
    ]
else:
    _DescribeInstanceTypeOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceTypeOfferingsPaginator(_DescribeInstanceTypeOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceTypeOfferings.html#EC2.Paginator.DescribeInstanceTypeOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancetypeofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceTypeOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceTypeOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceTypeOfferings.html#EC2.Paginator.DescribeInstanceTypeOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancetypeofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeInstanceTypesPaginatorBase = Paginator[DescribeInstanceTypesResultTypeDef]
else:
    _DescribeInstanceTypesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstanceTypesPaginator(_DescribeInstanceTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceTypes.html#EC2.Paginator.DescribeInstanceTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancetypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstanceTypesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstanceTypesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstanceTypes.html#EC2.Paginator.DescribeInstanceTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancetypespaginator)
        """

if TYPE_CHECKING:
    _DescribeInstancesPaginatorBase = Paginator[DescribeInstancesResultTypeDef]
else:
    _DescribeInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInstancesPaginator(_DescribeInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstances.html#EC2.Paginator.DescribeInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInstancesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInstances.html#EC2.Paginator.DescribeInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeInternetGatewaysPaginatorBase = Paginator[DescribeInternetGatewaysResultTypeDef]
else:
    _DescribeInternetGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeInternetGatewaysPaginator(_DescribeInternetGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInternetGateways.html#EC2.Paginator.DescribeInternetGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinternetgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeInternetGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[DescribeInternetGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeInternetGateways.html#EC2.Paginator.DescribeInternetGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeinternetgatewayspaginator)
        """

if TYPE_CHECKING:
    _DescribeIpamPoolsPaginatorBase = Paginator[DescribeIpamPoolsResultTypeDef]
else:
    _DescribeIpamPoolsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIpamPoolsPaginator(_DescribeIpamPoolsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpamPools.html#EC2.Paginator.DescribeIpamPools)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipampoolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIpamPoolsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeIpamPoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpamPools.html#EC2.Paginator.DescribeIpamPools.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipampoolspaginator)
        """

if TYPE_CHECKING:
    _DescribeIpamResourceDiscoveriesPaginatorBase = Paginator[
        DescribeIpamResourceDiscoveriesResultTypeDef
    ]
else:
    _DescribeIpamResourceDiscoveriesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIpamResourceDiscoveriesPaginator(_DescribeIpamResourceDiscoveriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpamResourceDiscoveries.html#EC2.Paginator.DescribeIpamResourceDiscoveries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipamresourcediscoveriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIpamResourceDiscoveriesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeIpamResourceDiscoveriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpamResourceDiscoveries.html#EC2.Paginator.DescribeIpamResourceDiscoveries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipamresourcediscoveriespaginator)
        """

if TYPE_CHECKING:
    _DescribeIpamResourceDiscoveryAssociationsPaginatorBase = Paginator[
        DescribeIpamResourceDiscoveryAssociationsResultTypeDef
    ]
else:
    _DescribeIpamResourceDiscoveryAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIpamResourceDiscoveryAssociationsPaginator(
    _DescribeIpamResourceDiscoveryAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpamResourceDiscoveryAssociations.html#EC2.Paginator.DescribeIpamResourceDiscoveryAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipamresourcediscoveryassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIpamResourceDiscoveryAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeIpamResourceDiscoveryAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpamResourceDiscoveryAssociations.html#EC2.Paginator.DescribeIpamResourceDiscoveryAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipamresourcediscoveryassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeIpamScopesPaginatorBase = Paginator[DescribeIpamScopesResultTypeDef]
else:
    _DescribeIpamScopesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIpamScopesPaginator(_DescribeIpamScopesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpamScopes.html#EC2.Paginator.DescribeIpamScopes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipamscopespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIpamScopesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeIpamScopesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpamScopes.html#EC2.Paginator.DescribeIpamScopes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipamscopespaginator)
        """

if TYPE_CHECKING:
    _DescribeIpamsPaginatorBase = Paginator[DescribeIpamsResultTypeDef]
else:
    _DescribeIpamsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIpamsPaginator(_DescribeIpamsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpams.html#EC2.Paginator.DescribeIpams)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipamspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIpamsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeIpamsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpams.html#EC2.Paginator.DescribeIpams.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipamspaginator)
        """

if TYPE_CHECKING:
    _DescribeIpv6PoolsPaginatorBase = Paginator[DescribeIpv6PoolsResultTypeDef]
else:
    _DescribeIpv6PoolsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeIpv6PoolsPaginator(_DescribeIpv6PoolsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpv6Pools.html#EC2.Paginator.DescribeIpv6Pools)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipv6poolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeIpv6PoolsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeIpv6PoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeIpv6Pools.html#EC2.Paginator.DescribeIpv6Pools.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeipv6poolspaginator)
        """

if TYPE_CHECKING:
    _DescribeLaunchTemplateVersionsPaginatorBase = Paginator[
        DescribeLaunchTemplateVersionsResultTypeDef
    ]
else:
    _DescribeLaunchTemplateVersionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLaunchTemplateVersionsPaginator(_DescribeLaunchTemplateVersionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLaunchTemplateVersions.html#EC2.Paginator.DescribeLaunchTemplateVersions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelaunchtemplateversionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLaunchTemplateVersionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLaunchTemplateVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLaunchTemplateVersions.html#EC2.Paginator.DescribeLaunchTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelaunchtemplateversionspaginator)
        """

if TYPE_CHECKING:
    _DescribeLaunchTemplatesPaginatorBase = Paginator[DescribeLaunchTemplatesResultTypeDef]
else:
    _DescribeLaunchTemplatesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLaunchTemplatesPaginator(_DescribeLaunchTemplatesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLaunchTemplates.html#EC2.Paginator.DescribeLaunchTemplates)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelaunchtemplatespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLaunchTemplatesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLaunchTemplatesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLaunchTemplates.html#EC2.Paginator.DescribeLaunchTemplates.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelaunchtemplatespaginator)
        """

if TYPE_CHECKING:
    _DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginatorBase = Paginator[
        DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef
    ]
else:
    _DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator(
    _DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations.html#EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayroutetablevirtualinterfacegroupassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self,
        **kwargs: Unpack[
            DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestPaginateTypeDef
        ],
    ) -> PageIterator[DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations.html#EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayroutetablevirtualinterfacegroupassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeLocalGatewayRouteTableVpcAssociationsPaginatorBase = Paginator[
        DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef
    ]
else:
    _DescribeLocalGatewayRouteTableVpcAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLocalGatewayRouteTableVpcAssociationsPaginator(
    _DescribeLocalGatewayRouteTableVpcAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayRouteTableVpcAssociations.html#EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayroutetablevpcassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLocalGatewayRouteTableVpcAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayRouteTableVpcAssociations.html#EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayroutetablevpcassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeLocalGatewayRouteTablesPaginatorBase = Paginator[
        DescribeLocalGatewayRouteTablesResultTypeDef
    ]
else:
    _DescribeLocalGatewayRouteTablesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLocalGatewayRouteTablesPaginator(_DescribeLocalGatewayRouteTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayRouteTables.html#EC2.Paginator.DescribeLocalGatewayRouteTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayroutetablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLocalGatewayRouteTablesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLocalGatewayRouteTablesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayRouteTables.html#EC2.Paginator.DescribeLocalGatewayRouteTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayroutetablespaginator)
        """

if TYPE_CHECKING:
    _DescribeLocalGatewayVirtualInterfaceGroupsPaginatorBase = Paginator[
        DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef
    ]
else:
    _DescribeLocalGatewayVirtualInterfaceGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLocalGatewayVirtualInterfaceGroupsPaginator(
    _DescribeLocalGatewayVirtualInterfaceGroupsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayVirtualInterfaceGroups.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayvirtualinterfacegroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLocalGatewayVirtualInterfaceGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayVirtualInterfaceGroups.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayvirtualinterfacegroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeLocalGatewayVirtualInterfacesPaginatorBase = Paginator[
        DescribeLocalGatewayVirtualInterfacesResultTypeDef
    ]
else:
    _DescribeLocalGatewayVirtualInterfacesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLocalGatewayVirtualInterfacesPaginator(
    _DescribeLocalGatewayVirtualInterfacesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayVirtualInterfaces.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayvirtualinterfacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLocalGatewayVirtualInterfacesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLocalGatewayVirtualInterfacesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGatewayVirtualInterfaces.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayvirtualinterfacespaginator)
        """

if TYPE_CHECKING:
    _DescribeLocalGatewaysPaginatorBase = Paginator[DescribeLocalGatewaysResultTypeDef]
else:
    _DescribeLocalGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeLocalGatewaysPaginator(_DescribeLocalGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGateways.html#EC2.Paginator.DescribeLocalGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeLocalGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[DescribeLocalGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeLocalGateways.html#EC2.Paginator.DescribeLocalGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describelocalgatewayspaginator)
        """

if TYPE_CHECKING:
    _DescribeMacHostsPaginatorBase = Paginator[DescribeMacHostsResultTypeDef]
else:
    _DescribeMacHostsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMacHostsPaginator(_DescribeMacHostsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeMacHosts.html#EC2.Paginator.DescribeMacHosts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describemachostspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMacHostsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMacHostsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeMacHosts.html#EC2.Paginator.DescribeMacHosts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describemachostspaginator)
        """

if TYPE_CHECKING:
    _DescribeManagedPrefixListsPaginatorBase = Paginator[DescribeManagedPrefixListsResultTypeDef]
else:
    _DescribeManagedPrefixListsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeManagedPrefixListsPaginator(_DescribeManagedPrefixListsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeManagedPrefixLists.html#EC2.Paginator.DescribeManagedPrefixLists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describemanagedprefixlistspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeManagedPrefixListsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeManagedPrefixListsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeManagedPrefixLists.html#EC2.Paginator.DescribeManagedPrefixLists.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describemanagedprefixlistspaginator)
        """

if TYPE_CHECKING:
    _DescribeMovingAddressesPaginatorBase = Paginator[DescribeMovingAddressesResultTypeDef]
else:
    _DescribeMovingAddressesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeMovingAddressesPaginator(_DescribeMovingAddressesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeMovingAddresses.html#EC2.Paginator.DescribeMovingAddresses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describemovingaddressespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeMovingAddressesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeMovingAddressesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeMovingAddresses.html#EC2.Paginator.DescribeMovingAddresses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describemovingaddressespaginator)
        """

if TYPE_CHECKING:
    _DescribeNatGatewaysPaginatorBase = Paginator[DescribeNatGatewaysResultTypeDef]
else:
    _DescribeNatGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNatGatewaysPaginator(_DescribeNatGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNatGateways.html#EC2.Paginator.DescribeNatGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenatgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNatGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNatGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNatGateways.html#EC2.Paginator.DescribeNatGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenatgatewayspaginator)
        """

if TYPE_CHECKING:
    _DescribeNetworkAclsPaginatorBase = Paginator[DescribeNetworkAclsResultTypeDef]
else:
    _DescribeNetworkAclsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNetworkAclsPaginator(_DescribeNetworkAclsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkAcls.html#EC2.Paginator.DescribeNetworkAcls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkaclspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNetworkAclsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNetworkAclsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkAcls.html#EC2.Paginator.DescribeNetworkAcls.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkaclspaginator)
        """

if TYPE_CHECKING:
    _DescribeNetworkInsightsAccessScopeAnalysesPaginatorBase = Paginator[
        DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef
    ]
else:
    _DescribeNetworkInsightsAccessScopeAnalysesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNetworkInsightsAccessScopeAnalysesPaginator(
    _DescribeNetworkInsightsAccessScopeAnalysesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInsightsAccessScopeAnalyses.html#EC2.Paginator.DescribeNetworkInsightsAccessScopeAnalyses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinsightsaccessscopeanalysespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNetworkInsightsAccessScopeAnalysesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInsightsAccessScopeAnalyses.html#EC2.Paginator.DescribeNetworkInsightsAccessScopeAnalyses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinsightsaccessscopeanalysespaginator)
        """

if TYPE_CHECKING:
    _DescribeNetworkInsightsAccessScopesPaginatorBase = Paginator[
        DescribeNetworkInsightsAccessScopesResultTypeDef
    ]
else:
    _DescribeNetworkInsightsAccessScopesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNetworkInsightsAccessScopesPaginator(
    _DescribeNetworkInsightsAccessScopesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInsightsAccessScopes.html#EC2.Paginator.DescribeNetworkInsightsAccessScopes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinsightsaccessscopespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNetworkInsightsAccessScopesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNetworkInsightsAccessScopesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInsightsAccessScopes.html#EC2.Paginator.DescribeNetworkInsightsAccessScopes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinsightsaccessscopespaginator)
        """

if TYPE_CHECKING:
    _DescribeNetworkInsightsAnalysesPaginatorBase = Paginator[
        DescribeNetworkInsightsAnalysesResultTypeDef
    ]
else:
    _DescribeNetworkInsightsAnalysesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNetworkInsightsAnalysesPaginator(_DescribeNetworkInsightsAnalysesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInsightsAnalyses.html#EC2.Paginator.DescribeNetworkInsightsAnalyses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinsightsanalysespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNetworkInsightsAnalysesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNetworkInsightsAnalysesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInsightsAnalyses.html#EC2.Paginator.DescribeNetworkInsightsAnalyses.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinsightsanalysespaginator)
        """

if TYPE_CHECKING:
    _DescribeNetworkInsightsPathsPaginatorBase = Paginator[
        DescribeNetworkInsightsPathsResultTypeDef
    ]
else:
    _DescribeNetworkInsightsPathsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNetworkInsightsPathsPaginator(_DescribeNetworkInsightsPathsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInsightsPaths.html#EC2.Paginator.DescribeNetworkInsightsPaths)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinsightspathspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNetworkInsightsPathsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNetworkInsightsPathsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInsightsPaths.html#EC2.Paginator.DescribeNetworkInsightsPaths.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinsightspathspaginator)
        """

if TYPE_CHECKING:
    _DescribeNetworkInterfacePermissionsPaginatorBase = Paginator[
        DescribeNetworkInterfacePermissionsResultTypeDef
    ]
else:
    _DescribeNetworkInterfacePermissionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNetworkInterfacePermissionsPaginator(
    _DescribeNetworkInterfacePermissionsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInterfacePermissions.html#EC2.Paginator.DescribeNetworkInterfacePermissions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinterfacepermissionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNetworkInterfacePermissionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNetworkInterfacePermissionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInterfacePermissions.html#EC2.Paginator.DescribeNetworkInterfacePermissions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinterfacepermissionspaginator)
        """

if TYPE_CHECKING:
    _DescribeNetworkInterfacesPaginatorBase = Paginator[DescribeNetworkInterfacesResultTypeDef]
else:
    _DescribeNetworkInterfacesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeNetworkInterfacesPaginator(_DescribeNetworkInterfacesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInterfaces.html#EC2.Paginator.DescribeNetworkInterfaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinterfacespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeNetworkInterfacesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeNetworkInterfacesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeNetworkInterfaces.html#EC2.Paginator.DescribeNetworkInterfaces.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describenetworkinterfacespaginator)
        """

if TYPE_CHECKING:
    _DescribePrefixListsPaginatorBase = Paginator[DescribePrefixListsResultTypeDef]
else:
    _DescribePrefixListsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePrefixListsPaginator(_DescribePrefixListsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribePrefixLists.html#EC2.Paginator.DescribePrefixLists)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeprefixlistspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePrefixListsRequestPaginateTypeDef]
    ) -> PageIterator[DescribePrefixListsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribePrefixLists.html#EC2.Paginator.DescribePrefixLists.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeprefixlistspaginator)
        """

if TYPE_CHECKING:
    _DescribePrincipalIdFormatPaginatorBase = Paginator[DescribePrincipalIdFormatResultTypeDef]
else:
    _DescribePrincipalIdFormatPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePrincipalIdFormatPaginator(_DescribePrincipalIdFormatPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribePrincipalIdFormat.html#EC2.Paginator.DescribePrincipalIdFormat)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeprincipalidformatpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePrincipalIdFormatRequestPaginateTypeDef]
    ) -> PageIterator[DescribePrincipalIdFormatResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribePrincipalIdFormat.html#EC2.Paginator.DescribePrincipalIdFormat.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeprincipalidformatpaginator)
        """

if TYPE_CHECKING:
    _DescribePublicIpv4PoolsPaginatorBase = Paginator[DescribePublicIpv4PoolsResultTypeDef]
else:
    _DescribePublicIpv4PoolsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribePublicIpv4PoolsPaginator(_DescribePublicIpv4PoolsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribePublicIpv4Pools.html#EC2.Paginator.DescribePublicIpv4Pools)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describepublicipv4poolspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribePublicIpv4PoolsRequestPaginateTypeDef]
    ) -> PageIterator[DescribePublicIpv4PoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribePublicIpv4Pools.html#EC2.Paginator.DescribePublicIpv4Pools.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describepublicipv4poolspaginator)
        """

if TYPE_CHECKING:
    _DescribeReplaceRootVolumeTasksPaginatorBase = Paginator[
        DescribeReplaceRootVolumeTasksResultTypeDef
    ]
else:
    _DescribeReplaceRootVolumeTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReplaceRootVolumeTasksPaginator(_DescribeReplaceRootVolumeTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeReplaceRootVolumeTasks.html#EC2.Paginator.DescribeReplaceRootVolumeTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describereplacerootvolumetaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReplaceRootVolumeTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeReplaceRootVolumeTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeReplaceRootVolumeTasks.html#EC2.Paginator.DescribeReplaceRootVolumeTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describereplacerootvolumetaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedInstancesModificationsPaginatorBase = Paginator[
        DescribeReservedInstancesModificationsResultTypeDef
    ]
else:
    _DescribeReservedInstancesModificationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedInstancesModificationsPaginator(
    _DescribeReservedInstancesModificationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeReservedInstancesModifications.html#EC2.Paginator.DescribeReservedInstancesModifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describereservedinstancesmodificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedInstancesModificationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeReservedInstancesModificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeReservedInstancesModifications.html#EC2.Paginator.DescribeReservedInstancesModifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describereservedinstancesmodificationspaginator)
        """

if TYPE_CHECKING:
    _DescribeReservedInstancesOfferingsPaginatorBase = Paginator[
        DescribeReservedInstancesOfferingsResultTypeDef
    ]
else:
    _DescribeReservedInstancesOfferingsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeReservedInstancesOfferingsPaginator(_DescribeReservedInstancesOfferingsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeReservedInstancesOfferings.html#EC2.Paginator.DescribeReservedInstancesOfferings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describereservedinstancesofferingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeReservedInstancesOfferingsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeReservedInstancesOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeReservedInstancesOfferings.html#EC2.Paginator.DescribeReservedInstancesOfferings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describereservedinstancesofferingspaginator)
        """

if TYPE_CHECKING:
    _DescribeRouteServerEndpointsPaginatorBase = Paginator[
        DescribeRouteServerEndpointsResultTypeDef
    ]
else:
    _DescribeRouteServerEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRouteServerEndpointsPaginator(_DescribeRouteServerEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeRouteServerEndpoints.html#EC2.Paginator.DescribeRouteServerEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describerouteserverendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRouteServerEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRouteServerEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeRouteServerEndpoints.html#EC2.Paginator.DescribeRouteServerEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describerouteserverendpointspaginator)
        """

if TYPE_CHECKING:
    _DescribeRouteServerPeersPaginatorBase = Paginator[DescribeRouteServerPeersResultTypeDef]
else:
    _DescribeRouteServerPeersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRouteServerPeersPaginator(_DescribeRouteServerPeersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeRouteServerPeers.html#EC2.Paginator.DescribeRouteServerPeers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describerouteserverpeerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRouteServerPeersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRouteServerPeersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeRouteServerPeers.html#EC2.Paginator.DescribeRouteServerPeers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describerouteserverpeerspaginator)
        """

if TYPE_CHECKING:
    _DescribeRouteServersPaginatorBase = Paginator[DescribeRouteServersResultTypeDef]
else:
    _DescribeRouteServersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRouteServersPaginator(_DescribeRouteServersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeRouteServers.html#EC2.Paginator.DescribeRouteServers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describerouteserverspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRouteServersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRouteServersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeRouteServers.html#EC2.Paginator.DescribeRouteServers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describerouteserverspaginator)
        """

if TYPE_CHECKING:
    _DescribeRouteTablesPaginatorBase = Paginator[DescribeRouteTablesResultTypeDef]
else:
    _DescribeRouteTablesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeRouteTablesPaginator(_DescribeRouteTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeRouteTables.html#EC2.Paginator.DescribeRouteTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeroutetablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeRouteTablesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeRouteTablesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeRouteTables.html#EC2.Paginator.DescribeRouteTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeroutetablespaginator)
        """

if TYPE_CHECKING:
    _DescribeScheduledInstanceAvailabilityPaginatorBase = Paginator[
        DescribeScheduledInstanceAvailabilityResultTypeDef
    ]
else:
    _DescribeScheduledInstanceAvailabilityPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeScheduledInstanceAvailabilityPaginator(
    _DescribeScheduledInstanceAvailabilityPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeScheduledInstanceAvailability.html#EC2.Paginator.DescribeScheduledInstanceAvailability)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describescheduledinstanceavailabilitypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScheduledInstanceAvailabilityRequestPaginateTypeDef]
    ) -> PageIterator[DescribeScheduledInstanceAvailabilityResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeScheduledInstanceAvailability.html#EC2.Paginator.DescribeScheduledInstanceAvailability.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describescheduledinstanceavailabilitypaginator)
        """

if TYPE_CHECKING:
    _DescribeScheduledInstancesPaginatorBase = Paginator[DescribeScheduledInstancesResultTypeDef]
else:
    _DescribeScheduledInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeScheduledInstancesPaginator(_DescribeScheduledInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeScheduledInstances.html#EC2.Paginator.DescribeScheduledInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describescheduledinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeScheduledInstancesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeScheduledInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeScheduledInstances.html#EC2.Paginator.DescribeScheduledInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describescheduledinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeSecurityGroupRulesPaginatorBase = Paginator[DescribeSecurityGroupRulesResultTypeDef]
else:
    _DescribeSecurityGroupRulesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSecurityGroupRulesPaginator(_DescribeSecurityGroupRulesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSecurityGroupRules.html#EC2.Paginator.DescribeSecurityGroupRules)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesecuritygrouprulespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSecurityGroupRulesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSecurityGroupRulesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSecurityGroupRules.html#EC2.Paginator.DescribeSecurityGroupRules.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesecuritygrouprulespaginator)
        """

if TYPE_CHECKING:
    _DescribeSecurityGroupVpcAssociationsPaginatorBase = Paginator[
        DescribeSecurityGroupVpcAssociationsResultTypeDef
    ]
else:
    _DescribeSecurityGroupVpcAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSecurityGroupVpcAssociationsPaginator(
    _DescribeSecurityGroupVpcAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSecurityGroupVpcAssociations.html#EC2.Paginator.DescribeSecurityGroupVpcAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesecuritygroupvpcassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSecurityGroupVpcAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSecurityGroupVpcAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSecurityGroupVpcAssociations.html#EC2.Paginator.DescribeSecurityGroupVpcAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesecuritygroupvpcassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeSecurityGroupsPaginatorBase = Paginator[DescribeSecurityGroupsResultTypeDef]
else:
    _DescribeSecurityGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSecurityGroupsPaginator(_DescribeSecurityGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSecurityGroups.html#EC2.Paginator.DescribeSecurityGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesecuritygroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSecurityGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSecurityGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSecurityGroups.html#EC2.Paginator.DescribeSecurityGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesecuritygroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeSnapshotTierStatusPaginatorBase = Paginator[DescribeSnapshotTierStatusResultTypeDef]
else:
    _DescribeSnapshotTierStatusPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSnapshotTierStatusPaginator(_DescribeSnapshotTierStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSnapshotTierStatus.html#EC2.Paginator.DescribeSnapshotTierStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesnapshottierstatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSnapshotTierStatusRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSnapshotTierStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSnapshotTierStatus.html#EC2.Paginator.DescribeSnapshotTierStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesnapshottierstatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeSnapshotsPaginatorBase = Paginator[DescribeSnapshotsResultTypeDef]
else:
    _DescribeSnapshotsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSnapshotsPaginator(_DescribeSnapshotsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSnapshots.html#EC2.Paginator.DescribeSnapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesnapshotspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSnapshotsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSnapshots.html#EC2.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesnapshotspaginator)
        """

if TYPE_CHECKING:
    _DescribeSpotFleetInstancesPaginatorBase = Paginator[DescribeSpotFleetInstancesResponseTypeDef]
else:
    _DescribeSpotFleetInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSpotFleetInstancesPaginator(_DescribeSpotFleetInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSpotFleetInstances.html#EC2.Paginator.DescribeSpotFleetInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describespotfleetinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSpotFleetInstancesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSpotFleetInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSpotFleetInstances.html#EC2.Paginator.DescribeSpotFleetInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describespotfleetinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeSpotFleetRequestsPaginatorBase = Paginator[DescribeSpotFleetRequestsResponseTypeDef]
else:
    _DescribeSpotFleetRequestsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSpotFleetRequestsPaginator(_DescribeSpotFleetRequestsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSpotFleetRequests.html#EC2.Paginator.DescribeSpotFleetRequests)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describespotfleetrequestspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSpotFleetRequestsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSpotFleetRequestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSpotFleetRequests.html#EC2.Paginator.DescribeSpotFleetRequests.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describespotfleetrequestspaginator)
        """

if TYPE_CHECKING:
    _DescribeSpotInstanceRequestsPaginatorBase = Paginator[
        DescribeSpotInstanceRequestsResultTypeDef
    ]
else:
    _DescribeSpotInstanceRequestsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSpotInstanceRequestsPaginator(_DescribeSpotInstanceRequestsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSpotInstanceRequests.html#EC2.Paginator.DescribeSpotInstanceRequests)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describespotinstancerequestspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSpotInstanceRequestsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSpotInstanceRequestsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSpotInstanceRequests.html#EC2.Paginator.DescribeSpotInstanceRequests.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describespotinstancerequestspaginator)
        """

if TYPE_CHECKING:
    _DescribeSpotPriceHistoryPaginatorBase = Paginator[DescribeSpotPriceHistoryResultTypeDef]
else:
    _DescribeSpotPriceHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSpotPriceHistoryPaginator(_DescribeSpotPriceHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSpotPriceHistory.html#EC2.Paginator.DescribeSpotPriceHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describespotpricehistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSpotPriceHistoryRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSpotPriceHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSpotPriceHistory.html#EC2.Paginator.DescribeSpotPriceHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describespotpricehistorypaginator)
        """

if TYPE_CHECKING:
    _DescribeStaleSecurityGroupsPaginatorBase = Paginator[DescribeStaleSecurityGroupsResultTypeDef]
else:
    _DescribeStaleSecurityGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStaleSecurityGroupsPaginator(_DescribeStaleSecurityGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeStaleSecurityGroups.html#EC2.Paginator.DescribeStaleSecurityGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describestalesecuritygroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStaleSecurityGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeStaleSecurityGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeStaleSecurityGroups.html#EC2.Paginator.DescribeStaleSecurityGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describestalesecuritygroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeStoreImageTasksPaginatorBase = Paginator[DescribeStoreImageTasksResultTypeDef]
else:
    _DescribeStoreImageTasksPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeStoreImageTasksPaginator(_DescribeStoreImageTasksPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeStoreImageTasks.html#EC2.Paginator.DescribeStoreImageTasks)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describestoreimagetaskspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeStoreImageTasksRequestPaginateTypeDef]
    ) -> PageIterator[DescribeStoreImageTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeStoreImageTasks.html#EC2.Paginator.DescribeStoreImageTasks.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describestoreimagetaskspaginator)
        """

if TYPE_CHECKING:
    _DescribeSubnetsPaginatorBase = Paginator[DescribeSubnetsResultTypeDef]
else:
    _DescribeSubnetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeSubnetsPaginator(_DescribeSubnetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSubnets.html#EC2.Paginator.DescribeSubnets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesubnetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeSubnetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeSubnetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeSubnets.html#EC2.Paginator.DescribeSubnets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describesubnetspaginator)
        """

if TYPE_CHECKING:
    _DescribeTagsPaginatorBase = Paginator[DescribeTagsResultTypeDef]
else:
    _DescribeTagsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTagsPaginator(_DescribeTagsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTags.html#EC2.Paginator.DescribeTags)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetagspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTagsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTagsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTags.html#EC2.Paginator.DescribeTags.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetagspaginator)
        """

if TYPE_CHECKING:
    _DescribeTrafficMirrorFiltersPaginatorBase = Paginator[
        DescribeTrafficMirrorFiltersResultTypeDef
    ]
else:
    _DescribeTrafficMirrorFiltersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTrafficMirrorFiltersPaginator(_DescribeTrafficMirrorFiltersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTrafficMirrorFilters.html#EC2.Paginator.DescribeTrafficMirrorFilters)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetrafficmirrorfilterspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTrafficMirrorFiltersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTrafficMirrorFiltersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTrafficMirrorFilters.html#EC2.Paginator.DescribeTrafficMirrorFilters.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetrafficmirrorfilterspaginator)
        """

if TYPE_CHECKING:
    _DescribeTrafficMirrorSessionsPaginatorBase = Paginator[
        DescribeTrafficMirrorSessionsResultTypeDef
    ]
else:
    _DescribeTrafficMirrorSessionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTrafficMirrorSessionsPaginator(_DescribeTrafficMirrorSessionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTrafficMirrorSessions.html#EC2.Paginator.DescribeTrafficMirrorSessions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetrafficmirrorsessionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTrafficMirrorSessionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTrafficMirrorSessionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTrafficMirrorSessions.html#EC2.Paginator.DescribeTrafficMirrorSessions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetrafficmirrorsessionspaginator)
        """

if TYPE_CHECKING:
    _DescribeTrafficMirrorTargetsPaginatorBase = Paginator[
        DescribeTrafficMirrorTargetsResultTypeDef
    ]
else:
    _DescribeTrafficMirrorTargetsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTrafficMirrorTargetsPaginator(_DescribeTrafficMirrorTargetsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTrafficMirrorTargets.html#EC2.Paginator.DescribeTrafficMirrorTargets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetrafficmirrortargetspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTrafficMirrorTargetsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTrafficMirrorTargetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTrafficMirrorTargets.html#EC2.Paginator.DescribeTrafficMirrorTargets.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetrafficmirrortargetspaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewayAttachmentsPaginatorBase = Paginator[
        DescribeTransitGatewayAttachmentsResultTypeDef
    ]
else:
    _DescribeTransitGatewayAttachmentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewayAttachmentsPaginator(_DescribeTransitGatewayAttachmentsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayAttachments.html#EC2.Paginator.DescribeTransitGatewayAttachments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayattachmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewayAttachmentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewayAttachmentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayAttachments.html#EC2.Paginator.DescribeTransitGatewayAttachments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayattachmentspaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewayConnectPeersPaginatorBase = Paginator[
        DescribeTransitGatewayConnectPeersResultTypeDef
    ]
else:
    _DescribeTransitGatewayConnectPeersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewayConnectPeersPaginator(_DescribeTransitGatewayConnectPeersPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayConnectPeers.html#EC2.Paginator.DescribeTransitGatewayConnectPeers)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayconnectpeerspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewayConnectPeersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewayConnectPeersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayConnectPeers.html#EC2.Paginator.DescribeTransitGatewayConnectPeers.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayconnectpeerspaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewayConnectsPaginatorBase = Paginator[
        DescribeTransitGatewayConnectsResultTypeDef
    ]
else:
    _DescribeTransitGatewayConnectsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewayConnectsPaginator(_DescribeTransitGatewayConnectsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayConnects.html#EC2.Paginator.DescribeTransitGatewayConnects)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayconnectspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewayConnectsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewayConnectsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayConnects.html#EC2.Paginator.DescribeTransitGatewayConnects.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayconnectspaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewayMulticastDomainsPaginatorBase = Paginator[
        DescribeTransitGatewayMulticastDomainsResultTypeDef
    ]
else:
    _DescribeTransitGatewayMulticastDomainsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewayMulticastDomainsPaginator(
    _DescribeTransitGatewayMulticastDomainsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayMulticastDomains.html#EC2.Paginator.DescribeTransitGatewayMulticastDomains)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewaymulticastdomainspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewayMulticastDomainsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewayMulticastDomainsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayMulticastDomains.html#EC2.Paginator.DescribeTransitGatewayMulticastDomains.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewaymulticastdomainspaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewayPeeringAttachmentsPaginatorBase = Paginator[
        DescribeTransitGatewayPeeringAttachmentsResultTypeDef
    ]
else:
    _DescribeTransitGatewayPeeringAttachmentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewayPeeringAttachmentsPaginator(
    _DescribeTransitGatewayPeeringAttachmentsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayPeeringAttachments.html#EC2.Paginator.DescribeTransitGatewayPeeringAttachments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewaypeeringattachmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewayPeeringAttachmentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewayPeeringAttachmentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayPeeringAttachments.html#EC2.Paginator.DescribeTransitGatewayPeeringAttachments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewaypeeringattachmentspaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewayPolicyTablesPaginatorBase = Paginator[
        DescribeTransitGatewayPolicyTablesResultTypeDef
    ]
else:
    _DescribeTransitGatewayPolicyTablesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewayPolicyTablesPaginator(_DescribeTransitGatewayPolicyTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayPolicyTables.html#EC2.Paginator.DescribeTransitGatewayPolicyTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewaypolicytablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewayPolicyTablesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewayPolicyTablesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayPolicyTables.html#EC2.Paginator.DescribeTransitGatewayPolicyTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewaypolicytablespaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewayRouteTableAnnouncementsPaginatorBase = Paginator[
        DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef
    ]
else:
    _DescribeTransitGatewayRouteTableAnnouncementsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewayRouteTableAnnouncementsPaginator(
    _DescribeTransitGatewayRouteTableAnnouncementsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayRouteTableAnnouncements.html#EC2.Paginator.DescribeTransitGatewayRouteTableAnnouncements)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayroutetableannouncementspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewayRouteTableAnnouncementsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayRouteTableAnnouncements.html#EC2.Paginator.DescribeTransitGatewayRouteTableAnnouncements.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayroutetableannouncementspaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewayRouteTablesPaginatorBase = Paginator[
        DescribeTransitGatewayRouteTablesResultTypeDef
    ]
else:
    _DescribeTransitGatewayRouteTablesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewayRouteTablesPaginator(_DescribeTransitGatewayRouteTablesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayRouteTables.html#EC2.Paginator.DescribeTransitGatewayRouteTables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayroutetablespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewayRouteTablesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewayRouteTablesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayRouteTables.html#EC2.Paginator.DescribeTransitGatewayRouteTables.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayroutetablespaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewayVpcAttachmentsPaginatorBase = Paginator[
        DescribeTransitGatewayVpcAttachmentsResultTypeDef
    ]
else:
    _DescribeTransitGatewayVpcAttachmentsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewayVpcAttachmentsPaginator(
    _DescribeTransitGatewayVpcAttachmentsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayVpcAttachments.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayvpcattachmentspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewayVpcAttachmentsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewayVpcAttachmentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGatewayVpcAttachments.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayvpcattachmentspaginator)
        """

if TYPE_CHECKING:
    _DescribeTransitGatewaysPaginatorBase = Paginator[DescribeTransitGatewaysResultTypeDef]
else:
    _DescribeTransitGatewaysPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTransitGatewaysPaginator(_DescribeTransitGatewaysPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGateways.html#EC2.Paginator.DescribeTransitGateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTransitGatewaysRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTransitGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTransitGateways.html#EC2.Paginator.DescribeTransitGateways.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetransitgatewayspaginator)
        """

if TYPE_CHECKING:
    _DescribeTrunkInterfaceAssociationsPaginatorBase = Paginator[
        DescribeTrunkInterfaceAssociationsResultTypeDef
    ]
else:
    _DescribeTrunkInterfaceAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeTrunkInterfaceAssociationsPaginator(_DescribeTrunkInterfaceAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTrunkInterfaceAssociations.html#EC2.Paginator.DescribeTrunkInterfaceAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetrunkinterfaceassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeTrunkInterfaceAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeTrunkInterfaceAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeTrunkInterfaceAssociations.html#EC2.Paginator.DescribeTrunkInterfaceAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describetrunkinterfaceassociationspaginator)
        """

if TYPE_CHECKING:
    _DescribeVerifiedAccessEndpointsPaginatorBase = Paginator[
        DescribeVerifiedAccessEndpointsResultTypeDef
    ]
else:
    _DescribeVerifiedAccessEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVerifiedAccessEndpointsPaginator(_DescribeVerifiedAccessEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessEndpoints.html#EC2.Paginator.DescribeVerifiedAccessEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccessendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVerifiedAccessEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVerifiedAccessEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessEndpoints.html#EC2.Paginator.DescribeVerifiedAccessEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccessendpointspaginator)
        """

if TYPE_CHECKING:
    _DescribeVerifiedAccessGroupsPaginatorBase = Paginator[
        DescribeVerifiedAccessGroupsResultTypeDef
    ]
else:
    _DescribeVerifiedAccessGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVerifiedAccessGroupsPaginator(_DescribeVerifiedAccessGroupsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessGroups.html#EC2.Paginator.DescribeVerifiedAccessGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccessgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVerifiedAccessGroupsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVerifiedAccessGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessGroups.html#EC2.Paginator.DescribeVerifiedAccessGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccessgroupspaginator)
        """

if TYPE_CHECKING:
    _DescribeVerifiedAccessInstanceLoggingConfigurationsPaginatorBase = Paginator[
        DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef
    ]
else:
    _DescribeVerifiedAccessInstanceLoggingConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator(
    _DescribeVerifiedAccessInstanceLoggingConfigurationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessInstanceLoggingConfigurations.html#EC2.Paginator.DescribeVerifiedAccessInstanceLoggingConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccessinstanceloggingconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self,
        **kwargs: Unpack[DescribeVerifiedAccessInstanceLoggingConfigurationsRequestPaginateTypeDef],
    ) -> PageIterator[DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessInstanceLoggingConfigurations.html#EC2.Paginator.DescribeVerifiedAccessInstanceLoggingConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccessinstanceloggingconfigurationspaginator)
        """

if TYPE_CHECKING:
    _DescribeVerifiedAccessInstancesPaginatorBase = Paginator[
        DescribeVerifiedAccessInstancesResultTypeDef
    ]
else:
    _DescribeVerifiedAccessInstancesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVerifiedAccessInstancesPaginator(_DescribeVerifiedAccessInstancesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessInstances.html#EC2.Paginator.DescribeVerifiedAccessInstances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccessinstancespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVerifiedAccessInstancesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVerifiedAccessInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessInstances.html#EC2.Paginator.DescribeVerifiedAccessInstances.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccessinstancespaginator)
        """

if TYPE_CHECKING:
    _DescribeVerifiedAccessTrustProvidersPaginatorBase = Paginator[
        DescribeVerifiedAccessTrustProvidersResultTypeDef
    ]
else:
    _DescribeVerifiedAccessTrustProvidersPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVerifiedAccessTrustProvidersPaginator(
    _DescribeVerifiedAccessTrustProvidersPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessTrustProviders.html#EC2.Paginator.DescribeVerifiedAccessTrustProviders)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccesstrustproviderspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVerifiedAccessTrustProvidersRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVerifiedAccessTrustProvidersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVerifiedAccessTrustProviders.html#EC2.Paginator.DescribeVerifiedAccessTrustProviders.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describeverifiedaccesstrustproviderspaginator)
        """

if TYPE_CHECKING:
    _DescribeVolumeStatusPaginatorBase = Paginator[DescribeVolumeStatusResultTypeDef]
else:
    _DescribeVolumeStatusPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVolumeStatusPaginator(_DescribeVolumeStatusPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVolumeStatus.html#EC2.Paginator.DescribeVolumeStatus)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevolumestatuspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVolumeStatusRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVolumeStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVolumeStatus.html#EC2.Paginator.DescribeVolumeStatus.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevolumestatuspaginator)
        """

if TYPE_CHECKING:
    _DescribeVolumesModificationsPaginatorBase = Paginator[
        DescribeVolumesModificationsResultTypeDef
    ]
else:
    _DescribeVolumesModificationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVolumesModificationsPaginator(_DescribeVolumesModificationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVolumesModifications.html#EC2.Paginator.DescribeVolumesModifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevolumesmodificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVolumesModificationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVolumesModificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVolumesModifications.html#EC2.Paginator.DescribeVolumesModifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevolumesmodificationspaginator)
        """

if TYPE_CHECKING:
    _DescribeVolumesPaginatorBase = Paginator[DescribeVolumesResultTypeDef]
else:
    _DescribeVolumesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVolumesPaginator(_DescribeVolumesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVolumes.html#EC2.Paginator.DescribeVolumes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevolumespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVolumesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVolumesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVolumes.html#EC2.Paginator.DescribeVolumes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevolumespaginator)
        """

if TYPE_CHECKING:
    _DescribeVpcClassicLinkDnsSupportPaginatorBase = Paginator[
        DescribeVpcClassicLinkDnsSupportResultTypeDef
    ]
else:
    _DescribeVpcClassicLinkDnsSupportPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVpcClassicLinkDnsSupportPaginator(_DescribeVpcClassicLinkDnsSupportPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcClassicLinkDnsSupport.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcclassiclinkdnssupportpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcClassicLinkDnsSupportRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVpcClassicLinkDnsSupportResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcClassicLinkDnsSupport.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcclassiclinkdnssupportpaginator)
        """

if TYPE_CHECKING:
    _DescribeVpcEndpointConnectionNotificationsPaginatorBase = Paginator[
        DescribeVpcEndpointConnectionNotificationsResultTypeDef
    ]
else:
    _DescribeVpcEndpointConnectionNotificationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVpcEndpointConnectionNotificationsPaginator(
    _DescribeVpcEndpointConnectionNotificationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointConnectionNotifications.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointconnectionnotificationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcEndpointConnectionNotificationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVpcEndpointConnectionNotificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointConnectionNotifications.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointconnectionnotificationspaginator)
        """

if TYPE_CHECKING:
    _DescribeVpcEndpointConnectionsPaginatorBase = Paginator[
        DescribeVpcEndpointConnectionsResultTypeDef
    ]
else:
    _DescribeVpcEndpointConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVpcEndpointConnectionsPaginator(_DescribeVpcEndpointConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointConnections.html#EC2.Paginator.DescribeVpcEndpointConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcEndpointConnectionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVpcEndpointConnectionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointConnections.html#EC2.Paginator.DescribeVpcEndpointConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointconnectionspaginator)
        """

if TYPE_CHECKING:
    _DescribeVpcEndpointServiceConfigurationsPaginatorBase = Paginator[
        DescribeVpcEndpointServiceConfigurationsResultTypeDef
    ]
else:
    _DescribeVpcEndpointServiceConfigurationsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVpcEndpointServiceConfigurationsPaginator(
    _DescribeVpcEndpointServiceConfigurationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointServiceConfigurations.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointserviceconfigurationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcEndpointServiceConfigurationsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVpcEndpointServiceConfigurationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointServiceConfigurations.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointserviceconfigurationspaginator)
        """

if TYPE_CHECKING:
    _DescribeVpcEndpointServicePermissionsPaginatorBase = Paginator[
        DescribeVpcEndpointServicePermissionsResultTypeDef
    ]
else:
    _DescribeVpcEndpointServicePermissionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVpcEndpointServicePermissionsPaginator(
    _DescribeVpcEndpointServicePermissionsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointServicePermissions.html#EC2.Paginator.DescribeVpcEndpointServicePermissions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointservicepermissionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcEndpointServicePermissionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVpcEndpointServicePermissionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointServicePermissions.html#EC2.Paginator.DescribeVpcEndpointServicePermissions.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointservicepermissionspaginator)
        """

if TYPE_CHECKING:
    _DescribeVpcEndpointServicesPaginatorBase = Paginator[DescribeVpcEndpointServicesResultTypeDef]
else:
    _DescribeVpcEndpointServicesPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVpcEndpointServicesPaginator(_DescribeVpcEndpointServicesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointServices.html#EC2.Paginator.DescribeVpcEndpointServices)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointservicespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcEndpointServicesRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVpcEndpointServicesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpointServices.html#EC2.Paginator.DescribeVpcEndpointServices.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointservicespaginator)
        """

if TYPE_CHECKING:
    _DescribeVpcEndpointsPaginatorBase = Paginator[DescribeVpcEndpointsResultTypeDef]
else:
    _DescribeVpcEndpointsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVpcEndpointsPaginator(_DescribeVpcEndpointsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpoints.html#EC2.Paginator.DescribeVpcEndpoints)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcEndpointsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVpcEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcEndpoints.html#EC2.Paginator.DescribeVpcEndpoints.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcendpointspaginator)
        """

if TYPE_CHECKING:
    _DescribeVpcPeeringConnectionsPaginatorBase = Paginator[
        DescribeVpcPeeringConnectionsResultTypeDef
    ]
else:
    _DescribeVpcPeeringConnectionsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVpcPeeringConnectionsPaginator(_DescribeVpcPeeringConnectionsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcPeeringConnections.html#EC2.Paginator.DescribeVpcPeeringConnections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcpeeringconnectionspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcPeeringConnectionsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVpcPeeringConnectionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcPeeringConnections.html#EC2.Paginator.DescribeVpcPeeringConnections.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcpeeringconnectionspaginator)
        """

if TYPE_CHECKING:
    _DescribeVpcsPaginatorBase = Paginator[DescribeVpcsResultTypeDef]
else:
    _DescribeVpcsPaginatorBase = Paginator  # type: ignore[assignment]

class DescribeVpcsPaginator(_DescribeVpcsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcs.html#EC2.Paginator.DescribeVpcs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[DescribeVpcsRequestPaginateTypeDef]
    ) -> PageIterator[DescribeVpcsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/DescribeVpcs.html#EC2.Paginator.DescribeVpcs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#describevpcspaginator)
        """

if TYPE_CHECKING:
    _GetAssociatedIpv6PoolCidrsPaginatorBase = Paginator[GetAssociatedIpv6PoolCidrsResultTypeDef]
else:
    _GetAssociatedIpv6PoolCidrsPaginatorBase = Paginator  # type: ignore[assignment]

class GetAssociatedIpv6PoolCidrsPaginator(_GetAssociatedIpv6PoolCidrsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetAssociatedIpv6PoolCidrs.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getassociatedipv6poolcidrspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAssociatedIpv6PoolCidrsRequestPaginateTypeDef]
    ) -> PageIterator[GetAssociatedIpv6PoolCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetAssociatedIpv6PoolCidrs.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getassociatedipv6poolcidrspaginator)
        """

if TYPE_CHECKING:
    _GetAwsNetworkPerformanceDataPaginatorBase = Paginator[
        GetAwsNetworkPerformanceDataResultTypeDef
    ]
else:
    _GetAwsNetworkPerformanceDataPaginatorBase = Paginator  # type: ignore[assignment]

class GetAwsNetworkPerformanceDataPaginator(_GetAwsNetworkPerformanceDataPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetAwsNetworkPerformanceData.html#EC2.Paginator.GetAwsNetworkPerformanceData)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getawsnetworkperformancedatapaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetAwsNetworkPerformanceDataRequestPaginateTypeDef]
    ) -> PageIterator[GetAwsNetworkPerformanceDataResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetAwsNetworkPerformanceData.html#EC2.Paginator.GetAwsNetworkPerformanceData.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getawsnetworkperformancedatapaginator)
        """

if TYPE_CHECKING:
    _GetGroupsForCapacityReservationPaginatorBase = Paginator[
        GetGroupsForCapacityReservationResultTypeDef
    ]
else:
    _GetGroupsForCapacityReservationPaginatorBase = Paginator  # type: ignore[assignment]

class GetGroupsForCapacityReservationPaginator(_GetGroupsForCapacityReservationPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetGroupsForCapacityReservation.html#EC2.Paginator.GetGroupsForCapacityReservation)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getgroupsforcapacityreservationpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetGroupsForCapacityReservationRequestPaginateTypeDef]
    ) -> PageIterator[GetGroupsForCapacityReservationResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetGroupsForCapacityReservation.html#EC2.Paginator.GetGroupsForCapacityReservation.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getgroupsforcapacityreservationpaginator)
        """

if TYPE_CHECKING:
    _GetInstanceTypesFromInstanceRequirementsPaginatorBase = Paginator[
        GetInstanceTypesFromInstanceRequirementsResultTypeDef
    ]
else:
    _GetInstanceTypesFromInstanceRequirementsPaginatorBase = Paginator  # type: ignore[assignment]

class GetInstanceTypesFromInstanceRequirementsPaginator(
    _GetInstanceTypesFromInstanceRequirementsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetInstanceTypesFromInstanceRequirements.html#EC2.Paginator.GetInstanceTypesFromInstanceRequirements)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getinstancetypesfrominstancerequirementspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetInstanceTypesFromInstanceRequirementsRequestPaginateTypeDef]
    ) -> PageIterator[GetInstanceTypesFromInstanceRequirementsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetInstanceTypesFromInstanceRequirements.html#EC2.Paginator.GetInstanceTypesFromInstanceRequirements.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getinstancetypesfrominstancerequirementspaginator)
        """

if TYPE_CHECKING:
    _GetIpamAddressHistoryPaginatorBase = Paginator[GetIpamAddressHistoryResultTypeDef]
else:
    _GetIpamAddressHistoryPaginatorBase = Paginator  # type: ignore[assignment]

class GetIpamAddressHistoryPaginator(_GetIpamAddressHistoryPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamAddressHistory.html#EC2.Paginator.GetIpamAddressHistory)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipamaddresshistorypaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIpamAddressHistoryRequestPaginateTypeDef]
    ) -> PageIterator[GetIpamAddressHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamAddressHistory.html#EC2.Paginator.GetIpamAddressHistory.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipamaddresshistorypaginator)
        """

if TYPE_CHECKING:
    _GetIpamDiscoveredAccountsPaginatorBase = Paginator[GetIpamDiscoveredAccountsResultTypeDef]
else:
    _GetIpamDiscoveredAccountsPaginatorBase = Paginator  # type: ignore[assignment]

class GetIpamDiscoveredAccountsPaginator(_GetIpamDiscoveredAccountsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamDiscoveredAccounts.html#EC2.Paginator.GetIpamDiscoveredAccounts)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipamdiscoveredaccountspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIpamDiscoveredAccountsRequestPaginateTypeDef]
    ) -> PageIterator[GetIpamDiscoveredAccountsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamDiscoveredAccounts.html#EC2.Paginator.GetIpamDiscoveredAccounts.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipamdiscoveredaccountspaginator)
        """

if TYPE_CHECKING:
    _GetIpamDiscoveredResourceCidrsPaginatorBase = Paginator[
        GetIpamDiscoveredResourceCidrsResultTypeDef
    ]
else:
    _GetIpamDiscoveredResourceCidrsPaginatorBase = Paginator  # type: ignore[assignment]

class GetIpamDiscoveredResourceCidrsPaginator(_GetIpamDiscoveredResourceCidrsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamDiscoveredResourceCidrs.html#EC2.Paginator.GetIpamDiscoveredResourceCidrs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipamdiscoveredresourcecidrspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIpamDiscoveredResourceCidrsRequestPaginateTypeDef]
    ) -> PageIterator[GetIpamDiscoveredResourceCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamDiscoveredResourceCidrs.html#EC2.Paginator.GetIpamDiscoveredResourceCidrs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipamdiscoveredresourcecidrspaginator)
        """

if TYPE_CHECKING:
    _GetIpamPoolAllocationsPaginatorBase = Paginator[GetIpamPoolAllocationsResultTypeDef]
else:
    _GetIpamPoolAllocationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetIpamPoolAllocationsPaginator(_GetIpamPoolAllocationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamPoolAllocations.html#EC2.Paginator.GetIpamPoolAllocations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipampoolallocationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIpamPoolAllocationsRequestPaginateTypeDef]
    ) -> PageIterator[GetIpamPoolAllocationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamPoolAllocations.html#EC2.Paginator.GetIpamPoolAllocations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipampoolallocationspaginator)
        """

if TYPE_CHECKING:
    _GetIpamPoolCidrsPaginatorBase = Paginator[GetIpamPoolCidrsResultTypeDef]
else:
    _GetIpamPoolCidrsPaginatorBase = Paginator  # type: ignore[assignment]

class GetIpamPoolCidrsPaginator(_GetIpamPoolCidrsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamPoolCidrs.html#EC2.Paginator.GetIpamPoolCidrs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipampoolcidrspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIpamPoolCidrsRequestPaginateTypeDef]
    ) -> PageIterator[GetIpamPoolCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamPoolCidrs.html#EC2.Paginator.GetIpamPoolCidrs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipampoolcidrspaginator)
        """

if TYPE_CHECKING:
    _GetIpamResourceCidrsPaginatorBase = Paginator[GetIpamResourceCidrsResultTypeDef]
else:
    _GetIpamResourceCidrsPaginatorBase = Paginator  # type: ignore[assignment]

class GetIpamResourceCidrsPaginator(_GetIpamResourceCidrsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamResourceCidrs.html#EC2.Paginator.GetIpamResourceCidrs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipamresourcecidrspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetIpamResourceCidrsRequestPaginateTypeDef]
    ) -> PageIterator[GetIpamResourceCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetIpamResourceCidrs.html#EC2.Paginator.GetIpamResourceCidrs.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getipamresourcecidrspaginator)
        """

if TYPE_CHECKING:
    _GetManagedPrefixListAssociationsPaginatorBase = Paginator[
        GetManagedPrefixListAssociationsResultTypeDef
    ]
else:
    _GetManagedPrefixListAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetManagedPrefixListAssociationsPaginator(_GetManagedPrefixListAssociationsPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetManagedPrefixListAssociations.html#EC2.Paginator.GetManagedPrefixListAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getmanagedprefixlistassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetManagedPrefixListAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetManagedPrefixListAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetManagedPrefixListAssociations.html#EC2.Paginator.GetManagedPrefixListAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getmanagedprefixlistassociationspaginator)
        """

if TYPE_CHECKING:
    _GetManagedPrefixListEntriesPaginatorBase = Paginator[GetManagedPrefixListEntriesResultTypeDef]
else:
    _GetManagedPrefixListEntriesPaginatorBase = Paginator  # type: ignore[assignment]

class GetManagedPrefixListEntriesPaginator(_GetManagedPrefixListEntriesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetManagedPrefixListEntries.html#EC2.Paginator.GetManagedPrefixListEntries)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getmanagedprefixlistentriespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetManagedPrefixListEntriesRequestPaginateTypeDef]
    ) -> PageIterator[GetManagedPrefixListEntriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetManagedPrefixListEntries.html#EC2.Paginator.GetManagedPrefixListEntries.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getmanagedprefixlistentriespaginator)
        """

if TYPE_CHECKING:
    _GetNetworkInsightsAccessScopeAnalysisFindingsPaginatorBase = Paginator[
        GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef
    ]
else:
    _GetNetworkInsightsAccessScopeAnalysisFindingsPaginatorBase = Paginator  # type: ignore[assignment]

class GetNetworkInsightsAccessScopeAnalysisFindingsPaginator(
    _GetNetworkInsightsAccessScopeAnalysisFindingsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetNetworkInsightsAccessScopeAnalysisFindings.html#EC2.Paginator.GetNetworkInsightsAccessScopeAnalysisFindings)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getnetworkinsightsaccessscopeanalysisfindingspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetNetworkInsightsAccessScopeAnalysisFindingsRequestPaginateTypeDef]
    ) -> PageIterator[GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetNetworkInsightsAccessScopeAnalysisFindings.html#EC2.Paginator.GetNetworkInsightsAccessScopeAnalysisFindings.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getnetworkinsightsaccessscopeanalysisfindingspaginator)
        """

if TYPE_CHECKING:
    _GetSecurityGroupsForVpcPaginatorBase = Paginator[GetSecurityGroupsForVpcResultTypeDef]
else:
    _GetSecurityGroupsForVpcPaginatorBase = Paginator  # type: ignore[assignment]

class GetSecurityGroupsForVpcPaginator(_GetSecurityGroupsForVpcPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetSecurityGroupsForVpc.html#EC2.Paginator.GetSecurityGroupsForVpc)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getsecuritygroupsforvpcpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSecurityGroupsForVpcRequestPaginateTypeDef]
    ) -> PageIterator[GetSecurityGroupsForVpcResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetSecurityGroupsForVpc.html#EC2.Paginator.GetSecurityGroupsForVpc.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getsecuritygroupsforvpcpaginator)
        """

if TYPE_CHECKING:
    _GetSpotPlacementScoresPaginatorBase = Paginator[GetSpotPlacementScoresResultTypeDef]
else:
    _GetSpotPlacementScoresPaginatorBase = Paginator  # type: ignore[assignment]

class GetSpotPlacementScoresPaginator(_GetSpotPlacementScoresPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetSpotPlacementScores.html#EC2.Paginator.GetSpotPlacementScores)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getspotplacementscorespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetSpotPlacementScoresRequestPaginateTypeDef]
    ) -> PageIterator[GetSpotPlacementScoresResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetSpotPlacementScores.html#EC2.Paginator.GetSpotPlacementScores.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getspotplacementscorespaginator)
        """

if TYPE_CHECKING:
    _GetTransitGatewayAttachmentPropagationsPaginatorBase = Paginator[
        GetTransitGatewayAttachmentPropagationsResultTypeDef
    ]
else:
    _GetTransitGatewayAttachmentPropagationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetTransitGatewayAttachmentPropagationsPaginator(
    _GetTransitGatewayAttachmentPropagationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayAttachmentPropagations.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewayattachmentpropagationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTransitGatewayAttachmentPropagationsRequestPaginateTypeDef]
    ) -> PageIterator[GetTransitGatewayAttachmentPropagationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayAttachmentPropagations.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewayattachmentpropagationspaginator)
        """

if TYPE_CHECKING:
    _GetTransitGatewayMulticastDomainAssociationsPaginatorBase = Paginator[
        GetTransitGatewayMulticastDomainAssociationsResultTypeDef
    ]
else:
    _GetTransitGatewayMulticastDomainAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetTransitGatewayMulticastDomainAssociationsPaginator(
    _GetTransitGatewayMulticastDomainAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayMulticastDomainAssociations.html#EC2.Paginator.GetTransitGatewayMulticastDomainAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewaymulticastdomainassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTransitGatewayMulticastDomainAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetTransitGatewayMulticastDomainAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayMulticastDomainAssociations.html#EC2.Paginator.GetTransitGatewayMulticastDomainAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewaymulticastdomainassociationspaginator)
        """

if TYPE_CHECKING:
    _GetTransitGatewayPolicyTableAssociationsPaginatorBase = Paginator[
        GetTransitGatewayPolicyTableAssociationsResultTypeDef
    ]
else:
    _GetTransitGatewayPolicyTableAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetTransitGatewayPolicyTableAssociationsPaginator(
    _GetTransitGatewayPolicyTableAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayPolicyTableAssociations.html#EC2.Paginator.GetTransitGatewayPolicyTableAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewaypolicytableassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTransitGatewayPolicyTableAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetTransitGatewayPolicyTableAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayPolicyTableAssociations.html#EC2.Paginator.GetTransitGatewayPolicyTableAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewaypolicytableassociationspaginator)
        """

if TYPE_CHECKING:
    _GetTransitGatewayPrefixListReferencesPaginatorBase = Paginator[
        GetTransitGatewayPrefixListReferencesResultTypeDef
    ]
else:
    _GetTransitGatewayPrefixListReferencesPaginatorBase = Paginator  # type: ignore[assignment]

class GetTransitGatewayPrefixListReferencesPaginator(
    _GetTransitGatewayPrefixListReferencesPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayPrefixListReferences.html#EC2.Paginator.GetTransitGatewayPrefixListReferences)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewayprefixlistreferencespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTransitGatewayPrefixListReferencesRequestPaginateTypeDef]
    ) -> PageIterator[GetTransitGatewayPrefixListReferencesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayPrefixListReferences.html#EC2.Paginator.GetTransitGatewayPrefixListReferences.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewayprefixlistreferencespaginator)
        """

if TYPE_CHECKING:
    _GetTransitGatewayRouteTableAssociationsPaginatorBase = Paginator[
        GetTransitGatewayRouteTableAssociationsResultTypeDef
    ]
else:
    _GetTransitGatewayRouteTableAssociationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetTransitGatewayRouteTableAssociationsPaginator(
    _GetTransitGatewayRouteTableAssociationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayRouteTableAssociations.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewayroutetableassociationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTransitGatewayRouteTableAssociationsRequestPaginateTypeDef]
    ) -> PageIterator[GetTransitGatewayRouteTableAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayRouteTableAssociations.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewayroutetableassociationspaginator)
        """

if TYPE_CHECKING:
    _GetTransitGatewayRouteTablePropagationsPaginatorBase = Paginator[
        GetTransitGatewayRouteTablePropagationsResultTypeDef
    ]
else:
    _GetTransitGatewayRouteTablePropagationsPaginatorBase = Paginator  # type: ignore[assignment]

class GetTransitGatewayRouteTablePropagationsPaginator(
    _GetTransitGatewayRouteTablePropagationsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayRouteTablePropagations.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewayroutetablepropagationspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetTransitGatewayRouteTablePropagationsRequestPaginateTypeDef]
    ) -> PageIterator[GetTransitGatewayRouteTablePropagationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetTransitGatewayRouteTablePropagations.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#gettransitgatewayroutetablepropagationspaginator)
        """

if TYPE_CHECKING:
    _GetVpnConnectionDeviceTypesPaginatorBase = Paginator[GetVpnConnectionDeviceTypesResultTypeDef]
else:
    _GetVpnConnectionDeviceTypesPaginatorBase = Paginator  # type: ignore[assignment]

class GetVpnConnectionDeviceTypesPaginator(_GetVpnConnectionDeviceTypesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetVpnConnectionDeviceTypes.html#EC2.Paginator.GetVpnConnectionDeviceTypes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getvpnconnectiondevicetypespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[GetVpnConnectionDeviceTypesRequestPaginateTypeDef]
    ) -> PageIterator[GetVpnConnectionDeviceTypesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/GetVpnConnectionDeviceTypes.html#EC2.Paginator.GetVpnConnectionDeviceTypes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#getvpnconnectiondevicetypespaginator)
        """

if TYPE_CHECKING:
    _ListImagesInRecycleBinPaginatorBase = Paginator[ListImagesInRecycleBinResultTypeDef]
else:
    _ListImagesInRecycleBinPaginatorBase = Paginator  # type: ignore[assignment]

class ListImagesInRecycleBinPaginator(_ListImagesInRecycleBinPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/ListImagesInRecycleBin.html#EC2.Paginator.ListImagesInRecycleBin)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#listimagesinrecyclebinpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListImagesInRecycleBinRequestPaginateTypeDef]
    ) -> PageIterator[ListImagesInRecycleBinResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/ListImagesInRecycleBin.html#EC2.Paginator.ListImagesInRecycleBin.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#listimagesinrecyclebinpaginator)
        """

if TYPE_CHECKING:
    _ListSnapshotsInRecycleBinPaginatorBase = Paginator[ListSnapshotsInRecycleBinResultTypeDef]
else:
    _ListSnapshotsInRecycleBinPaginatorBase = Paginator  # type: ignore[assignment]

class ListSnapshotsInRecycleBinPaginator(_ListSnapshotsInRecycleBinPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/ListSnapshotsInRecycleBin.html#EC2.Paginator.ListSnapshotsInRecycleBin)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#listsnapshotsinrecyclebinpaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[ListSnapshotsInRecycleBinRequestPaginateTypeDef]
    ) -> PageIterator[ListSnapshotsInRecycleBinResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/ListSnapshotsInRecycleBin.html#EC2.Paginator.ListSnapshotsInRecycleBin.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#listsnapshotsinrecyclebinpaginator)
        """

if TYPE_CHECKING:
    _SearchLocalGatewayRoutesPaginatorBase = Paginator[SearchLocalGatewayRoutesResultTypeDef]
else:
    _SearchLocalGatewayRoutesPaginatorBase = Paginator  # type: ignore[assignment]

class SearchLocalGatewayRoutesPaginator(_SearchLocalGatewayRoutesPaginatorBase):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/SearchLocalGatewayRoutes.html#EC2.Paginator.SearchLocalGatewayRoutes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#searchlocalgatewayroutespaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchLocalGatewayRoutesRequestPaginateTypeDef]
    ) -> PageIterator[SearchLocalGatewayRoutesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/SearchLocalGatewayRoutes.html#EC2.Paginator.SearchLocalGatewayRoutes.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#searchlocalgatewayroutespaginator)
        """

if TYPE_CHECKING:
    _SearchTransitGatewayMulticastGroupsPaginatorBase = Paginator[
        SearchTransitGatewayMulticastGroupsResultTypeDef
    ]
else:
    _SearchTransitGatewayMulticastGroupsPaginatorBase = Paginator  # type: ignore[assignment]

class SearchTransitGatewayMulticastGroupsPaginator(
    _SearchTransitGatewayMulticastGroupsPaginatorBase
):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/SearchTransitGatewayMulticastGroups.html#EC2.Paginator.SearchTransitGatewayMulticastGroups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#searchtransitgatewaymulticastgroupspaginator)
    """
    def paginate(  # type: ignore[override]
        self, **kwargs: Unpack[SearchTransitGatewayMulticastGroupsRequestPaginateTypeDef]
    ) -> PageIterator[SearchTransitGatewayMulticastGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/paginator/SearchTransitGatewayMulticastGroups.html#EC2.Paginator.SearchTransitGatewayMulticastGroups.paginate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators/#searchtransitgatewaymulticastgroupspaginator)
        """
