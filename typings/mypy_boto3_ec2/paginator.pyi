"""
Type annotations for ec2 service client paginators.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html)

Usage::

    ```python
    import boto3

    from mypy_boto3_ec2 import EC2Client
    from mypy_boto3_ec2.paginator import (
        DescribeAddressTransfersPaginator,
        DescribeAddressesAttributePaginator,
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
        DescribeVolumesPaginator,
        DescribeVolumesModificationsPaginator,
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

    client: EC2Client = boto3.client("ec2")

    describe_address_transfers_paginator: DescribeAddressTransfersPaginator = client.get_paginator("describe_address_transfers")
    describe_addresses_attribute_paginator: DescribeAddressesAttributePaginator = client.get_paginator("describe_addresses_attribute")
    describe_aws_network_performance_metric_subscriptions_paginator: DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator = client.get_paginator("describe_aws_network_performance_metric_subscriptions")
    describe_byoip_cidrs_paginator: DescribeByoipCidrsPaginator = client.get_paginator("describe_byoip_cidrs")
    describe_capacity_block_offerings_paginator: DescribeCapacityBlockOfferingsPaginator = client.get_paginator("describe_capacity_block_offerings")
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
    describe_route_tables_paginator: DescribeRouteTablesPaginator = client.get_paginator("describe_route_tables")
    describe_scheduled_instance_availability_paginator: DescribeScheduledInstanceAvailabilityPaginator = client.get_paginator("describe_scheduled_instance_availability")
    describe_scheduled_instances_paginator: DescribeScheduledInstancesPaginator = client.get_paginator("describe_scheduled_instances")
    describe_security_group_rules_paginator: DescribeSecurityGroupRulesPaginator = client.get_paginator("describe_security_group_rules")
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
    describe_volumes_paginator: DescribeVolumesPaginator = client.get_paginator("describe_volumes")
    describe_volumes_modifications_paginator: DescribeVolumesModificationsPaginator = client.get_paginator("describe_volumes_modifications")
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
import sys
from datetime import datetime
from typing import Iterator, List, Union

from botocore.paginate import Paginator as Boto3Paginator

from .literals import (
    ArchitectureTypeType,
    InstanceTypeType,
    IpamResourceTypeType,
    LocationTypeType,
    OfferingClassTypeType,
    OfferingTypeValuesType,
    RIProductDescriptionType,
    TargetCapacityUnitTypeType,
    TenancyType,
    VirtualizationTypeType,
)
from .type_defs import (
    DataQueryTypeDef,
    DescribeAddressesAttributeResultTypeDef,
    DescribeAddressTransfersResultTypeDef,
    DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef,
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
    DescribeDhcpOptionsResultTypeDef,
    DescribeEgressOnlyInternetGatewaysResultTypeDef,
    DescribeExportImageTasksResultTypeDef,
    DescribeFastLaunchImagesResultTypeDef,
    DescribeFastSnapshotRestoresResultTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeFlowLogsResultTypeDef,
    DescribeFpgaImagesResultTypeDef,
    DescribeHostReservationOfferingsResultTypeDef,
    DescribeHostReservationsResultTypeDef,
    DescribeHostsResultTypeDef,
    DescribeIamInstanceProfileAssociationsResultTypeDef,
    DescribeImagesResultTypeDef,
    DescribeImportImageTasksResultTypeDef,
    DescribeImportSnapshotTasksResultTypeDef,
    DescribeInstanceConnectEndpointsResultTypeDef,
    DescribeInstanceCreditSpecificationsResultTypeDef,
    DescribeInstanceEventWindowsResultTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeInstanceStatusResultTypeDef,
    DescribeInstanceTopologyResultTypeDef,
    DescribeInstanceTypeOfferingsResultTypeDef,
    DescribeInstanceTypesResultTypeDef,
    DescribeInternetGatewaysResultTypeDef,
    DescribeIpamPoolsResultTypeDef,
    DescribeIpamResourceDiscoveriesResultTypeDef,
    DescribeIpamResourceDiscoveryAssociationsResultTypeDef,
    DescribeIpamScopesResultTypeDef,
    DescribeIpamsResultTypeDef,
    DescribeIpv6PoolsResultTypeDef,
    DescribeLaunchTemplatesResultTypeDef,
    DescribeLaunchTemplateVersionsResultTypeDef,
    DescribeLocalGatewayRouteTablesResultTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef,
    DescribeLocalGatewaysResultTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef,
    DescribeLocalGatewayVirtualInterfacesResultTypeDef,
    DescribeManagedPrefixListsResultTypeDef,
    DescribeMovingAddressesResultTypeDef,
    DescribeNatGatewaysResultTypeDef,
    DescribeNetworkAclsResultTypeDef,
    DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef,
    DescribeNetworkInsightsAccessScopesResultTypeDef,
    DescribeNetworkInsightsAnalysesResultTypeDef,
    DescribeNetworkInsightsPathsResultTypeDef,
    DescribeNetworkInterfacePermissionsResultTypeDef,
    DescribeNetworkInterfacesResultTypeDef,
    DescribePrefixListsResultTypeDef,
    DescribePrincipalIdFormatResultTypeDef,
    DescribePublicIpv4PoolsResultTypeDef,
    DescribeReplaceRootVolumeTasksResultTypeDef,
    DescribeReservedInstancesModificationsResultTypeDef,
    DescribeReservedInstancesOfferingsResultTypeDef,
    DescribeRouteTablesResultTypeDef,
    DescribeScheduledInstanceAvailabilityResultTypeDef,
    DescribeScheduledInstancesResultTypeDef,
    DescribeSecurityGroupRulesResultTypeDef,
    DescribeSecurityGroupsResultTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeSnapshotTierStatusResultTypeDef,
    DescribeSpotFleetInstancesResponseTypeDef,
    DescribeSpotFleetRequestsResponseTypeDef,
    DescribeSpotInstanceRequestsResultTypeDef,
    DescribeSpotPriceHistoryResultTypeDef,
    DescribeStaleSecurityGroupsResultTypeDef,
    DescribeStoreImageTasksResultTypeDef,
    DescribeSubnetsResultTypeDef,
    DescribeTagsResultTypeDef,
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
    DescribeVolumesModificationsResultTypeDef,
    DescribeVolumesResultTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcClassicLinkDnsSupportResultTypeDef,
    DescribeVpcEndpointConnectionNotificationsResultTypeDef,
    DescribeVpcEndpointConnectionsResultTypeDef,
    DescribeVpcEndpointServiceConfigurationsResultTypeDef,
    DescribeVpcEndpointServicePermissionsResultTypeDef,
    DescribeVpcEndpointServicesResultTypeDef,
    DescribeVpcEndpointsResultTypeDef,
    DescribeVpcPeeringConnectionsResultTypeDef,
    DescribeVpcsResultTypeDef,
    FilterTypeDef,
    GetAssociatedIpv6PoolCidrsResultTypeDef,
    GetAwsNetworkPerformanceDataResultTypeDef,
    GetGroupsForCapacityReservationResultTypeDef,
    GetInstanceTypesFromInstanceRequirementsResultTypeDef,
    GetIpamAddressHistoryResultTypeDef,
    GetIpamDiscoveredAccountsResultTypeDef,
    GetIpamDiscoveredResourceCidrsResultTypeDef,
    GetIpamPoolAllocationsResultTypeDef,
    GetIpamPoolCidrsResultTypeDef,
    GetIpamResourceCidrsResultTypeDef,
    GetManagedPrefixListAssociationsResultTypeDef,
    GetManagedPrefixListEntriesResultTypeDef,
    GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef,
    GetSecurityGroupsForVpcResultTypeDef,
    GetSpotPlacementScoresResultTypeDef,
    GetTransitGatewayAttachmentPropagationsResultTypeDef,
    GetTransitGatewayMulticastDomainAssociationsResultTypeDef,
    GetTransitGatewayPolicyTableAssociationsResultTypeDef,
    GetTransitGatewayPrefixListReferencesResultTypeDef,
    GetTransitGatewayRouteTableAssociationsResultTypeDef,
    GetTransitGatewayRouteTablePropagationsResultTypeDef,
    GetVpnConnectionDeviceTypesResultTypeDef,
    InstanceRequirementsRequestTypeDef,
    InstanceRequirementsWithMetadataRequestTypeDef,
    ListImagesInRecycleBinResultTypeDef,
    ListSnapshotsInRecycleBinResultTypeDef,
    PaginatorConfigTypeDef,
    RequestIpamResourceTagTypeDef,
    ScheduledInstanceRecurrenceRequestTypeDef,
    SearchLocalGatewayRoutesResultTypeDef,
    SearchTransitGatewayMulticastGroupsResultTypeDef,
    SlotDateTimeRangeRequestTypeDef,
    SlotStartTimeRangeRequestTypeDef,
)

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

__all__ = (
    "DescribeAddressTransfersPaginator",
    "DescribeAddressesAttributePaginator",
    "DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator",
    "DescribeByoipCidrsPaginator",
    "DescribeCapacityBlockOfferingsPaginator",
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
    "DescribeRouteTablesPaginator",
    "DescribeScheduledInstanceAvailabilityPaginator",
    "DescribeScheduledInstancesPaginator",
    "DescribeSecurityGroupRulesPaginator",
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
    "DescribeVolumesPaginator",
    "DescribeVolumesModificationsPaginator",
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

class DescribeAddressTransfersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeAddressTransfers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeaddresstransferspaginator)
    """

    def paginate(
        self,
        *,
        AllocationIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAddressTransfersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeAddressTransfers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeaddresstransferspaginator)
        """

class DescribeAddressesAttributePaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeAddressesAttribute)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeaddressesattributepaginator)
    """

    def paginate(
        self,
        *,
        AllocationIds: List[str] = None,
        Attribute: Literal["domain-name"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAddressesAttributeResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeAddressesAttribute.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeaddressesattributepaginator)
        """

class DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeAwsNetworkPerformanceMetricSubscriptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeawsnetworkperformancemetricsubscriptionspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeAwsNetworkPerformanceMetricSubscriptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeawsnetworkperformancemetricsubscriptionspaginator)
        """

class DescribeByoipCidrsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describebyoipcidrspaginator)
    """

    def paginate(
        self, *, DryRun: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeByoipCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeByoipCidrs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describebyoipcidrspaginator)
        """

class DescribeCapacityBlockOfferingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCapacityBlockOfferings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityblockofferingspaginator)
    """

    def paginate(
        self,
        *,
        InstanceType: str,
        InstanceCount: int,
        CapacityDurationHours: int,
        DryRun: bool = None,
        StartDateRange: Union[datetime, str] = None,
        EndDateRange: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCapacityBlockOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCapacityBlockOfferings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityblockofferingspaginator)
        """

class DescribeCapacityReservationFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservationFleets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityreservationfleetspaginator)
    """

    def paginate(
        self,
        *,
        CapacityReservationFleetIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCapacityReservationFleetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservationFleets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityreservationfleetspaginator)
        """

class DescribeCapacityReservationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityreservationspaginator)
    """

    def paginate(
        self,
        *,
        CapacityReservationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCapacityReservationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCapacityReservations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecapacityreservationspaginator)
        """

class DescribeCarrierGatewaysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCarrierGateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecarriergatewayspaginator)
    """

    def paginate(
        self,
        *,
        CarrierGatewayIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCarrierGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCarrierGateways.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecarriergatewayspaginator)
        """

class DescribeClassicLinkInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclassiclinkinstancespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClassicLinkInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClassicLinkInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclassiclinkinstancespaginator)
        """

class DescribeClientVpnAuthorizationRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnauthorizationrulespaginator)
    """

    def paginate(
        self,
        *,
        ClientVpnEndpointId: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnAuthorizationRulesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnAuthorizationRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnauthorizationrulespaginator)
        """

class DescribeClientVpnConnectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnconnectionspaginator)
    """

    def paginate(
        self,
        *,
        ClientVpnEndpointId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnConnectionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnConnections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnconnectionspaginator)
        """

class DescribeClientVpnEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnendpointspaginator)
    """

    def paginate(
        self,
        *,
        ClientVpnEndpointIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnendpointspaginator)
        """

class DescribeClientVpnRoutesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnroutespaginator)
    """

    def paginate(
        self,
        *,
        ClientVpnEndpointId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnRoutesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnRoutes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpnroutespaginator)
        """

class DescribeClientVpnTargetNetworksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpntargetnetworkspaginator)
    """

    def paginate(
        self,
        *,
        ClientVpnEndpointId: str,
        AssociationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeClientVpnTargetNetworksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeClientVpnTargetNetworks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeclientvpntargetnetworkspaginator)
        """

class DescribeCoipPoolsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCoipPools)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecoippoolspaginator)
    """

    def paginate(
        self,
        *,
        PoolIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeCoipPoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeCoipPools.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describecoippoolspaginator)
        """

class DescribeDhcpOptionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describedhcpoptionspaginator)
    """

    def paginate(
        self,
        *,
        DhcpOptionsIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeDhcpOptionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeDhcpOptions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describedhcpoptionspaginator)
        """

class DescribeEgressOnlyInternetGatewaysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeegressonlyinternetgatewayspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        EgressOnlyInternetGatewayIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeEgressOnlyInternetGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeEgressOnlyInternetGateways.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeegressonlyinternetgatewayspaginator)
        """

class DescribeExportImageTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeexportimagetaskspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        ExportImageTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeExportImageTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeExportImageTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeexportimagetaskspaginator)
        """

class DescribeFastLaunchImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFastLaunchImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefastlaunchimagespaginator)
    """

    def paginate(
        self,
        *,
        ImageIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFastLaunchImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFastLaunchImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefastlaunchimagespaginator)
        """

class DescribeFastSnapshotRestoresPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefastsnapshotrestorespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFastSnapshotRestoresResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFastSnapshotRestores.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefastsnapshotrestorespaginator)
        """

class DescribeFleetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFleets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefleetspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        FleetIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFleetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFleets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefleetspaginator)
        """

class DescribeFlowLogsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeflowlogspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        FlowLogIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFlowLogsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFlowLogs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeflowlogspaginator)
        """

class DescribeFpgaImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefpgaimagespaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        FpgaImageIds: List[str] = None,
        Owners: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeFpgaImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeFpgaImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describefpgaimagespaginator)
        """

class DescribeHostReservationOfferingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostreservationofferingspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        MaxDuration: int = None,
        MinDuration: int = None,
        OfferingId: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeHostReservationOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeHostReservationOfferings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostreservationofferingspaginator)
        """

class DescribeHostReservationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostreservationspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        HostReservationIdSet: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeHostReservationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeHostReservations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostreservationspaginator)
        """

class DescribeHostsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeHosts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        HostIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeHostsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeHosts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describehostspaginator)
        """

class DescribeIamInstanceProfileAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeiaminstanceprofileassociationspaginator)
    """

    def paginate(
        self,
        *,
        AssociationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIamInstanceProfileAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIamInstanceProfileAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeiaminstanceprofileassociationspaginator)
        """

class DescribeImagesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeImages)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimagespaginator)
    """

    def paginate(
        self,
        *,
        ExecutableUsers: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        ImageIds: List[str] = None,
        Owners: List[str] = None,
        IncludeDeprecated: bool = None,
        IncludeDisabled: bool = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImagesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeImages.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimagespaginator)
        """

class DescribeImportImageTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimportimagetaskspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImportImageTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeImportImageTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimportimagetaskspaginator)
        """

class DescribeImportSnapshotTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimportsnapshottaskspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        ImportTaskIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeImportSnapshotTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeImportSnapshotTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeimportsnapshottaskspaginator)
        """

class DescribeInstanceConnectEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceConnectEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstanceconnectendpointspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        InstanceConnectEndpointIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceConnectEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceConnectEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstanceconnectendpointspaginator)
        """

class DescribeInstanceCreditSpecificationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancecreditspecificationspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        InstanceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceCreditSpecificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceCreditSpecifications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancecreditspecificationspaginator)
        """

class DescribeInstanceEventWindowsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceEventWindows)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstanceeventwindowspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        InstanceEventWindowIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceEventWindowsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceEventWindows.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstanceeventwindowspaginator)
        """

class DescribeInstanceStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancestatuspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        IncludeAllInstances: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancestatuspaginator)
        """

class DescribeInstanceTopologyPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTopology)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetopologypaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        InstanceIds: List[str] = None,
        GroupNames: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceTopologyResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTopology.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetopologypaginator)
        """

class DescribeInstanceTypeOfferingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypeOfferings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetypeofferingspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        LocationType: LocationTypeType = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceTypeOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypeOfferings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetypeofferingspaginator)
        """

class DescribeInstanceTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetypespaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        InstanceTypes: List[InstanceTypeType] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstanceTypesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstanceTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancetypespaginator)
        """

class DescribeInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        InstanceIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinstancespaginator)
        """

class DescribeInternetGatewaysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinternetgatewayspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        InternetGatewayIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeInternetGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeInternetGateways.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeinternetgatewayspaginator)
        """

class DescribeIpamPoolsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpamPools)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipampoolspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        IpamPoolIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpamPoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpamPools.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipampoolspaginator)
        """

class DescribeIpamResourceDiscoveriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpamResourceDiscoveries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamresourcediscoveriespaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        IpamResourceDiscoveryIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpamResourceDiscoveriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpamResourceDiscoveries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamresourcediscoveriespaginator)
        """

class DescribeIpamResourceDiscoveryAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpamResourceDiscoveryAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamresourcediscoveryassociationspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        IpamResourceDiscoveryAssociationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpamResourceDiscoveryAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpamResourceDiscoveryAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamresourcediscoveryassociationspaginator)
        """

class DescribeIpamScopesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpamScopes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamscopespaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        IpamScopeIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpamScopesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpamScopes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamscopespaginator)
        """

class DescribeIpamsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpams)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        IpamIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpamsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpams.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipamspaginator)
        """

class DescribeIpv6PoolsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpv6Pools)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipv6poolspaginator)
    """

    def paginate(
        self,
        *,
        PoolIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeIpv6PoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeIpv6Pools.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeipv6poolspaginator)
        """

class DescribeLaunchTemplateVersionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelaunchtemplateversionspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        LaunchTemplateId: str = None,
        LaunchTemplateName: str = None,
        Versions: List[str] = None,
        MinVersion: str = None,
        MaxVersion: str = None,
        Filters: List["FilterTypeDef"] = None,
        ResolveAlias: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLaunchTemplateVersionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplateVersions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelaunchtemplateversionspaginator)
        """

class DescribeLaunchTemplatesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelaunchtemplatespaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        LaunchTemplateIds: List[str] = None,
        LaunchTemplateNames: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLaunchTemplatesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLaunchTemplates.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelaunchtemplatespaginator)
        """

class DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablevirtualinterfacegroupassociationspaginator)
    """

    def paginate(
        self,
        *,
        LocalGatewayRouteTableVirtualInterfaceGroupAssociationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablevirtualinterfacegroupassociationspaginator)
        """

class DescribeLocalGatewayRouteTableVpcAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablevpcassociationspaginator)
    """

    def paginate(
        self,
        *,
        LocalGatewayRouteTableVpcAssociationIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTableVpcAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablevpcassociationspaginator)
        """

class DescribeLocalGatewayRouteTablesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablespaginator)
    """

    def paginate(
        self,
        *,
        LocalGatewayRouteTableIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayRouteTablesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayRouteTables.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayroutetablespaginator)
        """

class DescribeLocalGatewayVirtualInterfaceGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayvirtualinterfacegroupspaginator)
    """

    def paginate(
        self,
        *,
        LocalGatewayVirtualInterfaceGroupIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaceGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayvirtualinterfacegroupspaginator)
        """

class DescribeLocalGatewayVirtualInterfacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayvirtualinterfacespaginator)
    """

    def paginate(
        self,
        *,
        LocalGatewayVirtualInterfaceIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewayVirtualInterfacesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGatewayVirtualInterfaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayvirtualinterfacespaginator)
        """

class DescribeLocalGatewaysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayspaginator)
    """

    def paginate(
        self,
        *,
        LocalGatewayIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeLocalGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeLocalGateways.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describelocalgatewayspaginator)
        """

class DescribeManagedPrefixListsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeManagedPrefixLists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describemanagedprefixlistspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PrefixListIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeManagedPrefixListsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeManagedPrefixLists.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describemanagedprefixlistspaginator)
        """

class DescribeMovingAddressesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describemovingaddressespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PublicIps: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeMovingAddressesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeMovingAddresses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describemovingaddressespaginator)
        """

class DescribeNatGatewaysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenatgatewayspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        NatGatewayIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNatGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNatGateways.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenatgatewayspaginator)
        """

class DescribeNetworkAclsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkaclspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        NetworkAclIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkAclsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkAcls.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkaclspaginator)
        """

class DescribeNetworkInsightsAccessScopeAnalysesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAccessScopeAnalyses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsaccessscopeanalysespaginator)
    """

    def paginate(
        self,
        *,
        NetworkInsightsAccessScopeAnalysisIds: List[str] = None,
        NetworkInsightsAccessScopeId: str = None,
        AnalysisStartTimeBegin: Union[datetime, str] = None,
        AnalysisStartTimeEnd: Union[datetime, str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAccessScopeAnalyses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsaccessscopeanalysespaginator)
        """

class DescribeNetworkInsightsAccessScopesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAccessScopes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsaccessscopespaginator)
    """

    def paginate(
        self,
        *,
        NetworkInsightsAccessScopeIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInsightsAccessScopesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAccessScopes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsaccessscopespaginator)
        """

class DescribeNetworkInsightsAnalysesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAnalyses)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsanalysespaginator)
    """

    def paginate(
        self,
        *,
        NetworkInsightsAnalysisIds: List[str] = None,
        NetworkInsightsPathId: str = None,
        AnalysisStartTime: Union[datetime, str] = None,
        AnalysisEndTime: Union[datetime, str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInsightsAnalysesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsAnalyses.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightsanalysespaginator)
        """

class DescribeNetworkInsightsPathsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsPaths)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightspathspaginator)
    """

    def paginate(
        self,
        *,
        NetworkInsightsPathIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInsightsPathsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInsightsPaths.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinsightspathspaginator)
        """

class DescribeNetworkInterfacePermissionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinterfacepermissionspaginator)
    """

    def paginate(
        self,
        *,
        NetworkInterfacePermissionIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInterfacePermissionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfacePermissions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinterfacepermissionspaginator)
        """

class DescribeNetworkInterfacesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinterfacespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        NetworkInterfaceIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeNetworkInterfacesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeNetworkInterfaces.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describenetworkinterfacespaginator)
        """

class DescribePrefixListsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeprefixlistspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PrefixListIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePrefixListsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribePrefixLists.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeprefixlistspaginator)
        """

class DescribePrincipalIdFormatPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeprincipalidformatpaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Resources: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePrincipalIdFormatResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribePrincipalIdFormat.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeprincipalidformatpaginator)
        """

class DescribePublicIpv4PoolsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describepublicipv4poolspaginator)
    """

    def paginate(
        self,
        *,
        PoolIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribePublicIpv4PoolsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribePublicIpv4Pools.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describepublicipv4poolspaginator)
        """

class DescribeReplaceRootVolumeTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeReplaceRootVolumeTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereplacerootvolumetaskspaginator)
    """

    def paginate(
        self,
        *,
        ReplaceRootVolumeTaskIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReplaceRootVolumeTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeReplaceRootVolumeTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereplacerootvolumetaskspaginator)
        """

class DescribeReservedInstancesModificationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereservedinstancesmodificationspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        ReservedInstancesModificationIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReservedInstancesModificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesModifications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereservedinstancesmodificationspaginator)
        """

class DescribeReservedInstancesOfferingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereservedinstancesofferingspaginator)
    """

    def paginate(
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
        OfferingType: OfferingTypeValuesType = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeReservedInstancesOfferingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeReservedInstancesOfferings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describereservedinstancesofferingspaginator)
        """

class DescribeRouteTablesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeroutetablespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        RouteTableIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeRouteTablesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeRouteTables.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeroutetablespaginator)
        """

class DescribeScheduledInstanceAvailabilityPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describescheduledinstanceavailabilitypaginator)
    """

    def paginate(
        self,
        *,
        FirstSlotStartTimeRange: "SlotDateTimeRangeRequestTypeDef",
        Recurrence: "ScheduledInstanceRecurrenceRequestTypeDef",
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        MaxSlotDurationInHours: int = None,
        MinSlotDurationInHours: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScheduledInstanceAvailabilityResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstanceAvailability.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describescheduledinstanceavailabilitypaginator)
        """

class DescribeScheduledInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describescheduledinstancespaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        ScheduledInstanceIds: List[str] = None,
        SlotStartTimeRange: "SlotStartTimeRangeRequestTypeDef" = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeScheduledInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeScheduledInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describescheduledinstancespaginator)
        """

class DescribeSecurityGroupRulesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroupRules)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesecuritygrouprulespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        SecurityGroupRuleIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSecurityGroupRulesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroupRules.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesecuritygrouprulespaginator)
        """

class DescribeSecurityGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesecuritygroupspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        GroupIds: List[str] = None,
        GroupNames: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSecurityGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSecurityGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesecuritygroupspaginator)
        """

class DescribeSnapshotTierStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSnapshotTierStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesnapshottierstatuspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSnapshotTierStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSnapshotTierStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesnapshottierstatuspaginator)
        """

class DescribeSnapshotsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesnapshotspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        OwnerIds: List[str] = None,
        RestorableByUserIds: List[str] = None,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSnapshotsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSnapshots.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesnapshotspaginator)
        """

class DescribeSpotFleetInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotfleetinstancespaginator)
    """

    def paginate(
        self,
        *,
        SpotFleetRequestId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSpotFleetInstancesResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotfleetinstancespaginator)
        """

class DescribeSpotFleetRequestsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotfleetrequestspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        SpotFleetRequestIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSpotFleetRequestsResponseTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSpotFleetRequests.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotfleetrequestspaginator)
        """

class DescribeSpotInstanceRequestsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotinstancerequestspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        SpotInstanceRequestIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSpotInstanceRequestsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSpotInstanceRequests.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotinstancerequestspaginator)
        """

class DescribeSpotPriceHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotpricehistorypaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        AvailabilityZone: str = None,
        DryRun: bool = None,
        EndTime: Union[datetime, str] = None,
        InstanceTypes: List[InstanceTypeType] = None,
        ProductDescriptions: List[str] = None,
        StartTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSpotPriceHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSpotPriceHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describespotpricehistorypaginator)
        """

class DescribeStaleSecurityGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describestalesecuritygroupspaginator)
    """

    def paginate(
        self, *, VpcId: str, DryRun: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStaleSecurityGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeStaleSecurityGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describestalesecuritygroupspaginator)
        """

class DescribeStoreImageTasksPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeStoreImageTasks)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describestoreimagetaskspaginator)
    """

    def paginate(
        self,
        *,
        ImageIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeStoreImageTasksResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeStoreImageTasks.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describestoreimagetaskspaginator)
        """

class DescribeSubnetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSubnets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesubnetspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        SubnetIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeSubnetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeSubnets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describesubnetspaginator)
        """

class DescribeTagsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTags)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetagspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTagsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTags.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetagspaginator)
        """

class DescribeTrafficMirrorFiltersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrorfilterspaginator)
    """

    def paginate(
        self,
        *,
        TrafficMirrorFilterIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTrafficMirrorFiltersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorFilters.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrorfilterspaginator)
        """

class DescribeTrafficMirrorSessionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrorsessionspaginator)
    """

    def paginate(
        self,
        *,
        TrafficMirrorSessionIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTrafficMirrorSessionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorSessions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrorsessionspaginator)
        """

class DescribeTrafficMirrorTargetsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrortargetspaginator)
    """

    def paginate(
        self,
        *,
        TrafficMirrorTargetIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTrafficMirrorTargetsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTrafficMirrorTargets.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrafficmirrortargetspaginator)
        """

class DescribeTransitGatewayAttachmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayattachmentspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayAttachmentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayAttachments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayattachmentspaginator)
        """

class DescribeTransitGatewayConnectPeersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnectPeers)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayconnectpeerspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayConnectPeerIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayConnectPeersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnectPeers.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayconnectpeerspaginator)
        """

class DescribeTransitGatewayConnectsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnects)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayconnectspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayConnectsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayConnects.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayconnectspaginator)
        """

class DescribeTransitGatewayMulticastDomainsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayMulticastDomains)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaymulticastdomainspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayMulticastDomainIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayMulticastDomainsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayMulticastDomains.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaymulticastdomainspaginator)
        """

class DescribeTransitGatewayPeeringAttachmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPeeringAttachments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaypeeringattachmentspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayPeeringAttachmentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPeeringAttachments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaypeeringattachmentspaginator)
        """

class DescribeTransitGatewayPolicyTablesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPolicyTables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaypolicytablespaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayPolicyTableIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayPolicyTablesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayPolicyTables.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewaypolicytablespaginator)
        """

class DescribeTransitGatewayRouteTableAnnouncementsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTableAnnouncements)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayroutetableannouncementspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayRouteTableAnnouncementIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTableAnnouncements.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayroutetableannouncementspaginator)
        """

class DescribeTransitGatewayRouteTablesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayroutetablespaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayRouteTableIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayRouteTablesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayRouteTables.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayroutetablespaginator)
        """

class DescribeTransitGatewayVpcAttachmentsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayvpcattachmentspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayAttachmentIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewayVpcAttachmentsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGatewayVpcAttachments.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayvpcattachmentspaginator)
        """

class DescribeTransitGatewaysPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTransitGatewaysResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTransitGateways.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetransitgatewayspaginator)
        """

class DescribeTrunkInterfaceAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTrunkInterfaceAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrunkinterfaceassociationspaginator)
    """

    def paginate(
        self,
        *,
        AssociationIds: List[str] = None,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeTrunkInterfaceAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeTrunkInterfaceAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describetrunkinterfaceassociationspaginator)
        """

class DescribeVerifiedAccessEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessendpointspaginator)
    """

    def paginate(
        self,
        *,
        VerifiedAccessEndpointIds: List[str] = None,
        VerifiedAccessInstanceId: str = None,
        VerifiedAccessGroupId: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVerifiedAccessEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessendpointspaginator)
        """

class DescribeVerifiedAccessGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessgroupspaginator)
    """

    def paginate(
        self,
        *,
        VerifiedAccessGroupIds: List[str] = None,
        VerifiedAccessInstanceId: str = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVerifiedAccessGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessgroupspaginator)
        """

class DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessInstanceLoggingConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessinstanceloggingconfigurationspaginator)
    """

    def paginate(
        self,
        *,
        VerifiedAccessInstanceIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessInstanceLoggingConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessinstanceloggingconfigurationspaginator)
        """

class DescribeVerifiedAccessInstancesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessInstances)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessinstancespaginator)
    """

    def paginate(
        self,
        *,
        VerifiedAccessInstanceIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVerifiedAccessInstancesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessInstances.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccessinstancespaginator)
        """

class DescribeVerifiedAccessTrustProvidersPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessTrustProviders)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccesstrustproviderspaginator)
    """

    def paginate(
        self,
        *,
        VerifiedAccessTrustProviderIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVerifiedAccessTrustProvidersResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVerifiedAccessTrustProviders.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describeverifiedaccesstrustproviderspaginator)
        """

class DescribeVolumeStatusPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumestatuspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVolumeStatusResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVolumeStatus.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumestatuspaginator)
        """

class DescribeVolumesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVolumes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumespaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        VolumeIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVolumesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVolumes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumespaginator)
        """

class DescribeVolumesModificationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumesmodificationspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        VolumeIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVolumesModificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVolumesModifications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevolumesmodificationspaginator)
        """

class DescribeVpcClassicLinkDnsSupportPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcclassiclinkdnssupportpaginator)
    """

    def paginate(
        self, *, VpcIds: List[str] = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcClassicLinkDnsSupportResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcClassicLinkDnsSupport.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcclassiclinkdnssupportpaginator)
        """

class DescribeVpcEndpointConnectionNotificationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointconnectionnotificationspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        ConnectionNotificationId: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointConnectionNotificationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnectionNotifications.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointconnectionnotificationspaginator)
        """

class DescribeVpcEndpointConnectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointconnectionspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointConnectionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointConnections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointconnectionspaginator)
        """

class DescribeVpcEndpointServiceConfigurationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointserviceconfigurationspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        ServiceIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointServiceConfigurationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServiceConfigurations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointserviceconfigurationspaginator)
        """

class DescribeVpcEndpointServicePermissionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointservicepermissionspaginator)
    """

    def paginate(
        self,
        *,
        ServiceId: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointServicePermissionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServicePermissions.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointservicepermissionspaginator)
        """

class DescribeVpcEndpointServicesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointservicespaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        ServiceNames: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointServicesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpointServices.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointservicespaginator)
        """

class DescribeVpcEndpointsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointspaginator)
    """

    def paginate(
        self,
        *,
        DryRun: bool = None,
        VpcEndpointIds: List[str] = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcEndpointsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcEndpoints.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcendpointspaginator)
        """

class DescribeVpcPeeringConnectionsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcpeeringconnectionspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        VpcPeeringConnectionIds: List[str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcPeeringConnectionsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcPeeringConnections.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcpeeringconnectionspaginator)
        """

class DescribeVpcsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcspaginator)
    """

    def paginate(
        self,
        *,
        Filters: List["FilterTypeDef"] = None,
        VpcIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[DescribeVpcsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.DescribeVpcs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#describevpcspaginator)
        """

class GetAssociatedIpv6PoolCidrsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getassociatedipv6poolcidrspaginator)
    """

    def paginate(
        self, *, PoolId: str, DryRun: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAssociatedIpv6PoolCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetAssociatedIpv6PoolCidrs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getassociatedipv6poolcidrspaginator)
        """

class GetAwsNetworkPerformanceDataPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetAwsNetworkPerformanceData)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getawsnetworkperformancedatapaginator)
    """

    def paginate(
        self,
        *,
        DataQueries: List["DataQueryTypeDef"] = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetAwsNetworkPerformanceDataResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetAwsNetworkPerformanceData.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getawsnetworkperformancedatapaginator)
        """

class GetGroupsForCapacityReservationPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetGroupsForCapacityReservation)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getgroupsforcapacityreservationpaginator)
    """

    def paginate(
        self,
        *,
        CapacityReservationId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetGroupsForCapacityReservationResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetGroupsForCapacityReservation.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getgroupsforcapacityreservationpaginator)
        """

class GetInstanceTypesFromInstanceRequirementsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetInstanceTypesFromInstanceRequirements)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getinstancetypesfrominstancerequirementspaginator)
    """

    def paginate(
        self,
        *,
        ArchitectureTypes: List[ArchitectureTypeType],
        VirtualizationTypes: List[VirtualizationTypeType],
        InstanceRequirements: "InstanceRequirementsRequestTypeDef",
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetInstanceTypesFromInstanceRequirementsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetInstanceTypesFromInstanceRequirements.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getinstancetypesfrominstancerequirementspaginator)
        """

class GetIpamAddressHistoryPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamAddressHistory)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamaddresshistorypaginator)
    """

    def paginate(
        self,
        *,
        Cidr: str,
        IpamScopeId: str,
        DryRun: bool = None,
        VpcId: str = None,
        StartTime: Union[datetime, str] = None,
        EndTime: Union[datetime, str] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIpamAddressHistoryResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamAddressHistory.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamaddresshistorypaginator)
        """

class GetIpamDiscoveredAccountsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamDiscoveredAccounts)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamdiscoveredaccountspaginator)
    """

    def paginate(
        self,
        *,
        IpamResourceDiscoveryId: str,
        DiscoveryRegion: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIpamDiscoveredAccountsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamDiscoveredAccounts.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamdiscoveredaccountspaginator)
        """

class GetIpamDiscoveredResourceCidrsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamDiscoveredResourceCidrs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamdiscoveredresourcecidrspaginator)
    """

    def paginate(
        self,
        *,
        IpamResourceDiscoveryId: str,
        ResourceRegion: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIpamDiscoveredResourceCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamDiscoveredResourceCidrs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamdiscoveredresourcecidrspaginator)
        """

class GetIpamPoolAllocationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamPoolAllocations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipampoolallocationspaginator)
    """

    def paginate(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = None,
        IpamPoolAllocationId: str = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIpamPoolAllocationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamPoolAllocations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipampoolallocationspaginator)
        """

class GetIpamPoolCidrsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamPoolCidrs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipampoolcidrspaginator)
    """

    def paginate(
        self,
        *,
        IpamPoolId: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIpamPoolCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamPoolCidrs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipampoolcidrspaginator)
        """

class GetIpamResourceCidrsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamResourceCidrs)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamresourcecidrspaginator)
    """

    def paginate(
        self,
        *,
        IpamScopeId: str,
        DryRun: bool = None,
        Filters: List["FilterTypeDef"] = None,
        IpamPoolId: str = None,
        ResourceId: str = None,
        ResourceType: IpamResourceTypeType = None,
        ResourceTag: "RequestIpamResourceTagTypeDef" = None,
        ResourceOwner: str = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetIpamResourceCidrsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetIpamResourceCidrs.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getipamresourcecidrspaginator)
        """

class GetManagedPrefixListAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getmanagedprefixlistassociationspaginator)
    """

    def paginate(
        self,
        *,
        PrefixListId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetManagedPrefixListAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getmanagedprefixlistassociationspaginator)
        """

class GetManagedPrefixListEntriesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListEntries)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getmanagedprefixlistentriespaginator)
    """

    def paginate(
        self,
        *,
        PrefixListId: str,
        DryRun: bool = None,
        TargetVersion: int = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetManagedPrefixListEntriesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetManagedPrefixListEntries.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getmanagedprefixlistentriespaginator)
        """

class GetNetworkInsightsAccessScopeAnalysisFindingsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetNetworkInsightsAccessScopeAnalysisFindings)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getnetworkinsightsaccessscopeanalysisfindingspaginator)
    """

    def paginate(
        self,
        *,
        NetworkInsightsAccessScopeAnalysisId: str,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetNetworkInsightsAccessScopeAnalysisFindings.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getnetworkinsightsaccessscopeanalysisfindingspaginator)
        """

class GetSecurityGroupsForVpcPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetSecurityGroupsForVpc)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getsecuritygroupsforvpcpaginator)
    """

    def paginate(
        self,
        *,
        VpcId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSecurityGroupsForVpcResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetSecurityGroupsForVpc.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getsecuritygroupsforvpcpaginator)
        """

class GetSpotPlacementScoresPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetSpotPlacementScores)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getspotplacementscorespaginator)
    """

    def paginate(
        self,
        *,
        TargetCapacity: int,
        InstanceTypes: List[str] = None,
        TargetCapacityUnitType: TargetCapacityUnitTypeType = None,
        SingleAvailabilityZone: bool = None,
        RegionNames: List[str] = None,
        InstanceRequirementsWithMetadata: "InstanceRequirementsWithMetadataRequestTypeDef" = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetSpotPlacementScoresResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetSpotPlacementScores.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getspotplacementscorespaginator)
        """

class GetTransitGatewayAttachmentPropagationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayattachmentpropagationspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayAttachmentId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayAttachmentPropagationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayAttachmentPropagations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayattachmentpropagationspaginator)
        """

class GetTransitGatewayMulticastDomainAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayMulticastDomainAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewaymulticastdomainassociationspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayMulticastDomainAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayMulticastDomainAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewaymulticastdomainassociationspaginator)
        """

class GetTransitGatewayPolicyTableAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayPolicyTableAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewaypolicytableassociationspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayPolicyTableId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayPolicyTableAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayPolicyTableAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewaypolicytableassociationspaginator)
        """

class GetTransitGatewayPrefixListReferencesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayPrefixListReferences)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayprefixlistreferencespaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayPrefixListReferencesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayPrefixListReferences.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayprefixlistreferencespaginator)
        """

class GetTransitGatewayRouteTableAssociationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayroutetableassociationspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayRouteTableAssociationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTableAssociations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayroutetableassociationspaginator)
        """

class GetTransitGatewayRouteTablePropagationsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayroutetablepropagationspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayRouteTableId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetTransitGatewayRouteTablePropagationsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetTransitGatewayRouteTablePropagations.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#gettransitgatewayroutetablepropagationspaginator)
        """

class GetVpnConnectionDeviceTypesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetVpnConnectionDeviceTypes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getvpnconnectiondevicetypespaginator)
    """

    def paginate(
        self, *, DryRun: bool = None, PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[GetVpnConnectionDeviceTypesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.GetVpnConnectionDeviceTypes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#getvpnconnectiondevicetypespaginator)
        """

class ListImagesInRecycleBinPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.ListImagesInRecycleBin)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#listimagesinrecyclebinpaginator)
    """

    def paginate(
        self,
        *,
        ImageIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListImagesInRecycleBinResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.ListImagesInRecycleBin.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#listimagesinrecyclebinpaginator)
        """

class ListSnapshotsInRecycleBinPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.ListSnapshotsInRecycleBin)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#listsnapshotsinrecyclebinpaginator)
    """

    def paginate(
        self,
        *,
        SnapshotIds: List[str] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[ListSnapshotsInRecycleBinResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.ListSnapshotsInRecycleBin.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#listsnapshotsinrecyclebinpaginator)
        """

class SearchLocalGatewayRoutesPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.SearchLocalGatewayRoutes)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#searchlocalgatewayroutespaginator)
    """

    def paginate(
        self,
        *,
        LocalGatewayRouteTableId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchLocalGatewayRoutesResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.SearchLocalGatewayRoutes.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#searchlocalgatewayroutespaginator)
        """

class SearchTransitGatewayMulticastGroupsPaginator(Boto3Paginator):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.SearchTransitGatewayMulticastGroups)
    [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#searchtransitgatewaymulticastgroupspaginator)
    """

    def paginate(
        self,
        *,
        TransitGatewayMulticastDomainId: str,
        Filters: List["FilterTypeDef"] = None,
        DryRun: bool = None,
        PaginationConfig: PaginatorConfigTypeDef = None
    ) -> Iterator[SearchTransitGatewayMulticastGroupsResultTypeDef]:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/1.29.7/reference/services/ec2.html#EC2.Paginator.SearchTransitGatewayMulticastGroups.paginate)
        [Show boto3-stubs documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_ec2/paginators.html#searchtransitgatewaymulticastgroupspaginator)
        """
