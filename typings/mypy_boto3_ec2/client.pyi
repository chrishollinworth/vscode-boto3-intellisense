"""
Type annotations for ec2 service Client.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session
    from mypy_boto3_ec2.client import EC2Client

    session = Session()
    client: EC2Client = session.client("ec2")
    ```
"""

from __future__ import annotations

import sys
from typing import Any, overload

from botocore.client import BaseClient, ClientMeta
from botocore.errorfactory import BaseClientExceptions
from botocore.exceptions import ClientError as BotocoreClientError

from .paginator import (
    DescribeAddressesAttributePaginator,
    DescribeAddressTransfersPaginator,
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
    DescribeRouteServerEndpointsPaginator,
    DescribeRouteServerPeersPaginator,
    DescribeRouteServersPaginator,
    DescribeRouteTablesPaginator,
    DescribeScheduledInstanceAvailabilityPaginator,
    DescribeScheduledInstancesPaginator,
    DescribeSecurityGroupRulesPaginator,
    DescribeSecurityGroupsPaginator,
    DescribeSecurityGroupVpcAssociationsPaginator,
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
    AcceptAddressTransferRequestTypeDef,
    AcceptAddressTransferResultTypeDef,
    AcceptCapacityReservationBillingOwnershipRequestTypeDef,
    AcceptCapacityReservationBillingOwnershipResultTypeDef,
    AcceptReservedInstancesExchangeQuoteRequestTypeDef,
    AcceptReservedInstancesExchangeQuoteResultTypeDef,
    AcceptTransitGatewayMulticastDomainAssociationsRequestTypeDef,
    AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef,
    AcceptTransitGatewayPeeringAttachmentRequestTypeDef,
    AcceptTransitGatewayPeeringAttachmentResultTypeDef,
    AcceptTransitGatewayVpcAttachmentRequestTypeDef,
    AcceptTransitGatewayVpcAttachmentResultTypeDef,
    AcceptVpcEndpointConnectionsRequestTypeDef,
    AcceptVpcEndpointConnectionsResultTypeDef,
    AcceptVpcPeeringConnectionRequestTypeDef,
    AcceptVpcPeeringConnectionResultTypeDef,
    AdvertiseByoipCidrRequestTypeDef,
    AdvertiseByoipCidrResultTypeDef,
    AllocateAddressRequestTypeDef,
    AllocateAddressResultTypeDef,
    AllocateHostsRequestTypeDef,
    AllocateHostsResultTypeDef,
    AllocateIpamPoolCidrRequestTypeDef,
    AllocateIpamPoolCidrResultTypeDef,
    ApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef,
    ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef,
    AssignIpv6AddressesRequestTypeDef,
    AssignIpv6AddressesResultTypeDef,
    AssignPrivateIpAddressesRequestTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssignPrivateNatGatewayAddressRequestTypeDef,
    AssignPrivateNatGatewayAddressResultTypeDef,
    AssociateAddressRequestTypeDef,
    AssociateAddressResultTypeDef,
    AssociateCapacityReservationBillingOwnerRequestTypeDef,
    AssociateCapacityReservationBillingOwnerResultTypeDef,
    AssociateClientVpnTargetNetworkRequestTypeDef,
    AssociateClientVpnTargetNetworkResultTypeDef,
    AssociateDhcpOptionsRequestTypeDef,
    AssociateEnclaveCertificateIamRoleRequestTypeDef,
    AssociateEnclaveCertificateIamRoleResultTypeDef,
    AssociateIamInstanceProfileRequestTypeDef,
    AssociateIamInstanceProfileResultTypeDef,
    AssociateInstanceEventWindowRequestTypeDef,
    AssociateInstanceEventWindowResultTypeDef,
    AssociateIpamByoasnRequestTypeDef,
    AssociateIpamByoasnResultTypeDef,
    AssociateIpamResourceDiscoveryRequestTypeDef,
    AssociateIpamResourceDiscoveryResultTypeDef,
    AssociateNatGatewayAddressRequestTypeDef,
    AssociateNatGatewayAddressResultTypeDef,
    AssociateRouteServerRequestTypeDef,
    AssociateRouteServerResultTypeDef,
    AssociateRouteTableRequestTypeDef,
    AssociateRouteTableResultTypeDef,
    AssociateSecurityGroupVpcRequestTypeDef,
    AssociateSecurityGroupVpcResultTypeDef,
    AssociateSubnetCidrBlockRequestTypeDef,
    AssociateSubnetCidrBlockResultTypeDef,
    AssociateTransitGatewayMulticastDomainRequestTypeDef,
    AssociateTransitGatewayMulticastDomainResultTypeDef,
    AssociateTransitGatewayPolicyTableRequestTypeDef,
    AssociateTransitGatewayPolicyTableResultTypeDef,
    AssociateTransitGatewayRouteTableRequestTypeDef,
    AssociateTransitGatewayRouteTableResultTypeDef,
    AssociateTrunkInterfaceRequestTypeDef,
    AssociateTrunkInterfaceResultTypeDef,
    AssociateVpcCidrBlockRequestTypeDef,
    AssociateVpcCidrBlockResultTypeDef,
    AttachClassicLinkVpcRequestTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachInternetGatewayRequestTypeDef,
    AttachNetworkInterfaceRequestTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttachVerifiedAccessTrustProviderRequestTypeDef,
    AttachVerifiedAccessTrustProviderResultTypeDef,
    AttachVolumeRequestTypeDef,
    AttachVpnGatewayRequestTypeDef,
    AttachVpnGatewayResultTypeDef,
    AuthorizeClientVpnIngressRequestTypeDef,
    AuthorizeClientVpnIngressResultTypeDef,
    AuthorizeSecurityGroupEgressRequestTypeDef,
    AuthorizeSecurityGroupEgressResultTypeDef,
    AuthorizeSecurityGroupIngressRequestTypeDef,
    AuthorizeSecurityGroupIngressResultTypeDef,
    BundleInstanceRequestTypeDef,
    BundleInstanceResultTypeDef,
    CancelBundleTaskRequestTypeDef,
    CancelBundleTaskResultTypeDef,
    CancelCapacityReservationFleetsRequestTypeDef,
    CancelCapacityReservationFleetsResultTypeDef,
    CancelCapacityReservationRequestTypeDef,
    CancelCapacityReservationResultTypeDef,
    CancelConversionRequestTypeDef,
    CancelDeclarativePoliciesReportRequestTypeDef,
    CancelDeclarativePoliciesReportResultTypeDef,
    CancelExportTaskRequestTypeDef,
    CancelImageLaunchPermissionRequestTypeDef,
    CancelImageLaunchPermissionResultTypeDef,
    CancelImportTaskRequestTypeDef,
    CancelImportTaskResultTypeDef,
    CancelReservedInstancesListingRequestTypeDef,
    CancelReservedInstancesListingResultTypeDef,
    CancelSpotFleetRequestsRequestTypeDef,
    CancelSpotFleetRequestsResponseTypeDef,
    CancelSpotInstanceRequestsRequestTypeDef,
    CancelSpotInstanceRequestsResultTypeDef,
    ClientCreateTagsRequestTypeDef,
    ClientDeleteTagsRequestTypeDef,
    ConfirmProductInstanceRequestTypeDef,
    ConfirmProductInstanceResultTypeDef,
    CopyFpgaImageRequestTypeDef,
    CopyFpgaImageResultTypeDef,
    CopyImageRequestTypeDef,
    CopyImageResultTypeDef,
    CopySnapshotRequestTypeDef,
    CopySnapshotResultTypeDef,
    CreateCapacityReservationBySplittingRequestTypeDef,
    CreateCapacityReservationBySplittingResultTypeDef,
    CreateCapacityReservationFleetRequestTypeDef,
    CreateCapacityReservationFleetResultTypeDef,
    CreateCapacityReservationRequestTypeDef,
    CreateCapacityReservationResultTypeDef,
    CreateCarrierGatewayRequestTypeDef,
    CreateCarrierGatewayResultTypeDef,
    CreateClientVpnEndpointRequestTypeDef,
    CreateClientVpnEndpointResultTypeDef,
    CreateClientVpnRouteRequestTypeDef,
    CreateClientVpnRouteResultTypeDef,
    CreateCoipCidrRequestTypeDef,
    CreateCoipCidrResultTypeDef,
    CreateCoipPoolRequestTypeDef,
    CreateCoipPoolResultTypeDef,
    CreateCustomerGatewayRequestTypeDef,
    CreateCustomerGatewayResultTypeDef,
    CreateDefaultSubnetRequestTypeDef,
    CreateDefaultSubnetResultTypeDef,
    CreateDefaultVpcRequestTypeDef,
    CreateDefaultVpcResultTypeDef,
    CreateDhcpOptionsRequestTypeDef,
    CreateDhcpOptionsResultTypeDef,
    CreateEgressOnlyInternetGatewayRequestTypeDef,
    CreateEgressOnlyInternetGatewayResultTypeDef,
    CreateFleetRequestTypeDef,
    CreateFleetResultTypeDef,
    CreateFlowLogsRequestTypeDef,
    CreateFlowLogsResultTypeDef,
    CreateFpgaImageRequestTypeDef,
    CreateFpgaImageResultTypeDef,
    CreateImageRequestTypeDef,
    CreateImageResultTypeDef,
    CreateInstanceConnectEndpointRequestTypeDef,
    CreateInstanceConnectEndpointResultTypeDef,
    CreateInstanceEventWindowRequestTypeDef,
    CreateInstanceEventWindowResultTypeDef,
    CreateInstanceExportTaskRequestTypeDef,
    CreateInstanceExportTaskResultTypeDef,
    CreateInternetGatewayRequestTypeDef,
    CreateInternetGatewayResultTypeDef,
    CreateIpamExternalResourceVerificationTokenRequestTypeDef,
    CreateIpamExternalResourceVerificationTokenResultTypeDef,
    CreateIpamPoolRequestTypeDef,
    CreateIpamPoolResultTypeDef,
    CreateIpamRequestTypeDef,
    CreateIpamResourceDiscoveryRequestTypeDef,
    CreateIpamResourceDiscoveryResultTypeDef,
    CreateIpamResultTypeDef,
    CreateIpamScopeRequestTypeDef,
    CreateIpamScopeResultTypeDef,
    CreateKeyPairRequestTypeDef,
    CreateLaunchTemplateRequestTypeDef,
    CreateLaunchTemplateResultTypeDef,
    CreateLaunchTemplateVersionRequestTypeDef,
    CreateLaunchTemplateVersionResultTypeDef,
    CreateLocalGatewayRouteRequestTypeDef,
    CreateLocalGatewayRouteResultTypeDef,
    CreateLocalGatewayRouteTableRequestTypeDef,
    CreateLocalGatewayRouteTableResultTypeDef,
    CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestTypeDef,
    CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef,
    CreateLocalGatewayRouteTableVpcAssociationRequestTypeDef,
    CreateLocalGatewayRouteTableVpcAssociationResultTypeDef,
    CreateLocalGatewayVirtualInterfaceGroupRequestTypeDef,
    CreateLocalGatewayVirtualInterfaceGroupResultTypeDef,
    CreateLocalGatewayVirtualInterfaceRequestTypeDef,
    CreateLocalGatewayVirtualInterfaceResultTypeDef,
    CreateManagedPrefixListRequestTypeDef,
    CreateManagedPrefixListResultTypeDef,
    CreateNatGatewayRequestTypeDef,
    CreateNatGatewayResultTypeDef,
    CreateNetworkAclEntryRequestTypeDef,
    CreateNetworkAclRequestTypeDef,
    CreateNetworkAclResultTypeDef,
    CreateNetworkInsightsAccessScopeRequestTypeDef,
    CreateNetworkInsightsAccessScopeResultTypeDef,
    CreateNetworkInsightsPathRequestTypeDef,
    CreateNetworkInsightsPathResultTypeDef,
    CreateNetworkInterfacePermissionRequestTypeDef,
    CreateNetworkInterfacePermissionResultTypeDef,
    CreateNetworkInterfaceRequestTypeDef,
    CreateNetworkInterfaceResultTypeDef,
    CreatePlacementGroupRequestTypeDef,
    CreatePlacementGroupResultTypeDef,
    CreatePublicIpv4PoolRequestTypeDef,
    CreatePublicIpv4PoolResultTypeDef,
    CreateReplaceRootVolumeTaskRequestTypeDef,
    CreateReplaceRootVolumeTaskResultTypeDef,
    CreateReservedInstancesListingRequestTypeDef,
    CreateReservedInstancesListingResultTypeDef,
    CreateRestoreImageTaskRequestTypeDef,
    CreateRestoreImageTaskResultTypeDef,
    CreateRouteRequestTypeDef,
    CreateRouteResultTypeDef,
    CreateRouteServerEndpointRequestTypeDef,
    CreateRouteServerEndpointResultTypeDef,
    CreateRouteServerPeerRequestTypeDef,
    CreateRouteServerPeerResultTypeDef,
    CreateRouteServerRequestTypeDef,
    CreateRouteServerResultTypeDef,
    CreateRouteTableRequestTypeDef,
    CreateRouteTableResultTypeDef,
    CreateSecurityGroupRequestTypeDef,
    CreateSecurityGroupResultTypeDef,
    CreateSnapshotRequestTypeDef,
    CreateSnapshotsRequestTypeDef,
    CreateSnapshotsResultTypeDef,
    CreateSpotDatafeedSubscriptionRequestTypeDef,
    CreateSpotDatafeedSubscriptionResultTypeDef,
    CreateStoreImageTaskRequestTypeDef,
    CreateStoreImageTaskResultTypeDef,
    CreateSubnetCidrReservationRequestTypeDef,
    CreateSubnetCidrReservationResultTypeDef,
    CreateSubnetRequestTypeDef,
    CreateSubnetResultTypeDef,
    CreateTrafficMirrorFilterRequestTypeDef,
    CreateTrafficMirrorFilterResultTypeDef,
    CreateTrafficMirrorFilterRuleRequestTypeDef,
    CreateTrafficMirrorFilterRuleResultTypeDef,
    CreateTrafficMirrorSessionRequestTypeDef,
    CreateTrafficMirrorSessionResultTypeDef,
    CreateTrafficMirrorTargetRequestTypeDef,
    CreateTrafficMirrorTargetResultTypeDef,
    CreateTransitGatewayConnectPeerRequestTypeDef,
    CreateTransitGatewayConnectPeerResultTypeDef,
    CreateTransitGatewayConnectRequestTypeDef,
    CreateTransitGatewayConnectResultTypeDef,
    CreateTransitGatewayMulticastDomainRequestTypeDef,
    CreateTransitGatewayMulticastDomainResultTypeDef,
    CreateTransitGatewayPeeringAttachmentRequestTypeDef,
    CreateTransitGatewayPeeringAttachmentResultTypeDef,
    CreateTransitGatewayPolicyTableRequestTypeDef,
    CreateTransitGatewayPolicyTableResultTypeDef,
    CreateTransitGatewayPrefixListReferenceRequestTypeDef,
    CreateTransitGatewayPrefixListReferenceResultTypeDef,
    CreateTransitGatewayRequestTypeDef,
    CreateTransitGatewayResultTypeDef,
    CreateTransitGatewayRouteRequestTypeDef,
    CreateTransitGatewayRouteResultTypeDef,
    CreateTransitGatewayRouteTableAnnouncementRequestTypeDef,
    CreateTransitGatewayRouteTableAnnouncementResultTypeDef,
    CreateTransitGatewayRouteTableRequestTypeDef,
    CreateTransitGatewayRouteTableResultTypeDef,
    CreateTransitGatewayVpcAttachmentRequestTypeDef,
    CreateTransitGatewayVpcAttachmentResultTypeDef,
    CreateVerifiedAccessEndpointRequestTypeDef,
    CreateVerifiedAccessEndpointResultTypeDef,
    CreateVerifiedAccessGroupRequestTypeDef,
    CreateVerifiedAccessGroupResultTypeDef,
    CreateVerifiedAccessInstanceRequestTypeDef,
    CreateVerifiedAccessInstanceResultTypeDef,
    CreateVerifiedAccessTrustProviderRequestTypeDef,
    CreateVerifiedAccessTrustProviderResultTypeDef,
    CreateVolumeRequestTypeDef,
    CreateVpcBlockPublicAccessExclusionRequestTypeDef,
    CreateVpcBlockPublicAccessExclusionResultTypeDef,
    CreateVpcEndpointConnectionNotificationRequestTypeDef,
    CreateVpcEndpointConnectionNotificationResultTypeDef,
    CreateVpcEndpointRequestTypeDef,
    CreateVpcEndpointResultTypeDef,
    CreateVpcEndpointServiceConfigurationRequestTypeDef,
    CreateVpcEndpointServiceConfigurationResultTypeDef,
    CreateVpcPeeringConnectionRequestTypeDef,
    CreateVpcPeeringConnectionResultTypeDef,
    CreateVpcRequestTypeDef,
    CreateVpcResultTypeDef,
    CreateVpnConnectionRequestTypeDef,
    CreateVpnConnectionResultTypeDef,
    CreateVpnConnectionRouteRequestTypeDef,
    CreateVpnGatewayRequestTypeDef,
    CreateVpnGatewayResultTypeDef,
    DeleteCarrierGatewayRequestTypeDef,
    DeleteCarrierGatewayResultTypeDef,
    DeleteClientVpnEndpointRequestTypeDef,
    DeleteClientVpnEndpointResultTypeDef,
    DeleteClientVpnRouteRequestTypeDef,
    DeleteClientVpnRouteResultTypeDef,
    DeleteCoipCidrRequestTypeDef,
    DeleteCoipCidrResultTypeDef,
    DeleteCoipPoolRequestTypeDef,
    DeleteCoipPoolResultTypeDef,
    DeleteCustomerGatewayRequestTypeDef,
    DeleteDhcpOptionsRequestTypeDef,
    DeleteEgressOnlyInternetGatewayRequestTypeDef,
    DeleteEgressOnlyInternetGatewayResultTypeDef,
    DeleteFleetsRequestTypeDef,
    DeleteFleetsResultTypeDef,
    DeleteFlowLogsRequestTypeDef,
    DeleteFlowLogsResultTypeDef,
    DeleteFpgaImageRequestTypeDef,
    DeleteFpgaImageResultTypeDef,
    DeleteInstanceConnectEndpointRequestTypeDef,
    DeleteInstanceConnectEndpointResultTypeDef,
    DeleteInstanceEventWindowRequestTypeDef,
    DeleteInstanceEventWindowResultTypeDef,
    DeleteInternetGatewayRequestTypeDef,
    DeleteIpamExternalResourceVerificationTokenRequestTypeDef,
    DeleteIpamExternalResourceVerificationTokenResultTypeDef,
    DeleteIpamPoolRequestTypeDef,
    DeleteIpamPoolResultTypeDef,
    DeleteIpamRequestTypeDef,
    DeleteIpamResourceDiscoveryRequestTypeDef,
    DeleteIpamResourceDiscoveryResultTypeDef,
    DeleteIpamResultTypeDef,
    DeleteIpamScopeRequestTypeDef,
    DeleteIpamScopeResultTypeDef,
    DeleteKeyPairRequestTypeDef,
    DeleteKeyPairResultTypeDef,
    DeleteLaunchTemplateRequestTypeDef,
    DeleteLaunchTemplateResultTypeDef,
    DeleteLaunchTemplateVersionsRequestTypeDef,
    DeleteLaunchTemplateVersionsResultTypeDef,
    DeleteLocalGatewayRouteRequestTypeDef,
    DeleteLocalGatewayRouteResultTypeDef,
    DeleteLocalGatewayRouteTableRequestTypeDef,
    DeleteLocalGatewayRouteTableResultTypeDef,
    DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestTypeDef,
    DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef,
    DeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef,
    DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef,
    DeleteLocalGatewayVirtualInterfaceGroupRequestTypeDef,
    DeleteLocalGatewayVirtualInterfaceGroupResultTypeDef,
    DeleteLocalGatewayVirtualInterfaceRequestTypeDef,
    DeleteLocalGatewayVirtualInterfaceResultTypeDef,
    DeleteManagedPrefixListRequestTypeDef,
    DeleteManagedPrefixListResultTypeDef,
    DeleteNatGatewayRequestTypeDef,
    DeleteNatGatewayResultTypeDef,
    DeleteNetworkAclEntryRequestTypeDef,
    DeleteNetworkAclRequestTypeDef,
    DeleteNetworkInsightsAccessScopeAnalysisRequestTypeDef,
    DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef,
    DeleteNetworkInsightsAccessScopeRequestTypeDef,
    DeleteNetworkInsightsAccessScopeResultTypeDef,
    DeleteNetworkInsightsAnalysisRequestTypeDef,
    DeleteNetworkInsightsAnalysisResultTypeDef,
    DeleteNetworkInsightsPathRequestTypeDef,
    DeleteNetworkInsightsPathResultTypeDef,
    DeleteNetworkInterfacePermissionRequestTypeDef,
    DeleteNetworkInterfacePermissionResultTypeDef,
    DeleteNetworkInterfaceRequestTypeDef,
    DeletePlacementGroupRequestTypeDef,
    DeletePublicIpv4PoolRequestTypeDef,
    DeletePublicIpv4PoolResultTypeDef,
    DeleteQueuedReservedInstancesRequestTypeDef,
    DeleteQueuedReservedInstancesResultTypeDef,
    DeleteRouteRequestTypeDef,
    DeleteRouteServerEndpointRequestTypeDef,
    DeleteRouteServerEndpointResultTypeDef,
    DeleteRouteServerPeerRequestTypeDef,
    DeleteRouteServerPeerResultTypeDef,
    DeleteRouteServerRequestTypeDef,
    DeleteRouteServerResultTypeDef,
    DeleteRouteTableRequestTypeDef,
    DeleteSecurityGroupRequestTypeDef,
    DeleteSecurityGroupResultTypeDef,
    DeleteSnapshotRequestTypeDef,
    DeleteSpotDatafeedSubscriptionRequestTypeDef,
    DeleteSubnetCidrReservationRequestTypeDef,
    DeleteSubnetCidrReservationResultTypeDef,
    DeleteSubnetRequestTypeDef,
    DeleteTrafficMirrorFilterRequestTypeDef,
    DeleteTrafficMirrorFilterResultTypeDef,
    DeleteTrafficMirrorFilterRuleRequestTypeDef,
    DeleteTrafficMirrorFilterRuleResultTypeDef,
    DeleteTrafficMirrorSessionRequestTypeDef,
    DeleteTrafficMirrorSessionResultTypeDef,
    DeleteTrafficMirrorTargetRequestTypeDef,
    DeleteTrafficMirrorTargetResultTypeDef,
    DeleteTransitGatewayConnectPeerRequestTypeDef,
    DeleteTransitGatewayConnectPeerResultTypeDef,
    DeleteTransitGatewayConnectRequestTypeDef,
    DeleteTransitGatewayConnectResultTypeDef,
    DeleteTransitGatewayMulticastDomainRequestTypeDef,
    DeleteTransitGatewayMulticastDomainResultTypeDef,
    DeleteTransitGatewayPeeringAttachmentRequestTypeDef,
    DeleteTransitGatewayPeeringAttachmentResultTypeDef,
    DeleteTransitGatewayPolicyTableRequestTypeDef,
    DeleteTransitGatewayPolicyTableResultTypeDef,
    DeleteTransitGatewayPrefixListReferenceRequestTypeDef,
    DeleteTransitGatewayPrefixListReferenceResultTypeDef,
    DeleteTransitGatewayRequestTypeDef,
    DeleteTransitGatewayResultTypeDef,
    DeleteTransitGatewayRouteRequestTypeDef,
    DeleteTransitGatewayRouteResultTypeDef,
    DeleteTransitGatewayRouteTableAnnouncementRequestTypeDef,
    DeleteTransitGatewayRouteTableAnnouncementResultTypeDef,
    DeleteTransitGatewayRouteTableRequestTypeDef,
    DeleteTransitGatewayRouteTableResultTypeDef,
    DeleteTransitGatewayVpcAttachmentRequestTypeDef,
    DeleteTransitGatewayVpcAttachmentResultTypeDef,
    DeleteVerifiedAccessEndpointRequestTypeDef,
    DeleteVerifiedAccessEndpointResultTypeDef,
    DeleteVerifiedAccessGroupRequestTypeDef,
    DeleteVerifiedAccessGroupResultTypeDef,
    DeleteVerifiedAccessInstanceRequestTypeDef,
    DeleteVerifiedAccessInstanceResultTypeDef,
    DeleteVerifiedAccessTrustProviderRequestTypeDef,
    DeleteVerifiedAccessTrustProviderResultTypeDef,
    DeleteVolumeRequestTypeDef,
    DeleteVpcBlockPublicAccessExclusionRequestTypeDef,
    DeleteVpcBlockPublicAccessExclusionResultTypeDef,
    DeleteVpcEndpointConnectionNotificationsRequestTypeDef,
    DeleteVpcEndpointConnectionNotificationsResultTypeDef,
    DeleteVpcEndpointServiceConfigurationsRequestTypeDef,
    DeleteVpcEndpointServiceConfigurationsResultTypeDef,
    DeleteVpcEndpointsRequestTypeDef,
    DeleteVpcEndpointsResultTypeDef,
    DeleteVpcPeeringConnectionRequestTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DeleteVpcRequestTypeDef,
    DeleteVpnConnectionRequestTypeDef,
    DeleteVpnConnectionRouteRequestTypeDef,
    DeleteVpnGatewayRequestTypeDef,
    DeprovisionByoipCidrRequestTypeDef,
    DeprovisionByoipCidrResultTypeDef,
    DeprovisionIpamByoasnRequestTypeDef,
    DeprovisionIpamByoasnResultTypeDef,
    DeprovisionIpamPoolCidrRequestTypeDef,
    DeprovisionIpamPoolCidrResultTypeDef,
    DeprovisionPublicIpv4PoolCidrRequestTypeDef,
    DeprovisionPublicIpv4PoolCidrResultTypeDef,
    DeregisterImageRequestTypeDef,
    DeregisterInstanceEventNotificationAttributesRequestTypeDef,
    DeregisterInstanceEventNotificationAttributesResultTypeDef,
    DeregisterTransitGatewayMulticastGroupMembersRequestTypeDef,
    DeregisterTransitGatewayMulticastGroupMembersResultTypeDef,
    DeregisterTransitGatewayMulticastGroupSourcesRequestTypeDef,
    DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    DescribeAccountAttributesRequestTypeDef,
    DescribeAccountAttributesResultTypeDef,
    DescribeAddressesAttributeRequestTypeDef,
    DescribeAddressesAttributeResultTypeDef,
    DescribeAddressesRequestTypeDef,
    DescribeAddressesResultTypeDef,
    DescribeAddressTransfersRequestTypeDef,
    DescribeAddressTransfersResultTypeDef,
    DescribeAggregateIdFormatRequestTypeDef,
    DescribeAggregateIdFormatResultTypeDef,
    DescribeAvailabilityZonesRequestTypeDef,
    DescribeAvailabilityZonesResultTypeDef,
    DescribeAwsNetworkPerformanceMetricSubscriptionsRequestTypeDef,
    DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef,
    DescribeBundleTasksRequestTypeDef,
    DescribeBundleTasksResultTypeDef,
    DescribeByoipCidrsRequestTypeDef,
    DescribeByoipCidrsResultTypeDef,
    DescribeCapacityBlockExtensionHistoryRequestTypeDef,
    DescribeCapacityBlockExtensionHistoryResultTypeDef,
    DescribeCapacityBlockExtensionOfferingsRequestTypeDef,
    DescribeCapacityBlockExtensionOfferingsResultTypeDef,
    DescribeCapacityBlockOfferingsRequestTypeDef,
    DescribeCapacityBlockOfferingsResultTypeDef,
    DescribeCapacityReservationBillingRequestsRequestTypeDef,
    DescribeCapacityReservationBillingRequestsResultTypeDef,
    DescribeCapacityReservationFleetsRequestTypeDef,
    DescribeCapacityReservationFleetsResultTypeDef,
    DescribeCapacityReservationsRequestTypeDef,
    DescribeCapacityReservationsResultTypeDef,
    DescribeCarrierGatewaysRequestTypeDef,
    DescribeCarrierGatewaysResultTypeDef,
    DescribeClassicLinkInstancesRequestTypeDef,
    DescribeClassicLinkInstancesResultTypeDef,
    DescribeClientVpnAuthorizationRulesRequestTypeDef,
    DescribeClientVpnAuthorizationRulesResultTypeDef,
    DescribeClientVpnConnectionsRequestTypeDef,
    DescribeClientVpnConnectionsResultTypeDef,
    DescribeClientVpnEndpointsRequestTypeDef,
    DescribeClientVpnEndpointsResultTypeDef,
    DescribeClientVpnRoutesRequestTypeDef,
    DescribeClientVpnRoutesResultTypeDef,
    DescribeClientVpnTargetNetworksRequestTypeDef,
    DescribeClientVpnTargetNetworksResultTypeDef,
    DescribeCoipPoolsRequestTypeDef,
    DescribeCoipPoolsResultTypeDef,
    DescribeConversionTasksRequestTypeDef,
    DescribeConversionTasksResultTypeDef,
    DescribeCustomerGatewaysRequestTypeDef,
    DescribeCustomerGatewaysResultTypeDef,
    DescribeDeclarativePoliciesReportsRequestTypeDef,
    DescribeDeclarativePoliciesReportsResultTypeDef,
    DescribeDhcpOptionsRequestTypeDef,
    DescribeDhcpOptionsResultTypeDef,
    DescribeEgressOnlyInternetGatewaysRequestTypeDef,
    DescribeEgressOnlyInternetGatewaysResultTypeDef,
    DescribeElasticGpusRequestTypeDef,
    DescribeElasticGpusResultTypeDef,
    DescribeExportImageTasksRequestTypeDef,
    DescribeExportImageTasksResultTypeDef,
    DescribeExportTasksRequestTypeDef,
    DescribeExportTasksResultTypeDef,
    DescribeFastLaunchImagesRequestTypeDef,
    DescribeFastLaunchImagesResultTypeDef,
    DescribeFastSnapshotRestoresRequestTypeDef,
    DescribeFastSnapshotRestoresResultTypeDef,
    DescribeFleetHistoryRequestTypeDef,
    DescribeFleetHistoryResultTypeDef,
    DescribeFleetInstancesRequestTypeDef,
    DescribeFleetInstancesResultTypeDef,
    DescribeFleetsRequestTypeDef,
    DescribeFleetsResultTypeDef,
    DescribeFlowLogsRequestTypeDef,
    DescribeFlowLogsResultTypeDef,
    DescribeFpgaImageAttributeRequestTypeDef,
    DescribeFpgaImageAttributeResultTypeDef,
    DescribeFpgaImagesRequestTypeDef,
    DescribeFpgaImagesResultTypeDef,
    DescribeHostReservationOfferingsRequestTypeDef,
    DescribeHostReservationOfferingsResultTypeDef,
    DescribeHostReservationsRequestTypeDef,
    DescribeHostReservationsResultTypeDef,
    DescribeHostsRequestTypeDef,
    DescribeHostsResultTypeDef,
    DescribeIamInstanceProfileAssociationsRequestTypeDef,
    DescribeIamInstanceProfileAssociationsResultTypeDef,
    DescribeIdentityIdFormatRequestTypeDef,
    DescribeIdentityIdFormatResultTypeDef,
    DescribeIdFormatRequestTypeDef,
    DescribeIdFormatResultTypeDef,
    DescribeImageAttributeRequestTypeDef,
    DescribeImagesRequestTypeDef,
    DescribeImagesResultTypeDef,
    DescribeImportImageTasksRequestTypeDef,
    DescribeImportImageTasksResultTypeDef,
    DescribeImportSnapshotTasksRequestTypeDef,
    DescribeImportSnapshotTasksResultTypeDef,
    DescribeInstanceAttributeRequestTypeDef,
    DescribeInstanceConnectEndpointsRequestTypeDef,
    DescribeInstanceConnectEndpointsResultTypeDef,
    DescribeInstanceCreditSpecificationsRequestTypeDef,
    DescribeInstanceCreditSpecificationsResultTypeDef,
    DescribeInstanceEventNotificationAttributesRequestTypeDef,
    DescribeInstanceEventNotificationAttributesResultTypeDef,
    DescribeInstanceEventWindowsRequestTypeDef,
    DescribeInstanceEventWindowsResultTypeDef,
    DescribeInstanceImageMetadataRequestTypeDef,
    DescribeInstanceImageMetadataResultTypeDef,
    DescribeInstancesRequestTypeDef,
    DescribeInstancesResultTypeDef,
    DescribeInstanceStatusRequestTypeDef,
    DescribeInstanceStatusResultTypeDef,
    DescribeInstanceTopologyRequestTypeDef,
    DescribeInstanceTopologyResultTypeDef,
    DescribeInstanceTypeOfferingsRequestTypeDef,
    DescribeInstanceTypeOfferingsResultTypeDef,
    DescribeInstanceTypesRequestTypeDef,
    DescribeInstanceTypesResultTypeDef,
    DescribeInternetGatewaysRequestTypeDef,
    DescribeInternetGatewaysResultTypeDef,
    DescribeIpamByoasnRequestTypeDef,
    DescribeIpamByoasnResultTypeDef,
    DescribeIpamExternalResourceVerificationTokensRequestTypeDef,
    DescribeIpamExternalResourceVerificationTokensResultTypeDef,
    DescribeIpamPoolsRequestTypeDef,
    DescribeIpamPoolsResultTypeDef,
    DescribeIpamResourceDiscoveriesRequestTypeDef,
    DescribeIpamResourceDiscoveriesResultTypeDef,
    DescribeIpamResourceDiscoveryAssociationsRequestTypeDef,
    DescribeIpamResourceDiscoveryAssociationsResultTypeDef,
    DescribeIpamScopesRequestTypeDef,
    DescribeIpamScopesResultTypeDef,
    DescribeIpamsRequestTypeDef,
    DescribeIpamsResultTypeDef,
    DescribeIpv6PoolsRequestTypeDef,
    DescribeIpv6PoolsResultTypeDef,
    DescribeKeyPairsRequestTypeDef,
    DescribeKeyPairsResultTypeDef,
    DescribeLaunchTemplatesRequestTypeDef,
    DescribeLaunchTemplatesResultTypeDef,
    DescribeLaunchTemplateVersionsRequestTypeDef,
    DescribeLaunchTemplateVersionsResultTypeDef,
    DescribeLocalGatewayRouteTablesRequestTypeDef,
    DescribeLocalGatewayRouteTablesResultTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestTypeDef,
    DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsRequestTypeDef,
    DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef,
    DescribeLocalGatewaysRequestTypeDef,
    DescribeLocalGatewaysResultTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsRequestTypeDef,
    DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef,
    DescribeLocalGatewayVirtualInterfacesRequestTypeDef,
    DescribeLocalGatewayVirtualInterfacesResultTypeDef,
    DescribeLockedSnapshotsRequestTypeDef,
    DescribeLockedSnapshotsResultTypeDef,
    DescribeMacHostsRequestTypeDef,
    DescribeMacHostsResultTypeDef,
    DescribeManagedPrefixListsRequestTypeDef,
    DescribeManagedPrefixListsResultTypeDef,
    DescribeMovingAddressesRequestTypeDef,
    DescribeMovingAddressesResultTypeDef,
    DescribeNatGatewaysRequestTypeDef,
    DescribeNatGatewaysResultTypeDef,
    DescribeNetworkAclsRequestTypeDef,
    DescribeNetworkAclsResultTypeDef,
    DescribeNetworkInsightsAccessScopeAnalysesRequestTypeDef,
    DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef,
    DescribeNetworkInsightsAccessScopesRequestTypeDef,
    DescribeNetworkInsightsAccessScopesResultTypeDef,
    DescribeNetworkInsightsAnalysesRequestTypeDef,
    DescribeNetworkInsightsAnalysesResultTypeDef,
    DescribeNetworkInsightsPathsRequestTypeDef,
    DescribeNetworkInsightsPathsResultTypeDef,
    DescribeNetworkInterfaceAttributeRequestTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeNetworkInterfacePermissionsRequestTypeDef,
    DescribeNetworkInterfacePermissionsResultTypeDef,
    DescribeNetworkInterfacesRequestTypeDef,
    DescribeNetworkInterfacesResultTypeDef,
    DescribeOutpostLagsRequestTypeDef,
    DescribeOutpostLagsResultTypeDef,
    DescribePlacementGroupsRequestTypeDef,
    DescribePlacementGroupsResultTypeDef,
    DescribePrefixListsRequestTypeDef,
    DescribePrefixListsResultTypeDef,
    DescribePrincipalIdFormatRequestTypeDef,
    DescribePrincipalIdFormatResultTypeDef,
    DescribePublicIpv4PoolsRequestTypeDef,
    DescribePublicIpv4PoolsResultTypeDef,
    DescribeRegionsRequestTypeDef,
    DescribeRegionsResultTypeDef,
    DescribeReplaceRootVolumeTasksRequestTypeDef,
    DescribeReplaceRootVolumeTasksResultTypeDef,
    DescribeReservedInstancesListingsRequestTypeDef,
    DescribeReservedInstancesListingsResultTypeDef,
    DescribeReservedInstancesModificationsRequestTypeDef,
    DescribeReservedInstancesModificationsResultTypeDef,
    DescribeReservedInstancesOfferingsRequestTypeDef,
    DescribeReservedInstancesOfferingsResultTypeDef,
    DescribeReservedInstancesRequestTypeDef,
    DescribeReservedInstancesResultTypeDef,
    DescribeRouteServerEndpointsRequestTypeDef,
    DescribeRouteServerEndpointsResultTypeDef,
    DescribeRouteServerPeersRequestTypeDef,
    DescribeRouteServerPeersResultTypeDef,
    DescribeRouteServersRequestTypeDef,
    DescribeRouteServersResultTypeDef,
    DescribeRouteTablesRequestTypeDef,
    DescribeRouteTablesResultTypeDef,
    DescribeScheduledInstanceAvailabilityRequestTypeDef,
    DescribeScheduledInstanceAvailabilityResultTypeDef,
    DescribeScheduledInstancesRequestTypeDef,
    DescribeScheduledInstancesResultTypeDef,
    DescribeSecurityGroupReferencesRequestTypeDef,
    DescribeSecurityGroupReferencesResultTypeDef,
    DescribeSecurityGroupRulesRequestTypeDef,
    DescribeSecurityGroupRulesResultTypeDef,
    DescribeSecurityGroupsRequestTypeDef,
    DescribeSecurityGroupsResultTypeDef,
    DescribeSecurityGroupVpcAssociationsRequestTypeDef,
    DescribeSecurityGroupVpcAssociationsResultTypeDef,
    DescribeServiceLinkVirtualInterfacesRequestTypeDef,
    DescribeServiceLinkVirtualInterfacesResultTypeDef,
    DescribeSnapshotAttributeRequestTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeSnapshotsRequestTypeDef,
    DescribeSnapshotsResultTypeDef,
    DescribeSnapshotTierStatusRequestTypeDef,
    DescribeSnapshotTierStatusResultTypeDef,
    DescribeSpotDatafeedSubscriptionRequestTypeDef,
    DescribeSpotDatafeedSubscriptionResultTypeDef,
    DescribeSpotFleetInstancesRequestTypeDef,
    DescribeSpotFleetInstancesResponseTypeDef,
    DescribeSpotFleetRequestHistoryRequestTypeDef,
    DescribeSpotFleetRequestHistoryResponseTypeDef,
    DescribeSpotFleetRequestsRequestTypeDef,
    DescribeSpotFleetRequestsResponseTypeDef,
    DescribeSpotInstanceRequestsRequestTypeDef,
    DescribeSpotInstanceRequestsResultTypeDef,
    DescribeSpotPriceHistoryRequestTypeDef,
    DescribeSpotPriceHistoryResultTypeDef,
    DescribeStaleSecurityGroupsRequestTypeDef,
    DescribeStaleSecurityGroupsResultTypeDef,
    DescribeStoreImageTasksRequestTypeDef,
    DescribeStoreImageTasksResultTypeDef,
    DescribeSubnetsRequestTypeDef,
    DescribeSubnetsResultTypeDef,
    DescribeTagsRequestTypeDef,
    DescribeTagsResultTypeDef,
    DescribeTrafficMirrorFilterRulesRequestTypeDef,
    DescribeTrafficMirrorFilterRulesResultTypeDef,
    DescribeTrafficMirrorFiltersRequestTypeDef,
    DescribeTrafficMirrorFiltersResultTypeDef,
    DescribeTrafficMirrorSessionsRequestTypeDef,
    DescribeTrafficMirrorSessionsResultTypeDef,
    DescribeTrafficMirrorTargetsRequestTypeDef,
    DescribeTrafficMirrorTargetsResultTypeDef,
    DescribeTransitGatewayAttachmentsRequestTypeDef,
    DescribeTransitGatewayAttachmentsResultTypeDef,
    DescribeTransitGatewayConnectPeersRequestTypeDef,
    DescribeTransitGatewayConnectPeersResultTypeDef,
    DescribeTransitGatewayConnectsRequestTypeDef,
    DescribeTransitGatewayConnectsResultTypeDef,
    DescribeTransitGatewayMulticastDomainsRequestTypeDef,
    DescribeTransitGatewayMulticastDomainsResultTypeDef,
    DescribeTransitGatewayPeeringAttachmentsRequestTypeDef,
    DescribeTransitGatewayPeeringAttachmentsResultTypeDef,
    DescribeTransitGatewayPolicyTablesRequestTypeDef,
    DescribeTransitGatewayPolicyTablesResultTypeDef,
    DescribeTransitGatewayRouteTableAnnouncementsRequestTypeDef,
    DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef,
    DescribeTransitGatewayRouteTablesRequestTypeDef,
    DescribeTransitGatewayRouteTablesResultTypeDef,
    DescribeTransitGatewaysRequestTypeDef,
    DescribeTransitGatewaysResultTypeDef,
    DescribeTransitGatewayVpcAttachmentsRequestTypeDef,
    DescribeTransitGatewayVpcAttachmentsResultTypeDef,
    DescribeTrunkInterfaceAssociationsRequestTypeDef,
    DescribeTrunkInterfaceAssociationsResultTypeDef,
    DescribeVerifiedAccessEndpointsRequestTypeDef,
    DescribeVerifiedAccessEndpointsResultTypeDef,
    DescribeVerifiedAccessGroupsRequestTypeDef,
    DescribeVerifiedAccessGroupsResultTypeDef,
    DescribeVerifiedAccessInstanceLoggingConfigurationsRequestTypeDef,
    DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef,
    DescribeVerifiedAccessInstancesRequestTypeDef,
    DescribeVerifiedAccessInstancesResultTypeDef,
    DescribeVerifiedAccessTrustProvidersRequestTypeDef,
    DescribeVerifiedAccessTrustProvidersResultTypeDef,
    DescribeVolumeAttributeRequestTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumesModificationsRequestTypeDef,
    DescribeVolumesModificationsResultTypeDef,
    DescribeVolumesRequestTypeDef,
    DescribeVolumesResultTypeDef,
    DescribeVolumeStatusRequestTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcAttributeRequestTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DescribeVpcBlockPublicAccessExclusionsRequestTypeDef,
    DescribeVpcBlockPublicAccessExclusionsResultTypeDef,
    DescribeVpcBlockPublicAccessOptionsRequestTypeDef,
    DescribeVpcBlockPublicAccessOptionsResultTypeDef,
    DescribeVpcClassicLinkDnsSupportRequestTypeDef,
    DescribeVpcClassicLinkDnsSupportResultTypeDef,
    DescribeVpcClassicLinkRequestTypeDef,
    DescribeVpcClassicLinkResultTypeDef,
    DescribeVpcEndpointAssociationsRequestTypeDef,
    DescribeVpcEndpointAssociationsResultTypeDef,
    DescribeVpcEndpointConnectionNotificationsRequestTypeDef,
    DescribeVpcEndpointConnectionNotificationsResultTypeDef,
    DescribeVpcEndpointConnectionsRequestTypeDef,
    DescribeVpcEndpointConnectionsResultTypeDef,
    DescribeVpcEndpointServiceConfigurationsRequestTypeDef,
    DescribeVpcEndpointServiceConfigurationsResultTypeDef,
    DescribeVpcEndpointServicePermissionsRequestTypeDef,
    DescribeVpcEndpointServicePermissionsResultTypeDef,
    DescribeVpcEndpointServicesRequestTypeDef,
    DescribeVpcEndpointServicesResultTypeDef,
    DescribeVpcEndpointsRequestTypeDef,
    DescribeVpcEndpointsResultTypeDef,
    DescribeVpcPeeringConnectionsRequestTypeDef,
    DescribeVpcPeeringConnectionsResultTypeDef,
    DescribeVpcsRequestTypeDef,
    DescribeVpcsResultTypeDef,
    DescribeVpnConnectionsRequestTypeDef,
    DescribeVpnConnectionsResultTypeDef,
    DescribeVpnGatewaysRequestTypeDef,
    DescribeVpnGatewaysResultTypeDef,
    DetachClassicLinkVpcRequestTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DetachInternetGatewayRequestTypeDef,
    DetachNetworkInterfaceRequestTypeDef,
    DetachVerifiedAccessTrustProviderRequestTypeDef,
    DetachVerifiedAccessTrustProviderResultTypeDef,
    DetachVolumeRequestTypeDef,
    DetachVpnGatewayRequestTypeDef,
    DisableAddressTransferRequestTypeDef,
    DisableAddressTransferResultTypeDef,
    DisableAllowedImagesSettingsRequestTypeDef,
    DisableAllowedImagesSettingsResultTypeDef,
    DisableAwsNetworkPerformanceMetricSubscriptionRequestTypeDef,
    DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef,
    DisableEbsEncryptionByDefaultRequestTypeDef,
    DisableEbsEncryptionByDefaultResultTypeDef,
    DisableFastLaunchRequestTypeDef,
    DisableFastLaunchResultTypeDef,
    DisableFastSnapshotRestoresRequestTypeDef,
    DisableFastSnapshotRestoresResultTypeDef,
    DisableImageBlockPublicAccessRequestTypeDef,
    DisableImageBlockPublicAccessResultTypeDef,
    DisableImageDeprecationRequestTypeDef,
    DisableImageDeprecationResultTypeDef,
    DisableImageDeregistrationProtectionRequestTypeDef,
    DisableImageDeregistrationProtectionResultTypeDef,
    DisableImageRequestTypeDef,
    DisableImageResultTypeDef,
    DisableIpamOrganizationAdminAccountRequestTypeDef,
    DisableIpamOrganizationAdminAccountResultTypeDef,
    DisableRouteServerPropagationRequestTypeDef,
    DisableRouteServerPropagationResultTypeDef,
    DisableSerialConsoleAccessRequestTypeDef,
    DisableSerialConsoleAccessResultTypeDef,
    DisableSnapshotBlockPublicAccessRequestTypeDef,
    DisableSnapshotBlockPublicAccessResultTypeDef,
    DisableTransitGatewayRouteTablePropagationRequestTypeDef,
    DisableTransitGatewayRouteTablePropagationResultTypeDef,
    DisableVgwRoutePropagationRequestTypeDef,
    DisableVpcClassicLinkDnsSupportRequestTypeDef,
    DisableVpcClassicLinkDnsSupportResultTypeDef,
    DisableVpcClassicLinkRequestTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    DisassociateAddressRequestTypeDef,
    DisassociateCapacityReservationBillingOwnerRequestTypeDef,
    DisassociateCapacityReservationBillingOwnerResultTypeDef,
    DisassociateClientVpnTargetNetworkRequestTypeDef,
    DisassociateClientVpnTargetNetworkResultTypeDef,
    DisassociateEnclaveCertificateIamRoleRequestTypeDef,
    DisassociateEnclaveCertificateIamRoleResultTypeDef,
    DisassociateIamInstanceProfileRequestTypeDef,
    DisassociateIamInstanceProfileResultTypeDef,
    DisassociateInstanceEventWindowRequestTypeDef,
    DisassociateInstanceEventWindowResultTypeDef,
    DisassociateIpamByoasnRequestTypeDef,
    DisassociateIpamByoasnResultTypeDef,
    DisassociateIpamResourceDiscoveryRequestTypeDef,
    DisassociateIpamResourceDiscoveryResultTypeDef,
    DisassociateNatGatewayAddressRequestTypeDef,
    DisassociateNatGatewayAddressResultTypeDef,
    DisassociateRouteServerRequestTypeDef,
    DisassociateRouteServerResultTypeDef,
    DisassociateRouteTableRequestTypeDef,
    DisassociateSecurityGroupVpcRequestTypeDef,
    DisassociateSecurityGroupVpcResultTypeDef,
    DisassociateSubnetCidrBlockRequestTypeDef,
    DisassociateSubnetCidrBlockResultTypeDef,
    DisassociateTransitGatewayMulticastDomainRequestTypeDef,
    DisassociateTransitGatewayMulticastDomainResultTypeDef,
    DisassociateTransitGatewayPolicyTableRequestTypeDef,
    DisassociateTransitGatewayPolicyTableResultTypeDef,
    DisassociateTransitGatewayRouteTableRequestTypeDef,
    DisassociateTransitGatewayRouteTableResultTypeDef,
    DisassociateTrunkInterfaceRequestTypeDef,
    DisassociateTrunkInterfaceResultTypeDef,
    DisassociateVpcCidrBlockRequestTypeDef,
    DisassociateVpcCidrBlockResultTypeDef,
    EmptyResponseMetadataTypeDef,
    EnableAddressTransferRequestTypeDef,
    EnableAddressTransferResultTypeDef,
    EnableAllowedImagesSettingsRequestTypeDef,
    EnableAllowedImagesSettingsResultTypeDef,
    EnableAwsNetworkPerformanceMetricSubscriptionRequestTypeDef,
    EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef,
    EnableEbsEncryptionByDefaultRequestTypeDef,
    EnableEbsEncryptionByDefaultResultTypeDef,
    EnableFastLaunchRequestTypeDef,
    EnableFastLaunchResultTypeDef,
    EnableFastSnapshotRestoresRequestTypeDef,
    EnableFastSnapshotRestoresResultTypeDef,
    EnableImageBlockPublicAccessRequestTypeDef,
    EnableImageBlockPublicAccessResultTypeDef,
    EnableImageDeprecationRequestTypeDef,
    EnableImageDeprecationResultTypeDef,
    EnableImageDeregistrationProtectionRequestTypeDef,
    EnableImageDeregistrationProtectionResultTypeDef,
    EnableImageRequestTypeDef,
    EnableImageResultTypeDef,
    EnableIpamOrganizationAdminAccountRequestTypeDef,
    EnableIpamOrganizationAdminAccountResultTypeDef,
    EnableReachabilityAnalyzerOrganizationSharingRequestTypeDef,
    EnableReachabilityAnalyzerOrganizationSharingResultTypeDef,
    EnableRouteServerPropagationRequestTypeDef,
    EnableRouteServerPropagationResultTypeDef,
    EnableSerialConsoleAccessRequestTypeDef,
    EnableSerialConsoleAccessResultTypeDef,
    EnableSnapshotBlockPublicAccessRequestTypeDef,
    EnableSnapshotBlockPublicAccessResultTypeDef,
    EnableTransitGatewayRouteTablePropagationRequestTypeDef,
    EnableTransitGatewayRouteTablePropagationResultTypeDef,
    EnableVgwRoutePropagationRequestTypeDef,
    EnableVolumeIORequestTypeDef,
    EnableVpcClassicLinkDnsSupportRequestTypeDef,
    EnableVpcClassicLinkDnsSupportResultTypeDef,
    EnableVpcClassicLinkRequestTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    ExportClientVpnClientCertificateRevocationListRequestTypeDef,
    ExportClientVpnClientCertificateRevocationListResultTypeDef,
    ExportClientVpnClientConfigurationRequestTypeDef,
    ExportClientVpnClientConfigurationResultTypeDef,
    ExportImageRequestTypeDef,
    ExportImageResultTypeDef,
    ExportTransitGatewayRoutesRequestTypeDef,
    ExportTransitGatewayRoutesResultTypeDef,
    ExportVerifiedAccessInstanceClientConfigurationRequestTypeDef,
    ExportVerifiedAccessInstanceClientConfigurationResultTypeDef,
    GetAllowedImagesSettingsRequestTypeDef,
    GetAllowedImagesSettingsResultTypeDef,
    GetAssociatedEnclaveCertificateIamRolesRequestTypeDef,
    GetAssociatedEnclaveCertificateIamRolesResultTypeDef,
    GetAssociatedIpv6PoolCidrsRequestTypeDef,
    GetAssociatedIpv6PoolCidrsResultTypeDef,
    GetAwsNetworkPerformanceDataRequestTypeDef,
    GetAwsNetworkPerformanceDataResultTypeDef,
    GetCapacityReservationUsageRequestTypeDef,
    GetCapacityReservationUsageResultTypeDef,
    GetCoipPoolUsageRequestTypeDef,
    GetCoipPoolUsageResultTypeDef,
    GetConsoleOutputRequestTypeDef,
    GetConsoleOutputResultTypeDef,
    GetConsoleScreenshotRequestTypeDef,
    GetConsoleScreenshotResultTypeDef,
    GetDeclarativePoliciesReportSummaryRequestTypeDef,
    GetDeclarativePoliciesReportSummaryResultTypeDef,
    GetDefaultCreditSpecificationRequestTypeDef,
    GetDefaultCreditSpecificationResultTypeDef,
    GetEbsDefaultKmsKeyIdRequestTypeDef,
    GetEbsDefaultKmsKeyIdResultTypeDef,
    GetEbsEncryptionByDefaultRequestTypeDef,
    GetEbsEncryptionByDefaultResultTypeDef,
    GetFlowLogsIntegrationTemplateRequestTypeDef,
    GetFlowLogsIntegrationTemplateResultTypeDef,
    GetGroupsForCapacityReservationRequestTypeDef,
    GetGroupsForCapacityReservationResultTypeDef,
    GetHostReservationPurchasePreviewRequestTypeDef,
    GetHostReservationPurchasePreviewResultTypeDef,
    GetImageBlockPublicAccessStateRequestTypeDef,
    GetImageBlockPublicAccessStateResultTypeDef,
    GetInstanceMetadataDefaultsRequestTypeDef,
    GetInstanceMetadataDefaultsResultTypeDef,
    GetInstanceTpmEkPubRequestTypeDef,
    GetInstanceTpmEkPubResultTypeDef,
    GetInstanceTypesFromInstanceRequirementsRequestTypeDef,
    GetInstanceTypesFromInstanceRequirementsResultTypeDef,
    GetInstanceUefiDataRequestTypeDef,
    GetInstanceUefiDataResultTypeDef,
    GetIpamAddressHistoryRequestTypeDef,
    GetIpamAddressHistoryResultTypeDef,
    GetIpamDiscoveredAccountsRequestTypeDef,
    GetIpamDiscoveredAccountsResultTypeDef,
    GetIpamDiscoveredPublicAddressesRequestTypeDef,
    GetIpamDiscoveredPublicAddressesResultTypeDef,
    GetIpamDiscoveredResourceCidrsRequestTypeDef,
    GetIpamDiscoveredResourceCidrsResultTypeDef,
    GetIpamPoolAllocationsRequestTypeDef,
    GetIpamPoolAllocationsResultTypeDef,
    GetIpamPoolCidrsRequestTypeDef,
    GetIpamPoolCidrsResultTypeDef,
    GetIpamResourceCidrsRequestTypeDef,
    GetIpamResourceCidrsResultTypeDef,
    GetLaunchTemplateDataRequestTypeDef,
    GetLaunchTemplateDataResultTypeDef,
    GetManagedPrefixListAssociationsRequestTypeDef,
    GetManagedPrefixListAssociationsResultTypeDef,
    GetManagedPrefixListEntriesRequestTypeDef,
    GetManagedPrefixListEntriesResultTypeDef,
    GetNetworkInsightsAccessScopeAnalysisFindingsRequestTypeDef,
    GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef,
    GetNetworkInsightsAccessScopeContentRequestTypeDef,
    GetNetworkInsightsAccessScopeContentResultTypeDef,
    GetPasswordDataRequestTypeDef,
    GetPasswordDataResultTypeDef,
    GetReservedInstancesExchangeQuoteRequestTypeDef,
    GetReservedInstancesExchangeQuoteResultTypeDef,
    GetRouteServerAssociationsRequestTypeDef,
    GetRouteServerAssociationsResultTypeDef,
    GetRouteServerPropagationsRequestTypeDef,
    GetRouteServerPropagationsResultTypeDef,
    GetRouteServerRoutingDatabaseRequestTypeDef,
    GetRouteServerRoutingDatabaseResultTypeDef,
    GetSecurityGroupsForVpcRequestTypeDef,
    GetSecurityGroupsForVpcResultTypeDef,
    GetSerialConsoleAccessStatusRequestTypeDef,
    GetSerialConsoleAccessStatusResultTypeDef,
    GetSnapshotBlockPublicAccessStateRequestTypeDef,
    GetSnapshotBlockPublicAccessStateResultTypeDef,
    GetSpotPlacementScoresRequestTypeDef,
    GetSpotPlacementScoresResultTypeDef,
    GetSubnetCidrReservationsRequestTypeDef,
    GetSubnetCidrReservationsResultTypeDef,
    GetTransitGatewayAttachmentPropagationsRequestTypeDef,
    GetTransitGatewayAttachmentPropagationsResultTypeDef,
    GetTransitGatewayMulticastDomainAssociationsRequestTypeDef,
    GetTransitGatewayMulticastDomainAssociationsResultTypeDef,
    GetTransitGatewayPolicyTableAssociationsRequestTypeDef,
    GetTransitGatewayPolicyTableAssociationsResultTypeDef,
    GetTransitGatewayPolicyTableEntriesRequestTypeDef,
    GetTransitGatewayPolicyTableEntriesResultTypeDef,
    GetTransitGatewayPrefixListReferencesRequestTypeDef,
    GetTransitGatewayPrefixListReferencesResultTypeDef,
    GetTransitGatewayRouteTableAssociationsRequestTypeDef,
    GetTransitGatewayRouteTableAssociationsResultTypeDef,
    GetTransitGatewayRouteTablePropagationsRequestTypeDef,
    GetTransitGatewayRouteTablePropagationsResultTypeDef,
    GetVerifiedAccessEndpointPolicyRequestTypeDef,
    GetVerifiedAccessEndpointPolicyResultTypeDef,
    GetVerifiedAccessEndpointTargetsRequestTypeDef,
    GetVerifiedAccessEndpointTargetsResultTypeDef,
    GetVerifiedAccessGroupPolicyRequestTypeDef,
    GetVerifiedAccessGroupPolicyResultTypeDef,
    GetVpnConnectionDeviceSampleConfigurationRequestTypeDef,
    GetVpnConnectionDeviceSampleConfigurationResultTypeDef,
    GetVpnConnectionDeviceTypesRequestTypeDef,
    GetVpnConnectionDeviceTypesResultTypeDef,
    GetVpnTunnelReplacementStatusRequestTypeDef,
    GetVpnTunnelReplacementStatusResultTypeDef,
    ImageAttributeTypeDef,
    ImportClientVpnClientCertificateRevocationListRequestTypeDef,
    ImportClientVpnClientCertificateRevocationListResultTypeDef,
    ImportImageRequestTypeDef,
    ImportImageResultTypeDef,
    ImportInstanceRequestTypeDef,
    ImportInstanceResultTypeDef,
    ImportKeyPairRequestTypeDef,
    ImportKeyPairResultTypeDef,
    ImportSnapshotRequestTypeDef,
    ImportSnapshotResultTypeDef,
    ImportVolumeRequestTypeDef,
    ImportVolumeResultTypeDef,
    InstanceAttributeTypeDef,
    KeyPairTypeDef,
    ListImagesInRecycleBinRequestTypeDef,
    ListImagesInRecycleBinResultTypeDef,
    ListSnapshotsInRecycleBinRequestTypeDef,
    ListSnapshotsInRecycleBinResultTypeDef,
    LockSnapshotRequestTypeDef,
    LockSnapshotResultTypeDef,
    ModifyAddressAttributeRequestTypeDef,
    ModifyAddressAttributeResultTypeDef,
    ModifyAvailabilityZoneGroupRequestTypeDef,
    ModifyAvailabilityZoneGroupResultTypeDef,
    ModifyCapacityReservationFleetRequestTypeDef,
    ModifyCapacityReservationFleetResultTypeDef,
    ModifyCapacityReservationRequestTypeDef,
    ModifyCapacityReservationResultTypeDef,
    ModifyClientVpnEndpointRequestTypeDef,
    ModifyClientVpnEndpointResultTypeDef,
    ModifyDefaultCreditSpecificationRequestTypeDef,
    ModifyDefaultCreditSpecificationResultTypeDef,
    ModifyEbsDefaultKmsKeyIdRequestTypeDef,
    ModifyEbsDefaultKmsKeyIdResultTypeDef,
    ModifyFleetRequestTypeDef,
    ModifyFleetResultTypeDef,
    ModifyFpgaImageAttributeRequestTypeDef,
    ModifyFpgaImageAttributeResultTypeDef,
    ModifyHostsRequestTypeDef,
    ModifyHostsResultTypeDef,
    ModifyIdentityIdFormatRequestTypeDef,
    ModifyIdFormatRequestTypeDef,
    ModifyImageAttributeRequestTypeDef,
    ModifyInstanceAttributeRequestTypeDef,
    ModifyInstanceCapacityReservationAttributesRequestTypeDef,
    ModifyInstanceCapacityReservationAttributesResultTypeDef,
    ModifyInstanceCpuOptionsRequestTypeDef,
    ModifyInstanceCpuOptionsResultTypeDef,
    ModifyInstanceCreditSpecificationRequestTypeDef,
    ModifyInstanceCreditSpecificationResultTypeDef,
    ModifyInstanceEventStartTimeRequestTypeDef,
    ModifyInstanceEventStartTimeResultTypeDef,
    ModifyInstanceEventWindowRequestTypeDef,
    ModifyInstanceEventWindowResultTypeDef,
    ModifyInstanceMaintenanceOptionsRequestTypeDef,
    ModifyInstanceMaintenanceOptionsResultTypeDef,
    ModifyInstanceMetadataDefaultsRequestTypeDef,
    ModifyInstanceMetadataDefaultsResultTypeDef,
    ModifyInstanceMetadataOptionsRequestTypeDef,
    ModifyInstanceMetadataOptionsResultTypeDef,
    ModifyInstanceNetworkPerformanceRequestTypeDef,
    ModifyInstanceNetworkPerformanceResultTypeDef,
    ModifyInstancePlacementRequestTypeDef,
    ModifyInstancePlacementResultTypeDef,
    ModifyIpamPoolRequestTypeDef,
    ModifyIpamPoolResultTypeDef,
    ModifyIpamRequestTypeDef,
    ModifyIpamResourceCidrRequestTypeDef,
    ModifyIpamResourceCidrResultTypeDef,
    ModifyIpamResourceDiscoveryRequestTypeDef,
    ModifyIpamResourceDiscoveryResultTypeDef,
    ModifyIpamResultTypeDef,
    ModifyIpamScopeRequestTypeDef,
    ModifyIpamScopeResultTypeDef,
    ModifyLaunchTemplateRequestTypeDef,
    ModifyLaunchTemplateResultTypeDef,
    ModifyLocalGatewayRouteRequestTypeDef,
    ModifyLocalGatewayRouteResultTypeDef,
    ModifyManagedPrefixListRequestTypeDef,
    ModifyManagedPrefixListResultTypeDef,
    ModifyNetworkInterfaceAttributeRequestTypeDef,
    ModifyPrivateDnsNameOptionsRequestTypeDef,
    ModifyPrivateDnsNameOptionsResultTypeDef,
    ModifyReservedInstancesRequestTypeDef,
    ModifyReservedInstancesResultTypeDef,
    ModifyRouteServerRequestTypeDef,
    ModifyRouteServerResultTypeDef,
    ModifySecurityGroupRulesRequestTypeDef,
    ModifySecurityGroupRulesResultTypeDef,
    ModifySnapshotAttributeRequestTypeDef,
    ModifySnapshotTierRequestTypeDef,
    ModifySnapshotTierResultTypeDef,
    ModifySpotFleetRequestRequestTypeDef,
    ModifySpotFleetRequestResponseTypeDef,
    ModifySubnetAttributeRequestTypeDef,
    ModifyTrafficMirrorFilterNetworkServicesRequestTypeDef,
    ModifyTrafficMirrorFilterNetworkServicesResultTypeDef,
    ModifyTrafficMirrorFilterRuleRequestTypeDef,
    ModifyTrafficMirrorFilterRuleResultTypeDef,
    ModifyTrafficMirrorSessionRequestTypeDef,
    ModifyTrafficMirrorSessionResultTypeDef,
    ModifyTransitGatewayPrefixListReferenceRequestTypeDef,
    ModifyTransitGatewayPrefixListReferenceResultTypeDef,
    ModifyTransitGatewayRequestTypeDef,
    ModifyTransitGatewayResultTypeDef,
    ModifyTransitGatewayVpcAttachmentRequestTypeDef,
    ModifyTransitGatewayVpcAttachmentResultTypeDef,
    ModifyVerifiedAccessEndpointPolicyRequestTypeDef,
    ModifyVerifiedAccessEndpointPolicyResultTypeDef,
    ModifyVerifiedAccessEndpointRequestTypeDef,
    ModifyVerifiedAccessEndpointResultTypeDef,
    ModifyVerifiedAccessGroupPolicyRequestTypeDef,
    ModifyVerifiedAccessGroupPolicyResultTypeDef,
    ModifyVerifiedAccessGroupRequestTypeDef,
    ModifyVerifiedAccessGroupResultTypeDef,
    ModifyVerifiedAccessInstanceLoggingConfigurationRequestTypeDef,
    ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef,
    ModifyVerifiedAccessInstanceRequestTypeDef,
    ModifyVerifiedAccessInstanceResultTypeDef,
    ModifyVerifiedAccessTrustProviderRequestTypeDef,
    ModifyVerifiedAccessTrustProviderResultTypeDef,
    ModifyVolumeAttributeRequestTypeDef,
    ModifyVolumeRequestTypeDef,
    ModifyVolumeResultTypeDef,
    ModifyVpcAttributeRequestTypeDef,
    ModifyVpcBlockPublicAccessExclusionRequestTypeDef,
    ModifyVpcBlockPublicAccessExclusionResultTypeDef,
    ModifyVpcBlockPublicAccessOptionsRequestTypeDef,
    ModifyVpcBlockPublicAccessOptionsResultTypeDef,
    ModifyVpcEndpointConnectionNotificationRequestTypeDef,
    ModifyVpcEndpointConnectionNotificationResultTypeDef,
    ModifyVpcEndpointRequestTypeDef,
    ModifyVpcEndpointResultTypeDef,
    ModifyVpcEndpointServiceConfigurationRequestTypeDef,
    ModifyVpcEndpointServiceConfigurationResultTypeDef,
    ModifyVpcEndpointServicePayerResponsibilityRequestTypeDef,
    ModifyVpcEndpointServicePayerResponsibilityResultTypeDef,
    ModifyVpcEndpointServicePermissionsRequestTypeDef,
    ModifyVpcEndpointServicePermissionsResultTypeDef,
    ModifyVpcPeeringConnectionOptionsRequestTypeDef,
    ModifyVpcPeeringConnectionOptionsResultTypeDef,
    ModifyVpcTenancyRequestTypeDef,
    ModifyVpcTenancyResultTypeDef,
    ModifyVpnConnectionOptionsRequestTypeDef,
    ModifyVpnConnectionOptionsResultTypeDef,
    ModifyVpnConnectionRequestTypeDef,
    ModifyVpnConnectionResultTypeDef,
    ModifyVpnTunnelCertificateRequestTypeDef,
    ModifyVpnTunnelCertificateResultTypeDef,
    ModifyVpnTunnelOptionsRequestTypeDef,
    ModifyVpnTunnelOptionsResultTypeDef,
    MonitorInstancesRequestTypeDef,
    MonitorInstancesResultTypeDef,
    MoveAddressToVpcRequestTypeDef,
    MoveAddressToVpcResultTypeDef,
    MoveByoipCidrToIpamRequestTypeDef,
    MoveByoipCidrToIpamResultTypeDef,
    MoveCapacityReservationInstancesRequestTypeDef,
    MoveCapacityReservationInstancesResultTypeDef,
    ProvisionByoipCidrRequestTypeDef,
    ProvisionByoipCidrResultTypeDef,
    ProvisionIpamByoasnRequestTypeDef,
    ProvisionIpamByoasnResultTypeDef,
    ProvisionIpamPoolCidrRequestTypeDef,
    ProvisionIpamPoolCidrResultTypeDef,
    ProvisionPublicIpv4PoolCidrRequestTypeDef,
    ProvisionPublicIpv4PoolCidrResultTypeDef,
    PurchaseCapacityBlockExtensionRequestTypeDef,
    PurchaseCapacityBlockExtensionResultTypeDef,
    PurchaseCapacityBlockRequestTypeDef,
    PurchaseCapacityBlockResultTypeDef,
    PurchaseHostReservationRequestTypeDef,
    PurchaseHostReservationResultTypeDef,
    PurchaseReservedInstancesOfferingRequestTypeDef,
    PurchaseReservedInstancesOfferingResultTypeDef,
    PurchaseScheduledInstancesRequestTypeDef,
    PurchaseScheduledInstancesResultTypeDef,
    RebootInstancesRequestTypeDef,
    RegisterImageRequestTypeDef,
    RegisterImageResultTypeDef,
    RegisterInstanceEventNotificationAttributesRequestTypeDef,
    RegisterInstanceEventNotificationAttributesResultTypeDef,
    RegisterTransitGatewayMulticastGroupMembersRequestTypeDef,
    RegisterTransitGatewayMulticastGroupMembersResultTypeDef,
    RegisterTransitGatewayMulticastGroupSourcesRequestTypeDef,
    RegisterTransitGatewayMulticastGroupSourcesResultTypeDef,
    RejectCapacityReservationBillingOwnershipRequestTypeDef,
    RejectCapacityReservationBillingOwnershipResultTypeDef,
    RejectTransitGatewayMulticastDomainAssociationsRequestTypeDef,
    RejectTransitGatewayMulticastDomainAssociationsResultTypeDef,
    RejectTransitGatewayPeeringAttachmentRequestTypeDef,
    RejectTransitGatewayPeeringAttachmentResultTypeDef,
    RejectTransitGatewayVpcAttachmentRequestTypeDef,
    RejectTransitGatewayVpcAttachmentResultTypeDef,
    RejectVpcEndpointConnectionsRequestTypeDef,
    RejectVpcEndpointConnectionsResultTypeDef,
    RejectVpcPeeringConnectionRequestTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReleaseAddressRequestTypeDef,
    ReleaseHostsRequestTypeDef,
    ReleaseHostsResultTypeDef,
    ReleaseIpamPoolAllocationRequestTypeDef,
    ReleaseIpamPoolAllocationResultTypeDef,
    ReplaceIamInstanceProfileAssociationRequestTypeDef,
    ReplaceIamInstanceProfileAssociationResultTypeDef,
    ReplaceImageCriteriaInAllowedImagesSettingsRequestTypeDef,
    ReplaceImageCriteriaInAllowedImagesSettingsResultTypeDef,
    ReplaceNetworkAclAssociationRequestTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    ReplaceNetworkAclEntryRequestTypeDef,
    ReplaceRouteRequestTypeDef,
    ReplaceRouteTableAssociationRequestTypeDef,
    ReplaceRouteTableAssociationResultTypeDef,
    ReplaceTransitGatewayRouteRequestTypeDef,
    ReplaceTransitGatewayRouteResultTypeDef,
    ReplaceVpnTunnelRequestTypeDef,
    ReplaceVpnTunnelResultTypeDef,
    ReportInstanceStatusRequestTypeDef,
    RequestSpotFleetRequestTypeDef,
    RequestSpotFleetResponseTypeDef,
    RequestSpotInstancesRequestTypeDef,
    RequestSpotInstancesResultTypeDef,
    ReservationResponseTypeDef,
    ResetAddressAttributeRequestTypeDef,
    ResetAddressAttributeResultTypeDef,
    ResetEbsDefaultKmsKeyIdRequestTypeDef,
    ResetEbsDefaultKmsKeyIdResultTypeDef,
    ResetFpgaImageAttributeRequestTypeDef,
    ResetFpgaImageAttributeResultTypeDef,
    ResetImageAttributeRequestTypeDef,
    ResetInstanceAttributeRequestTypeDef,
    ResetNetworkInterfaceAttributeRequestTypeDef,
    ResetSnapshotAttributeRequestTypeDef,
    RestoreAddressToClassicRequestTypeDef,
    RestoreAddressToClassicResultTypeDef,
    RestoreImageFromRecycleBinRequestTypeDef,
    RestoreImageFromRecycleBinResultTypeDef,
    RestoreManagedPrefixListVersionRequestTypeDef,
    RestoreManagedPrefixListVersionResultTypeDef,
    RestoreSnapshotFromRecycleBinRequestTypeDef,
    RestoreSnapshotFromRecycleBinResultTypeDef,
    RestoreSnapshotTierRequestTypeDef,
    RestoreSnapshotTierResultTypeDef,
    RevokeClientVpnIngressRequestTypeDef,
    RevokeClientVpnIngressResultTypeDef,
    RevokeSecurityGroupEgressRequestTypeDef,
    RevokeSecurityGroupEgressResultTypeDef,
    RevokeSecurityGroupIngressRequestTypeDef,
    RevokeSecurityGroupIngressResultTypeDef,
    RunInstancesRequestTypeDef,
    RunScheduledInstancesRequestTypeDef,
    RunScheduledInstancesResultTypeDef,
    SearchLocalGatewayRoutesRequestTypeDef,
    SearchLocalGatewayRoutesResultTypeDef,
    SearchTransitGatewayMulticastGroupsRequestTypeDef,
    SearchTransitGatewayMulticastGroupsResultTypeDef,
    SearchTransitGatewayRoutesRequestTypeDef,
    SearchTransitGatewayRoutesResultTypeDef,
    SendDiagnosticInterruptRequestTypeDef,
    SnapshotResponseTypeDef,
    StartDeclarativePoliciesReportRequestTypeDef,
    StartDeclarativePoliciesReportResultTypeDef,
    StartInstancesRequestTypeDef,
    StartInstancesResultTypeDef,
    StartNetworkInsightsAccessScopeAnalysisRequestTypeDef,
    StartNetworkInsightsAccessScopeAnalysisResultTypeDef,
    StartNetworkInsightsAnalysisRequestTypeDef,
    StartNetworkInsightsAnalysisResultTypeDef,
    StartVpcEndpointServicePrivateDnsVerificationRequestTypeDef,
    StartVpcEndpointServicePrivateDnsVerificationResultTypeDef,
    StopInstancesRequestTypeDef,
    StopInstancesResultTypeDef,
    TerminateClientVpnConnectionsRequestTypeDef,
    TerminateClientVpnConnectionsResultTypeDef,
    TerminateInstancesRequestTypeDef,
    TerminateInstancesResultTypeDef,
    UnassignIpv6AddressesRequestTypeDef,
    UnassignIpv6AddressesResultTypeDef,
    UnassignPrivateIpAddressesRequestTypeDef,
    UnassignPrivateNatGatewayAddressRequestTypeDef,
    UnassignPrivateNatGatewayAddressResultTypeDef,
    UnlockSnapshotRequestTypeDef,
    UnlockSnapshotResultTypeDef,
    UnmonitorInstancesRequestTypeDef,
    UnmonitorInstancesResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef,
    UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef,
    UpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef,
    UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef,
    VolumeAttachmentResponseTypeDef,
    VolumeResponseTypeDef,
    WithdrawByoipCidrRequestTypeDef,
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

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import type as Type
    from collections.abc import Mapping
else:
    from typing import Dict, Mapping, Type
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = ("EC2Client",)

class Exceptions(BaseClientExceptions):
    ClientError: Type[BotocoreClientError]

class EC2Client(BaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        EC2Client exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2.html#EC2.Client)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/can_paginate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#can_paginate)
        """

    def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/generate_presigned_url.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#generate_presigned_url)
        """

    def accept_address_transfer(
        self, **kwargs: Unpack[AcceptAddressTransferRequestTypeDef]
    ) -> AcceptAddressTransferResultTypeDef:
        """
        Accepts an Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/accept_address_transfer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_address_transfer)
        """

    def accept_capacity_reservation_billing_ownership(
        self, **kwargs: Unpack[AcceptCapacityReservationBillingOwnershipRequestTypeDef]
    ) -> AcceptCapacityReservationBillingOwnershipResultTypeDef:
        """
        Accepts a request to assign billing of the available capacity of a shared
        Capacity Reservation to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/accept_capacity_reservation_billing_ownership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_capacity_reservation_billing_ownership)
        """

    def accept_reserved_instances_exchange_quote(
        self, **kwargs: Unpack[AcceptReservedInstancesExchangeQuoteRequestTypeDef]
    ) -> AcceptReservedInstancesExchangeQuoteResultTypeDef:
        """
        Accepts the Convertible Reserved Instance exchange quote described in the
        <a>GetReservedInstancesExchangeQuote</a> call.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/accept_reserved_instances_exchange_quote.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_reserved_instances_exchange_quote)
        """

    def accept_transit_gateway_multicast_domain_associations(
        self, **kwargs: Unpack[AcceptTransitGatewayMulticastDomainAssociationsRequestTypeDef]
    ) -> AcceptTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        Accepts a request to associate subnets with a transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/accept_transit_gateway_multicast_domain_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_transit_gateway_multicast_domain_associations)
        """

    def accept_transit_gateway_peering_attachment(
        self, **kwargs: Unpack[AcceptTransitGatewayPeeringAttachmentRequestTypeDef]
    ) -> AcceptTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Accepts a transit gateway peering attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/accept_transit_gateway_peering_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_transit_gateway_peering_attachment)
        """

    def accept_transit_gateway_vpc_attachment(
        self, **kwargs: Unpack[AcceptTransitGatewayVpcAttachmentRequestTypeDef]
    ) -> AcceptTransitGatewayVpcAttachmentResultTypeDef:
        """
        Accepts a request to attach a VPC to a transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/accept_transit_gateway_vpc_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_transit_gateway_vpc_attachment)
        """

    def accept_vpc_endpoint_connections(
        self, **kwargs: Unpack[AcceptVpcEndpointConnectionsRequestTypeDef]
    ) -> AcceptVpcEndpointConnectionsResultTypeDef:
        """
        Accepts connection requests to your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/accept_vpc_endpoint_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_vpc_endpoint_connections)
        """

    def accept_vpc_peering_connection(
        self, **kwargs: Unpack[AcceptVpcPeeringConnectionRequestTypeDef]
    ) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        Accept a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/accept_vpc_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#accept_vpc_peering_connection)
        """

    def advertise_byoip_cidr(
        self, **kwargs: Unpack[AdvertiseByoipCidrRequestTypeDef]
    ) -> AdvertiseByoipCidrResultTypeDef:
        """
        Advertises an IPv4 or IPv6 address range that is provisioned for use with your
        Amazon Web Services resources through bring your own IP addresses (BYOIP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/advertise_byoip_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#advertise_byoip_cidr)
        """

    def allocate_address(
        self, **kwargs: Unpack[AllocateAddressRequestTypeDef]
    ) -> AllocateAddressResultTypeDef:
        """
        Allocates an Elastic IP address to your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/allocate_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#allocate_address)
        """

    def allocate_hosts(
        self, **kwargs: Unpack[AllocateHostsRequestTypeDef]
    ) -> AllocateHostsResultTypeDef:
        """
        Allocates a Dedicated Host to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/allocate_hosts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#allocate_hosts)
        """

    def allocate_ipam_pool_cidr(
        self, **kwargs: Unpack[AllocateIpamPoolCidrRequestTypeDef]
    ) -> AllocateIpamPoolCidrResultTypeDef:
        """
        Allocate a CIDR from an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/allocate_ipam_pool_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#allocate_ipam_pool_cidr)
        """

    def apply_security_groups_to_client_vpn_target_network(
        self, **kwargs: Unpack[ApplySecurityGroupsToClientVpnTargetNetworkRequestTypeDef]
    ) -> ApplySecurityGroupsToClientVpnTargetNetworkResultTypeDef:
        """
        Applies a security group to the association between the target network and the
        Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/apply_security_groups_to_client_vpn_target_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#apply_security_groups_to_client_vpn_target_network)
        """

    def assign_ipv6_addresses(
        self, **kwargs: Unpack[AssignIpv6AddressesRequestTypeDef]
    ) -> AssignIpv6AddressesResultTypeDef:
        """
        Assigns the specified IPv6 addresses to the specified network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/assign_ipv6_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#assign_ipv6_addresses)
        """

    def assign_private_ip_addresses(
        self, **kwargs: Unpack[AssignPrivateIpAddressesRequestTypeDef]
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        Assigns the specified secondary private IP addresses to the specified network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/assign_private_ip_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#assign_private_ip_addresses)
        """

    def assign_private_nat_gateway_address(
        self, **kwargs: Unpack[AssignPrivateNatGatewayAddressRequestTypeDef]
    ) -> AssignPrivateNatGatewayAddressResultTypeDef:
        """
        Assigns private IPv4 addresses to a private NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/assign_private_nat_gateway_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#assign_private_nat_gateway_address)
        """

    def associate_address(
        self, **kwargs: Unpack[AssociateAddressRequestTypeDef]
    ) -> AssociateAddressResultTypeDef:
        """
        Associates an Elastic IP address, or carrier IP address (for instances that are
        in subnets in Wavelength Zones) with an instance or a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_address)
        """

    def associate_capacity_reservation_billing_owner(
        self, **kwargs: Unpack[AssociateCapacityReservationBillingOwnerRequestTypeDef]
    ) -> AssociateCapacityReservationBillingOwnerResultTypeDef:
        """
        Initiates a request to assign billing of the unused capacity of a shared
        Capacity Reservation to a consumer account that is consolidated under the same
        Amazon Web Services organizations payer account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_capacity_reservation_billing_owner.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_capacity_reservation_billing_owner)
        """

    def associate_client_vpn_target_network(
        self, **kwargs: Unpack[AssociateClientVpnTargetNetworkRequestTypeDef]
    ) -> AssociateClientVpnTargetNetworkResultTypeDef:
        """
        Associates a target network with a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_client_vpn_target_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_client_vpn_target_network)
        """

    def associate_dhcp_options(
        self, **kwargs: Unpack[AssociateDhcpOptionsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Associates a set of DHCP options (that you've previously created) with the
        specified VPC, or associates no DHCP options with the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_dhcp_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_dhcp_options)
        """

    def associate_enclave_certificate_iam_role(
        self, **kwargs: Unpack[AssociateEnclaveCertificateIamRoleRequestTypeDef]
    ) -> AssociateEnclaveCertificateIamRoleResultTypeDef:
        """
        Associates an Identity and Access Management (IAM) role with an Certificate
        Manager (ACM) certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_enclave_certificate_iam_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_enclave_certificate_iam_role)
        """

    def associate_iam_instance_profile(
        self, **kwargs: Unpack[AssociateIamInstanceProfileRequestTypeDef]
    ) -> AssociateIamInstanceProfileResultTypeDef:
        """
        Associates an IAM instance profile with a running or stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_iam_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_iam_instance_profile)
        """

    def associate_instance_event_window(
        self, **kwargs: Unpack[AssociateInstanceEventWindowRequestTypeDef]
    ) -> AssociateInstanceEventWindowResultTypeDef:
        """
        Associates one or more targets with an event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_instance_event_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_instance_event_window)
        """

    def associate_ipam_byoasn(
        self, **kwargs: Unpack[AssociateIpamByoasnRequestTypeDef]
    ) -> AssociateIpamByoasnResultTypeDef:
        """
        Associates your Autonomous System Number (ASN) with a BYOIP CIDR that you own
        in the same Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_ipam_byoasn.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_ipam_byoasn)
        """

    def associate_ipam_resource_discovery(
        self, **kwargs: Unpack[AssociateIpamResourceDiscoveryRequestTypeDef]
    ) -> AssociateIpamResourceDiscoveryResultTypeDef:
        """
        Associates an IPAM resource discovery with an Amazon VPC IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_ipam_resource_discovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_ipam_resource_discovery)
        """

    def associate_nat_gateway_address(
        self, **kwargs: Unpack[AssociateNatGatewayAddressRequestTypeDef]
    ) -> AssociateNatGatewayAddressResultTypeDef:
        """
        Associates Elastic IP addresses (EIPs) and private IPv4 addresses with a public
        NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_nat_gateway_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_nat_gateway_address)
        """

    def associate_route_server(
        self, **kwargs: Unpack[AssociateRouteServerRequestTypeDef]
    ) -> AssociateRouteServerResultTypeDef:
        """
        Associates a route server with a VPC to enable dynamic route updates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_route_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_route_server)
        """

    def associate_route_table(
        self, **kwargs: Unpack[AssociateRouteTableRequestTypeDef]
    ) -> AssociateRouteTableResultTypeDef:
        """
        Associates a subnet in your VPC or an internet gateway or virtual private
        gateway attached to your VPC with a route table in your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_route_table)
        """

    def associate_security_group_vpc(
        self, **kwargs: Unpack[AssociateSecurityGroupVpcRequestTypeDef]
    ) -> AssociateSecurityGroupVpcResultTypeDef:
        """
        Associates a security group with another VPC in the same Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_security_group_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_security_group_vpc)
        """

    def associate_subnet_cidr_block(
        self, **kwargs: Unpack[AssociateSubnetCidrBlockRequestTypeDef]
    ) -> AssociateSubnetCidrBlockResultTypeDef:
        """
        Associates a CIDR block with your subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_subnet_cidr_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_subnet_cidr_block)
        """

    def associate_transit_gateway_multicast_domain(
        self, **kwargs: Unpack[AssociateTransitGatewayMulticastDomainRequestTypeDef]
    ) -> AssociateTransitGatewayMulticastDomainResultTypeDef:
        """
        Associates the specified subnets and transit gateway attachments with the
        specified transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_transit_gateway_multicast_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_transit_gateway_multicast_domain)
        """

    def associate_transit_gateway_policy_table(
        self, **kwargs: Unpack[AssociateTransitGatewayPolicyTableRequestTypeDef]
    ) -> AssociateTransitGatewayPolicyTableResultTypeDef:
        """
        Associates the specified transit gateway attachment with a transit gateway
        policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_transit_gateway_policy_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_transit_gateway_policy_table)
        """

    def associate_transit_gateway_route_table(
        self, **kwargs: Unpack[AssociateTransitGatewayRouteTableRequestTypeDef]
    ) -> AssociateTransitGatewayRouteTableResultTypeDef:
        """
        Associates the specified attachment with the specified transit gateway route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_transit_gateway_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_transit_gateway_route_table)
        """

    def associate_trunk_interface(
        self, **kwargs: Unpack[AssociateTrunkInterfaceRequestTypeDef]
    ) -> AssociateTrunkInterfaceResultTypeDef:
        """
        Associates a branch network interface with a trunk network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_trunk_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_trunk_interface)
        """

    def associate_vpc_cidr_block(
        self, **kwargs: Unpack[AssociateVpcCidrBlockRequestTypeDef]
    ) -> AssociateVpcCidrBlockResultTypeDef:
        """
        Associates a CIDR block with your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/associate_vpc_cidr_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#associate_vpc_cidr_block)
        """

    def attach_classic_link_vpc(
        self, **kwargs: Unpack[AttachClassicLinkVpcRequestTypeDef]
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/attach_classic_link_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_classic_link_vpc)
        """

    def attach_internet_gateway(
        self, **kwargs: Unpack[AttachInternetGatewayRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Attaches an internet gateway or a virtual private gateway to a VPC, enabling
        connectivity between the internet and the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/attach_internet_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_internet_gateway)
        """

    def attach_network_interface(
        self, **kwargs: Unpack[AttachNetworkInterfaceRequestTypeDef]
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        Attaches a network interface to an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/attach_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_network_interface)
        """

    def attach_verified_access_trust_provider(
        self, **kwargs: Unpack[AttachVerifiedAccessTrustProviderRequestTypeDef]
    ) -> AttachVerifiedAccessTrustProviderResultTypeDef:
        """
        Attaches the specified Amazon Web Services Verified Access trust provider to
        the specified Amazon Web Services Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/attach_verified_access_trust_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_verified_access_trust_provider)
        """

    def attach_volume(
        self, **kwargs: Unpack[AttachVolumeRequestTypeDef]
    ) -> VolumeAttachmentResponseTypeDef:
        """
        Attaches an EBS volume to a running or stopped instance and exposes it to the
        instance with the specified device name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/attach_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_volume)
        """

    def attach_vpn_gateway(
        self, **kwargs: Unpack[AttachVpnGatewayRequestTypeDef]
    ) -> AttachVpnGatewayResultTypeDef:
        """
        Attaches an available virtual private gateway to a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/attach_vpn_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#attach_vpn_gateway)
        """

    def authorize_client_vpn_ingress(
        self, **kwargs: Unpack[AuthorizeClientVpnIngressRequestTypeDef]
    ) -> AuthorizeClientVpnIngressResultTypeDef:
        """
        Adds an ingress authorization rule to a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/authorize_client_vpn_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#authorize_client_vpn_ingress)
        """

    def authorize_security_group_egress(
        self, **kwargs: Unpack[AuthorizeSecurityGroupEgressRequestTypeDef]
    ) -> AuthorizeSecurityGroupEgressResultTypeDef:
        """
        Adds the specified outbound (egress) rules to a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/authorize_security_group_egress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#authorize_security_group_egress)
        """

    def authorize_security_group_ingress(
        self, **kwargs: Unpack[AuthorizeSecurityGroupIngressRequestTypeDef]
    ) -> AuthorizeSecurityGroupIngressResultTypeDef:
        """
        Adds the specified inbound (ingress) rules to a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/authorize_security_group_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#authorize_security_group_ingress)
        """

    def bundle_instance(
        self, **kwargs: Unpack[BundleInstanceRequestTypeDef]
    ) -> BundleInstanceResultTypeDef:
        """
        Bundles an Amazon instance store-backed Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/bundle_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#bundle_instance)
        """

    def cancel_bundle_task(
        self, **kwargs: Unpack[CancelBundleTaskRequestTypeDef]
    ) -> CancelBundleTaskResultTypeDef:
        """
        Cancels a bundling operation for an instance store-backed Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_bundle_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_bundle_task)
        """

    def cancel_capacity_reservation(
        self, **kwargs: Unpack[CancelCapacityReservationRequestTypeDef]
    ) -> CancelCapacityReservationResultTypeDef:
        """
        Cancels the specified Capacity Reservation, releases the reserved capacity, and
        changes the Capacity Reservation's state to <code>cancelled</code>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_capacity_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_capacity_reservation)
        """

    def cancel_capacity_reservation_fleets(
        self, **kwargs: Unpack[CancelCapacityReservationFleetsRequestTypeDef]
    ) -> CancelCapacityReservationFleetsResultTypeDef:
        """
        Cancels one or more Capacity Reservation Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_capacity_reservation_fleets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_capacity_reservation_fleets)
        """

    def cancel_conversion_task(
        self, **kwargs: Unpack[CancelConversionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Cancels an active conversion task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_conversion_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_conversion_task)
        """

    def cancel_declarative_policies_report(
        self, **kwargs: Unpack[CancelDeclarativePoliciesReportRequestTypeDef]
    ) -> CancelDeclarativePoliciesReportResultTypeDef:
        """
        Cancels the generation of an account status report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_declarative_policies_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_declarative_policies_report)
        """

    def cancel_export_task(
        self, **kwargs: Unpack[CancelExportTaskRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Cancels an active export task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_export_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_export_task)
        """

    def cancel_image_launch_permission(
        self, **kwargs: Unpack[CancelImageLaunchPermissionRequestTypeDef]
    ) -> CancelImageLaunchPermissionResultTypeDef:
        """
        Removes your Amazon Web Services account from the launch permissions for the
        specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_image_launch_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_image_launch_permission)
        """

    def cancel_import_task(
        self, **kwargs: Unpack[CancelImportTaskRequestTypeDef]
    ) -> CancelImportTaskResultTypeDef:
        """
        Cancels an in-process import virtual machine or import snapshot task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_import_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_import_task)
        """

    def cancel_reserved_instances_listing(
        self, **kwargs: Unpack[CancelReservedInstancesListingRequestTypeDef]
    ) -> CancelReservedInstancesListingResultTypeDef:
        """
        Cancels the specified Reserved Instance listing in the Reserved Instance
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_reserved_instances_listing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_reserved_instances_listing)
        """

    def cancel_spot_fleet_requests(
        self, **kwargs: Unpack[CancelSpotFleetRequestsRequestTypeDef]
    ) -> CancelSpotFleetRequestsResponseTypeDef:
        """
        Cancels the specified Spot Fleet requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_spot_fleet_requests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_spot_fleet_requests)
        """

    def cancel_spot_instance_requests(
        self, **kwargs: Unpack[CancelSpotInstanceRequestsRequestTypeDef]
    ) -> CancelSpotInstanceRequestsResultTypeDef:
        """
        Cancels one or more Spot Instance requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/cancel_spot_instance_requests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#cancel_spot_instance_requests)
        """

    def confirm_product_instance(
        self, **kwargs: Unpack[ConfirmProductInstanceRequestTypeDef]
    ) -> ConfirmProductInstanceResultTypeDef:
        """
        Determines whether a product code is associated with an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/confirm_product_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#confirm_product_instance)
        """

    def copy_fpga_image(
        self, **kwargs: Unpack[CopyFpgaImageRequestTypeDef]
    ) -> CopyFpgaImageResultTypeDef:
        """
        Copies the specified Amazon FPGA Image (AFI) to the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/copy_fpga_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#copy_fpga_image)
        """

    def copy_image(self, **kwargs: Unpack[CopyImageRequestTypeDef]) -> CopyImageResultTypeDef:
        """
        Initiates an AMI copy operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/copy_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#copy_image)
        """

    def copy_snapshot(
        self, **kwargs: Unpack[CopySnapshotRequestTypeDef]
    ) -> CopySnapshotResultTypeDef:
        """
        Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/copy_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#copy_snapshot)
        """

    def create_capacity_reservation(
        self, **kwargs: Unpack[CreateCapacityReservationRequestTypeDef]
    ) -> CreateCapacityReservationResultTypeDef:
        """
        Creates a new Capacity Reservation with the specified attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_capacity_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_capacity_reservation)
        """

    def create_capacity_reservation_by_splitting(
        self, **kwargs: Unpack[CreateCapacityReservationBySplittingRequestTypeDef]
    ) -> CreateCapacityReservationBySplittingResultTypeDef:
        """
        Create a new Capacity Reservation by splitting the capacity of the source
        Capacity Reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_capacity_reservation_by_splitting.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_capacity_reservation_by_splitting)
        """

    def create_capacity_reservation_fleet(
        self, **kwargs: Unpack[CreateCapacityReservationFleetRequestTypeDef]
    ) -> CreateCapacityReservationFleetResultTypeDef:
        """
        Creates a Capacity Reservation Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_capacity_reservation_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_capacity_reservation_fleet)
        """

    def create_carrier_gateway(
        self, **kwargs: Unpack[CreateCarrierGatewayRequestTypeDef]
    ) -> CreateCarrierGatewayResultTypeDef:
        """
        Creates a carrier gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_carrier_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_carrier_gateway)
        """

    def create_client_vpn_endpoint(
        self, **kwargs: Unpack[CreateClientVpnEndpointRequestTypeDef]
    ) -> CreateClientVpnEndpointResultTypeDef:
        """
        Creates a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_client_vpn_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_client_vpn_endpoint)
        """

    def create_client_vpn_route(
        self, **kwargs: Unpack[CreateClientVpnRouteRequestTypeDef]
    ) -> CreateClientVpnRouteResultTypeDef:
        """
        Adds a route to a network to a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_client_vpn_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_client_vpn_route)
        """

    def create_coip_cidr(
        self, **kwargs: Unpack[CreateCoipCidrRequestTypeDef]
    ) -> CreateCoipCidrResultTypeDef:
        """
        Creates a range of customer-owned IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_coip_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_coip_cidr)
        """

    def create_coip_pool(
        self, **kwargs: Unpack[CreateCoipPoolRequestTypeDef]
    ) -> CreateCoipPoolResultTypeDef:
        """
        Creates a pool of customer-owned IP (CoIP) addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_coip_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_coip_pool)
        """

    def create_customer_gateway(
        self, **kwargs: Unpack[CreateCustomerGatewayRequestTypeDef]
    ) -> CreateCustomerGatewayResultTypeDef:
        """
        Provides information to Amazon Web Services about your customer gateway device.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_customer_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_customer_gateway)
        """

    def create_default_subnet(
        self, **kwargs: Unpack[CreateDefaultSubnetRequestTypeDef]
    ) -> CreateDefaultSubnetResultTypeDef:
        """
        Creates a default subnet with a size <code>/20</code> IPv4 CIDR block in the
        specified Availability Zone in your default VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_default_subnet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_default_subnet)
        """

    def create_default_vpc(
        self, **kwargs: Unpack[CreateDefaultVpcRequestTypeDef]
    ) -> CreateDefaultVpcResultTypeDef:
        """
        Creates a default VPC with a size <code>/16</code> IPv4 CIDR block and a
        default subnet in each Availability Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_default_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_default_vpc)
        """

    def create_dhcp_options(
        self, **kwargs: Unpack[CreateDhcpOptionsRequestTypeDef]
    ) -> CreateDhcpOptionsResultTypeDef:
        """
        Creates a custom set of DHCP options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_dhcp_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_dhcp_options)
        """

    def create_egress_only_internet_gateway(
        self, **kwargs: Unpack[CreateEgressOnlyInternetGatewayRequestTypeDef]
    ) -> CreateEgressOnlyInternetGatewayResultTypeDef:
        """
        [IPv6 only] Creates an egress-only internet gateway for your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_egress_only_internet_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_egress_only_internet_gateway)
        """

    def create_fleet(self, **kwargs: Unpack[CreateFleetRequestTypeDef]) -> CreateFleetResultTypeDef:
        """
        Creates an EC2 Fleet that contains the configuration information for On-Demand
        Instances and Spot Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_fleet)
        """

    def create_flow_logs(
        self, **kwargs: Unpack[CreateFlowLogsRequestTypeDef]
    ) -> CreateFlowLogsResultTypeDef:
        """
        Creates one or more flow logs to capture information about IP traffic for a
        specific network interface, subnet, or VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_flow_logs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_flow_logs)
        """

    def create_fpga_image(
        self, **kwargs: Unpack[CreateFpgaImageRequestTypeDef]
    ) -> CreateFpgaImageResultTypeDef:
        """
        Creates an Amazon FPGA Image (AFI) from the specified design checkpoint (DCP).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_fpga_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_fpga_image)
        """

    def create_image(self, **kwargs: Unpack[CreateImageRequestTypeDef]) -> CreateImageResultTypeDef:
        """
        Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is
        either running or stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_image)
        """

    def create_instance_connect_endpoint(
        self, **kwargs: Unpack[CreateInstanceConnectEndpointRequestTypeDef]
    ) -> CreateInstanceConnectEndpointResultTypeDef:
        """
        Creates an EC2 Instance Connect Endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_instance_connect_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_instance_connect_endpoint)
        """

    def create_instance_event_window(
        self, **kwargs: Unpack[CreateInstanceEventWindowRequestTypeDef]
    ) -> CreateInstanceEventWindowResultTypeDef:
        """
        Creates an event window in which scheduled events for the associated Amazon EC2
        instances can run.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_instance_event_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_instance_event_window)
        """

    def create_instance_export_task(
        self, **kwargs: Unpack[CreateInstanceExportTaskRequestTypeDef]
    ) -> CreateInstanceExportTaskResultTypeDef:
        """
        Exports a running or stopped instance to an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_instance_export_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_instance_export_task)
        """

    def create_internet_gateway(
        self, **kwargs: Unpack[CreateInternetGatewayRequestTypeDef]
    ) -> CreateInternetGatewayResultTypeDef:
        """
        Creates an internet gateway for use with a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_internet_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_internet_gateway)
        """

    def create_ipam(self, **kwargs: Unpack[CreateIpamRequestTypeDef]) -> CreateIpamResultTypeDef:
        """
        Create an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_ipam.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_ipam)
        """

    def create_ipam_external_resource_verification_token(
        self, **kwargs: Unpack[CreateIpamExternalResourceVerificationTokenRequestTypeDef]
    ) -> CreateIpamExternalResourceVerificationTokenResultTypeDef:
        """
        Create a verification token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_ipam_external_resource_verification_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_ipam_external_resource_verification_token)
        """

    def create_ipam_pool(
        self, **kwargs: Unpack[CreateIpamPoolRequestTypeDef]
    ) -> CreateIpamPoolResultTypeDef:
        """
        Create an IP address pool for Amazon VPC IP Address Manager (IPAM).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_ipam_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_ipam_pool)
        """

    def create_ipam_resource_discovery(
        self, **kwargs: Unpack[CreateIpamResourceDiscoveryRequestTypeDef]
    ) -> CreateIpamResourceDiscoveryResultTypeDef:
        """
        Creates an IPAM resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_ipam_resource_discovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_ipam_resource_discovery)
        """

    def create_ipam_scope(
        self, **kwargs: Unpack[CreateIpamScopeRequestTypeDef]
    ) -> CreateIpamScopeResultTypeDef:
        """
        Create an IPAM scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_ipam_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_ipam_scope)
        """

    def create_key_pair(self, **kwargs: Unpack[CreateKeyPairRequestTypeDef]) -> KeyPairTypeDef:
        """
        Creates an ED25519 or 2048-bit RSA key pair with the specified name and in the
        specified format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_key_pair)
        """

    def create_launch_template(
        self, **kwargs: Unpack[CreateLaunchTemplateRequestTypeDef]
    ) -> CreateLaunchTemplateResultTypeDef:
        """
        Creates a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_launch_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_launch_template)
        """

    def create_launch_template_version(
        self, **kwargs: Unpack[CreateLaunchTemplateVersionRequestTypeDef]
    ) -> CreateLaunchTemplateVersionResultTypeDef:
        """
        Creates a new version of a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_launch_template_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_launch_template_version)
        """

    def create_local_gateway_route(
        self, **kwargs: Unpack[CreateLocalGatewayRouteRequestTypeDef]
    ) -> CreateLocalGatewayRouteResultTypeDef:
        """
        Creates a static route for the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_local_gateway_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_route)
        """

    def create_local_gateway_route_table(
        self, **kwargs: Unpack[CreateLocalGatewayRouteTableRequestTypeDef]
    ) -> CreateLocalGatewayRouteTableResultTypeDef:
        """
        Creates a local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_local_gateway_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_route_table)
        """

    def create_local_gateway_route_table_virtual_interface_group_association(
        self,
        **kwargs: Unpack[
            CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestTypeDef
        ],
    ) -> CreateLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef:
        """
        Creates a local gateway route table virtual interface group association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_local_gateway_route_table_virtual_interface_group_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_route_table_virtual_interface_group_association)
        """

    def create_local_gateway_route_table_vpc_association(
        self, **kwargs: Unpack[CreateLocalGatewayRouteTableVpcAssociationRequestTypeDef]
    ) -> CreateLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        Associates the specified VPC with the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_local_gateway_route_table_vpc_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_route_table_vpc_association)
        """

    def create_local_gateway_virtual_interface(
        self, **kwargs: Unpack[CreateLocalGatewayVirtualInterfaceRequestTypeDef]
    ) -> CreateLocalGatewayVirtualInterfaceResultTypeDef:
        """
        Create a virtual interface for a local gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_local_gateway_virtual_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_virtual_interface)
        """

    def create_local_gateway_virtual_interface_group(
        self, **kwargs: Unpack[CreateLocalGatewayVirtualInterfaceGroupRequestTypeDef]
    ) -> CreateLocalGatewayVirtualInterfaceGroupResultTypeDef:
        """
        Create a local gateway virtual interface group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_local_gateway_virtual_interface_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_local_gateway_virtual_interface_group)
        """

    def create_managed_prefix_list(
        self, **kwargs: Unpack[CreateManagedPrefixListRequestTypeDef]
    ) -> CreateManagedPrefixListResultTypeDef:
        """
        Creates a managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_managed_prefix_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_managed_prefix_list)
        """

    def create_nat_gateway(
        self, **kwargs: Unpack[CreateNatGatewayRequestTypeDef]
    ) -> CreateNatGatewayResultTypeDef:
        """
        Creates a NAT gateway in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_nat_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_nat_gateway)
        """

    def create_network_acl(
        self, **kwargs: Unpack[CreateNetworkAclRequestTypeDef]
    ) -> CreateNetworkAclResultTypeDef:
        """
        Creates a network ACL in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_network_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_acl)
        """

    def create_network_acl_entry(
        self, **kwargs: Unpack[CreateNetworkAclEntryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates an entry (a rule) in a network ACL with the specified rule number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_network_acl_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_acl_entry)
        """

    def create_network_insights_access_scope(
        self, **kwargs: Unpack[CreateNetworkInsightsAccessScopeRequestTypeDef]
    ) -> CreateNetworkInsightsAccessScopeResultTypeDef:
        """
        Creates a Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_network_insights_access_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_insights_access_scope)
        """

    def create_network_insights_path(
        self, **kwargs: Unpack[CreateNetworkInsightsPathRequestTypeDef]
    ) -> CreateNetworkInsightsPathResultTypeDef:
        """
        Creates a path to analyze for reachability.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_network_insights_path.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_insights_path)
        """

    def create_network_interface(
        self, **kwargs: Unpack[CreateNetworkInterfaceRequestTypeDef]
    ) -> CreateNetworkInterfaceResultTypeDef:
        """
        Creates a network interface in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_interface)
        """

    def create_network_interface_permission(
        self, **kwargs: Unpack[CreateNetworkInterfacePermissionRequestTypeDef]
    ) -> CreateNetworkInterfacePermissionResultTypeDef:
        """
        Grants an Amazon Web Services-authorized account permission to attach the
        specified network interface to an instance in their account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_network_interface_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_network_interface_permission)
        """

    def create_placement_group(
        self, **kwargs: Unpack[CreatePlacementGroupRequestTypeDef]
    ) -> CreatePlacementGroupResultTypeDef:
        """
        Creates a placement group in which to launch instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_placement_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_placement_group)
        """

    def create_public_ipv4_pool(
        self, **kwargs: Unpack[CreatePublicIpv4PoolRequestTypeDef]
    ) -> CreatePublicIpv4PoolResultTypeDef:
        """
        Creates a public IPv4 address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_public_ipv4_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_public_ipv4_pool)
        """

    def create_replace_root_volume_task(
        self, **kwargs: Unpack[CreateReplaceRootVolumeTaskRequestTypeDef]
    ) -> CreateReplaceRootVolumeTaskResultTypeDef:
        """
        Replaces the EBS-backed root volume for a <code>running</code> instance with a
        new volume that is restored to the original root volume's launch state, that is
        restored to a specific snapshot taken from the original root volume, or that is
        restored from an AMI that has the same key characteristics...

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_replace_root_volume_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_replace_root_volume_task)
        """

    def create_reserved_instances_listing(
        self, **kwargs: Unpack[CreateReservedInstancesListingRequestTypeDef]
    ) -> CreateReservedInstancesListingResultTypeDef:
        """
        Creates a listing for Amazon EC2 Standard Reserved Instances to be sold in the
        Reserved Instance Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_reserved_instances_listing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_reserved_instances_listing)
        """

    def create_restore_image_task(
        self, **kwargs: Unpack[CreateRestoreImageTaskRequestTypeDef]
    ) -> CreateRestoreImageTaskResultTypeDef:
        """
        Starts a task that restores an AMI from an Amazon S3 object that was previously
        created by using <a
        href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateStoreImageTask.html">CreateStoreImageTask</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_restore_image_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_restore_image_task)
        """

    def create_route(self, **kwargs: Unpack[CreateRouteRequestTypeDef]) -> CreateRouteResultTypeDef:
        """
        Creates a route in a route table within a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_route)
        """

    def create_route_server(
        self, **kwargs: Unpack[CreateRouteServerRequestTypeDef]
    ) -> CreateRouteServerResultTypeDef:
        """
        Creates a new route server to manage dynamic routing in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_route_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_route_server)
        """

    def create_route_server_endpoint(
        self, **kwargs: Unpack[CreateRouteServerEndpointRequestTypeDef]
    ) -> CreateRouteServerEndpointResultTypeDef:
        """
        Creates a new endpoint for a route server in a specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_route_server_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_route_server_endpoint)
        """

    def create_route_server_peer(
        self, **kwargs: Unpack[CreateRouteServerPeerRequestTypeDef]
    ) -> CreateRouteServerPeerResultTypeDef:
        """
        Creates a new BGP peer for a specified route server endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_route_server_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_route_server_peer)
        """

    def create_route_table(
        self, **kwargs: Unpack[CreateRouteTableRequestTypeDef]
    ) -> CreateRouteTableResultTypeDef:
        """
        Creates a route table for the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_route_table)
        """

    def create_security_group(
        self, **kwargs: Unpack[CreateSecurityGroupRequestTypeDef]
    ) -> CreateSecurityGroupResultTypeDef:
        """
        Creates a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_security_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_security_group)
        """

    def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotRequestTypeDef]
    ) -> SnapshotResponseTypeDef:
        """
        Creates a snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_snapshot)
        """

    def create_snapshots(
        self, **kwargs: Unpack[CreateSnapshotsRequestTypeDef]
    ) -> CreateSnapshotsResultTypeDef:
        """
        Creates crash-consistent snapshots of multiple EBS volumes attached to an
        Amazon EC2 instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_snapshots)
        """

    def create_spot_datafeed_subscription(
        self, **kwargs: Unpack[CreateSpotDatafeedSubscriptionRequestTypeDef]
    ) -> CreateSpotDatafeedSubscriptionResultTypeDef:
        """
        Creates a data feed for Spot Instances, enabling you to view Spot Instance
        usage logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_spot_datafeed_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_spot_datafeed_subscription)
        """

    def create_store_image_task(
        self, **kwargs: Unpack[CreateStoreImageTaskRequestTypeDef]
    ) -> CreateStoreImageTaskResultTypeDef:
        """
        Stores an AMI as a single object in an Amazon S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_store_image_task.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_store_image_task)
        """

    def create_subnet(
        self, **kwargs: Unpack[CreateSubnetRequestTypeDef]
    ) -> CreateSubnetResultTypeDef:
        """
        Creates a subnet in the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_subnet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_subnet)
        """

    def create_subnet_cidr_reservation(
        self, **kwargs: Unpack[CreateSubnetCidrReservationRequestTypeDef]
    ) -> CreateSubnetCidrReservationResultTypeDef:
        """
        Creates a subnet CIDR reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_subnet_cidr_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_subnet_cidr_reservation)
        """

    def create_tags(self, **kwargs: Unpack[ClientCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_tags)
        """

    def create_traffic_mirror_filter(
        self, **kwargs: Unpack[CreateTrafficMirrorFilterRequestTypeDef]
    ) -> CreateTrafficMirrorFilterResultTypeDef:
        """
        Creates a Traffic Mirror filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_traffic_mirror_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_traffic_mirror_filter)
        """

    def create_traffic_mirror_filter_rule(
        self, **kwargs: Unpack[CreateTrafficMirrorFilterRuleRequestTypeDef]
    ) -> CreateTrafficMirrorFilterRuleResultTypeDef:
        """
        Creates a Traffic Mirror filter rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_traffic_mirror_filter_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_traffic_mirror_filter_rule)
        """

    def create_traffic_mirror_session(
        self, **kwargs: Unpack[CreateTrafficMirrorSessionRequestTypeDef]
    ) -> CreateTrafficMirrorSessionResultTypeDef:
        """
        Creates a Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_traffic_mirror_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_traffic_mirror_session)
        """

    def create_traffic_mirror_target(
        self, **kwargs: Unpack[CreateTrafficMirrorTargetRequestTypeDef]
    ) -> CreateTrafficMirrorTargetResultTypeDef:
        """
        Creates a target for your Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_traffic_mirror_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_traffic_mirror_target)
        """

    def create_transit_gateway(
        self, **kwargs: Unpack[CreateTransitGatewayRequestTypeDef]
    ) -> CreateTransitGatewayResultTypeDef:
        """
        Creates a transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway)
        """

    def create_transit_gateway_connect(
        self, **kwargs: Unpack[CreateTransitGatewayConnectRequestTypeDef]
    ) -> CreateTransitGatewayConnectResultTypeDef:
        """
        Creates a Connect attachment from a specified transit gateway attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_connect.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_connect)
        """

    def create_transit_gateway_connect_peer(
        self, **kwargs: Unpack[CreateTransitGatewayConnectPeerRequestTypeDef]
    ) -> CreateTransitGatewayConnectPeerResultTypeDef:
        """
        Creates a Connect peer for a specified transit gateway Connect attachment
        between a transit gateway and an appliance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_connect_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_connect_peer)
        """

    def create_transit_gateway_multicast_domain(
        self, **kwargs: Unpack[CreateTransitGatewayMulticastDomainRequestTypeDef]
    ) -> CreateTransitGatewayMulticastDomainResultTypeDef:
        """
        Creates a multicast domain using the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_multicast_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_multicast_domain)
        """

    def create_transit_gateway_peering_attachment(
        self, **kwargs: Unpack[CreateTransitGatewayPeeringAttachmentRequestTypeDef]
    ) -> CreateTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Requests a transit gateway peering attachment between the specified transit
        gateway (requester) and a peer transit gateway (accepter).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_peering_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_peering_attachment)
        """

    def create_transit_gateway_policy_table(
        self, **kwargs: Unpack[CreateTransitGatewayPolicyTableRequestTypeDef]
    ) -> CreateTransitGatewayPolicyTableResultTypeDef:
        """
        Creates a transit gateway policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_policy_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_policy_table)
        """

    def create_transit_gateway_prefix_list_reference(
        self, **kwargs: Unpack[CreateTransitGatewayPrefixListReferenceRequestTypeDef]
    ) -> CreateTransitGatewayPrefixListReferenceResultTypeDef:
        """
        Creates a reference (route) to a prefix list in a specified transit gateway
        route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_prefix_list_reference.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_prefix_list_reference)
        """

    def create_transit_gateway_route(
        self, **kwargs: Unpack[CreateTransitGatewayRouteRequestTypeDef]
    ) -> CreateTransitGatewayRouteResultTypeDef:
        """
        Creates a static route for the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_route)
        """

    def create_transit_gateway_route_table(
        self, **kwargs: Unpack[CreateTransitGatewayRouteTableRequestTypeDef]
    ) -> CreateTransitGatewayRouteTableResultTypeDef:
        """
        Creates a route table for the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_route_table)
        """

    def create_transit_gateway_route_table_announcement(
        self, **kwargs: Unpack[CreateTransitGatewayRouteTableAnnouncementRequestTypeDef]
    ) -> CreateTransitGatewayRouteTableAnnouncementResultTypeDef:
        """
        Advertises a new transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_route_table_announcement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_route_table_announcement)
        """

    def create_transit_gateway_vpc_attachment(
        self, **kwargs: Unpack[CreateTransitGatewayVpcAttachmentRequestTypeDef]
    ) -> CreateTransitGatewayVpcAttachmentResultTypeDef:
        """
        Attaches the specified VPC to the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_transit_gateway_vpc_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_transit_gateway_vpc_attachment)
        """

    def create_verified_access_endpoint(
        self, **kwargs: Unpack[CreateVerifiedAccessEndpointRequestTypeDef]
    ) -> CreateVerifiedAccessEndpointResultTypeDef:
        """
        An Amazon Web Services Verified Access endpoint is where you define your
        application along with an optional endpoint-level access policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_verified_access_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_verified_access_endpoint)
        """

    def create_verified_access_group(
        self, **kwargs: Unpack[CreateVerifiedAccessGroupRequestTypeDef]
    ) -> CreateVerifiedAccessGroupResultTypeDef:
        """
        An Amazon Web Services Verified Access group is a collection of Amazon Web
        Services Verified Access endpoints who's associated applications have similar
        security requirements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_verified_access_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_verified_access_group)
        """

    def create_verified_access_instance(
        self, **kwargs: Unpack[CreateVerifiedAccessInstanceRequestTypeDef]
    ) -> CreateVerifiedAccessInstanceResultTypeDef:
        """
        An Amazon Web Services Verified Access instance is a regional entity that
        evaluates application requests and grants access only when your security
        requirements are met.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_verified_access_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_verified_access_instance)
        """

    def create_verified_access_trust_provider(
        self, **kwargs: Unpack[CreateVerifiedAccessTrustProviderRequestTypeDef]
    ) -> CreateVerifiedAccessTrustProviderResultTypeDef:
        """
        A trust provider is a third-party entity that creates, maintains, and manages
        identity information for users and devices.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_verified_access_trust_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_verified_access_trust_provider)
        """

    def create_volume(self, **kwargs: Unpack[CreateVolumeRequestTypeDef]) -> VolumeResponseTypeDef:
        """
        Creates an EBS volume that can be attached to an instance in the same
        Availability Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_volume)
        """

    def create_vpc(self, **kwargs: Unpack[CreateVpcRequestTypeDef]) -> CreateVpcResultTypeDef:
        """
        Creates a VPC with the specified CIDR blocks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc)
        """

    def create_vpc_block_public_access_exclusion(
        self, **kwargs: Unpack[CreateVpcBlockPublicAccessExclusionRequestTypeDef]
    ) -> CreateVpcBlockPublicAccessExclusionResultTypeDef:
        """
        Create a VPC Block Public Access (BPA) exclusion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_vpc_block_public_access_exclusion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc_block_public_access_exclusion)
        """

    def create_vpc_endpoint(
        self, **kwargs: Unpack[CreateVpcEndpointRequestTypeDef]
    ) -> CreateVpcEndpointResultTypeDef:
        """
        Creates a VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_vpc_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc_endpoint)
        """

    def create_vpc_endpoint_connection_notification(
        self, **kwargs: Unpack[CreateVpcEndpointConnectionNotificationRequestTypeDef]
    ) -> CreateVpcEndpointConnectionNotificationResultTypeDef:
        """
        Creates a connection notification for a specified VPC endpoint or VPC endpoint
        service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_vpc_endpoint_connection_notification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc_endpoint_connection_notification)
        """

    def create_vpc_endpoint_service_configuration(
        self, **kwargs: Unpack[CreateVpcEndpointServiceConfigurationRequestTypeDef]
    ) -> CreateVpcEndpointServiceConfigurationResultTypeDef:
        """
        Creates a VPC endpoint service to which service consumers (Amazon Web Services
        accounts, users, and IAM roles) can connect.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_vpc_endpoint_service_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc_endpoint_service_configuration)
        """

    def create_vpc_peering_connection(
        self, **kwargs: Unpack[CreateVpcPeeringConnectionRequestTypeDef]
    ) -> CreateVpcPeeringConnectionResultTypeDef:
        """
        Requests a VPC peering connection between two VPCs: a requester VPC that you
        own and an accepter VPC with which to create the connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_vpc_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpc_peering_connection)
        """

    def create_vpn_connection(
        self, **kwargs: Unpack[CreateVpnConnectionRequestTypeDef]
    ) -> CreateVpnConnectionResultTypeDef:
        """
        Creates a VPN connection between an existing virtual private gateway or transit
        gateway and a customer gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_vpn_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpn_connection)
        """

    def create_vpn_connection_route(
        self, **kwargs: Unpack[CreateVpnConnectionRouteRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Creates a static route associated with a VPN connection between an existing
        virtual private gateway and a VPN customer gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_vpn_connection_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpn_connection_route)
        """

    def create_vpn_gateway(
        self, **kwargs: Unpack[CreateVpnGatewayRequestTypeDef]
    ) -> CreateVpnGatewayResultTypeDef:
        """
        Creates a virtual private gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/create_vpn_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#create_vpn_gateway)
        """

    def delete_carrier_gateway(
        self, **kwargs: Unpack[DeleteCarrierGatewayRequestTypeDef]
    ) -> DeleteCarrierGatewayResultTypeDef:
        """
        Deletes a carrier gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_carrier_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_carrier_gateway)
        """

    def delete_client_vpn_endpoint(
        self, **kwargs: Unpack[DeleteClientVpnEndpointRequestTypeDef]
    ) -> DeleteClientVpnEndpointResultTypeDef:
        """
        Deletes the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_client_vpn_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_client_vpn_endpoint)
        """

    def delete_client_vpn_route(
        self, **kwargs: Unpack[DeleteClientVpnRouteRequestTypeDef]
    ) -> DeleteClientVpnRouteResultTypeDef:
        """
        Deletes a route from a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_client_vpn_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_client_vpn_route)
        """

    def delete_coip_cidr(
        self, **kwargs: Unpack[DeleteCoipCidrRequestTypeDef]
    ) -> DeleteCoipCidrResultTypeDef:
        """
        Deletes a range of customer-owned IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_coip_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_coip_cidr)
        """

    def delete_coip_pool(
        self, **kwargs: Unpack[DeleteCoipPoolRequestTypeDef]
    ) -> DeleteCoipPoolResultTypeDef:
        """
        Deletes a pool of customer-owned IP (CoIP) addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_coip_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_coip_pool)
        """

    def delete_customer_gateway(
        self, **kwargs: Unpack[DeleteCustomerGatewayRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified customer gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_customer_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_customer_gateway)
        """

    def delete_dhcp_options(
        self, **kwargs: Unpack[DeleteDhcpOptionsRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified set of DHCP options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_dhcp_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_dhcp_options)
        """

    def delete_egress_only_internet_gateway(
        self, **kwargs: Unpack[DeleteEgressOnlyInternetGatewayRequestTypeDef]
    ) -> DeleteEgressOnlyInternetGatewayResultTypeDef:
        """
        Deletes an egress-only internet gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_egress_only_internet_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_egress_only_internet_gateway)
        """

    def delete_fleets(
        self, **kwargs: Unpack[DeleteFleetsRequestTypeDef]
    ) -> DeleteFleetsResultTypeDef:
        """
        Deletes the specified EC2 Fleet request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_fleets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_fleets)
        """

    def delete_flow_logs(
        self, **kwargs: Unpack[DeleteFlowLogsRequestTypeDef]
    ) -> DeleteFlowLogsResultTypeDef:
        """
        Deletes one or more flow logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_flow_logs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_flow_logs)
        """

    def delete_fpga_image(
        self, **kwargs: Unpack[DeleteFpgaImageRequestTypeDef]
    ) -> DeleteFpgaImageResultTypeDef:
        """
        Deletes the specified Amazon FPGA Image (AFI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_fpga_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_fpga_image)
        """

    def delete_instance_connect_endpoint(
        self, **kwargs: Unpack[DeleteInstanceConnectEndpointRequestTypeDef]
    ) -> DeleteInstanceConnectEndpointResultTypeDef:
        """
        Deletes the specified EC2 Instance Connect Endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_instance_connect_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_instance_connect_endpoint)
        """

    def delete_instance_event_window(
        self, **kwargs: Unpack[DeleteInstanceEventWindowRequestTypeDef]
    ) -> DeleteInstanceEventWindowResultTypeDef:
        """
        Deletes the specified event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_instance_event_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_instance_event_window)
        """

    def delete_internet_gateway(
        self, **kwargs: Unpack[DeleteInternetGatewayRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified internet gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_internet_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_internet_gateway)
        """

    def delete_ipam(self, **kwargs: Unpack[DeleteIpamRequestTypeDef]) -> DeleteIpamResultTypeDef:
        """
        Delete an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_ipam.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_ipam)
        """

    def delete_ipam_external_resource_verification_token(
        self, **kwargs: Unpack[DeleteIpamExternalResourceVerificationTokenRequestTypeDef]
    ) -> DeleteIpamExternalResourceVerificationTokenResultTypeDef:
        """
        Delete a verification token.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_ipam_external_resource_verification_token.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_ipam_external_resource_verification_token)
        """

    def delete_ipam_pool(
        self, **kwargs: Unpack[DeleteIpamPoolRequestTypeDef]
    ) -> DeleteIpamPoolResultTypeDef:
        """
        Delete an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_ipam_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_ipam_pool)
        """

    def delete_ipam_resource_discovery(
        self, **kwargs: Unpack[DeleteIpamResourceDiscoveryRequestTypeDef]
    ) -> DeleteIpamResourceDiscoveryResultTypeDef:
        """
        Deletes an IPAM resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_ipam_resource_discovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_ipam_resource_discovery)
        """

    def delete_ipam_scope(
        self, **kwargs: Unpack[DeleteIpamScopeRequestTypeDef]
    ) -> DeleteIpamScopeResultTypeDef:
        """
        Delete the scope for an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_ipam_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_ipam_scope)
        """

    def delete_key_pair(
        self, **kwargs: Unpack[DeleteKeyPairRequestTypeDef]
    ) -> DeleteKeyPairResultTypeDef:
        """
        Deletes the specified key pair, by removing the public key from Amazon EC2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_key_pair)
        """

    def delete_launch_template(
        self, **kwargs: Unpack[DeleteLaunchTemplateRequestTypeDef]
    ) -> DeleteLaunchTemplateResultTypeDef:
        """
        Deletes a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_launch_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_launch_template)
        """

    def delete_launch_template_versions(
        self, **kwargs: Unpack[DeleteLaunchTemplateVersionsRequestTypeDef]
    ) -> DeleteLaunchTemplateVersionsResultTypeDef:
        """
        Deletes one or more versions of a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_launch_template_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_launch_template_versions)
        """

    def delete_local_gateway_route(
        self, **kwargs: Unpack[DeleteLocalGatewayRouteRequestTypeDef]
    ) -> DeleteLocalGatewayRouteResultTypeDef:
        """
        Deletes the specified route from the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_local_gateway_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_route)
        """

    def delete_local_gateway_route_table(
        self, **kwargs: Unpack[DeleteLocalGatewayRouteTableRequestTypeDef]
    ) -> DeleteLocalGatewayRouteTableResultTypeDef:
        """
        Deletes a local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_local_gateway_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_route_table)
        """

    def delete_local_gateway_route_table_virtual_interface_group_association(
        self,
        **kwargs: Unpack[
            DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationRequestTypeDef
        ],
    ) -> DeleteLocalGatewayRouteTableVirtualInterfaceGroupAssociationResultTypeDef:
        """
        Deletes a local gateway route table virtual interface group association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_local_gateway_route_table_virtual_interface_group_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_route_table_virtual_interface_group_association)
        """

    def delete_local_gateway_route_table_vpc_association(
        self, **kwargs: Unpack[DeleteLocalGatewayRouteTableVpcAssociationRequestTypeDef]
    ) -> DeleteLocalGatewayRouteTableVpcAssociationResultTypeDef:
        """
        Deletes the specified association between a VPC and local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_local_gateway_route_table_vpc_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_route_table_vpc_association)
        """

    def delete_local_gateway_virtual_interface(
        self, **kwargs: Unpack[DeleteLocalGatewayVirtualInterfaceRequestTypeDef]
    ) -> DeleteLocalGatewayVirtualInterfaceResultTypeDef:
        """
        Deletes the specified local gateway virtual interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_local_gateway_virtual_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_virtual_interface)
        """

    def delete_local_gateway_virtual_interface_group(
        self, **kwargs: Unpack[DeleteLocalGatewayVirtualInterfaceGroupRequestTypeDef]
    ) -> DeleteLocalGatewayVirtualInterfaceGroupResultTypeDef:
        """
        Delete the specified local gateway interface group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_local_gateway_virtual_interface_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_local_gateway_virtual_interface_group)
        """

    def delete_managed_prefix_list(
        self, **kwargs: Unpack[DeleteManagedPrefixListRequestTypeDef]
    ) -> DeleteManagedPrefixListResultTypeDef:
        """
        Deletes the specified managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_managed_prefix_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_managed_prefix_list)
        """

    def delete_nat_gateway(
        self, **kwargs: Unpack[DeleteNatGatewayRequestTypeDef]
    ) -> DeleteNatGatewayResultTypeDef:
        """
        Deletes the specified NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_nat_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_nat_gateway)
        """

    def delete_network_acl(
        self, **kwargs: Unpack[DeleteNetworkAclRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_network_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_acl)
        """

    def delete_network_acl_entry(
        self, **kwargs: Unpack[DeleteNetworkAclEntryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified ingress or egress entry (rule) from the specified network
        ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_network_acl_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_acl_entry)
        """

    def delete_network_insights_access_scope(
        self, **kwargs: Unpack[DeleteNetworkInsightsAccessScopeRequestTypeDef]
    ) -> DeleteNetworkInsightsAccessScopeResultTypeDef:
        """
        Deletes the specified Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_network_insights_access_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_insights_access_scope)
        """

    def delete_network_insights_access_scope_analysis(
        self, **kwargs: Unpack[DeleteNetworkInsightsAccessScopeAnalysisRequestTypeDef]
    ) -> DeleteNetworkInsightsAccessScopeAnalysisResultTypeDef:
        """
        Deletes the specified Network Access Scope analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_network_insights_access_scope_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_insights_access_scope_analysis)
        """

    def delete_network_insights_analysis(
        self, **kwargs: Unpack[DeleteNetworkInsightsAnalysisRequestTypeDef]
    ) -> DeleteNetworkInsightsAnalysisResultTypeDef:
        """
        Deletes the specified network insights analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_network_insights_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_insights_analysis)
        """

    def delete_network_insights_path(
        self, **kwargs: Unpack[DeleteNetworkInsightsPathRequestTypeDef]
    ) -> DeleteNetworkInsightsPathResultTypeDef:
        """
        Deletes the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_network_insights_path.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_insights_path)
        """

    def delete_network_interface(
        self, **kwargs: Unpack[DeleteNetworkInterfaceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_interface)
        """

    def delete_network_interface_permission(
        self, **kwargs: Unpack[DeleteNetworkInterfacePermissionRequestTypeDef]
    ) -> DeleteNetworkInterfacePermissionResultTypeDef:
        """
        Deletes a permission for a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_network_interface_permission.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_network_interface_permission)
        """

    def delete_placement_group(
        self, **kwargs: Unpack[DeletePlacementGroupRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified placement group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_placement_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_placement_group)
        """

    def delete_public_ipv4_pool(
        self, **kwargs: Unpack[DeletePublicIpv4PoolRequestTypeDef]
    ) -> DeletePublicIpv4PoolResultTypeDef:
        """
        Delete a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_public_ipv4_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_public_ipv4_pool)
        """

    def delete_queued_reserved_instances(
        self, **kwargs: Unpack[DeleteQueuedReservedInstancesRequestTypeDef]
    ) -> DeleteQueuedReservedInstancesResultTypeDef:
        """
        Deletes the queued purchases for the specified Reserved Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_queued_reserved_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_queued_reserved_instances)
        """

    def delete_route(
        self, **kwargs: Unpack[DeleteRouteRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified route from the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_route)
        """

    def delete_route_server(
        self, **kwargs: Unpack[DeleteRouteServerRequestTypeDef]
    ) -> DeleteRouteServerResultTypeDef:
        """
        Deletes the specified route server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_route_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_route_server)
        """

    def delete_route_server_endpoint(
        self, **kwargs: Unpack[DeleteRouteServerEndpointRequestTypeDef]
    ) -> DeleteRouteServerEndpointResultTypeDef:
        """
        Deletes the specified route server endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_route_server_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_route_server_endpoint)
        """

    def delete_route_server_peer(
        self, **kwargs: Unpack[DeleteRouteServerPeerRequestTypeDef]
    ) -> DeleteRouteServerPeerResultTypeDef:
        """
        Deletes the specified BGP peer from a route server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_route_server_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_route_server_peer)
        """

    def delete_route_table(
        self, **kwargs: Unpack[DeleteRouteTableRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_route_table)
        """

    def delete_security_group(
        self, **kwargs: Unpack[DeleteSecurityGroupRequestTypeDef]
    ) -> DeleteSecurityGroupResultTypeDef:
        """
        Deletes a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_security_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_security_group)
        """

    def delete_snapshot(
        self, **kwargs: Unpack[DeleteSnapshotRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_snapshot)
        """

    def delete_spot_datafeed_subscription(
        self, **kwargs: Unpack[DeleteSpotDatafeedSubscriptionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the data feed for Spot Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_spot_datafeed_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_spot_datafeed_subscription)
        """

    def delete_subnet(
        self, **kwargs: Unpack[DeleteSubnetRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_subnet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_subnet)
        """

    def delete_subnet_cidr_reservation(
        self, **kwargs: Unpack[DeleteSubnetCidrReservationRequestTypeDef]
    ) -> DeleteSubnetCidrReservationResultTypeDef:
        """
        Deletes a subnet CIDR reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_subnet_cidr_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_subnet_cidr_reservation)
        """

    def delete_tags(self, **kwargs: Unpack[ClientDeleteTagsRequestTypeDef]) -> None:
        """
        Deletes the specified set of tags from the specified set of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_tags)
        """

    def delete_traffic_mirror_filter(
        self, **kwargs: Unpack[DeleteTrafficMirrorFilterRequestTypeDef]
    ) -> DeleteTrafficMirrorFilterResultTypeDef:
        """
        Deletes the specified Traffic Mirror filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_traffic_mirror_filter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_traffic_mirror_filter)
        """

    def delete_traffic_mirror_filter_rule(
        self, **kwargs: Unpack[DeleteTrafficMirrorFilterRuleRequestTypeDef]
    ) -> DeleteTrafficMirrorFilterRuleResultTypeDef:
        """
        Deletes the specified Traffic Mirror rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_traffic_mirror_filter_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_traffic_mirror_filter_rule)
        """

    def delete_traffic_mirror_session(
        self, **kwargs: Unpack[DeleteTrafficMirrorSessionRequestTypeDef]
    ) -> DeleteTrafficMirrorSessionResultTypeDef:
        """
        Deletes the specified Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_traffic_mirror_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_traffic_mirror_session)
        """

    def delete_traffic_mirror_target(
        self, **kwargs: Unpack[DeleteTrafficMirrorTargetRequestTypeDef]
    ) -> DeleteTrafficMirrorTargetResultTypeDef:
        """
        Deletes the specified Traffic Mirror target.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_traffic_mirror_target.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_traffic_mirror_target)
        """

    def delete_transit_gateway(
        self, **kwargs: Unpack[DeleteTransitGatewayRequestTypeDef]
    ) -> DeleteTransitGatewayResultTypeDef:
        """
        Deletes the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway)
        """

    def delete_transit_gateway_connect(
        self, **kwargs: Unpack[DeleteTransitGatewayConnectRequestTypeDef]
    ) -> DeleteTransitGatewayConnectResultTypeDef:
        """
        Deletes the specified Connect attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_connect.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_connect)
        """

    def delete_transit_gateway_connect_peer(
        self, **kwargs: Unpack[DeleteTransitGatewayConnectPeerRequestTypeDef]
    ) -> DeleteTransitGatewayConnectPeerResultTypeDef:
        """
        Deletes the specified Connect peer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_connect_peer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_connect_peer)
        """

    def delete_transit_gateway_multicast_domain(
        self, **kwargs: Unpack[DeleteTransitGatewayMulticastDomainRequestTypeDef]
    ) -> DeleteTransitGatewayMulticastDomainResultTypeDef:
        """
        Deletes the specified transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_multicast_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_multicast_domain)
        """

    def delete_transit_gateway_peering_attachment(
        self, **kwargs: Unpack[DeleteTransitGatewayPeeringAttachmentRequestTypeDef]
    ) -> DeleteTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Deletes a transit gateway peering attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_peering_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_peering_attachment)
        """

    def delete_transit_gateway_policy_table(
        self, **kwargs: Unpack[DeleteTransitGatewayPolicyTableRequestTypeDef]
    ) -> DeleteTransitGatewayPolicyTableResultTypeDef:
        """
        Deletes the specified transit gateway policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_policy_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_policy_table)
        """

    def delete_transit_gateway_prefix_list_reference(
        self, **kwargs: Unpack[DeleteTransitGatewayPrefixListReferenceRequestTypeDef]
    ) -> DeleteTransitGatewayPrefixListReferenceResultTypeDef:
        """
        Deletes a reference (route) to a prefix list in a specified transit gateway
        route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_prefix_list_reference.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_prefix_list_reference)
        """

    def delete_transit_gateway_route(
        self, **kwargs: Unpack[DeleteTransitGatewayRouteRequestTypeDef]
    ) -> DeleteTransitGatewayRouteResultTypeDef:
        """
        Deletes the specified route from the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_route)
        """

    def delete_transit_gateway_route_table(
        self, **kwargs: Unpack[DeleteTransitGatewayRouteTableRequestTypeDef]
    ) -> DeleteTransitGatewayRouteTableResultTypeDef:
        """
        Deletes the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_route_table)
        """

    def delete_transit_gateway_route_table_announcement(
        self, **kwargs: Unpack[DeleteTransitGatewayRouteTableAnnouncementRequestTypeDef]
    ) -> DeleteTransitGatewayRouteTableAnnouncementResultTypeDef:
        """
        Advertises to the transit gateway that a transit gateway route table is deleted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_route_table_announcement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_route_table_announcement)
        """

    def delete_transit_gateway_vpc_attachment(
        self, **kwargs: Unpack[DeleteTransitGatewayVpcAttachmentRequestTypeDef]
    ) -> DeleteTransitGatewayVpcAttachmentResultTypeDef:
        """
        Deletes the specified VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_transit_gateway_vpc_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_transit_gateway_vpc_attachment)
        """

    def delete_verified_access_endpoint(
        self, **kwargs: Unpack[DeleteVerifiedAccessEndpointRequestTypeDef]
    ) -> DeleteVerifiedAccessEndpointResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_verified_access_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_verified_access_endpoint)
        """

    def delete_verified_access_group(
        self, **kwargs: Unpack[DeleteVerifiedAccessGroupRequestTypeDef]
    ) -> DeleteVerifiedAccessGroupResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_verified_access_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_verified_access_group)
        """

    def delete_verified_access_instance(
        self, **kwargs: Unpack[DeleteVerifiedAccessInstanceRequestTypeDef]
    ) -> DeleteVerifiedAccessInstanceResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_verified_access_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_verified_access_instance)
        """

    def delete_verified_access_trust_provider(
        self, **kwargs: Unpack[DeleteVerifiedAccessTrustProviderRequestTypeDef]
    ) -> DeleteVerifiedAccessTrustProviderResultTypeDef:
        """
        Delete an Amazon Web Services Verified Access trust provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_verified_access_trust_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_verified_access_trust_provider)
        """

    def delete_volume(
        self, **kwargs: Unpack[DeleteVolumeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified EBS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_volume)
        """

    def delete_vpc(self, **kwargs: Unpack[DeleteVpcRequestTypeDef]) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc)
        """

    def delete_vpc_block_public_access_exclusion(
        self, **kwargs: Unpack[DeleteVpcBlockPublicAccessExclusionRequestTypeDef]
    ) -> DeleteVpcBlockPublicAccessExclusionResultTypeDef:
        """
        Delete a VPC Block Public Access (BPA) exclusion.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_vpc_block_public_access_exclusion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc_block_public_access_exclusion)
        """

    def delete_vpc_endpoint_connection_notifications(
        self, **kwargs: Unpack[DeleteVpcEndpointConnectionNotificationsRequestTypeDef]
    ) -> DeleteVpcEndpointConnectionNotificationsResultTypeDef:
        """
        Deletes the specified VPC endpoint connection notifications.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_vpc_endpoint_connection_notifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc_endpoint_connection_notifications)
        """

    def delete_vpc_endpoint_service_configurations(
        self, **kwargs: Unpack[DeleteVpcEndpointServiceConfigurationsRequestTypeDef]
    ) -> DeleteVpcEndpointServiceConfigurationsResultTypeDef:
        """
        Deletes the specified VPC endpoint service configurations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_vpc_endpoint_service_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc_endpoint_service_configurations)
        """

    def delete_vpc_endpoints(
        self, **kwargs: Unpack[DeleteVpcEndpointsRequestTypeDef]
    ) -> DeleteVpcEndpointsResultTypeDef:
        """
        Deletes the specified VPC endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_vpc_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc_endpoints)
        """

    def delete_vpc_peering_connection(
        self, **kwargs: Unpack[DeleteVpcPeeringConnectionRequestTypeDef]
    ) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        Deletes a VPC peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_vpc_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpc_peering_connection)
        """

    def delete_vpn_connection(
        self, **kwargs: Unpack[DeleteVpnConnectionRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_vpn_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpn_connection)
        """

    def delete_vpn_connection_route(
        self, **kwargs: Unpack[DeleteVpnConnectionRouteRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified static route associated with a VPN connection between an
        existing virtual private gateway and a VPN customer gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_vpn_connection_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpn_connection_route)
        """

    def delete_vpn_gateway(
        self, **kwargs: Unpack[DeleteVpnGatewayRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes the specified virtual private gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/delete_vpn_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#delete_vpn_gateway)
        """

    def deprovision_byoip_cidr(
        self, **kwargs: Unpack[DeprovisionByoipCidrRequestTypeDef]
    ) -> DeprovisionByoipCidrResultTypeDef:
        """
        Releases the specified address range that you provisioned for use with your
        Amazon Web Services resources through bring your own IP addresses (BYOIP) and
        deletes the corresponding address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/deprovision_byoip_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deprovision_byoip_cidr)
        """

    def deprovision_ipam_byoasn(
        self, **kwargs: Unpack[DeprovisionIpamByoasnRequestTypeDef]
    ) -> DeprovisionIpamByoasnResultTypeDef:
        """
        Deprovisions your Autonomous System Number (ASN) from your Amazon Web Services
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/deprovision_ipam_byoasn.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deprovision_ipam_byoasn)
        """

    def deprovision_ipam_pool_cidr(
        self, **kwargs: Unpack[DeprovisionIpamPoolCidrRequestTypeDef]
    ) -> DeprovisionIpamPoolCidrResultTypeDef:
        """
        Deprovision a CIDR provisioned from an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/deprovision_ipam_pool_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deprovision_ipam_pool_cidr)
        """

    def deprovision_public_ipv4_pool_cidr(
        self, **kwargs: Unpack[DeprovisionPublicIpv4PoolCidrRequestTypeDef]
    ) -> DeprovisionPublicIpv4PoolCidrResultTypeDef:
        """
        Deprovision a CIDR from a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/deprovision_public_ipv4_pool_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deprovision_public_ipv4_pool_cidr)
        """

    def deregister_image(self, **kwargs: Unpack[DeregisterImageRequestTypeDef]) -> Dict[str, Any]:
        """
        Deregisters the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/deregister_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deregister_image)
        """

    def deregister_instance_event_notification_attributes(
        self, **kwargs: Unpack[DeregisterInstanceEventNotificationAttributesRequestTypeDef]
    ) -> DeregisterInstanceEventNotificationAttributesResultTypeDef:
        """
        Deregisters tag keys to prevent tags that have the specified tag keys from
        being included in scheduled event notifications for resources in the Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/deregister_instance_event_notification_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deregister_instance_event_notification_attributes)
        """

    def deregister_transit_gateway_multicast_group_members(
        self, **kwargs: Unpack[DeregisterTransitGatewayMulticastGroupMembersRequestTypeDef]
    ) -> DeregisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        Deregisters the specified members (network interfaces) from the transit gateway
        multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/deregister_transit_gateway_multicast_group_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deregister_transit_gateway_multicast_group_members)
        """

    def deregister_transit_gateway_multicast_group_sources(
        self, **kwargs: Unpack[DeregisterTransitGatewayMulticastGroupSourcesRequestTypeDef]
    ) -> DeregisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        Deregisters the specified sources (network interfaces) from the transit gateway
        multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/deregister_transit_gateway_multicast_group_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#deregister_transit_gateway_multicast_group_sources)
        """

    def describe_account_attributes(
        self, **kwargs: Unpack[DescribeAccountAttributesRequestTypeDef]
    ) -> DescribeAccountAttributesResultTypeDef:
        """
        Describes attributes of your Amazon Web Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_account_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_account_attributes)
        """

    def describe_address_transfers(
        self, **kwargs: Unpack[DescribeAddressTransfersRequestTypeDef]
    ) -> DescribeAddressTransfersResultTypeDef:
        """
        Describes an Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_address_transfers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_address_transfers)
        """

    def describe_addresses(
        self, **kwargs: Unpack[DescribeAddressesRequestTypeDef]
    ) -> DescribeAddressesResultTypeDef:
        """
        Describes the specified Elastic IP addresses or all of your Elastic IP
        addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_addresses)
        """

    def describe_addresses_attribute(
        self, **kwargs: Unpack[DescribeAddressesAttributeRequestTypeDef]
    ) -> DescribeAddressesAttributeResultTypeDef:
        """
        Describes the attributes of the specified Elastic IP addresses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_addresses_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_addresses_attribute)
        """

    def describe_aggregate_id_format(
        self, **kwargs: Unpack[DescribeAggregateIdFormatRequestTypeDef]
    ) -> DescribeAggregateIdFormatResultTypeDef:
        """
        Describes the longer ID format settings for all resource types in a specific
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_aggregate_id_format.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_aggregate_id_format)
        """

    def describe_availability_zones(
        self, **kwargs: Unpack[DescribeAvailabilityZonesRequestTypeDef]
    ) -> DescribeAvailabilityZonesResultTypeDef:
        """
        Describes the Availability Zones, Local Zones, and Wavelength Zones that are
        available to you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_availability_zones.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_availability_zones)
        """

    def describe_aws_network_performance_metric_subscriptions(
        self, **kwargs: Unpack[DescribeAwsNetworkPerformanceMetricSubscriptionsRequestTypeDef]
    ) -> DescribeAwsNetworkPerformanceMetricSubscriptionsResultTypeDef:
        """
        Describes the current Infrastructure Performance metric subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_aws_network_performance_metric_subscriptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_aws_network_performance_metric_subscriptions)
        """

    def describe_bundle_tasks(
        self, **kwargs: Unpack[DescribeBundleTasksRequestTypeDef]
    ) -> DescribeBundleTasksResultTypeDef:
        """
        Describes the specified bundle tasks or all of your bundle tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_bundle_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_bundle_tasks)
        """

    def describe_byoip_cidrs(
        self, **kwargs: Unpack[DescribeByoipCidrsRequestTypeDef]
    ) -> DescribeByoipCidrsResultTypeDef:
        """
        Describes the IP address ranges that were specified in calls to
        <a>ProvisionByoipCidr</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_byoip_cidrs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_byoip_cidrs)
        """

    def describe_capacity_block_extension_history(
        self, **kwargs: Unpack[DescribeCapacityBlockExtensionHistoryRequestTypeDef]
    ) -> DescribeCapacityBlockExtensionHistoryResultTypeDef:
        """
        Describes the events for the specified Capacity Block extension during the
        specified time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_capacity_block_extension_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_capacity_block_extension_history)
        """

    def describe_capacity_block_extension_offerings(
        self, **kwargs: Unpack[DescribeCapacityBlockExtensionOfferingsRequestTypeDef]
    ) -> DescribeCapacityBlockExtensionOfferingsResultTypeDef:
        """
        Describes Capacity Block extension offerings available for purchase in the
        Amazon Web Services Region that you're currently using.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_capacity_block_extension_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_capacity_block_extension_offerings)
        """

    def describe_capacity_block_offerings(
        self, **kwargs: Unpack[DescribeCapacityBlockOfferingsRequestTypeDef]
    ) -> DescribeCapacityBlockOfferingsResultTypeDef:
        """
        Describes Capacity Block offerings available for purchase in the Amazon Web
        Services Region that you're currently using.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_capacity_block_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_capacity_block_offerings)
        """

    def describe_capacity_reservation_billing_requests(
        self, **kwargs: Unpack[DescribeCapacityReservationBillingRequestsRequestTypeDef]
    ) -> DescribeCapacityReservationBillingRequestsResultTypeDef:
        """
        Describes a request to assign the billing of the unused capacity of a Capacity
        Reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_capacity_reservation_billing_requests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_capacity_reservation_billing_requests)
        """

    def describe_capacity_reservation_fleets(
        self, **kwargs: Unpack[DescribeCapacityReservationFleetsRequestTypeDef]
    ) -> DescribeCapacityReservationFleetsResultTypeDef:
        """
        Describes one or more Capacity Reservation Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_capacity_reservation_fleets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_capacity_reservation_fleets)
        """

    def describe_capacity_reservations(
        self, **kwargs: Unpack[DescribeCapacityReservationsRequestTypeDef]
    ) -> DescribeCapacityReservationsResultTypeDef:
        """
        Describes one or more of your Capacity Reservations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_capacity_reservations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_capacity_reservations)
        """

    def describe_carrier_gateways(
        self, **kwargs: Unpack[DescribeCarrierGatewaysRequestTypeDef]
    ) -> DescribeCarrierGatewaysResultTypeDef:
        """
        Describes one or more of your carrier gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_carrier_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_carrier_gateways)
        """

    def describe_classic_link_instances(
        self, **kwargs: Unpack[DescribeClassicLinkInstancesRequestTypeDef]
    ) -> DescribeClassicLinkInstancesResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_classic_link_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_classic_link_instances)
        """

    def describe_client_vpn_authorization_rules(
        self, **kwargs: Unpack[DescribeClientVpnAuthorizationRulesRequestTypeDef]
    ) -> DescribeClientVpnAuthorizationRulesResultTypeDef:
        """
        Describes the authorization rules for a specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_client_vpn_authorization_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_authorization_rules)
        """

    def describe_client_vpn_connections(
        self, **kwargs: Unpack[DescribeClientVpnConnectionsRequestTypeDef]
    ) -> DescribeClientVpnConnectionsResultTypeDef:
        """
        Describes active client connections and connections that have been terminated
        within the last 60 minutes for the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_client_vpn_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_connections)
        """

    def describe_client_vpn_endpoints(
        self, **kwargs: Unpack[DescribeClientVpnEndpointsRequestTypeDef]
    ) -> DescribeClientVpnEndpointsResultTypeDef:
        """
        Describes one or more Client VPN endpoints in the account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_client_vpn_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_endpoints)
        """

    def describe_client_vpn_routes(
        self, **kwargs: Unpack[DescribeClientVpnRoutesRequestTypeDef]
    ) -> DescribeClientVpnRoutesResultTypeDef:
        """
        Describes the routes for the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_client_vpn_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_routes)
        """

    def describe_client_vpn_target_networks(
        self, **kwargs: Unpack[DescribeClientVpnTargetNetworksRequestTypeDef]
    ) -> DescribeClientVpnTargetNetworksResultTypeDef:
        """
        Describes the target networks associated with the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_client_vpn_target_networks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_client_vpn_target_networks)
        """

    def describe_coip_pools(
        self, **kwargs: Unpack[DescribeCoipPoolsRequestTypeDef]
    ) -> DescribeCoipPoolsResultTypeDef:
        """
        Describes the specified customer-owned address pools or all of your
        customer-owned address pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_coip_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_coip_pools)
        """

    def describe_conversion_tasks(
        self, **kwargs: Unpack[DescribeConversionTasksRequestTypeDef]
    ) -> DescribeConversionTasksResultTypeDef:
        """
        Describes the specified conversion tasks or all your conversion tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_conversion_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_conversion_tasks)
        """

    def describe_customer_gateways(
        self, **kwargs: Unpack[DescribeCustomerGatewaysRequestTypeDef]
    ) -> DescribeCustomerGatewaysResultTypeDef:
        """
        Describes one or more of your VPN customer gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_customer_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_customer_gateways)
        """

    def describe_declarative_policies_reports(
        self, **kwargs: Unpack[DescribeDeclarativePoliciesReportsRequestTypeDef]
    ) -> DescribeDeclarativePoliciesReportsResultTypeDef:
        """
        Describes the metadata of an account status report, including the status of the
        report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_declarative_policies_reports.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_declarative_policies_reports)
        """

    def describe_dhcp_options(
        self, **kwargs: Unpack[DescribeDhcpOptionsRequestTypeDef]
    ) -> DescribeDhcpOptionsResultTypeDef:
        """
        Describes your DHCP option sets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_dhcp_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_dhcp_options)
        """

    def describe_egress_only_internet_gateways(
        self, **kwargs: Unpack[DescribeEgressOnlyInternetGatewaysRequestTypeDef]
    ) -> DescribeEgressOnlyInternetGatewaysResultTypeDef:
        """
        Describes your egress-only internet gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_egress_only_internet_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_egress_only_internet_gateways)
        """

    def describe_elastic_gpus(
        self, **kwargs: Unpack[DescribeElasticGpusRequestTypeDef]
    ) -> DescribeElasticGpusResultTypeDef:
        """
        Amazon Elastic Graphics reached end of life on January 8, 2024.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_elastic_gpus.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_elastic_gpus)
        """

    def describe_export_image_tasks(
        self, **kwargs: Unpack[DescribeExportImageTasksRequestTypeDef]
    ) -> DescribeExportImageTasksResultTypeDef:
        """
        Describes the specified export image tasks or all of your export image tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_export_image_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_export_image_tasks)
        """

    def describe_export_tasks(
        self, **kwargs: Unpack[DescribeExportTasksRequestTypeDef]
    ) -> DescribeExportTasksResultTypeDef:
        """
        Describes the specified export instance tasks or all of your export instance
        tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_export_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_export_tasks)
        """

    def describe_fast_launch_images(
        self, **kwargs: Unpack[DescribeFastLaunchImagesRequestTypeDef]
    ) -> DescribeFastLaunchImagesResultTypeDef:
        """
        Describe details for Windows AMIs that are configured for Windows fast launch.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_fast_launch_images.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fast_launch_images)
        """

    def describe_fast_snapshot_restores(
        self, **kwargs: Unpack[DescribeFastSnapshotRestoresRequestTypeDef]
    ) -> DescribeFastSnapshotRestoresResultTypeDef:
        """
        Describes the state of fast snapshot restores for your snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_fast_snapshot_restores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fast_snapshot_restores)
        """

    def describe_fleet_history(
        self, **kwargs: Unpack[DescribeFleetHistoryRequestTypeDef]
    ) -> DescribeFleetHistoryResultTypeDef:
        """
        Describes the events for the specified EC2 Fleet during the specified time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_fleet_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fleet_history)
        """

    def describe_fleet_instances(
        self, **kwargs: Unpack[DescribeFleetInstancesRequestTypeDef]
    ) -> DescribeFleetInstancesResultTypeDef:
        """
        Describes the running instances for the specified EC2 Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_fleet_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fleet_instances)
        """

    def describe_fleets(
        self, **kwargs: Unpack[DescribeFleetsRequestTypeDef]
    ) -> DescribeFleetsResultTypeDef:
        """
        Describes the specified EC2 Fleet or all of your EC2 Fleets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_fleets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fleets)
        """

    def describe_flow_logs(
        self, **kwargs: Unpack[DescribeFlowLogsRequestTypeDef]
    ) -> DescribeFlowLogsResultTypeDef:
        """
        Describes one or more flow logs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_flow_logs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_flow_logs)
        """

    def describe_fpga_image_attribute(
        self, **kwargs: Unpack[DescribeFpgaImageAttributeRequestTypeDef]
    ) -> DescribeFpgaImageAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified Amazon FPGA Image (AFI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_fpga_image_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fpga_image_attribute)
        """

    def describe_fpga_images(
        self, **kwargs: Unpack[DescribeFpgaImagesRequestTypeDef]
    ) -> DescribeFpgaImagesResultTypeDef:
        """
        Describes the Amazon FPGA Images (AFIs) available to you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_fpga_images.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_fpga_images)
        """

    def describe_host_reservation_offerings(
        self, **kwargs: Unpack[DescribeHostReservationOfferingsRequestTypeDef]
    ) -> DescribeHostReservationOfferingsResultTypeDef:
        """
        Describes the Dedicated Host reservations that are available to purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_host_reservation_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_host_reservation_offerings)
        """

    def describe_host_reservations(
        self, **kwargs: Unpack[DescribeHostReservationsRequestTypeDef]
    ) -> DescribeHostReservationsResultTypeDef:
        """
        Describes reservations that are associated with Dedicated Hosts in your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_host_reservations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_host_reservations)
        """

    def describe_hosts(
        self, **kwargs: Unpack[DescribeHostsRequestTypeDef]
    ) -> DescribeHostsResultTypeDef:
        """
        Describes the specified Dedicated Hosts or all your Dedicated Hosts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_hosts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_hosts)
        """

    def describe_iam_instance_profile_associations(
        self, **kwargs: Unpack[DescribeIamInstanceProfileAssociationsRequestTypeDef]
    ) -> DescribeIamInstanceProfileAssociationsResultTypeDef:
        """
        Describes your IAM instance profile associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_iam_instance_profile_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_iam_instance_profile_associations)
        """

    def describe_id_format(
        self, **kwargs: Unpack[DescribeIdFormatRequestTypeDef]
    ) -> DescribeIdFormatResultTypeDef:
        """
        Describes the ID format settings for your resources on a per-Region basis, for
        example, to view which resource types are enabled for longer IDs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_id_format.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_id_format)
        """

    def describe_identity_id_format(
        self, **kwargs: Unpack[DescribeIdentityIdFormatRequestTypeDef]
    ) -> DescribeIdentityIdFormatResultTypeDef:
        """
        Describes the ID format settings for resources for the specified IAM user, IAM
        role, or root user.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_identity_id_format.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_identity_id_format)
        """

    def describe_image_attribute(
        self, **kwargs: Unpack[DescribeImageAttributeRequestTypeDef]
    ) -> ImageAttributeTypeDef:
        """
        Describes the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_image_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_image_attribute)
        """

    def describe_images(
        self, **kwargs: Unpack[DescribeImagesRequestTypeDef]
    ) -> DescribeImagesResultTypeDef:
        """
        Describes the specified images (AMIs, AKIs, and ARIs) available to you or all
        of the images available to you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_images.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_images)
        """

    def describe_import_image_tasks(
        self, **kwargs: Unpack[DescribeImportImageTasksRequestTypeDef]
    ) -> DescribeImportImageTasksResultTypeDef:
        """
        Displays details about an import virtual machine or import snapshot tasks that
        are already created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_import_image_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_import_image_tasks)
        """

    def describe_import_snapshot_tasks(
        self, **kwargs: Unpack[DescribeImportSnapshotTasksRequestTypeDef]
    ) -> DescribeImportSnapshotTasksResultTypeDef:
        """
        Describes your import snapshot tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_import_snapshot_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_import_snapshot_tasks)
        """

    def describe_instance_attribute(
        self, **kwargs: Unpack[DescribeInstanceAttributeRequestTypeDef]
    ) -> InstanceAttributeTypeDef:
        """
        Describes the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_attribute)
        """

    def describe_instance_connect_endpoints(
        self, **kwargs: Unpack[DescribeInstanceConnectEndpointsRequestTypeDef]
    ) -> DescribeInstanceConnectEndpointsResultTypeDef:
        """
        Describes the specified EC2 Instance Connect Endpoints or all EC2 Instance
        Connect Endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_connect_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_connect_endpoints)
        """

    def describe_instance_credit_specifications(
        self, **kwargs: Unpack[DescribeInstanceCreditSpecificationsRequestTypeDef]
    ) -> DescribeInstanceCreditSpecificationsResultTypeDef:
        """
        Describes the credit option for CPU usage of the specified burstable
        performance instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_credit_specifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_credit_specifications)
        """

    def describe_instance_event_notification_attributes(
        self, **kwargs: Unpack[DescribeInstanceEventNotificationAttributesRequestTypeDef]
    ) -> DescribeInstanceEventNotificationAttributesResultTypeDef:
        """
        Describes the tag keys that are registered to appear in scheduled event
        notifications for resources in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_event_notification_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_event_notification_attributes)
        """

    def describe_instance_event_windows(
        self, **kwargs: Unpack[DescribeInstanceEventWindowsRequestTypeDef]
    ) -> DescribeInstanceEventWindowsResultTypeDef:
        """
        Describes the specified event windows or all event windows.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_event_windows.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_event_windows)
        """

    def describe_instance_image_metadata(
        self, **kwargs: Unpack[DescribeInstanceImageMetadataRequestTypeDef]
    ) -> DescribeInstanceImageMetadataResultTypeDef:
        """
        Describes the AMI that was used to launch an instance, even if the AMI is
        deprecated, deregistered, made private (no longer public or shared with your
        account), or not allowed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_image_metadata.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_image_metadata)
        """

    def describe_instance_status(
        self, **kwargs: Unpack[DescribeInstanceStatusRequestTypeDef]
    ) -> DescribeInstanceStatusResultTypeDef:
        """
        Describes the status of the specified instances or all of your instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_status)
        """

    def describe_instance_topology(
        self, **kwargs: Unpack[DescribeInstanceTopologyRequestTypeDef]
    ) -> DescribeInstanceTopologyResultTypeDef:
        """
        Describes a tree-based hierarchy that represents the physical host placement of
        your EC2 instances within an Availability Zone or Local Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_topology.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_topology)
        """

    def describe_instance_type_offerings(
        self, **kwargs: Unpack[DescribeInstanceTypeOfferingsRequestTypeDef]
    ) -> DescribeInstanceTypeOfferingsResultTypeDef:
        """
        Lists the instance types that are offered for the specified location.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_type_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_type_offerings)
        """

    def describe_instance_types(
        self, **kwargs: Unpack[DescribeInstanceTypesRequestTypeDef]
    ) -> DescribeInstanceTypesResultTypeDef:
        """
        Describes the specified instance types.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instance_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instance_types)
        """

    def describe_instances(
        self, **kwargs: Unpack[DescribeInstancesRequestTypeDef]
    ) -> DescribeInstancesResultTypeDef:
        """
        Describes the specified instances or all instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_instances)
        """

    def describe_internet_gateways(
        self, **kwargs: Unpack[DescribeInternetGatewaysRequestTypeDef]
    ) -> DescribeInternetGatewaysResultTypeDef:
        """
        Describes your internet gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_internet_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_internet_gateways)
        """

    def describe_ipam_byoasn(
        self, **kwargs: Unpack[DescribeIpamByoasnRequestTypeDef]
    ) -> DescribeIpamByoasnResultTypeDef:
        """
        Describes your Autonomous System Numbers (ASNs), their provisioning statuses,
        and the BYOIP CIDRs with which they are associated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_ipam_byoasn.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_byoasn)
        """

    def describe_ipam_external_resource_verification_tokens(
        self, **kwargs: Unpack[DescribeIpamExternalResourceVerificationTokensRequestTypeDef]
    ) -> DescribeIpamExternalResourceVerificationTokensResultTypeDef:
        """
        Describe verification tokens.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_ipam_external_resource_verification_tokens.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_external_resource_verification_tokens)
        """

    def describe_ipam_pools(
        self, **kwargs: Unpack[DescribeIpamPoolsRequestTypeDef]
    ) -> DescribeIpamPoolsResultTypeDef:
        """
        Get information about your IPAM pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_ipam_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_pools)
        """

    def describe_ipam_resource_discoveries(
        self, **kwargs: Unpack[DescribeIpamResourceDiscoveriesRequestTypeDef]
    ) -> DescribeIpamResourceDiscoveriesResultTypeDef:
        """
        Describes IPAM resource discoveries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_ipam_resource_discoveries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_resource_discoveries)
        """

    def describe_ipam_resource_discovery_associations(
        self, **kwargs: Unpack[DescribeIpamResourceDiscoveryAssociationsRequestTypeDef]
    ) -> DescribeIpamResourceDiscoveryAssociationsResultTypeDef:
        """
        Describes resource discovery association with an Amazon VPC IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_ipam_resource_discovery_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_resource_discovery_associations)
        """

    def describe_ipam_scopes(
        self, **kwargs: Unpack[DescribeIpamScopesRequestTypeDef]
    ) -> DescribeIpamScopesResultTypeDef:
        """
        Get information about your IPAM scopes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_ipam_scopes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipam_scopes)
        """

    def describe_ipams(
        self, **kwargs: Unpack[DescribeIpamsRequestTypeDef]
    ) -> DescribeIpamsResultTypeDef:
        """
        Get information about your IPAM pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_ipams.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipams)
        """

    def describe_ipv6_pools(
        self, **kwargs: Unpack[DescribeIpv6PoolsRequestTypeDef]
    ) -> DescribeIpv6PoolsResultTypeDef:
        """
        Describes your IPv6 address pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_ipv6_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_ipv6_pools)
        """

    def describe_key_pairs(
        self, **kwargs: Unpack[DescribeKeyPairsRequestTypeDef]
    ) -> DescribeKeyPairsResultTypeDef:
        """
        Describes the specified key pairs or all of your key pairs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_key_pairs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_key_pairs)
        """

    def describe_launch_template_versions(
        self, **kwargs: Unpack[DescribeLaunchTemplateVersionsRequestTypeDef]
    ) -> DescribeLaunchTemplateVersionsResultTypeDef:
        """
        Describes one or more versions of a specified launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_launch_template_versions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_launch_template_versions)
        """

    def describe_launch_templates(
        self, **kwargs: Unpack[DescribeLaunchTemplatesRequestTypeDef]
    ) -> DescribeLaunchTemplatesResultTypeDef:
        """
        Describes one or more launch templates.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_launch_templates.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_launch_templates)
        """

    def describe_local_gateway_route_table_virtual_interface_group_associations(
        self,
        **kwargs: Unpack[
            DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsRequestTypeDef
        ],
    ) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsResultTypeDef:
        """
        Describes the associations between virtual interface groups and local gateway
        route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_local_gateway_route_table_virtual_interface_group_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_route_table_virtual_interface_group_associations)
        """

    def describe_local_gateway_route_table_vpc_associations(
        self, **kwargs: Unpack[DescribeLocalGatewayRouteTableVpcAssociationsRequestTypeDef]
    ) -> DescribeLocalGatewayRouteTableVpcAssociationsResultTypeDef:
        """
        Describes the specified associations between VPCs and local gateway route
        tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_local_gateway_route_table_vpc_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_route_table_vpc_associations)
        """

    def describe_local_gateway_route_tables(
        self, **kwargs: Unpack[DescribeLocalGatewayRouteTablesRequestTypeDef]
    ) -> DescribeLocalGatewayRouteTablesResultTypeDef:
        """
        Describes one or more local gateway route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_local_gateway_route_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_route_tables)
        """

    def describe_local_gateway_virtual_interface_groups(
        self, **kwargs: Unpack[DescribeLocalGatewayVirtualInterfaceGroupsRequestTypeDef]
    ) -> DescribeLocalGatewayVirtualInterfaceGroupsResultTypeDef:
        """
        Describes the specified local gateway virtual interface groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_local_gateway_virtual_interface_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_virtual_interface_groups)
        """

    def describe_local_gateway_virtual_interfaces(
        self, **kwargs: Unpack[DescribeLocalGatewayVirtualInterfacesRequestTypeDef]
    ) -> DescribeLocalGatewayVirtualInterfacesResultTypeDef:
        """
        Describes the specified local gateway virtual interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_local_gateway_virtual_interfaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateway_virtual_interfaces)
        """

    def describe_local_gateways(
        self, **kwargs: Unpack[DescribeLocalGatewaysRequestTypeDef]
    ) -> DescribeLocalGatewaysResultTypeDef:
        """
        Describes one or more local gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_local_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_local_gateways)
        """

    def describe_locked_snapshots(
        self, **kwargs: Unpack[DescribeLockedSnapshotsRequestTypeDef]
    ) -> DescribeLockedSnapshotsResultTypeDef:
        """
        Describes the lock status for a snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_locked_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_locked_snapshots)
        """

    def describe_mac_hosts(
        self, **kwargs: Unpack[DescribeMacHostsRequestTypeDef]
    ) -> DescribeMacHostsResultTypeDef:
        """
        Describes the specified EC2 Mac Dedicated Host or all of your EC2 Mac Dedicated
        Hosts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_mac_hosts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_mac_hosts)
        """

    def describe_managed_prefix_lists(
        self, **kwargs: Unpack[DescribeManagedPrefixListsRequestTypeDef]
    ) -> DescribeManagedPrefixListsResultTypeDef:
        """
        Describes your managed prefix lists and any Amazon Web Services-managed prefix
        lists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_managed_prefix_lists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_managed_prefix_lists)
        """

    def describe_moving_addresses(
        self, **kwargs: Unpack[DescribeMovingAddressesRequestTypeDef]
    ) -> DescribeMovingAddressesResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_moving_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_moving_addresses)
        """

    def describe_nat_gateways(
        self, **kwargs: Unpack[DescribeNatGatewaysRequestTypeDef]
    ) -> DescribeNatGatewaysResultTypeDef:
        """
        Describes your NAT gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_nat_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_nat_gateways)
        """

    def describe_network_acls(
        self, **kwargs: Unpack[DescribeNetworkAclsRequestTypeDef]
    ) -> DescribeNetworkAclsResultTypeDef:
        """
        Describes your network ACLs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_network_acls.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_acls)
        """

    def describe_network_insights_access_scope_analyses(
        self, **kwargs: Unpack[DescribeNetworkInsightsAccessScopeAnalysesRequestTypeDef]
    ) -> DescribeNetworkInsightsAccessScopeAnalysesResultTypeDef:
        """
        Describes the specified Network Access Scope analyses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_network_insights_access_scope_analyses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_insights_access_scope_analyses)
        """

    def describe_network_insights_access_scopes(
        self, **kwargs: Unpack[DescribeNetworkInsightsAccessScopesRequestTypeDef]
    ) -> DescribeNetworkInsightsAccessScopesResultTypeDef:
        """
        Describes the specified Network Access Scopes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_network_insights_access_scopes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_insights_access_scopes)
        """

    def describe_network_insights_analyses(
        self, **kwargs: Unpack[DescribeNetworkInsightsAnalysesRequestTypeDef]
    ) -> DescribeNetworkInsightsAnalysesResultTypeDef:
        """
        Describes one or more of your network insights analyses.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_network_insights_analyses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_insights_analyses)
        """

    def describe_network_insights_paths(
        self, **kwargs: Unpack[DescribeNetworkInsightsPathsRequestTypeDef]
    ) -> DescribeNetworkInsightsPathsResultTypeDef:
        """
        Describes one or more of your paths.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_network_insights_paths.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_insights_paths)
        """

    def describe_network_interface_attribute(
        self, **kwargs: Unpack[DescribeNetworkInterfaceAttributeRequestTypeDef]
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        Describes a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_network_interface_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_interface_attribute)
        """

    def describe_network_interface_permissions(
        self, **kwargs: Unpack[DescribeNetworkInterfacePermissionsRequestTypeDef]
    ) -> DescribeNetworkInterfacePermissionsResultTypeDef:
        """
        Describes the permissions for your network interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_network_interface_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_interface_permissions)
        """

    def describe_network_interfaces(
        self, **kwargs: Unpack[DescribeNetworkInterfacesRequestTypeDef]
    ) -> DescribeNetworkInterfacesResultTypeDef:
        """
        Describes the specified network interfaces or all your network interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_network_interfaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_network_interfaces)
        """

    def describe_outpost_lags(
        self, **kwargs: Unpack[DescribeOutpostLagsRequestTypeDef]
    ) -> DescribeOutpostLagsResultTypeDef:
        """
        Describes the Outposts link aggregation groups (LAGs).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_outpost_lags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_outpost_lags)
        """

    def describe_placement_groups(
        self, **kwargs: Unpack[DescribePlacementGroupsRequestTypeDef]
    ) -> DescribePlacementGroupsResultTypeDef:
        """
        Describes the specified placement groups or all of your placement groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_placement_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_placement_groups)
        """

    def describe_prefix_lists(
        self, **kwargs: Unpack[DescribePrefixListsRequestTypeDef]
    ) -> DescribePrefixListsResultTypeDef:
        """
        Describes available Amazon Web Services services in a prefix list format, which
        includes the prefix list name and prefix list ID of the service and the IP
        address range for the service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_prefix_lists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_prefix_lists)
        """

    def describe_principal_id_format(
        self, **kwargs: Unpack[DescribePrincipalIdFormatRequestTypeDef]
    ) -> DescribePrincipalIdFormatResultTypeDef:
        """
        Describes the ID format settings for the root user and all IAM roles and IAM
        users that have explicitly specified a longer ID (17-character ID) preference.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_principal_id_format.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_principal_id_format)
        """

    def describe_public_ipv4_pools(
        self, **kwargs: Unpack[DescribePublicIpv4PoolsRequestTypeDef]
    ) -> DescribePublicIpv4PoolsResultTypeDef:
        """
        Describes the specified IPv4 address pools.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_public_ipv4_pools.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_public_ipv4_pools)
        """

    def describe_regions(
        self, **kwargs: Unpack[DescribeRegionsRequestTypeDef]
    ) -> DescribeRegionsResultTypeDef:
        """
        Describes the Regions that are enabled for your account, or all Regions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_regions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_regions)
        """

    def describe_replace_root_volume_tasks(
        self, **kwargs: Unpack[DescribeReplaceRootVolumeTasksRequestTypeDef]
    ) -> DescribeReplaceRootVolumeTasksResultTypeDef:
        """
        Describes a root volume replacement task.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_replace_root_volume_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_replace_root_volume_tasks)
        """

    def describe_reserved_instances(
        self, **kwargs: Unpack[DescribeReservedInstancesRequestTypeDef]
    ) -> DescribeReservedInstancesResultTypeDef:
        """
        Describes one or more of the Reserved Instances that you purchased.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_reserved_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_reserved_instances)
        """

    def describe_reserved_instances_listings(
        self, **kwargs: Unpack[DescribeReservedInstancesListingsRequestTypeDef]
    ) -> DescribeReservedInstancesListingsResultTypeDef:
        """
        Describes your account's Reserved Instance listings in the Reserved Instance
        Marketplace.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_reserved_instances_listings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_reserved_instances_listings)
        """

    def describe_reserved_instances_modifications(
        self, **kwargs: Unpack[DescribeReservedInstancesModificationsRequestTypeDef]
    ) -> DescribeReservedInstancesModificationsResultTypeDef:
        """
        Describes the modifications made to your Reserved Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_reserved_instances_modifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_reserved_instances_modifications)
        """

    def describe_reserved_instances_offerings(
        self, **kwargs: Unpack[DescribeReservedInstancesOfferingsRequestTypeDef]
    ) -> DescribeReservedInstancesOfferingsResultTypeDef:
        """
        Describes Reserved Instance offerings that are available for purchase.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_reserved_instances_offerings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_reserved_instances_offerings)
        """

    def describe_route_server_endpoints(
        self, **kwargs: Unpack[DescribeRouteServerEndpointsRequestTypeDef]
    ) -> DescribeRouteServerEndpointsResultTypeDef:
        """
        Describes one or more route server endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_route_server_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_route_server_endpoints)
        """

    def describe_route_server_peers(
        self, **kwargs: Unpack[DescribeRouteServerPeersRequestTypeDef]
    ) -> DescribeRouteServerPeersResultTypeDef:
        """
        Describes one or more route server peers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_route_server_peers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_route_server_peers)
        """

    def describe_route_servers(
        self, **kwargs: Unpack[DescribeRouteServersRequestTypeDef]
    ) -> DescribeRouteServersResultTypeDef:
        """
        Describes one or more route servers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_route_servers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_route_servers)
        """

    def describe_route_tables(
        self, **kwargs: Unpack[DescribeRouteTablesRequestTypeDef]
    ) -> DescribeRouteTablesResultTypeDef:
        """
        Describes your route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_route_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_route_tables)
        """

    def describe_scheduled_instance_availability(
        self, **kwargs: Unpack[DescribeScheduledInstanceAvailabilityRequestTypeDef]
    ) -> DescribeScheduledInstanceAvailabilityResultTypeDef:
        """
        Finds available schedules that meet the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_scheduled_instance_availability.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_scheduled_instance_availability)
        """

    def describe_scheduled_instances(
        self, **kwargs: Unpack[DescribeScheduledInstancesRequestTypeDef]
    ) -> DescribeScheduledInstancesResultTypeDef:
        """
        Describes the specified Scheduled Instances or all your Scheduled Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_scheduled_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_scheduled_instances)
        """

    def describe_security_group_references(
        self, **kwargs: Unpack[DescribeSecurityGroupReferencesRequestTypeDef]
    ) -> DescribeSecurityGroupReferencesResultTypeDef:
        """
        Describes the VPCs on the other side of a VPC peering or Transit Gateway
        connection that are referencing the security groups you've specified in this
        request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_security_group_references.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_security_group_references)
        """

    def describe_security_group_rules(
        self, **kwargs: Unpack[DescribeSecurityGroupRulesRequestTypeDef]
    ) -> DescribeSecurityGroupRulesResultTypeDef:
        """
        Describes one or more of your security group rules.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_security_group_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_security_group_rules)
        """

    def describe_security_group_vpc_associations(
        self, **kwargs: Unpack[DescribeSecurityGroupVpcAssociationsRequestTypeDef]
    ) -> DescribeSecurityGroupVpcAssociationsResultTypeDef:
        """
        Describes security group VPC associations made with <a
        href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateSecurityGroupVpc.html">AssociateSecurityGroupVpc</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_security_group_vpc_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_security_group_vpc_associations)
        """

    def describe_security_groups(
        self, **kwargs: Unpack[DescribeSecurityGroupsRequestTypeDef]
    ) -> DescribeSecurityGroupsResultTypeDef:
        """
        Describes the specified security groups or all of your security groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_security_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_security_groups)
        """

    def describe_service_link_virtual_interfaces(
        self, **kwargs: Unpack[DescribeServiceLinkVirtualInterfacesRequestTypeDef]
    ) -> DescribeServiceLinkVirtualInterfacesResultTypeDef:
        """
        Describes the Outpost service link virtual interfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_service_link_virtual_interfaces.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_service_link_virtual_interfaces)
        """

    def describe_snapshot_attribute(
        self, **kwargs: Unpack[DescribeSnapshotAttributeRequestTypeDef]
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_snapshot_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_snapshot_attribute)
        """

    def describe_snapshot_tier_status(
        self, **kwargs: Unpack[DescribeSnapshotTierStatusRequestTypeDef]
    ) -> DescribeSnapshotTierStatusResultTypeDef:
        """
        Describes the storage tier status of one or more Amazon EBS snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_snapshot_tier_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_snapshot_tier_status)
        """

    def describe_snapshots(
        self, **kwargs: Unpack[DescribeSnapshotsRequestTypeDef]
    ) -> DescribeSnapshotsResultTypeDef:
        """
        Describes the specified EBS snapshots available to you or all of the EBS
        snapshots available to you.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_snapshots.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_snapshots)
        """

    def describe_spot_datafeed_subscription(
        self, **kwargs: Unpack[DescribeSpotDatafeedSubscriptionRequestTypeDef]
    ) -> DescribeSpotDatafeedSubscriptionResultTypeDef:
        """
        Describes the data feed for Spot Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_spot_datafeed_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_datafeed_subscription)
        """

    def describe_spot_fleet_instances(
        self, **kwargs: Unpack[DescribeSpotFleetInstancesRequestTypeDef]
    ) -> DescribeSpotFleetInstancesResponseTypeDef:
        """
        Describes the running instances for the specified Spot Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_spot_fleet_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_fleet_instances)
        """

    def describe_spot_fleet_request_history(
        self, **kwargs: Unpack[DescribeSpotFleetRequestHistoryRequestTypeDef]
    ) -> DescribeSpotFleetRequestHistoryResponseTypeDef:
        """
        Describes the events for the specified Spot Fleet request during the specified
        time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_spot_fleet_request_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_fleet_request_history)
        """

    def describe_spot_fleet_requests(
        self, **kwargs: Unpack[DescribeSpotFleetRequestsRequestTypeDef]
    ) -> DescribeSpotFleetRequestsResponseTypeDef:
        """
        Describes your Spot Fleet requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_spot_fleet_requests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_fleet_requests)
        """

    def describe_spot_instance_requests(
        self, **kwargs: Unpack[DescribeSpotInstanceRequestsRequestTypeDef]
    ) -> DescribeSpotInstanceRequestsResultTypeDef:
        """
        Describes the specified Spot Instance requests.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_spot_instance_requests.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_instance_requests)
        """

    def describe_spot_price_history(
        self, **kwargs: Unpack[DescribeSpotPriceHistoryRequestTypeDef]
    ) -> DescribeSpotPriceHistoryResultTypeDef:
        """
        Describes the Spot price history.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_spot_price_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_spot_price_history)
        """

    def describe_stale_security_groups(
        self, **kwargs: Unpack[DescribeStaleSecurityGroupsRequestTypeDef]
    ) -> DescribeStaleSecurityGroupsResultTypeDef:
        """
        Describes the stale security group rules for security groups referenced across
        a VPC peering connection, transit gateway connection, or with a security group
        VPC association.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_stale_security_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_stale_security_groups)
        """

    def describe_store_image_tasks(
        self, **kwargs: Unpack[DescribeStoreImageTasksRequestTypeDef]
    ) -> DescribeStoreImageTasksResultTypeDef:
        """
        Describes the progress of the AMI store tasks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_store_image_tasks.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_store_image_tasks)
        """

    def describe_subnets(
        self, **kwargs: Unpack[DescribeSubnetsRequestTypeDef]
    ) -> DescribeSubnetsResultTypeDef:
        """
        Describes your subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_subnets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_subnets)
        """

    def describe_tags(
        self, **kwargs: Unpack[DescribeTagsRequestTypeDef]
    ) -> DescribeTagsResultTypeDef:
        """
        Describes the specified tags for your EC2 resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_tags)
        """

    def describe_traffic_mirror_filter_rules(
        self, **kwargs: Unpack[DescribeTrafficMirrorFilterRulesRequestTypeDef]
    ) -> DescribeTrafficMirrorFilterRulesResultTypeDef:
        """
        Describe traffic mirror filters that determine the traffic that is mirrored.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_traffic_mirror_filter_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_traffic_mirror_filter_rules)
        """

    def describe_traffic_mirror_filters(
        self, **kwargs: Unpack[DescribeTrafficMirrorFiltersRequestTypeDef]
    ) -> DescribeTrafficMirrorFiltersResultTypeDef:
        """
        Describes one or more Traffic Mirror filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_traffic_mirror_filters.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_traffic_mirror_filters)
        """

    def describe_traffic_mirror_sessions(
        self, **kwargs: Unpack[DescribeTrafficMirrorSessionsRequestTypeDef]
    ) -> DescribeTrafficMirrorSessionsResultTypeDef:
        """
        Describes one or more Traffic Mirror sessions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_traffic_mirror_sessions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_traffic_mirror_sessions)
        """

    def describe_traffic_mirror_targets(
        self, **kwargs: Unpack[DescribeTrafficMirrorTargetsRequestTypeDef]
    ) -> DescribeTrafficMirrorTargetsResultTypeDef:
        """
        Information about one or more Traffic Mirror targets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_traffic_mirror_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_traffic_mirror_targets)
        """

    def describe_transit_gateway_attachments(
        self, **kwargs: Unpack[DescribeTransitGatewayAttachmentsRequestTypeDef]
    ) -> DescribeTransitGatewayAttachmentsResultTypeDef:
        """
        Describes one or more attachments between resources and transit gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateway_attachments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_attachments)
        """

    def describe_transit_gateway_connect_peers(
        self, **kwargs: Unpack[DescribeTransitGatewayConnectPeersRequestTypeDef]
    ) -> DescribeTransitGatewayConnectPeersResultTypeDef:
        """
        Describes one or more Connect peers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateway_connect_peers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_connect_peers)
        """

    def describe_transit_gateway_connects(
        self, **kwargs: Unpack[DescribeTransitGatewayConnectsRequestTypeDef]
    ) -> DescribeTransitGatewayConnectsResultTypeDef:
        """
        Describes one or more Connect attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateway_connects.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_connects)
        """

    def describe_transit_gateway_multicast_domains(
        self, **kwargs: Unpack[DescribeTransitGatewayMulticastDomainsRequestTypeDef]
    ) -> DescribeTransitGatewayMulticastDomainsResultTypeDef:
        """
        Describes one or more transit gateway multicast domains.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateway_multicast_domains.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_multicast_domains)
        """

    def describe_transit_gateway_peering_attachments(
        self, **kwargs: Unpack[DescribeTransitGatewayPeeringAttachmentsRequestTypeDef]
    ) -> DescribeTransitGatewayPeeringAttachmentsResultTypeDef:
        """
        Describes your transit gateway peering attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateway_peering_attachments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_peering_attachments)
        """

    def describe_transit_gateway_policy_tables(
        self, **kwargs: Unpack[DescribeTransitGatewayPolicyTablesRequestTypeDef]
    ) -> DescribeTransitGatewayPolicyTablesResultTypeDef:
        """
        Describes one or more transit gateway route policy tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateway_policy_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_policy_tables)
        """

    def describe_transit_gateway_route_table_announcements(
        self, **kwargs: Unpack[DescribeTransitGatewayRouteTableAnnouncementsRequestTypeDef]
    ) -> DescribeTransitGatewayRouteTableAnnouncementsResultTypeDef:
        """
        Describes one or more transit gateway route table advertisements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateway_route_table_announcements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_route_table_announcements)
        """

    def describe_transit_gateway_route_tables(
        self, **kwargs: Unpack[DescribeTransitGatewayRouteTablesRequestTypeDef]
    ) -> DescribeTransitGatewayRouteTablesResultTypeDef:
        """
        Describes one or more transit gateway route tables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateway_route_tables.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_route_tables)
        """

    def describe_transit_gateway_vpc_attachments(
        self, **kwargs: Unpack[DescribeTransitGatewayVpcAttachmentsRequestTypeDef]
    ) -> DescribeTransitGatewayVpcAttachmentsResultTypeDef:
        """
        Describes one or more VPC attachments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateway_vpc_attachments.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateway_vpc_attachments)
        """

    def describe_transit_gateways(
        self, **kwargs: Unpack[DescribeTransitGatewaysRequestTypeDef]
    ) -> DescribeTransitGatewaysResultTypeDef:
        """
        Describes one or more transit gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_transit_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_transit_gateways)
        """

    def describe_trunk_interface_associations(
        self, **kwargs: Unpack[DescribeTrunkInterfaceAssociationsRequestTypeDef]
    ) -> DescribeTrunkInterfaceAssociationsResultTypeDef:
        """
        Describes one or more network interface trunk associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_trunk_interface_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_trunk_interface_associations)
        """

    def describe_verified_access_endpoints(
        self, **kwargs: Unpack[DescribeVerifiedAccessEndpointsRequestTypeDef]
    ) -> DescribeVerifiedAccessEndpointsResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_verified_access_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_endpoints)
        """

    def describe_verified_access_groups(
        self, **kwargs: Unpack[DescribeVerifiedAccessGroupsRequestTypeDef]
    ) -> DescribeVerifiedAccessGroupsResultTypeDef:
        """
        Describes the specified Verified Access groups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_verified_access_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_groups)
        """

    def describe_verified_access_instance_logging_configurations(
        self, **kwargs: Unpack[DescribeVerifiedAccessInstanceLoggingConfigurationsRequestTypeDef]
    ) -> DescribeVerifiedAccessInstanceLoggingConfigurationsResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_verified_access_instance_logging_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_instance_logging_configurations)
        """

    def describe_verified_access_instances(
        self, **kwargs: Unpack[DescribeVerifiedAccessInstancesRequestTypeDef]
    ) -> DescribeVerifiedAccessInstancesResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_verified_access_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_instances)
        """

    def describe_verified_access_trust_providers(
        self, **kwargs: Unpack[DescribeVerifiedAccessTrustProvidersRequestTypeDef]
    ) -> DescribeVerifiedAccessTrustProvidersResultTypeDef:
        """
        Describes the specified Amazon Web Services Verified Access trust providers.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_verified_access_trust_providers.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_verified_access_trust_providers)
        """

    def describe_volume_attribute(
        self, **kwargs: Unpack[DescribeVolumeAttributeRequestTypeDef]
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_volume_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_volume_attribute)
        """

    def describe_volume_status(
        self, **kwargs: Unpack[DescribeVolumeStatusRequestTypeDef]
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        Describes the status of the specified volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_volume_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_volume_status)
        """

    def describe_volumes(
        self, **kwargs: Unpack[DescribeVolumesRequestTypeDef]
    ) -> DescribeVolumesResultTypeDef:
        """
        Describes the specified EBS volumes or all of your EBS volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_volumes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_volumes)
        """

    def describe_volumes_modifications(
        self, **kwargs: Unpack[DescribeVolumesModificationsRequestTypeDef]
    ) -> DescribeVolumesModificationsResultTypeDef:
        """
        Describes the most recent volume modification request for the specified EBS
        volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_volumes_modifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_volumes_modifications)
        """

    def describe_vpc_attribute(
        self, **kwargs: Unpack[DescribeVpcAttributeRequestTypeDef]
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_attribute)
        """

    def describe_vpc_block_public_access_exclusions(
        self, **kwargs: Unpack[DescribeVpcBlockPublicAccessExclusionsRequestTypeDef]
    ) -> DescribeVpcBlockPublicAccessExclusionsResultTypeDef:
        """
        Describe VPC Block Public Access (BPA) exclusions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_block_public_access_exclusions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_block_public_access_exclusions)
        """

    def describe_vpc_block_public_access_options(
        self, **kwargs: Unpack[DescribeVpcBlockPublicAccessOptionsRequestTypeDef]
    ) -> DescribeVpcBlockPublicAccessOptionsResultTypeDef:
        """
        Describe VPC Block Public Access (BPA) options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_block_public_access_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_block_public_access_options)
        """

    def describe_vpc_classic_link(
        self, **kwargs: Unpack[DescribeVpcClassicLinkRequestTypeDef]
    ) -> DescribeVpcClassicLinkResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_classic_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_classic_link)
        """

    def describe_vpc_classic_link_dns_support(
        self, **kwargs: Unpack[DescribeVpcClassicLinkDnsSupportRequestTypeDef]
    ) -> DescribeVpcClassicLinkDnsSupportResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_classic_link_dns_support.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_classic_link_dns_support)
        """

    def describe_vpc_endpoint_associations(
        self, **kwargs: Unpack[DescribeVpcEndpointAssociationsRequestTypeDef]
    ) -> DescribeVpcEndpointAssociationsResultTypeDef:
        """
        Describes the VPC resources, VPC endpoint services, Amazon Lattice services, or
        service networks associated with the VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_endpoint_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_associations)
        """

    def describe_vpc_endpoint_connection_notifications(
        self, **kwargs: Unpack[DescribeVpcEndpointConnectionNotificationsRequestTypeDef]
    ) -> DescribeVpcEndpointConnectionNotificationsResultTypeDef:
        """
        Describes the connection notifications for VPC endpoints and VPC endpoint
        services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_endpoint_connection_notifications.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_connection_notifications)
        """

    def describe_vpc_endpoint_connections(
        self, **kwargs: Unpack[DescribeVpcEndpointConnectionsRequestTypeDef]
    ) -> DescribeVpcEndpointConnectionsResultTypeDef:
        """
        Describes the VPC endpoint connections to your VPC endpoint services, including
        any endpoints that are pending your acceptance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_endpoint_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_connections)
        """

    def describe_vpc_endpoint_service_configurations(
        self, **kwargs: Unpack[DescribeVpcEndpointServiceConfigurationsRequestTypeDef]
    ) -> DescribeVpcEndpointServiceConfigurationsResultTypeDef:
        """
        Describes the VPC endpoint service configurations in your account (your
        services).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_endpoint_service_configurations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_service_configurations)
        """

    def describe_vpc_endpoint_service_permissions(
        self, **kwargs: Unpack[DescribeVpcEndpointServicePermissionsRequestTypeDef]
    ) -> DescribeVpcEndpointServicePermissionsResultTypeDef:
        """
        Describes the principals (service consumers) that are permitted to discover
        your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_endpoint_service_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_service_permissions)
        """

    def describe_vpc_endpoint_services(
        self, **kwargs: Unpack[DescribeVpcEndpointServicesRequestTypeDef]
    ) -> DescribeVpcEndpointServicesResultTypeDef:
        """
        Describes available services to which you can create a VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_endpoint_services.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoint_services)
        """

    def describe_vpc_endpoints(
        self, **kwargs: Unpack[DescribeVpcEndpointsRequestTypeDef]
    ) -> DescribeVpcEndpointsResultTypeDef:
        """
        Describes your VPC endpoints.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_endpoints.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_endpoints)
        """

    def describe_vpc_peering_connections(
        self, **kwargs: Unpack[DescribeVpcPeeringConnectionsRequestTypeDef]
    ) -> DescribeVpcPeeringConnectionsResultTypeDef:
        """
        Describes your VPC peering connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpc_peering_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpc_peering_connections)
        """

    def describe_vpcs(
        self, **kwargs: Unpack[DescribeVpcsRequestTypeDef]
    ) -> DescribeVpcsResultTypeDef:
        """
        Describes your VPCs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpcs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpcs)
        """

    def describe_vpn_connections(
        self, **kwargs: Unpack[DescribeVpnConnectionsRequestTypeDef]
    ) -> DescribeVpnConnectionsResultTypeDef:
        """
        Describes one or more of your VPN connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpn_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpn_connections)
        """

    def describe_vpn_gateways(
        self, **kwargs: Unpack[DescribeVpnGatewaysRequestTypeDef]
    ) -> DescribeVpnGatewaysResultTypeDef:
        """
        Describes one or more of your virtual private gateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/describe_vpn_gateways.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#describe_vpn_gateways)
        """

    def detach_classic_link_vpc(
        self, **kwargs: Unpack[DetachClassicLinkVpcRequestTypeDef]
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/detach_classic_link_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_classic_link_vpc)
        """

    def detach_internet_gateway(
        self, **kwargs: Unpack[DetachInternetGatewayRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches an internet gateway from a VPC, disabling connectivity between the
        internet and the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/detach_internet_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_internet_gateway)
        """

    def detach_network_interface(
        self, **kwargs: Unpack[DetachNetworkInterfaceRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches a network interface from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/detach_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_network_interface)
        """

    def detach_verified_access_trust_provider(
        self, **kwargs: Unpack[DetachVerifiedAccessTrustProviderRequestTypeDef]
    ) -> DetachVerifiedAccessTrustProviderResultTypeDef:
        """
        Detaches the specified Amazon Web Services Verified Access trust provider from
        the specified Amazon Web Services Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/detach_verified_access_trust_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_verified_access_trust_provider)
        """

    def detach_volume(
        self, **kwargs: Unpack[DetachVolumeRequestTypeDef]
    ) -> VolumeAttachmentResponseTypeDef:
        """
        Detaches an EBS volume from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/detach_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_volume)
        """

    def detach_vpn_gateway(
        self, **kwargs: Unpack[DetachVpnGatewayRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Detaches a virtual private gateway from a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/detach_vpn_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#detach_vpn_gateway)
        """

    def disable_address_transfer(
        self, **kwargs: Unpack[DisableAddressTransferRequestTypeDef]
    ) -> DisableAddressTransferResultTypeDef:
        """
        Disables Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_address_transfer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_address_transfer)
        """

    def disable_allowed_images_settings(
        self, **kwargs: Unpack[DisableAllowedImagesSettingsRequestTypeDef]
    ) -> DisableAllowedImagesSettingsResultTypeDef:
        """
        Disables Allowed AMIs for your account in the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_allowed_images_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_allowed_images_settings)
        """

    def disable_aws_network_performance_metric_subscription(
        self, **kwargs: Unpack[DisableAwsNetworkPerformanceMetricSubscriptionRequestTypeDef]
    ) -> DisableAwsNetworkPerformanceMetricSubscriptionResultTypeDef:
        """
        Disables Infrastructure Performance metric subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_aws_network_performance_metric_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_aws_network_performance_metric_subscription)
        """

    def disable_ebs_encryption_by_default(
        self, **kwargs: Unpack[DisableEbsEncryptionByDefaultRequestTypeDef]
    ) -> DisableEbsEncryptionByDefaultResultTypeDef:
        """
        Disables EBS encryption by default for your account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_ebs_encryption_by_default.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_ebs_encryption_by_default)
        """

    def disable_fast_launch(
        self, **kwargs: Unpack[DisableFastLaunchRequestTypeDef]
    ) -> DisableFastLaunchResultTypeDef:
        """
        Discontinue Windows fast launch for a Windows AMI, and clean up existing
        pre-provisioned snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_fast_launch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_fast_launch)
        """

    def disable_fast_snapshot_restores(
        self, **kwargs: Unpack[DisableFastSnapshotRestoresRequestTypeDef]
    ) -> DisableFastSnapshotRestoresResultTypeDef:
        """
        Disables fast snapshot restores for the specified snapshots in the specified
        Availability Zones.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_fast_snapshot_restores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_fast_snapshot_restores)
        """

    def disable_image(
        self, **kwargs: Unpack[DisableImageRequestTypeDef]
    ) -> DisableImageResultTypeDef:
        """
        Sets the AMI state to <code>disabled</code> and removes all launch permissions
        from the AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_image)
        """

    def disable_image_block_public_access(
        self, **kwargs: Unpack[DisableImageBlockPublicAccessRequestTypeDef]
    ) -> DisableImageBlockPublicAccessResultTypeDef:
        """
        Disables <i>block public access for AMIs</i> at the account level in the
        specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_image_block_public_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_image_block_public_access)
        """

    def disable_image_deprecation(
        self, **kwargs: Unpack[DisableImageDeprecationRequestTypeDef]
    ) -> DisableImageDeprecationResultTypeDef:
        """
        Cancels the deprecation of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_image_deprecation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_image_deprecation)
        """

    def disable_image_deregistration_protection(
        self, **kwargs: Unpack[DisableImageDeregistrationProtectionRequestTypeDef]
    ) -> DisableImageDeregistrationProtectionResultTypeDef:
        """
        Disables deregistration protection for an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_image_deregistration_protection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_image_deregistration_protection)
        """

    def disable_ipam_organization_admin_account(
        self, **kwargs: Unpack[DisableIpamOrganizationAdminAccountRequestTypeDef]
    ) -> DisableIpamOrganizationAdminAccountResultTypeDef:
        """
        Disable the IPAM account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_ipam_organization_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_ipam_organization_admin_account)
        """

    def disable_route_server_propagation(
        self, **kwargs: Unpack[DisableRouteServerPropagationRequestTypeDef]
    ) -> DisableRouteServerPropagationResultTypeDef:
        """
        Disables route propagation from a route server to a specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_route_server_propagation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_route_server_propagation)
        """

    def disable_serial_console_access(
        self, **kwargs: Unpack[DisableSerialConsoleAccessRequestTypeDef]
    ) -> DisableSerialConsoleAccessResultTypeDef:
        """
        Disables access to the EC2 serial console of all instances for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_serial_console_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_serial_console_access)
        """

    def disable_snapshot_block_public_access(
        self, **kwargs: Unpack[DisableSnapshotBlockPublicAccessRequestTypeDef]
    ) -> DisableSnapshotBlockPublicAccessResultTypeDef:
        """
        Disables the <i>block public access for snapshots</i> setting at the account
        level for the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_snapshot_block_public_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_snapshot_block_public_access)
        """

    def disable_transit_gateway_route_table_propagation(
        self, **kwargs: Unpack[DisableTransitGatewayRouteTablePropagationRequestTypeDef]
    ) -> DisableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        Disables the specified resource attachment from propagating routes to the
        specified propagation route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_transit_gateway_route_table_propagation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_transit_gateway_route_table_propagation)
        """

    def disable_vgw_route_propagation(
        self, **kwargs: Unpack[DisableVgwRoutePropagationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disables a virtual private gateway (VGW) from propagating routes to a specified
        route table of a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_vgw_route_propagation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_vgw_route_propagation)
        """

    def disable_vpc_classic_link(
        self, **kwargs: Unpack[DisableVpcClassicLinkRequestTypeDef]
    ) -> DisableVpcClassicLinkResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_vpc_classic_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_vpc_classic_link)
        """

    def disable_vpc_classic_link_dns_support(
        self, **kwargs: Unpack[DisableVpcClassicLinkDnsSupportRequestTypeDef]
    ) -> DisableVpcClassicLinkDnsSupportResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disable_vpc_classic_link_dns_support.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disable_vpc_classic_link_dns_support)
        """

    def disassociate_address(
        self, **kwargs: Unpack[DisassociateAddressRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates an Elastic IP address from the instance or network interface it's
        associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_address)
        """

    def disassociate_capacity_reservation_billing_owner(
        self, **kwargs: Unpack[DisassociateCapacityReservationBillingOwnerRequestTypeDef]
    ) -> DisassociateCapacityReservationBillingOwnerResultTypeDef:
        """
        Cancels a pending request to assign billing of the unused capacity of a
        Capacity Reservation to a consumer account, or revokes a request that has
        already been accepted.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_capacity_reservation_billing_owner.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_capacity_reservation_billing_owner)
        """

    def disassociate_client_vpn_target_network(
        self, **kwargs: Unpack[DisassociateClientVpnTargetNetworkRequestTypeDef]
    ) -> DisassociateClientVpnTargetNetworkResultTypeDef:
        """
        Disassociates a target network from the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_client_vpn_target_network.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_client_vpn_target_network)
        """

    def disassociate_enclave_certificate_iam_role(
        self, **kwargs: Unpack[DisassociateEnclaveCertificateIamRoleRequestTypeDef]
    ) -> DisassociateEnclaveCertificateIamRoleResultTypeDef:
        """
        Disassociates an IAM role from an Certificate Manager (ACM) certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_enclave_certificate_iam_role.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_enclave_certificate_iam_role)
        """

    def disassociate_iam_instance_profile(
        self, **kwargs: Unpack[DisassociateIamInstanceProfileRequestTypeDef]
    ) -> DisassociateIamInstanceProfileResultTypeDef:
        """
        Disassociates an IAM instance profile from a running or stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_iam_instance_profile.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_iam_instance_profile)
        """

    def disassociate_instance_event_window(
        self, **kwargs: Unpack[DisassociateInstanceEventWindowRequestTypeDef]
    ) -> DisassociateInstanceEventWindowResultTypeDef:
        """
        Disassociates one or more targets from an event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_instance_event_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_instance_event_window)
        """

    def disassociate_ipam_byoasn(
        self, **kwargs: Unpack[DisassociateIpamByoasnRequestTypeDef]
    ) -> DisassociateIpamByoasnResultTypeDef:
        """
        Remove the association between your Autonomous System Number (ASN) and your
        BYOIP CIDR.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_ipam_byoasn.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_ipam_byoasn)
        """

    def disassociate_ipam_resource_discovery(
        self, **kwargs: Unpack[DisassociateIpamResourceDiscoveryRequestTypeDef]
    ) -> DisassociateIpamResourceDiscoveryResultTypeDef:
        """
        Disassociates a resource discovery from an Amazon VPC IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_ipam_resource_discovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_ipam_resource_discovery)
        """

    def disassociate_nat_gateway_address(
        self, **kwargs: Unpack[DisassociateNatGatewayAddressRequestTypeDef]
    ) -> DisassociateNatGatewayAddressResultTypeDef:
        """
        Disassociates secondary Elastic IP addresses (EIPs) from a public NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_nat_gateway_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_nat_gateway_address)
        """

    def disassociate_route_server(
        self, **kwargs: Unpack[DisassociateRouteServerRequestTypeDef]
    ) -> DisassociateRouteServerResultTypeDef:
        """
        Disassociates a route server from a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_route_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_route_server)
        """

    def disassociate_route_table(
        self, **kwargs: Unpack[DisassociateRouteTableRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Disassociates a subnet or gateway from a route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_route_table)
        """

    def disassociate_security_group_vpc(
        self, **kwargs: Unpack[DisassociateSecurityGroupVpcRequestTypeDef]
    ) -> DisassociateSecurityGroupVpcResultTypeDef:
        """
        Disassociates a security group from a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_security_group_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_security_group_vpc)
        """

    def disassociate_subnet_cidr_block(
        self, **kwargs: Unpack[DisassociateSubnetCidrBlockRequestTypeDef]
    ) -> DisassociateSubnetCidrBlockResultTypeDef:
        """
        Disassociates a CIDR block from a subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_subnet_cidr_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_subnet_cidr_block)
        """

    def disassociate_transit_gateway_multicast_domain(
        self, **kwargs: Unpack[DisassociateTransitGatewayMulticastDomainRequestTypeDef]
    ) -> DisassociateTransitGatewayMulticastDomainResultTypeDef:
        """
        Disassociates the specified subnets from the transit gateway multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_transit_gateway_multicast_domain.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_transit_gateway_multicast_domain)
        """

    def disassociate_transit_gateway_policy_table(
        self, **kwargs: Unpack[DisassociateTransitGatewayPolicyTableRequestTypeDef]
    ) -> DisassociateTransitGatewayPolicyTableResultTypeDef:
        """
        Removes the association between an an attachment and a policy table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_transit_gateway_policy_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_transit_gateway_policy_table)
        """

    def disassociate_transit_gateway_route_table(
        self, **kwargs: Unpack[DisassociateTransitGatewayRouteTableRequestTypeDef]
    ) -> DisassociateTransitGatewayRouteTableResultTypeDef:
        """
        Disassociates a resource attachment from a transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_transit_gateway_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_transit_gateway_route_table)
        """

    def disassociate_trunk_interface(
        self, **kwargs: Unpack[DisassociateTrunkInterfaceRequestTypeDef]
    ) -> DisassociateTrunkInterfaceResultTypeDef:
        """
        Removes an association between a branch network interface with a trunk network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_trunk_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_trunk_interface)
        """

    def disassociate_vpc_cidr_block(
        self, **kwargs: Unpack[DisassociateVpcCidrBlockRequestTypeDef]
    ) -> DisassociateVpcCidrBlockResultTypeDef:
        """
        Disassociates a CIDR block from a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/disassociate_vpc_cidr_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#disassociate_vpc_cidr_block)
        """

    def enable_address_transfer(
        self, **kwargs: Unpack[EnableAddressTransferRequestTypeDef]
    ) -> EnableAddressTransferResultTypeDef:
        """
        Enables Elastic IP address transfer.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_address_transfer.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_address_transfer)
        """

    def enable_allowed_images_settings(
        self, **kwargs: Unpack[EnableAllowedImagesSettingsRequestTypeDef]
    ) -> EnableAllowedImagesSettingsResultTypeDef:
        """
        Enables Allowed AMIs for your account in the specified Amazon Web Services
        Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_allowed_images_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_allowed_images_settings)
        """

    def enable_aws_network_performance_metric_subscription(
        self, **kwargs: Unpack[EnableAwsNetworkPerformanceMetricSubscriptionRequestTypeDef]
    ) -> EnableAwsNetworkPerformanceMetricSubscriptionResultTypeDef:
        """
        Enables Infrastructure Performance subscriptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_aws_network_performance_metric_subscription.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_aws_network_performance_metric_subscription)
        """

    def enable_ebs_encryption_by_default(
        self, **kwargs: Unpack[EnableEbsEncryptionByDefaultRequestTypeDef]
    ) -> EnableEbsEncryptionByDefaultResultTypeDef:
        """
        Enables EBS encryption by default for your account in the current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_ebs_encryption_by_default.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_ebs_encryption_by_default)
        """

    def enable_fast_launch(
        self, **kwargs: Unpack[EnableFastLaunchRequestTypeDef]
    ) -> EnableFastLaunchResultTypeDef:
        """
        When you enable Windows fast launch for a Windows AMI, images are
        pre-provisioned, using snapshots to launch instances up to 65% faster.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_fast_launch.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_fast_launch)
        """

    def enable_fast_snapshot_restores(
        self, **kwargs: Unpack[EnableFastSnapshotRestoresRequestTypeDef]
    ) -> EnableFastSnapshotRestoresResultTypeDef:
        """
        Enables fast snapshot restores for the specified snapshots in the specified
        Availability Zones.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_fast_snapshot_restores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_fast_snapshot_restores)
        """

    def enable_image(self, **kwargs: Unpack[EnableImageRequestTypeDef]) -> EnableImageResultTypeDef:
        """
        Re-enables a disabled AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_image)
        """

    def enable_image_block_public_access(
        self, **kwargs: Unpack[EnableImageBlockPublicAccessRequestTypeDef]
    ) -> EnableImageBlockPublicAccessResultTypeDef:
        """
        Enables <i>block public access for AMIs</i> at the account level in the
        specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_image_block_public_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_image_block_public_access)
        """

    def enable_image_deprecation(
        self, **kwargs: Unpack[EnableImageDeprecationRequestTypeDef]
    ) -> EnableImageDeprecationResultTypeDef:
        """
        Enables deprecation of the specified AMI at the specified date and time.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_image_deprecation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_image_deprecation)
        """

    def enable_image_deregistration_protection(
        self, **kwargs: Unpack[EnableImageDeregistrationProtectionRequestTypeDef]
    ) -> EnableImageDeregistrationProtectionResultTypeDef:
        """
        Enables deregistration protection for an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_image_deregistration_protection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_image_deregistration_protection)
        """

    def enable_ipam_organization_admin_account(
        self, **kwargs: Unpack[EnableIpamOrganizationAdminAccountRequestTypeDef]
    ) -> EnableIpamOrganizationAdminAccountResultTypeDef:
        """
        Enable an Organizations member account as the IPAM admin account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_ipam_organization_admin_account.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_ipam_organization_admin_account)
        """

    def enable_reachability_analyzer_organization_sharing(
        self, **kwargs: Unpack[EnableReachabilityAnalyzerOrganizationSharingRequestTypeDef]
    ) -> EnableReachabilityAnalyzerOrganizationSharingResultTypeDef:
        """
        Establishes a trust relationship between Reachability Analyzer and
        Organizations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_reachability_analyzer_organization_sharing.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_reachability_analyzer_organization_sharing)
        """

    def enable_route_server_propagation(
        self, **kwargs: Unpack[EnableRouteServerPropagationRequestTypeDef]
    ) -> EnableRouteServerPropagationResultTypeDef:
        """
        Defines which route tables the route server can update with routes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_route_server_propagation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_route_server_propagation)
        """

    def enable_serial_console_access(
        self, **kwargs: Unpack[EnableSerialConsoleAccessRequestTypeDef]
    ) -> EnableSerialConsoleAccessResultTypeDef:
        """
        Enables access to the EC2 serial console of all instances for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_serial_console_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_serial_console_access)
        """

    def enable_snapshot_block_public_access(
        self, **kwargs: Unpack[EnableSnapshotBlockPublicAccessRequestTypeDef]
    ) -> EnableSnapshotBlockPublicAccessResultTypeDef:
        """
        Enables or modifies the <i>block public access for snapshots</i> setting at the
        account level for the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_snapshot_block_public_access.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_snapshot_block_public_access)
        """

    def enable_transit_gateway_route_table_propagation(
        self, **kwargs: Unpack[EnableTransitGatewayRouteTablePropagationRequestTypeDef]
    ) -> EnableTransitGatewayRouteTablePropagationResultTypeDef:
        """
        Enables the specified attachment to propagate routes to the specified
        propagation route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_transit_gateway_route_table_propagation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_transit_gateway_route_table_propagation)
        """

    def enable_vgw_route_propagation(
        self, **kwargs: Unpack[EnableVgwRoutePropagationRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables a virtual private gateway (VGW) to propagate routes to the specified
        route table of a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_vgw_route_propagation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_vgw_route_propagation)
        """

    def enable_volume_io(
        self, **kwargs: Unpack[EnableVolumeIORequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Enables I/O operations for a volume that had I/O operations disabled because
        the data on the volume was potentially inconsistent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_volume_io.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_volume_io)
        """

    def enable_vpc_classic_link(
        self, **kwargs: Unpack[EnableVpcClassicLinkRequestTypeDef]
    ) -> EnableVpcClassicLinkResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_vpc_classic_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_vpc_classic_link)
        """

    def enable_vpc_classic_link_dns_support(
        self, **kwargs: Unpack[EnableVpcClassicLinkDnsSupportRequestTypeDef]
    ) -> EnableVpcClassicLinkDnsSupportResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/enable_vpc_classic_link_dns_support.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#enable_vpc_classic_link_dns_support)
        """

    def export_client_vpn_client_certificate_revocation_list(
        self, **kwargs: Unpack[ExportClientVpnClientCertificateRevocationListRequestTypeDef]
    ) -> ExportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        Downloads the client certificate revocation list for the specified Client VPN
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/export_client_vpn_client_certificate_revocation_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#export_client_vpn_client_certificate_revocation_list)
        """

    def export_client_vpn_client_configuration(
        self, **kwargs: Unpack[ExportClientVpnClientConfigurationRequestTypeDef]
    ) -> ExportClientVpnClientConfigurationResultTypeDef:
        """
        Downloads the contents of the Client VPN endpoint configuration file for the
        specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/export_client_vpn_client_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#export_client_vpn_client_configuration)
        """

    def export_image(self, **kwargs: Unpack[ExportImageRequestTypeDef]) -> ExportImageResultTypeDef:
        """
        Exports an Amazon Machine Image (AMI) to a VM file.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/export_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#export_image)
        """

    def export_transit_gateway_routes(
        self, **kwargs: Unpack[ExportTransitGatewayRoutesRequestTypeDef]
    ) -> ExportTransitGatewayRoutesResultTypeDef:
        """
        Exports routes from the specified transit gateway route table to the specified
        S3 bucket.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/export_transit_gateway_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#export_transit_gateway_routes)
        """

    def export_verified_access_instance_client_configuration(
        self, **kwargs: Unpack[ExportVerifiedAccessInstanceClientConfigurationRequestTypeDef]
    ) -> ExportVerifiedAccessInstanceClientConfigurationResultTypeDef:
        """
        Exports the client configuration for a Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/export_verified_access_instance_client_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#export_verified_access_instance_client_configuration)
        """

    def get_allowed_images_settings(
        self, **kwargs: Unpack[GetAllowedImagesSettingsRequestTypeDef]
    ) -> GetAllowedImagesSettingsResultTypeDef:
        """
        Gets the current state of the Allowed AMIs setting and the list of Allowed AMIs
        criteria at the account level in the specified Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_allowed_images_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_allowed_images_settings)
        """

    def get_associated_enclave_certificate_iam_roles(
        self, **kwargs: Unpack[GetAssociatedEnclaveCertificateIamRolesRequestTypeDef]
    ) -> GetAssociatedEnclaveCertificateIamRolesResultTypeDef:
        """
        Returns the IAM roles that are associated with the specified ACM (ACM)
        certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_associated_enclave_certificate_iam_roles.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_associated_enclave_certificate_iam_roles)
        """

    def get_associated_ipv6_pool_cidrs(
        self, **kwargs: Unpack[GetAssociatedIpv6PoolCidrsRequestTypeDef]
    ) -> GetAssociatedIpv6PoolCidrsResultTypeDef:
        """
        Gets information about the IPv6 CIDR block associations for a specified IPv6
        address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_associated_ipv6_pool_cidrs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_associated_ipv6_pool_cidrs)
        """

    def get_aws_network_performance_data(
        self, **kwargs: Unpack[GetAwsNetworkPerformanceDataRequestTypeDef]
    ) -> GetAwsNetworkPerformanceDataResultTypeDef:
        """
        Gets network performance data.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_aws_network_performance_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_aws_network_performance_data)
        """

    def get_capacity_reservation_usage(
        self, **kwargs: Unpack[GetCapacityReservationUsageRequestTypeDef]
    ) -> GetCapacityReservationUsageResultTypeDef:
        """
        Gets usage information about a Capacity Reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_capacity_reservation_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_capacity_reservation_usage)
        """

    def get_coip_pool_usage(
        self, **kwargs: Unpack[GetCoipPoolUsageRequestTypeDef]
    ) -> GetCoipPoolUsageResultTypeDef:
        """
        Describes the allocations from the specified customer-owned address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_coip_pool_usage.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_coip_pool_usage)
        """

    def get_console_output(
        self, **kwargs: Unpack[GetConsoleOutputRequestTypeDef]
    ) -> GetConsoleOutputResultTypeDef:
        """
        Gets the console output for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_console_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_console_output)
        """

    def get_console_screenshot(
        self, **kwargs: Unpack[GetConsoleScreenshotRequestTypeDef]
    ) -> GetConsoleScreenshotResultTypeDef:
        """
        Retrieve a JPG-format screenshot of a running instance to help with
        troubleshooting.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_console_screenshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_console_screenshot)
        """

    def get_declarative_policies_report_summary(
        self, **kwargs: Unpack[GetDeclarativePoliciesReportSummaryRequestTypeDef]
    ) -> GetDeclarativePoliciesReportSummaryResultTypeDef:
        """
        Retrieves a summary of the account status report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_declarative_policies_report_summary.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_declarative_policies_report_summary)
        """

    def get_default_credit_specification(
        self, **kwargs: Unpack[GetDefaultCreditSpecificationRequestTypeDef]
    ) -> GetDefaultCreditSpecificationResultTypeDef:
        """
        Describes the default credit option for CPU usage of a burstable performance
        instance family.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_default_credit_specification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_default_credit_specification)
        """

    def get_ebs_default_kms_key_id(
        self, **kwargs: Unpack[GetEbsDefaultKmsKeyIdRequestTypeDef]
    ) -> GetEbsDefaultKmsKeyIdResultTypeDef:
        """
        Describes the default KMS key for EBS encryption by default for your account in
        this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_ebs_default_kms_key_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ebs_default_kms_key_id)
        """

    def get_ebs_encryption_by_default(
        self, **kwargs: Unpack[GetEbsEncryptionByDefaultRequestTypeDef]
    ) -> GetEbsEncryptionByDefaultResultTypeDef:
        """
        Describes whether EBS encryption by default is enabled for your account in the
        current Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_ebs_encryption_by_default.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ebs_encryption_by_default)
        """

    def get_flow_logs_integration_template(
        self, **kwargs: Unpack[GetFlowLogsIntegrationTemplateRequestTypeDef]
    ) -> GetFlowLogsIntegrationTemplateResultTypeDef:
        """
        Generates a CloudFormation template that streamlines and automates the
        integration of VPC flow logs with Amazon Athena.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_flow_logs_integration_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_flow_logs_integration_template)
        """

    def get_groups_for_capacity_reservation(
        self, **kwargs: Unpack[GetGroupsForCapacityReservationRequestTypeDef]
    ) -> GetGroupsForCapacityReservationResultTypeDef:
        """
        Lists the resource groups to which a Capacity Reservation has been added.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_groups_for_capacity_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_groups_for_capacity_reservation)
        """

    def get_host_reservation_purchase_preview(
        self, **kwargs: Unpack[GetHostReservationPurchasePreviewRequestTypeDef]
    ) -> GetHostReservationPurchasePreviewResultTypeDef:
        """
        Preview a reservation purchase with configurations that match those of your
        Dedicated Host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_host_reservation_purchase_preview.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_host_reservation_purchase_preview)
        """

    def get_image_block_public_access_state(
        self, **kwargs: Unpack[GetImageBlockPublicAccessStateRequestTypeDef]
    ) -> GetImageBlockPublicAccessStateResultTypeDef:
        """
        Gets the current state of <i>block public access for AMIs</i> at the account
        level in the specified Amazon Web Services Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_image_block_public_access_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_image_block_public_access_state)
        """

    def get_instance_metadata_defaults(
        self, **kwargs: Unpack[GetInstanceMetadataDefaultsRequestTypeDef]
    ) -> GetInstanceMetadataDefaultsResultTypeDef:
        """
        Gets the default instance metadata service (IMDS) settings that are set at the
        account level in the specified Amazon Web Services&#x2028; Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_instance_metadata_defaults.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_instance_metadata_defaults)
        """

    def get_instance_tpm_ek_pub(
        self, **kwargs: Unpack[GetInstanceTpmEkPubRequestTypeDef]
    ) -> GetInstanceTpmEkPubResultTypeDef:
        """
        Gets the public endorsement key associated with the Nitro Trusted Platform
        Module (NitroTPM) for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_instance_tpm_ek_pub.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_instance_tpm_ek_pub)
        """

    def get_instance_types_from_instance_requirements(
        self, **kwargs: Unpack[GetInstanceTypesFromInstanceRequirementsRequestTypeDef]
    ) -> GetInstanceTypesFromInstanceRequirementsResultTypeDef:
        """
        Returns a list of instance types with the specified instance attributes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_instance_types_from_instance_requirements.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_instance_types_from_instance_requirements)
        """

    def get_instance_uefi_data(
        self, **kwargs: Unpack[GetInstanceUefiDataRequestTypeDef]
    ) -> GetInstanceUefiDataResultTypeDef:
        """
        A binary representation of the UEFI variable store.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_instance_uefi_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_instance_uefi_data)
        """

    def get_ipam_address_history(
        self, **kwargs: Unpack[GetIpamAddressHistoryRequestTypeDef]
    ) -> GetIpamAddressHistoryResultTypeDef:
        """
        Retrieve historical information about a CIDR within an IPAM scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_ipam_address_history.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_address_history)
        """

    def get_ipam_discovered_accounts(
        self, **kwargs: Unpack[GetIpamDiscoveredAccountsRequestTypeDef]
    ) -> GetIpamDiscoveredAccountsResultTypeDef:
        """
        Gets IPAM discovered accounts.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_ipam_discovered_accounts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_discovered_accounts)
        """

    def get_ipam_discovered_public_addresses(
        self, **kwargs: Unpack[GetIpamDiscoveredPublicAddressesRequestTypeDef]
    ) -> GetIpamDiscoveredPublicAddressesResultTypeDef:
        """
        Gets the public IP addresses that have been discovered by IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_ipam_discovered_public_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_discovered_public_addresses)
        """

    def get_ipam_discovered_resource_cidrs(
        self, **kwargs: Unpack[GetIpamDiscoveredResourceCidrsRequestTypeDef]
    ) -> GetIpamDiscoveredResourceCidrsResultTypeDef:
        """
        Returns the resource CIDRs that are monitored as part of a resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_ipam_discovered_resource_cidrs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_discovered_resource_cidrs)
        """

    def get_ipam_pool_allocations(
        self, **kwargs: Unpack[GetIpamPoolAllocationsRequestTypeDef]
    ) -> GetIpamPoolAllocationsResultTypeDef:
        """
        Get a list of all the CIDR allocations in an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_ipam_pool_allocations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_pool_allocations)
        """

    def get_ipam_pool_cidrs(
        self, **kwargs: Unpack[GetIpamPoolCidrsRequestTypeDef]
    ) -> GetIpamPoolCidrsResultTypeDef:
        """
        Get the CIDRs provisioned to an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_ipam_pool_cidrs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_pool_cidrs)
        """

    def get_ipam_resource_cidrs(
        self, **kwargs: Unpack[GetIpamResourceCidrsRequestTypeDef]
    ) -> GetIpamResourceCidrsResultTypeDef:
        """
        Returns resource CIDRs managed by IPAM in a given scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_ipam_resource_cidrs.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_ipam_resource_cidrs)
        """

    def get_launch_template_data(
        self, **kwargs: Unpack[GetLaunchTemplateDataRequestTypeDef]
    ) -> GetLaunchTemplateDataResultTypeDef:
        """
        Retrieves the configuration data of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_launch_template_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_launch_template_data)
        """

    def get_managed_prefix_list_associations(
        self, **kwargs: Unpack[GetManagedPrefixListAssociationsRequestTypeDef]
    ) -> GetManagedPrefixListAssociationsResultTypeDef:
        """
        Gets information about the resources that are associated with the specified
        managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_managed_prefix_list_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_managed_prefix_list_associations)
        """

    def get_managed_prefix_list_entries(
        self, **kwargs: Unpack[GetManagedPrefixListEntriesRequestTypeDef]
    ) -> GetManagedPrefixListEntriesResultTypeDef:
        """
        Gets information about the entries for a specified managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_managed_prefix_list_entries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_managed_prefix_list_entries)
        """

    def get_network_insights_access_scope_analysis_findings(
        self, **kwargs: Unpack[GetNetworkInsightsAccessScopeAnalysisFindingsRequestTypeDef]
    ) -> GetNetworkInsightsAccessScopeAnalysisFindingsResultTypeDef:
        """
        Gets the findings for the specified Network Access Scope analysis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_network_insights_access_scope_analysis_findings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_network_insights_access_scope_analysis_findings)
        """

    def get_network_insights_access_scope_content(
        self, **kwargs: Unpack[GetNetworkInsightsAccessScopeContentRequestTypeDef]
    ) -> GetNetworkInsightsAccessScopeContentResultTypeDef:
        """
        Gets the content for the specified Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_network_insights_access_scope_content.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_network_insights_access_scope_content)
        """

    def get_password_data(
        self, **kwargs: Unpack[GetPasswordDataRequestTypeDef]
    ) -> GetPasswordDataResultTypeDef:
        """
        Retrieves the encrypted administrator password for a running Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_password_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_password_data)
        """

    def get_reserved_instances_exchange_quote(
        self, **kwargs: Unpack[GetReservedInstancesExchangeQuoteRequestTypeDef]
    ) -> GetReservedInstancesExchangeQuoteResultTypeDef:
        """
        Returns a quote and exchange information for exchanging one or more specified
        Convertible Reserved Instances for a new Convertible Reserved Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_reserved_instances_exchange_quote.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_reserved_instances_exchange_quote)
        """

    def get_route_server_associations(
        self, **kwargs: Unpack[GetRouteServerAssociationsRequestTypeDef]
    ) -> GetRouteServerAssociationsResultTypeDef:
        """
        Gets information about the associations for the specified route server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_route_server_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_route_server_associations)
        """

    def get_route_server_propagations(
        self, **kwargs: Unpack[GetRouteServerPropagationsRequestTypeDef]
    ) -> GetRouteServerPropagationsResultTypeDef:
        """
        Gets information about the route propagations for the specified route server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_route_server_propagations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_route_server_propagations)
        """

    def get_route_server_routing_database(
        self, **kwargs: Unpack[GetRouteServerRoutingDatabaseRequestTypeDef]
    ) -> GetRouteServerRoutingDatabaseResultTypeDef:
        """
        Gets the routing database for the specified route server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_route_server_routing_database.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_route_server_routing_database)
        """

    def get_security_groups_for_vpc(
        self, **kwargs: Unpack[GetSecurityGroupsForVpcRequestTypeDef]
    ) -> GetSecurityGroupsForVpcResultTypeDef:
        """
        Gets security groups that can be associated by the Amazon Web Services account
        making the request with network interfaces in the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_security_groups_for_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_security_groups_for_vpc)
        """

    def get_serial_console_access_status(
        self, **kwargs: Unpack[GetSerialConsoleAccessStatusRequestTypeDef]
    ) -> GetSerialConsoleAccessStatusResultTypeDef:
        """
        Retrieves the access status of your account to the EC2 serial console of all
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_serial_console_access_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_serial_console_access_status)
        """

    def get_snapshot_block_public_access_state(
        self, **kwargs: Unpack[GetSnapshotBlockPublicAccessStateRequestTypeDef]
    ) -> GetSnapshotBlockPublicAccessStateResultTypeDef:
        """
        Gets the current state of <i>block public access for snapshots</i> setting for
        the account and Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_snapshot_block_public_access_state.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_snapshot_block_public_access_state)
        """

    def get_spot_placement_scores(
        self, **kwargs: Unpack[GetSpotPlacementScoresRequestTypeDef]
    ) -> GetSpotPlacementScoresResultTypeDef:
        """
        Calculates the Spot placement score for a Region or Availability Zone based on
        the specified target capacity and compute requirements.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_spot_placement_scores.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_spot_placement_scores)
        """

    def get_subnet_cidr_reservations(
        self, **kwargs: Unpack[GetSubnetCidrReservationsRequestTypeDef]
    ) -> GetSubnetCidrReservationsResultTypeDef:
        """
        Gets information about the subnet CIDR reservations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_subnet_cidr_reservations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_subnet_cidr_reservations)
        """

    def get_transit_gateway_attachment_propagations(
        self, **kwargs: Unpack[GetTransitGatewayAttachmentPropagationsRequestTypeDef]
    ) -> GetTransitGatewayAttachmentPropagationsResultTypeDef:
        """
        Lists the route tables to which the specified resource attachment propagates
        routes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_transit_gateway_attachment_propagations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_attachment_propagations)
        """

    def get_transit_gateway_multicast_domain_associations(
        self, **kwargs: Unpack[GetTransitGatewayMulticastDomainAssociationsRequestTypeDef]
    ) -> GetTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        Gets information about the associations for the transit gateway multicast
        domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_transit_gateway_multicast_domain_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_multicast_domain_associations)
        """

    def get_transit_gateway_policy_table_associations(
        self, **kwargs: Unpack[GetTransitGatewayPolicyTableAssociationsRequestTypeDef]
    ) -> GetTransitGatewayPolicyTableAssociationsResultTypeDef:
        """
        Gets a list of the transit gateway policy table associations.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_transit_gateway_policy_table_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_policy_table_associations)
        """

    def get_transit_gateway_policy_table_entries(
        self, **kwargs: Unpack[GetTransitGatewayPolicyTableEntriesRequestTypeDef]
    ) -> GetTransitGatewayPolicyTableEntriesResultTypeDef:
        """
        Returns a list of transit gateway policy table entries.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_transit_gateway_policy_table_entries.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_policy_table_entries)
        """

    def get_transit_gateway_prefix_list_references(
        self, **kwargs: Unpack[GetTransitGatewayPrefixListReferencesRequestTypeDef]
    ) -> GetTransitGatewayPrefixListReferencesResultTypeDef:
        """
        Gets information about the prefix list references in a specified transit
        gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_transit_gateway_prefix_list_references.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_prefix_list_references)
        """

    def get_transit_gateway_route_table_associations(
        self, **kwargs: Unpack[GetTransitGatewayRouteTableAssociationsRequestTypeDef]
    ) -> GetTransitGatewayRouteTableAssociationsResultTypeDef:
        """
        Gets information about the associations for the specified transit gateway route
        table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_transit_gateway_route_table_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_route_table_associations)
        """

    def get_transit_gateway_route_table_propagations(
        self, **kwargs: Unpack[GetTransitGatewayRouteTablePropagationsRequestTypeDef]
    ) -> GetTransitGatewayRouteTablePropagationsResultTypeDef:
        """
        Gets information about the route table propagations for the specified transit
        gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_transit_gateway_route_table_propagations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_transit_gateway_route_table_propagations)
        """

    def get_verified_access_endpoint_policy(
        self, **kwargs: Unpack[GetVerifiedAccessEndpointPolicyRequestTypeDef]
    ) -> GetVerifiedAccessEndpointPolicyResultTypeDef:
        """
        Get the Verified Access policy associated with the endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_verified_access_endpoint_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_verified_access_endpoint_policy)
        """

    def get_verified_access_endpoint_targets(
        self, **kwargs: Unpack[GetVerifiedAccessEndpointTargetsRequestTypeDef]
    ) -> GetVerifiedAccessEndpointTargetsResultTypeDef:
        """
        Gets the targets for the specified network CIDR endpoint for Verified Access.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_verified_access_endpoint_targets.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_verified_access_endpoint_targets)
        """

    def get_verified_access_group_policy(
        self, **kwargs: Unpack[GetVerifiedAccessGroupPolicyRequestTypeDef]
    ) -> GetVerifiedAccessGroupPolicyResultTypeDef:
        """
        Shows the contents of the Verified Access policy associated with the group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_verified_access_group_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_verified_access_group_policy)
        """

    def get_vpn_connection_device_sample_configuration(
        self, **kwargs: Unpack[GetVpnConnectionDeviceSampleConfigurationRequestTypeDef]
    ) -> GetVpnConnectionDeviceSampleConfigurationResultTypeDef:
        """
        Download an Amazon Web Services-provided sample configuration file to be used
        with the customer gateway device specified for your Site-to-Site VPN
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_vpn_connection_device_sample_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_vpn_connection_device_sample_configuration)
        """

    def get_vpn_connection_device_types(
        self, **kwargs: Unpack[GetVpnConnectionDeviceTypesRequestTypeDef]
    ) -> GetVpnConnectionDeviceTypesResultTypeDef:
        """
        Obtain a list of customer gateway devices for which sample configuration files
        can be provided.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_vpn_connection_device_types.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_vpn_connection_device_types)
        """

    def get_vpn_tunnel_replacement_status(
        self, **kwargs: Unpack[GetVpnTunnelReplacementStatusRequestTypeDef]
    ) -> GetVpnTunnelReplacementStatusResultTypeDef:
        """
        Get details of available tunnel endpoint maintenance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_vpn_tunnel_replacement_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_vpn_tunnel_replacement_status)
        """

    def import_client_vpn_client_certificate_revocation_list(
        self, **kwargs: Unpack[ImportClientVpnClientCertificateRevocationListRequestTypeDef]
    ) -> ImportClientVpnClientCertificateRevocationListResultTypeDef:
        """
        Uploads a client certificate revocation list to the specified Client VPN
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/import_client_vpn_client_certificate_revocation_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_client_vpn_client_certificate_revocation_list)
        """

    def import_image(self, **kwargs: Unpack[ImportImageRequestTypeDef]) -> ImportImageResultTypeDef:
        """
        To import your virtual machines (VMs) with a console-based experience, you can
        use the <i>Import virtual machine images to Amazon Web Services</i> template in
        the <a
        href="https://console.aws.amazon.com/migrationhub/orchestrator">Migration Hub
        Orchestrator console</a>.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/import_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_image)
        """

    def import_instance(
        self, **kwargs: Unpack[ImportInstanceRequestTypeDef]
    ) -> ImportInstanceResultTypeDef:
        """
        We recommend that you use the <a
        href="https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ImportImage.html">
        <code>ImportImage</code> </a> API instead.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/import_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_instance)
        """

    def import_key_pair(
        self, **kwargs: Unpack[ImportKeyPairRequestTypeDef]
    ) -> ImportKeyPairResultTypeDef:
        """
        Imports the public key from an RSA or ED25519 key pair that you created using a
        third-party tool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/import_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_key_pair)
        """

    def import_snapshot(
        self, **kwargs: Unpack[ImportSnapshotRequestTypeDef]
    ) -> ImportSnapshotResultTypeDef:
        """
        Imports a disk into an EBS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/import_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_snapshot)
        """

    def import_volume(
        self, **kwargs: Unpack[ImportVolumeRequestTypeDef]
    ) -> ImportVolumeResultTypeDef:
        """
        This API action supports only single-volume VMs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/import_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#import_volume)
        """

    def list_images_in_recycle_bin(
        self, **kwargs: Unpack[ListImagesInRecycleBinRequestTypeDef]
    ) -> ListImagesInRecycleBinResultTypeDef:
        """
        Lists one or more AMIs that are currently in the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/list_images_in_recycle_bin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#list_images_in_recycle_bin)
        """

    def list_snapshots_in_recycle_bin(
        self, **kwargs: Unpack[ListSnapshotsInRecycleBinRequestTypeDef]
    ) -> ListSnapshotsInRecycleBinResultTypeDef:
        """
        Lists one or more snapshots that are currently in the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/list_snapshots_in_recycle_bin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#list_snapshots_in_recycle_bin)
        """

    def lock_snapshot(
        self, **kwargs: Unpack[LockSnapshotRequestTypeDef]
    ) -> LockSnapshotResultTypeDef:
        """
        Locks an Amazon EBS snapshot in either <i>governance</i> or <i>compliance</i>
        mode to protect it against accidental or malicious deletions for a specific
        duration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/lock_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#lock_snapshot)
        """

    def modify_address_attribute(
        self, **kwargs: Unpack[ModifyAddressAttributeRequestTypeDef]
    ) -> ModifyAddressAttributeResultTypeDef:
        """
        Modifies an attribute of the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_address_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_address_attribute)
        """

    def modify_availability_zone_group(
        self, **kwargs: Unpack[ModifyAvailabilityZoneGroupRequestTypeDef]
    ) -> ModifyAvailabilityZoneGroupResultTypeDef:
        """
        Changes the opt-in status of the specified zone group for your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_availability_zone_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_availability_zone_group)
        """

    def modify_capacity_reservation(
        self, **kwargs: Unpack[ModifyCapacityReservationRequestTypeDef]
    ) -> ModifyCapacityReservationResultTypeDef:
        """
        Modifies a Capacity Reservation's capacity, instance eligibility, and the
        conditions under which it is to be released.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_capacity_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_capacity_reservation)
        """

    def modify_capacity_reservation_fleet(
        self, **kwargs: Unpack[ModifyCapacityReservationFleetRequestTypeDef]
    ) -> ModifyCapacityReservationFleetResultTypeDef:
        """
        Modifies a Capacity Reservation Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_capacity_reservation_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_capacity_reservation_fleet)
        """

    def modify_client_vpn_endpoint(
        self, **kwargs: Unpack[ModifyClientVpnEndpointRequestTypeDef]
    ) -> ModifyClientVpnEndpointResultTypeDef:
        """
        Modifies the specified Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_client_vpn_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_client_vpn_endpoint)
        """

    def modify_default_credit_specification(
        self, **kwargs: Unpack[ModifyDefaultCreditSpecificationRequestTypeDef]
    ) -> ModifyDefaultCreditSpecificationResultTypeDef:
        """
        Modifies the default credit option for CPU usage of burstable performance
        instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_default_credit_specification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_default_credit_specification)
        """

    def modify_ebs_default_kms_key_id(
        self, **kwargs: Unpack[ModifyEbsDefaultKmsKeyIdRequestTypeDef]
    ) -> ModifyEbsDefaultKmsKeyIdResultTypeDef:
        """
        Changes the default KMS key for EBS encryption by default for your account in
        this Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_ebs_default_kms_key_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ebs_default_kms_key_id)
        """

    def modify_fleet(self, **kwargs: Unpack[ModifyFleetRequestTypeDef]) -> ModifyFleetResultTypeDef:
        """
        Modifies the specified EC2 Fleet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_fleet)
        """

    def modify_fpga_image_attribute(
        self, **kwargs: Unpack[ModifyFpgaImageAttributeRequestTypeDef]
    ) -> ModifyFpgaImageAttributeResultTypeDef:
        """
        Modifies the specified attribute of the specified Amazon FPGA Image (AFI).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_fpga_image_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_fpga_image_attribute)
        """

    def modify_hosts(self, **kwargs: Unpack[ModifyHostsRequestTypeDef]) -> ModifyHostsResultTypeDef:
        """
        Modify the auto-placement setting of a Dedicated Host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_hosts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_hosts)
        """

    def modify_id_format(
        self, **kwargs: Unpack[ModifyIdFormatRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the ID format for the specified resource on a per-Region basis.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_id_format.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_id_format)
        """

    def modify_identity_id_format(
        self, **kwargs: Unpack[ModifyIdentityIdFormatRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the ID format of a resource for a specified IAM user, IAM role, or the
        root user for an account; or all IAM users, IAM roles, and the root user for an
        account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_identity_id_format.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_identity_id_format)
        """

    def modify_image_attribute(
        self, **kwargs: Unpack[ModifyImageAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_image_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_image_attribute)
        """

    def modify_instance_attribute(
        self, **kwargs: Unpack[ModifyInstanceAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_attribute)
        """

    def modify_instance_capacity_reservation_attributes(
        self, **kwargs: Unpack[ModifyInstanceCapacityReservationAttributesRequestTypeDef]
    ) -> ModifyInstanceCapacityReservationAttributesResultTypeDef:
        """
        Modifies the Capacity Reservation settings for a stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_capacity_reservation_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_capacity_reservation_attributes)
        """

    def modify_instance_cpu_options(
        self, **kwargs: Unpack[ModifyInstanceCpuOptionsRequestTypeDef]
    ) -> ModifyInstanceCpuOptionsResultTypeDef:
        """
        By default, all vCPUs for the instance type are active when you launch an
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_cpu_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_cpu_options)
        """

    def modify_instance_credit_specification(
        self, **kwargs: Unpack[ModifyInstanceCreditSpecificationRequestTypeDef]
    ) -> ModifyInstanceCreditSpecificationResultTypeDef:
        """
        Modifies the credit option for CPU usage on a running or stopped burstable
        performance instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_credit_specification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_credit_specification)
        """

    def modify_instance_event_start_time(
        self, **kwargs: Unpack[ModifyInstanceEventStartTimeRequestTypeDef]
    ) -> ModifyInstanceEventStartTimeResultTypeDef:
        """
        Modifies the start time for a scheduled Amazon EC2 instance event.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_event_start_time.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_event_start_time)
        """

    def modify_instance_event_window(
        self, **kwargs: Unpack[ModifyInstanceEventWindowRequestTypeDef]
    ) -> ModifyInstanceEventWindowResultTypeDef:
        """
        Modifies the specified event window.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_event_window.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_event_window)
        """

    def modify_instance_maintenance_options(
        self, **kwargs: Unpack[ModifyInstanceMaintenanceOptionsRequestTypeDef]
    ) -> ModifyInstanceMaintenanceOptionsResultTypeDef:
        """
        Modifies the recovery behavior of your instance to disable simplified automatic
        recovery or set the recovery behavior to default.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_maintenance_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_maintenance_options)
        """

    def modify_instance_metadata_defaults(
        self, **kwargs: Unpack[ModifyInstanceMetadataDefaultsRequestTypeDef]
    ) -> ModifyInstanceMetadataDefaultsResultTypeDef:
        """
        Modifies the default instance metadata service (IMDS) settings at the account
        level in the specified Amazon Web Services&#x2028; Region.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_metadata_defaults.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_metadata_defaults)
        """

    def modify_instance_metadata_options(
        self, **kwargs: Unpack[ModifyInstanceMetadataOptionsRequestTypeDef]
    ) -> ModifyInstanceMetadataOptionsResultTypeDef:
        """
        Modify the instance metadata parameters on a running or stopped instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_metadata_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_metadata_options)
        """

    def modify_instance_network_performance_options(
        self, **kwargs: Unpack[ModifyInstanceNetworkPerformanceRequestTypeDef]
    ) -> ModifyInstanceNetworkPerformanceResultTypeDef:
        """
        Change the configuration of the network performance options for an existing
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_network_performance_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_network_performance_options)
        """

    def modify_instance_placement(
        self, **kwargs: Unpack[ModifyInstancePlacementRequestTypeDef]
    ) -> ModifyInstancePlacementResultTypeDef:
        """
        Modifies the placement attributes for a specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_placement.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_instance_placement)
        """

    def modify_ipam(self, **kwargs: Unpack[ModifyIpamRequestTypeDef]) -> ModifyIpamResultTypeDef:
        """
        Modify the configurations of an IPAM.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_ipam.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam)
        """

    def modify_ipam_pool(
        self, **kwargs: Unpack[ModifyIpamPoolRequestTypeDef]
    ) -> ModifyIpamPoolResultTypeDef:
        """
        Modify the configurations of an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_ipam_pool.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam_pool)
        """

    def modify_ipam_resource_cidr(
        self, **kwargs: Unpack[ModifyIpamResourceCidrRequestTypeDef]
    ) -> ModifyIpamResourceCidrResultTypeDef:
        """
        Modify a resource CIDR.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_ipam_resource_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam_resource_cidr)
        """

    def modify_ipam_resource_discovery(
        self, **kwargs: Unpack[ModifyIpamResourceDiscoveryRequestTypeDef]
    ) -> ModifyIpamResourceDiscoveryResultTypeDef:
        """
        Modifies a resource discovery.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_ipam_resource_discovery.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam_resource_discovery)
        """

    def modify_ipam_scope(
        self, **kwargs: Unpack[ModifyIpamScopeRequestTypeDef]
    ) -> ModifyIpamScopeResultTypeDef:
        """
        Modify an IPAM scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_ipam_scope.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_ipam_scope)
        """

    def modify_launch_template(
        self, **kwargs: Unpack[ModifyLaunchTemplateRequestTypeDef]
    ) -> ModifyLaunchTemplateResultTypeDef:
        """
        Modifies a launch template.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_launch_template.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_launch_template)
        """

    def modify_local_gateway_route(
        self, **kwargs: Unpack[ModifyLocalGatewayRouteRequestTypeDef]
    ) -> ModifyLocalGatewayRouteResultTypeDef:
        """
        Modifies the specified local gateway route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_local_gateway_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_local_gateway_route)
        """

    def modify_managed_prefix_list(
        self, **kwargs: Unpack[ModifyManagedPrefixListRequestTypeDef]
    ) -> ModifyManagedPrefixListResultTypeDef:
        """
        Modifies the specified managed prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_managed_prefix_list.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_managed_prefix_list)
        """

    def modify_network_interface_attribute(
        self, **kwargs: Unpack[ModifyNetworkInterfaceAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_network_interface_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_network_interface_attribute)
        """

    def modify_private_dns_name_options(
        self, **kwargs: Unpack[ModifyPrivateDnsNameOptionsRequestTypeDef]
    ) -> ModifyPrivateDnsNameOptionsResultTypeDef:
        """
        Modifies the options for instance hostnames for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_private_dns_name_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_private_dns_name_options)
        """

    def modify_reserved_instances(
        self, **kwargs: Unpack[ModifyReservedInstancesRequestTypeDef]
    ) -> ModifyReservedInstancesResultTypeDef:
        """
        Modifies the configuration of your Reserved Instances, such as the Availability
        Zone, instance count, or instance type.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_reserved_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_reserved_instances)
        """

    def modify_route_server(
        self, **kwargs: Unpack[ModifyRouteServerRequestTypeDef]
    ) -> ModifyRouteServerResultTypeDef:
        """
        Modifies the configuration of an existing route server.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_route_server.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_route_server)
        """

    def modify_security_group_rules(
        self, **kwargs: Unpack[ModifySecurityGroupRulesRequestTypeDef]
    ) -> ModifySecurityGroupRulesResultTypeDef:
        """
        Modifies the rules of a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_security_group_rules.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_security_group_rules)
        """

    def modify_snapshot_attribute(
        self, **kwargs: Unpack[ModifySnapshotAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Adds or removes permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_snapshot_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_snapshot_attribute)
        """

    def modify_snapshot_tier(
        self, **kwargs: Unpack[ModifySnapshotTierRequestTypeDef]
    ) -> ModifySnapshotTierResultTypeDef:
        """
        Archives an Amazon EBS snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_snapshot_tier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_snapshot_tier)
        """

    def modify_spot_fleet_request(
        self, **kwargs: Unpack[ModifySpotFleetRequestRequestTypeDef]
    ) -> ModifySpotFleetRequestResponseTypeDef:
        """
        Modifies the specified Spot Fleet request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_spot_fleet_request.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_spot_fleet_request)
        """

    def modify_subnet_attribute(
        self, **kwargs: Unpack[ModifySubnetAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies a subnet attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_subnet_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_subnet_attribute)
        """

    def modify_traffic_mirror_filter_network_services(
        self, **kwargs: Unpack[ModifyTrafficMirrorFilterNetworkServicesRequestTypeDef]
    ) -> ModifyTrafficMirrorFilterNetworkServicesResultTypeDef:
        """
        Allows or restricts mirroring network services.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_traffic_mirror_filter_network_services.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_traffic_mirror_filter_network_services)
        """

    def modify_traffic_mirror_filter_rule(
        self, **kwargs: Unpack[ModifyTrafficMirrorFilterRuleRequestTypeDef]
    ) -> ModifyTrafficMirrorFilterRuleResultTypeDef:
        """
        Modifies the specified Traffic Mirror rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_traffic_mirror_filter_rule.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_traffic_mirror_filter_rule)
        """

    def modify_traffic_mirror_session(
        self, **kwargs: Unpack[ModifyTrafficMirrorSessionRequestTypeDef]
    ) -> ModifyTrafficMirrorSessionResultTypeDef:
        """
        Modifies a Traffic Mirror session.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_traffic_mirror_session.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_traffic_mirror_session)
        """

    def modify_transit_gateway(
        self, **kwargs: Unpack[ModifyTransitGatewayRequestTypeDef]
    ) -> ModifyTransitGatewayResultTypeDef:
        """
        Modifies the specified transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_transit_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_transit_gateway)
        """

    def modify_transit_gateway_prefix_list_reference(
        self, **kwargs: Unpack[ModifyTransitGatewayPrefixListReferenceRequestTypeDef]
    ) -> ModifyTransitGatewayPrefixListReferenceResultTypeDef:
        """
        Modifies a reference (route) to a prefix list in a specified transit gateway
        route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_transit_gateway_prefix_list_reference.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_transit_gateway_prefix_list_reference)
        """

    def modify_transit_gateway_vpc_attachment(
        self, **kwargs: Unpack[ModifyTransitGatewayVpcAttachmentRequestTypeDef]
    ) -> ModifyTransitGatewayVpcAttachmentResultTypeDef:
        """
        Modifies the specified VPC attachment.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_transit_gateway_vpc_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_transit_gateway_vpc_attachment)
        """

    def modify_verified_access_endpoint(
        self, **kwargs: Unpack[ModifyVerifiedAccessEndpointRequestTypeDef]
    ) -> ModifyVerifiedAccessEndpointResultTypeDef:
        """
        Modifies the configuration of the specified Amazon Web Services Verified Access
        endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_verified_access_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_endpoint)
        """

    def modify_verified_access_endpoint_policy(
        self, **kwargs: Unpack[ModifyVerifiedAccessEndpointPolicyRequestTypeDef]
    ) -> ModifyVerifiedAccessEndpointPolicyResultTypeDef:
        """
        Modifies the specified Amazon Web Services Verified Access endpoint policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_verified_access_endpoint_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_endpoint_policy)
        """

    def modify_verified_access_group(
        self, **kwargs: Unpack[ModifyVerifiedAccessGroupRequestTypeDef]
    ) -> ModifyVerifiedAccessGroupResultTypeDef:
        """
        Modifies the specified Amazon Web Services Verified Access group configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_verified_access_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_group)
        """

    def modify_verified_access_group_policy(
        self, **kwargs: Unpack[ModifyVerifiedAccessGroupPolicyRequestTypeDef]
    ) -> ModifyVerifiedAccessGroupPolicyResultTypeDef:
        """
        Modifies the specified Amazon Web Services Verified Access group policy.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_verified_access_group_policy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_group_policy)
        """

    def modify_verified_access_instance(
        self, **kwargs: Unpack[ModifyVerifiedAccessInstanceRequestTypeDef]
    ) -> ModifyVerifiedAccessInstanceResultTypeDef:
        """
        Modifies the configuration of the specified Amazon Web Services Verified Access
        instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_verified_access_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_instance)
        """

    def modify_verified_access_instance_logging_configuration(
        self, **kwargs: Unpack[ModifyVerifiedAccessInstanceLoggingConfigurationRequestTypeDef]
    ) -> ModifyVerifiedAccessInstanceLoggingConfigurationResultTypeDef:
        """
        Modifies the logging configuration for the specified Amazon Web Services
        Verified Access instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_verified_access_instance_logging_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_instance_logging_configuration)
        """

    def modify_verified_access_trust_provider(
        self, **kwargs: Unpack[ModifyVerifiedAccessTrustProviderRequestTypeDef]
    ) -> ModifyVerifiedAccessTrustProviderResultTypeDef:
        """
        Modifies the configuration of the specified Amazon Web Services Verified Access
        trust provider.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_verified_access_trust_provider.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_verified_access_trust_provider)
        """

    def modify_volume(
        self, **kwargs: Unpack[ModifyVolumeRequestTypeDef]
    ) -> ModifyVolumeResultTypeDef:
        """
        You can modify several parameters of an existing EBS volume, including volume
        size, volume type, and IOPS capacity.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_volume)
        """

    def modify_volume_attribute(
        self, **kwargs: Unpack[ModifyVolumeAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies a volume attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_volume_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_volume_attribute)
        """

    def modify_vpc_attribute(
        self, **kwargs: Unpack[ModifyVpcAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Modifies the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_attribute)
        """

    def modify_vpc_block_public_access_exclusion(
        self, **kwargs: Unpack[ModifyVpcBlockPublicAccessExclusionRequestTypeDef]
    ) -> ModifyVpcBlockPublicAccessExclusionResultTypeDef:
        """
        Modify VPC Block Public Access (BPA) exclusions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_block_public_access_exclusion.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_block_public_access_exclusion)
        """

    def modify_vpc_block_public_access_options(
        self, **kwargs: Unpack[ModifyVpcBlockPublicAccessOptionsRequestTypeDef]
    ) -> ModifyVpcBlockPublicAccessOptionsResultTypeDef:
        """
        Modify VPC Block Public Access (BPA) options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_block_public_access_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_block_public_access_options)
        """

    def modify_vpc_endpoint(
        self, **kwargs: Unpack[ModifyVpcEndpointRequestTypeDef]
    ) -> ModifyVpcEndpointResultTypeDef:
        """
        Modifies attributes of a specified VPC endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_endpoint.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint)
        """

    def modify_vpc_endpoint_connection_notification(
        self, **kwargs: Unpack[ModifyVpcEndpointConnectionNotificationRequestTypeDef]
    ) -> ModifyVpcEndpointConnectionNotificationResultTypeDef:
        """
        Modifies a connection notification for VPC endpoint or VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_endpoint_connection_notification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint_connection_notification)
        """

    def modify_vpc_endpoint_service_configuration(
        self, **kwargs: Unpack[ModifyVpcEndpointServiceConfigurationRequestTypeDef]
    ) -> ModifyVpcEndpointServiceConfigurationResultTypeDef:
        """
        Modifies the attributes of the specified VPC endpoint service configuration.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_endpoint_service_configuration.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint_service_configuration)
        """

    def modify_vpc_endpoint_service_payer_responsibility(
        self, **kwargs: Unpack[ModifyVpcEndpointServicePayerResponsibilityRequestTypeDef]
    ) -> ModifyVpcEndpointServicePayerResponsibilityResultTypeDef:
        """
        Modifies the payer responsibility for your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_endpoint_service_payer_responsibility.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint_service_payer_responsibility)
        """

    def modify_vpc_endpoint_service_permissions(
        self, **kwargs: Unpack[ModifyVpcEndpointServicePermissionsRequestTypeDef]
    ) -> ModifyVpcEndpointServicePermissionsResultTypeDef:
        """
        Modifies the permissions for your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_endpoint_service_permissions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_endpoint_service_permissions)
        """

    def modify_vpc_peering_connection_options(
        self, **kwargs: Unpack[ModifyVpcPeeringConnectionOptionsRequestTypeDef]
    ) -> ModifyVpcPeeringConnectionOptionsResultTypeDef:
        """
        Modifies the VPC peering connection options on one side of a VPC peering
        connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_peering_connection_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_peering_connection_options)
        """

    def modify_vpc_tenancy(
        self, **kwargs: Unpack[ModifyVpcTenancyRequestTypeDef]
    ) -> ModifyVpcTenancyResultTypeDef:
        """
        Modifies the instance tenancy attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpc_tenancy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpc_tenancy)
        """

    def modify_vpn_connection(
        self, **kwargs: Unpack[ModifyVpnConnectionRequestTypeDef]
    ) -> ModifyVpnConnectionResultTypeDef:
        """
        Modifies the customer gateway or the target gateway of an Amazon Web Services
        Site-to-Site VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpn_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpn_connection)
        """

    def modify_vpn_connection_options(
        self, **kwargs: Unpack[ModifyVpnConnectionOptionsRequestTypeDef]
    ) -> ModifyVpnConnectionOptionsResultTypeDef:
        """
        Modifies the connection options for your Site-to-Site VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpn_connection_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpn_connection_options)
        """

    def modify_vpn_tunnel_certificate(
        self, **kwargs: Unpack[ModifyVpnTunnelCertificateRequestTypeDef]
    ) -> ModifyVpnTunnelCertificateResultTypeDef:
        """
        Modifies the VPN tunnel endpoint certificate.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpn_tunnel_certificate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpn_tunnel_certificate)
        """

    def modify_vpn_tunnel_options(
        self, **kwargs: Unpack[ModifyVpnTunnelOptionsRequestTypeDef]
    ) -> ModifyVpnTunnelOptionsResultTypeDef:
        """
        Modifies the options for a VPN tunnel in an Amazon Web Services Site-to-Site
        VPN connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_vpn_tunnel_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#modify_vpn_tunnel_options)
        """

    def monitor_instances(
        self, **kwargs: Unpack[MonitorInstancesRequestTypeDef]
    ) -> MonitorInstancesResultTypeDef:
        """
        Enables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/monitor_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#monitor_instances)
        """

    def move_address_to_vpc(
        self, **kwargs: Unpack[MoveAddressToVpcRequestTypeDef]
    ) -> MoveAddressToVpcResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/move_address_to_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#move_address_to_vpc)
        """

    def move_byoip_cidr_to_ipam(
        self, **kwargs: Unpack[MoveByoipCidrToIpamRequestTypeDef]
    ) -> MoveByoipCidrToIpamResultTypeDef:
        """
        Move a BYOIPv4 CIDR to IPAM from a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/move_byoip_cidr_to_ipam.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#move_byoip_cidr_to_ipam)
        """

    def move_capacity_reservation_instances(
        self, **kwargs: Unpack[MoveCapacityReservationInstancesRequestTypeDef]
    ) -> MoveCapacityReservationInstancesResultTypeDef:
        """
        Move available capacity from a source Capacity Reservation to a destination
        Capacity Reservation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/move_capacity_reservation_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#move_capacity_reservation_instances)
        """

    def provision_byoip_cidr(
        self, **kwargs: Unpack[ProvisionByoipCidrRequestTypeDef]
    ) -> ProvisionByoipCidrResultTypeDef:
        """
        Provisions an IPv4 or IPv6 address range for use with your Amazon Web Services
        resources through bring your own IP addresses (BYOIP) and creates a
        corresponding address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/provision_byoip_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#provision_byoip_cidr)
        """

    def provision_ipam_byoasn(
        self, **kwargs: Unpack[ProvisionIpamByoasnRequestTypeDef]
    ) -> ProvisionIpamByoasnResultTypeDef:
        """
        Provisions your Autonomous System Number (ASN) for use in your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/provision_ipam_byoasn.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#provision_ipam_byoasn)
        """

    def provision_ipam_pool_cidr(
        self, **kwargs: Unpack[ProvisionIpamPoolCidrRequestTypeDef]
    ) -> ProvisionIpamPoolCidrResultTypeDef:
        """
        Provision a CIDR to an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/provision_ipam_pool_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#provision_ipam_pool_cidr)
        """

    def provision_public_ipv4_pool_cidr(
        self, **kwargs: Unpack[ProvisionPublicIpv4PoolCidrRequestTypeDef]
    ) -> ProvisionPublicIpv4PoolCidrResultTypeDef:
        """
        Provision a CIDR to a public IPv4 pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/provision_public_ipv4_pool_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#provision_public_ipv4_pool_cidr)
        """

    def purchase_capacity_block(
        self, **kwargs: Unpack[PurchaseCapacityBlockRequestTypeDef]
    ) -> PurchaseCapacityBlockResultTypeDef:
        """
        Purchase the Capacity Block for use with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/purchase_capacity_block.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#purchase_capacity_block)
        """

    def purchase_capacity_block_extension(
        self, **kwargs: Unpack[PurchaseCapacityBlockExtensionRequestTypeDef]
    ) -> PurchaseCapacityBlockExtensionResultTypeDef:
        """
        Purchase the Capacity Block extension for use with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/purchase_capacity_block_extension.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#purchase_capacity_block_extension)
        """

    def purchase_host_reservation(
        self, **kwargs: Unpack[PurchaseHostReservationRequestTypeDef]
    ) -> PurchaseHostReservationResultTypeDef:
        """
        Purchase a reservation with configurations that match those of your Dedicated
        Host.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/purchase_host_reservation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#purchase_host_reservation)
        """

    def purchase_reserved_instances_offering(
        self, **kwargs: Unpack[PurchaseReservedInstancesOfferingRequestTypeDef]
    ) -> PurchaseReservedInstancesOfferingResultTypeDef:
        """
        Purchases a Reserved Instance for use with your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/purchase_reserved_instances_offering.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#purchase_reserved_instances_offering)
        """

    def purchase_scheduled_instances(
        self, **kwargs: Unpack[PurchaseScheduledInstancesRequestTypeDef]
    ) -> PurchaseScheduledInstancesResultTypeDef:
        """
        You can no longer purchase Scheduled Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/purchase_scheduled_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#purchase_scheduled_instances)
        """

    def reboot_instances(
        self, **kwargs: Unpack[RebootInstancesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Requests a reboot of the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reboot_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reboot_instances)
        """

    def register_image(
        self, **kwargs: Unpack[RegisterImageRequestTypeDef]
    ) -> RegisterImageResultTypeDef:
        """
        Registers an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/register_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#register_image)
        """

    def register_instance_event_notification_attributes(
        self, **kwargs: Unpack[RegisterInstanceEventNotificationAttributesRequestTypeDef]
    ) -> RegisterInstanceEventNotificationAttributesResultTypeDef:
        """
        Registers a set of tag keys to include in scheduled event notifications for
        your resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/register_instance_event_notification_attributes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#register_instance_event_notification_attributes)
        """

    def register_transit_gateway_multicast_group_members(
        self, **kwargs: Unpack[RegisterTransitGatewayMulticastGroupMembersRequestTypeDef]
    ) -> RegisterTransitGatewayMulticastGroupMembersResultTypeDef:
        """
        Registers members (network interfaces) with the transit gateway multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/register_transit_gateway_multicast_group_members.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#register_transit_gateway_multicast_group_members)
        """

    def register_transit_gateway_multicast_group_sources(
        self, **kwargs: Unpack[RegisterTransitGatewayMulticastGroupSourcesRequestTypeDef]
    ) -> RegisterTransitGatewayMulticastGroupSourcesResultTypeDef:
        """
        Registers sources (network interfaces) with the specified transit gateway
        multicast group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/register_transit_gateway_multicast_group_sources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#register_transit_gateway_multicast_group_sources)
        """

    def reject_capacity_reservation_billing_ownership(
        self, **kwargs: Unpack[RejectCapacityReservationBillingOwnershipRequestTypeDef]
    ) -> RejectCapacityReservationBillingOwnershipResultTypeDef:
        """
        Rejects a request to assign billing of the available capacity of a shared
        Capacity Reservation to your account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reject_capacity_reservation_billing_ownership.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_capacity_reservation_billing_ownership)
        """

    def reject_transit_gateway_multicast_domain_associations(
        self, **kwargs: Unpack[RejectTransitGatewayMulticastDomainAssociationsRequestTypeDef]
    ) -> RejectTransitGatewayMulticastDomainAssociationsResultTypeDef:
        """
        Rejects a request to associate cross-account subnets with a transit gateway
        multicast domain.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reject_transit_gateway_multicast_domain_associations.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_transit_gateway_multicast_domain_associations)
        """

    def reject_transit_gateway_peering_attachment(
        self, **kwargs: Unpack[RejectTransitGatewayPeeringAttachmentRequestTypeDef]
    ) -> RejectTransitGatewayPeeringAttachmentResultTypeDef:
        """
        Rejects a transit gateway peering attachment request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reject_transit_gateway_peering_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_transit_gateway_peering_attachment)
        """

    def reject_transit_gateway_vpc_attachment(
        self, **kwargs: Unpack[RejectTransitGatewayVpcAttachmentRequestTypeDef]
    ) -> RejectTransitGatewayVpcAttachmentResultTypeDef:
        """
        Rejects a request to attach a VPC to a transit gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reject_transit_gateway_vpc_attachment.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_transit_gateway_vpc_attachment)
        """

    def reject_vpc_endpoint_connections(
        self, **kwargs: Unpack[RejectVpcEndpointConnectionsRequestTypeDef]
    ) -> RejectVpcEndpointConnectionsResultTypeDef:
        """
        Rejects VPC endpoint connection requests to your VPC endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reject_vpc_endpoint_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_vpc_endpoint_connections)
        """

    def reject_vpc_peering_connection(
        self, **kwargs: Unpack[RejectVpcPeeringConnectionRequestTypeDef]
    ) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        Rejects a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reject_vpc_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reject_vpc_peering_connection)
        """

    def release_address(
        self, **kwargs: Unpack[ReleaseAddressRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Releases the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/release_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#release_address)
        """

    def release_hosts(
        self, **kwargs: Unpack[ReleaseHostsRequestTypeDef]
    ) -> ReleaseHostsResultTypeDef:
        """
        When you no longer want to use an On-Demand Dedicated Host it can be released.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/release_hosts.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#release_hosts)
        """

    def release_ipam_pool_allocation(
        self, **kwargs: Unpack[ReleaseIpamPoolAllocationRequestTypeDef]
    ) -> ReleaseIpamPoolAllocationResultTypeDef:
        """
        Release an allocation within an IPAM pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/release_ipam_pool_allocation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#release_ipam_pool_allocation)
        """

    def replace_iam_instance_profile_association(
        self, **kwargs: Unpack[ReplaceIamInstanceProfileAssociationRequestTypeDef]
    ) -> ReplaceIamInstanceProfileAssociationResultTypeDef:
        """
        Replaces an IAM instance profile for the specified running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/replace_iam_instance_profile_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_iam_instance_profile_association)
        """

    def replace_image_criteria_in_allowed_images_settings(
        self, **kwargs: Unpack[ReplaceImageCriteriaInAllowedImagesSettingsRequestTypeDef]
    ) -> ReplaceImageCriteriaInAllowedImagesSettingsResultTypeDef:
        """
        Sets or replaces the criteria for Allowed AMIs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/replace_image_criteria_in_allowed_images_settings.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_image_criteria_in_allowed_images_settings)
        """

    def replace_network_acl_association(
        self, **kwargs: Unpack[ReplaceNetworkAclAssociationRequestTypeDef]
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        Changes which network ACL a subnet is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/replace_network_acl_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_network_acl_association)
        """

    def replace_network_acl_entry(
        self, **kwargs: Unpack[ReplaceNetworkAclEntryRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Replaces an entry (rule) in a network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/replace_network_acl_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_network_acl_entry)
        """

    def replace_route(
        self, **kwargs: Unpack[ReplaceRouteRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Replaces an existing route within a route table in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/replace_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_route)
        """

    def replace_route_table_association(
        self, **kwargs: Unpack[ReplaceRouteTableAssociationRequestTypeDef]
    ) -> ReplaceRouteTableAssociationResultTypeDef:
        """
        Changes the route table associated with a given subnet, internet gateway, or
        virtual private gateway in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/replace_route_table_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_route_table_association)
        """

    def replace_transit_gateway_route(
        self, **kwargs: Unpack[ReplaceTransitGatewayRouteRequestTypeDef]
    ) -> ReplaceTransitGatewayRouteResultTypeDef:
        """
        Replaces the specified route in the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/replace_transit_gateway_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_transit_gateway_route)
        """

    def replace_vpn_tunnel(
        self, **kwargs: Unpack[ReplaceVpnTunnelRequestTypeDef]
    ) -> ReplaceVpnTunnelResultTypeDef:
        """
        Trigger replacement of specified VPN tunnel.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/replace_vpn_tunnel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#replace_vpn_tunnel)
        """

    def report_instance_status(
        self, **kwargs: Unpack[ReportInstanceStatusRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Submits feedback about the status of an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/report_instance_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#report_instance_status)
        """

    def request_spot_fleet(
        self, **kwargs: Unpack[RequestSpotFleetRequestTypeDef]
    ) -> RequestSpotFleetResponseTypeDef:
        """
        Creates a Spot Fleet request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/request_spot_fleet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#request_spot_fleet)
        """

    def request_spot_instances(
        self, **kwargs: Unpack[RequestSpotInstancesRequestTypeDef]
    ) -> RequestSpotInstancesResultTypeDef:
        """
        Creates a Spot Instance request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/request_spot_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#request_spot_instances)
        """

    def reset_address_attribute(
        self, **kwargs: Unpack[ResetAddressAttributeRequestTypeDef]
    ) -> ResetAddressAttributeResultTypeDef:
        """
        Resets the attribute of the specified IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reset_address_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_address_attribute)
        """

    def reset_ebs_default_kms_key_id(
        self, **kwargs: Unpack[ResetEbsDefaultKmsKeyIdRequestTypeDef]
    ) -> ResetEbsDefaultKmsKeyIdResultTypeDef:
        """
        Resets the default KMS key for EBS encryption for your account in this Region
        to the Amazon Web Services managed KMS key for EBS.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reset_ebs_default_kms_key_id.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_ebs_default_kms_key_id)
        """

    def reset_fpga_image_attribute(
        self, **kwargs: Unpack[ResetFpgaImageAttributeRequestTypeDef]
    ) -> ResetFpgaImageAttributeResultTypeDef:
        """
        Resets the specified attribute of the specified Amazon FPGA Image (AFI) to its
        default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reset_fpga_image_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_fpga_image_attribute)
        """

    def reset_image_attribute(
        self, **kwargs: Unpack[ResetImageAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resets an attribute of an AMI to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reset_image_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_image_attribute)
        """

    def reset_instance_attribute(
        self, **kwargs: Unpack[ResetInstanceAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reset_instance_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_instance_attribute)
        """

    def reset_network_interface_attribute(
        self, **kwargs: Unpack[ResetNetworkInterfaceAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resets a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reset_network_interface_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_network_interface_attribute)
        """

    def reset_snapshot_attribute(
        self, **kwargs: Unpack[ResetSnapshotAttributeRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Resets permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/reset_snapshot_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#reset_snapshot_attribute)
        """

    def restore_address_to_classic(
        self, **kwargs: Unpack[RestoreAddressToClassicRequestTypeDef]
    ) -> RestoreAddressToClassicResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/restore_address_to_classic.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_address_to_classic)
        """

    def restore_image_from_recycle_bin(
        self, **kwargs: Unpack[RestoreImageFromRecycleBinRequestTypeDef]
    ) -> RestoreImageFromRecycleBinResultTypeDef:
        """
        Restores an AMI from the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/restore_image_from_recycle_bin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_image_from_recycle_bin)
        """

    def restore_managed_prefix_list_version(
        self, **kwargs: Unpack[RestoreManagedPrefixListVersionRequestTypeDef]
    ) -> RestoreManagedPrefixListVersionResultTypeDef:
        """
        Restores the entries from a previous version of a managed prefix list to a new
        version of the prefix list.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/restore_managed_prefix_list_version.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_managed_prefix_list_version)
        """

    def restore_snapshot_from_recycle_bin(
        self, **kwargs: Unpack[RestoreSnapshotFromRecycleBinRequestTypeDef]
    ) -> RestoreSnapshotFromRecycleBinResultTypeDef:
        """
        Restores a snapshot from the Recycle Bin.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/restore_snapshot_from_recycle_bin.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_snapshot_from_recycle_bin)
        """

    def restore_snapshot_tier(
        self, **kwargs: Unpack[RestoreSnapshotTierRequestTypeDef]
    ) -> RestoreSnapshotTierResultTypeDef:
        """
        Restores an archived Amazon EBS snapshot for use temporarily or permanently, or
        modifies the restore period or restore type for a snapshot that was previously
        temporarily restored.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/restore_snapshot_tier.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#restore_snapshot_tier)
        """

    def revoke_client_vpn_ingress(
        self, **kwargs: Unpack[RevokeClientVpnIngressRequestTypeDef]
    ) -> RevokeClientVpnIngressResultTypeDef:
        """
        Removes an ingress authorization rule from a Client VPN endpoint.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/revoke_client_vpn_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#revoke_client_vpn_ingress)
        """

    def revoke_security_group_egress(
        self, **kwargs: Unpack[RevokeSecurityGroupEgressRequestTypeDef]
    ) -> RevokeSecurityGroupEgressResultTypeDef:
        """
        Removes the specified outbound (egress) rules from the specified security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/revoke_security_group_egress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#revoke_security_group_egress)
        """

    def revoke_security_group_ingress(
        self, **kwargs: Unpack[RevokeSecurityGroupIngressRequestTypeDef]
    ) -> RevokeSecurityGroupIngressResultTypeDef:
        """
        Removes the specified inbound (ingress) rules from a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/revoke_security_group_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#revoke_security_group_ingress)
        """

    def run_instances(
        self, **kwargs: Unpack[RunInstancesRequestTypeDef]
    ) -> ReservationResponseTypeDef:
        """
        Launches the specified number of instances using an AMI for which you have
        permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#run_instances)
        """

    def run_scheduled_instances(
        self, **kwargs: Unpack[RunScheduledInstancesRequestTypeDef]
    ) -> RunScheduledInstancesResultTypeDef:
        """
        Launches the specified Scheduled Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/run_scheduled_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#run_scheduled_instances)
        """

    def search_local_gateway_routes(
        self, **kwargs: Unpack[SearchLocalGatewayRoutesRequestTypeDef]
    ) -> SearchLocalGatewayRoutesResultTypeDef:
        """
        Searches for routes in the specified local gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/search_local_gateway_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#search_local_gateway_routes)
        """

    def search_transit_gateway_multicast_groups(
        self, **kwargs: Unpack[SearchTransitGatewayMulticastGroupsRequestTypeDef]
    ) -> SearchTransitGatewayMulticastGroupsResultTypeDef:
        """
        Searches one or more transit gateway multicast groups and returns the group
        membership information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/search_transit_gateway_multicast_groups.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#search_transit_gateway_multicast_groups)
        """

    def search_transit_gateway_routes(
        self, **kwargs: Unpack[SearchTransitGatewayRoutesRequestTypeDef]
    ) -> SearchTransitGatewayRoutesResultTypeDef:
        """
        Searches for routes in the specified transit gateway route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/search_transit_gateway_routes.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#search_transit_gateway_routes)
        """

    def send_diagnostic_interrupt(
        self, **kwargs: Unpack[SendDiagnosticInterruptRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Sends a diagnostic interrupt to the specified Amazon EC2 instance to trigger a
        <i>kernel panic</i> (on Linux instances), or a <i>blue screen</i>/<i>stop
        error</i> (on Windows instances).

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/send_diagnostic_interrupt.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#send_diagnostic_interrupt)
        """

    def start_declarative_policies_report(
        self, **kwargs: Unpack[StartDeclarativePoliciesReportRequestTypeDef]
    ) -> StartDeclarativePoliciesReportResultTypeDef:
        """
        Generates an account status report.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/start_declarative_policies_report.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#start_declarative_policies_report)
        """

    def start_instances(
        self, **kwargs: Unpack[StartInstancesRequestTypeDef]
    ) -> StartInstancesResultTypeDef:
        """
        Starts an Amazon EBS-backed instance that you've previously stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/start_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#start_instances)
        """

    def start_network_insights_access_scope_analysis(
        self, **kwargs: Unpack[StartNetworkInsightsAccessScopeAnalysisRequestTypeDef]
    ) -> StartNetworkInsightsAccessScopeAnalysisResultTypeDef:
        """
        Starts analyzing the specified Network Access Scope.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/start_network_insights_access_scope_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#start_network_insights_access_scope_analysis)
        """

    def start_network_insights_analysis(
        self, **kwargs: Unpack[StartNetworkInsightsAnalysisRequestTypeDef]
    ) -> StartNetworkInsightsAnalysisResultTypeDef:
        """
        Starts analyzing the specified path.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/start_network_insights_analysis.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#start_network_insights_analysis)
        """

    def start_vpc_endpoint_service_private_dns_verification(
        self, **kwargs: Unpack[StartVpcEndpointServicePrivateDnsVerificationRequestTypeDef]
    ) -> StartVpcEndpointServicePrivateDnsVerificationResultTypeDef:
        """
        Initiates the verification process to prove that the service provider owns the
        private DNS name domain for the endpoint service.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/start_vpc_endpoint_service_private_dns_verification.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#start_vpc_endpoint_service_private_dns_verification)
        """

    def stop_instances(
        self, **kwargs: Unpack[StopInstancesRequestTypeDef]
    ) -> StopInstancesResultTypeDef:
        """
        Stops an Amazon EBS-backed instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/stop_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#stop_instances)
        """

    def terminate_client_vpn_connections(
        self, **kwargs: Unpack[TerminateClientVpnConnectionsRequestTypeDef]
    ) -> TerminateClientVpnConnectionsResultTypeDef:
        """
        Terminates active Client VPN endpoint connections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/terminate_client_vpn_connections.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#terminate_client_vpn_connections)
        """

    def terminate_instances(
        self, **kwargs: Unpack[TerminateInstancesRequestTypeDef]
    ) -> TerminateInstancesResultTypeDef:
        """
        Shuts down the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/terminate_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#terminate_instances)
        """

    def unassign_ipv6_addresses(
        self, **kwargs: Unpack[UnassignIpv6AddressesRequestTypeDef]
    ) -> UnassignIpv6AddressesResultTypeDef:
        """
        Unassigns the specified IPv6 addresses or Prefix Delegation prefixes from a
        network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/unassign_ipv6_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unassign_ipv6_addresses)
        """

    def unassign_private_ip_addresses(
        self, **kwargs: Unpack[UnassignPrivateIpAddressesRequestTypeDef]
    ) -> EmptyResponseMetadataTypeDef:
        """
        Unassigns the specified secondary private IP addresses or IPv4 Prefix
        Delegation prefixes from a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/unassign_private_ip_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unassign_private_ip_addresses)
        """

    def unassign_private_nat_gateway_address(
        self, **kwargs: Unpack[UnassignPrivateNatGatewayAddressRequestTypeDef]
    ) -> UnassignPrivateNatGatewayAddressResultTypeDef:
        """
        Unassigns secondary private IPv4 addresses from a private NAT gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/unassign_private_nat_gateway_address.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unassign_private_nat_gateway_address)
        """

    def unlock_snapshot(
        self, **kwargs: Unpack[UnlockSnapshotRequestTypeDef]
    ) -> UnlockSnapshotResultTypeDef:
        """
        Unlocks a snapshot that is locked in governance mode or that is locked in
        compliance mode but still in the cooling-off period.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/unlock_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unlock_snapshot)
        """

    def unmonitor_instances(
        self, **kwargs: Unpack[UnmonitorInstancesRequestTypeDef]
    ) -> UnmonitorInstancesResultTypeDef:
        """
        Disables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/unmonitor_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#unmonitor_instances)
        """

    def update_security_group_rule_descriptions_egress(
        self, **kwargs: Unpack[UpdateSecurityGroupRuleDescriptionsEgressRequestTypeDef]
    ) -> UpdateSecurityGroupRuleDescriptionsEgressResultTypeDef:
        """
        Updates the description of an egress (outbound) security group rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/update_security_group_rule_descriptions_egress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#update_security_group_rule_descriptions_egress)
        """

    def update_security_group_rule_descriptions_ingress(
        self, **kwargs: Unpack[UpdateSecurityGroupRuleDescriptionsIngressRequestTypeDef]
    ) -> UpdateSecurityGroupRuleDescriptionsIngressResultTypeDef:
        """
        Updates the description of an ingress (inbound) security group rule.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/update_security_group_rule_descriptions_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#update_security_group_rule_descriptions_ingress)
        """

    def withdraw_byoip_cidr(
        self, **kwargs: Unpack[WithdrawByoipCidrRequestTypeDef]
    ) -> WithdrawByoipCidrResultTypeDef:
        """
        Stops advertising an address range that is provisioned as an address pool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/withdraw_byoip_cidr.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#withdraw_byoip_cidr)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_address_transfers"]
    ) -> DescribeAddressTransfersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_addresses_attribute"]
    ) -> DescribeAddressesAttributePaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_aws_network_performance_metric_subscriptions"]
    ) -> DescribeAwsNetworkPerformanceMetricSubscriptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_byoip_cidrs"]
    ) -> DescribeByoipCidrsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_capacity_block_extension_history"]
    ) -> DescribeCapacityBlockExtensionHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_capacity_block_extension_offerings"]
    ) -> DescribeCapacityBlockExtensionOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_capacity_block_offerings"]
    ) -> DescribeCapacityBlockOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_capacity_reservation_billing_requests"]
    ) -> DescribeCapacityReservationBillingRequestsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_capacity_reservation_fleets"]
    ) -> DescribeCapacityReservationFleetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_capacity_reservations"]
    ) -> DescribeCapacityReservationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_carrier_gateways"]
    ) -> DescribeCarrierGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_classic_link_instances"]
    ) -> DescribeClassicLinkInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_client_vpn_authorization_rules"]
    ) -> DescribeClientVpnAuthorizationRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_client_vpn_connections"]
    ) -> DescribeClientVpnConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_client_vpn_endpoints"]
    ) -> DescribeClientVpnEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_client_vpn_routes"]
    ) -> DescribeClientVpnRoutesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_client_vpn_target_networks"]
    ) -> DescribeClientVpnTargetNetworksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_coip_pools"]
    ) -> DescribeCoipPoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_dhcp_options"]
    ) -> DescribeDhcpOptionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_egress_only_internet_gateways"]
    ) -> DescribeEgressOnlyInternetGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_export_image_tasks"]
    ) -> DescribeExportImageTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_fast_launch_images"]
    ) -> DescribeFastLaunchImagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_fast_snapshot_restores"]
    ) -> DescribeFastSnapshotRestoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_fleets"]
    ) -> DescribeFleetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_flow_logs"]
    ) -> DescribeFlowLogsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_fpga_images"]
    ) -> DescribeFpgaImagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_host_reservation_offerings"]
    ) -> DescribeHostReservationOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_host_reservations"]
    ) -> DescribeHostReservationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_hosts"]
    ) -> DescribeHostsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_iam_instance_profile_associations"]
    ) -> DescribeIamInstanceProfileAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_images"]
    ) -> DescribeImagesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_import_image_tasks"]
    ) -> DescribeImportImageTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_import_snapshot_tasks"]
    ) -> DescribeImportSnapshotTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_connect_endpoints"]
    ) -> DescribeInstanceConnectEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_credit_specifications"]
    ) -> DescribeInstanceCreditSpecificationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_event_windows"]
    ) -> DescribeInstanceEventWindowsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_image_metadata"]
    ) -> DescribeInstanceImageMetadataPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_status"]
    ) -> DescribeInstanceStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_topology"]
    ) -> DescribeInstanceTopologyPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_type_offerings"]
    ) -> DescribeInstanceTypeOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instance_types"]
    ) -> DescribeInstanceTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_instances"]
    ) -> DescribeInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_internet_gateways"]
    ) -> DescribeInternetGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ipam_pools"]
    ) -> DescribeIpamPoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ipam_resource_discoveries"]
    ) -> DescribeIpamResourceDiscoveriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ipam_resource_discovery_associations"]
    ) -> DescribeIpamResourceDiscoveryAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ipam_scopes"]
    ) -> DescribeIpamScopesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ipams"]
    ) -> DescribeIpamsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_ipv6_pools"]
    ) -> DescribeIpv6PoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_launch_template_versions"]
    ) -> DescribeLaunchTemplateVersionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_launch_templates"]
    ) -> DescribeLaunchTemplatesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self,
        operation_name: Literal[
            "describe_local_gateway_route_table_virtual_interface_group_associations"
        ],
    ) -> DescribeLocalGatewayRouteTableVirtualInterfaceGroupAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_local_gateway_route_table_vpc_associations"]
    ) -> DescribeLocalGatewayRouteTableVpcAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_local_gateway_route_tables"]
    ) -> DescribeLocalGatewayRouteTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_local_gateway_virtual_interface_groups"]
    ) -> DescribeLocalGatewayVirtualInterfaceGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_local_gateway_virtual_interfaces"]
    ) -> DescribeLocalGatewayVirtualInterfacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_local_gateways"]
    ) -> DescribeLocalGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_mac_hosts"]
    ) -> DescribeMacHostsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_managed_prefix_lists"]
    ) -> DescribeManagedPrefixListsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_moving_addresses"]
    ) -> DescribeMovingAddressesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_nat_gateways"]
    ) -> DescribeNatGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_network_acls"]
    ) -> DescribeNetworkAclsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_network_insights_access_scope_analyses"]
    ) -> DescribeNetworkInsightsAccessScopeAnalysesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_network_insights_access_scopes"]
    ) -> DescribeNetworkInsightsAccessScopesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_network_insights_analyses"]
    ) -> DescribeNetworkInsightsAnalysesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_network_insights_paths"]
    ) -> DescribeNetworkInsightsPathsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_network_interface_permissions"]
    ) -> DescribeNetworkInterfacePermissionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_network_interfaces"]
    ) -> DescribeNetworkInterfacesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_prefix_lists"]
    ) -> DescribePrefixListsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_principal_id_format"]
    ) -> DescribePrincipalIdFormatPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_public_ipv4_pools"]
    ) -> DescribePublicIpv4PoolsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_replace_root_volume_tasks"]
    ) -> DescribeReplaceRootVolumeTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_instances_modifications"]
    ) -> DescribeReservedInstancesModificationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_reserved_instances_offerings"]
    ) -> DescribeReservedInstancesOfferingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_route_server_endpoints"]
    ) -> DescribeRouteServerEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_route_server_peers"]
    ) -> DescribeRouteServerPeersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_route_servers"]
    ) -> DescribeRouteServersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_route_tables"]
    ) -> DescribeRouteTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_scheduled_instance_availability"]
    ) -> DescribeScheduledInstanceAvailabilityPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_scheduled_instances"]
    ) -> DescribeScheduledInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_security_group_rules"]
    ) -> DescribeSecurityGroupRulesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_security_group_vpc_associations"]
    ) -> DescribeSecurityGroupVpcAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_security_groups"]
    ) -> DescribeSecurityGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_snapshot_tier_status"]
    ) -> DescribeSnapshotTierStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_snapshots"]
    ) -> DescribeSnapshotsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_spot_fleet_instances"]
    ) -> DescribeSpotFleetInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_spot_fleet_requests"]
    ) -> DescribeSpotFleetRequestsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_spot_instance_requests"]
    ) -> DescribeSpotInstanceRequestsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_spot_price_history"]
    ) -> DescribeSpotPriceHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_stale_security_groups"]
    ) -> DescribeStaleSecurityGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_store_image_tasks"]
    ) -> DescribeStoreImageTasksPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_subnets"]
    ) -> DescribeSubnetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_tags"]
    ) -> DescribeTagsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_traffic_mirror_filters"]
    ) -> DescribeTrafficMirrorFiltersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_traffic_mirror_sessions"]
    ) -> DescribeTrafficMirrorSessionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_traffic_mirror_targets"]
    ) -> DescribeTrafficMirrorTargetsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateway_attachments"]
    ) -> DescribeTransitGatewayAttachmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateway_connect_peers"]
    ) -> DescribeTransitGatewayConnectPeersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateway_connects"]
    ) -> DescribeTransitGatewayConnectsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateway_multicast_domains"]
    ) -> DescribeTransitGatewayMulticastDomainsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateway_peering_attachments"]
    ) -> DescribeTransitGatewayPeeringAttachmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateway_policy_tables"]
    ) -> DescribeTransitGatewayPolicyTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateway_route_table_announcements"]
    ) -> DescribeTransitGatewayRouteTableAnnouncementsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateway_route_tables"]
    ) -> DescribeTransitGatewayRouteTablesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateway_vpc_attachments"]
    ) -> DescribeTransitGatewayVpcAttachmentsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_transit_gateways"]
    ) -> DescribeTransitGatewaysPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_trunk_interface_associations"]
    ) -> DescribeTrunkInterfaceAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_verified_access_endpoints"]
    ) -> DescribeVerifiedAccessEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_verified_access_groups"]
    ) -> DescribeVerifiedAccessGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_verified_access_instance_logging_configurations"]
    ) -> DescribeVerifiedAccessInstanceLoggingConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_verified_access_instances"]
    ) -> DescribeVerifiedAccessInstancesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_verified_access_trust_providers"]
    ) -> DescribeVerifiedAccessTrustProvidersPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_volume_status"]
    ) -> DescribeVolumeStatusPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_volumes_modifications"]
    ) -> DescribeVolumesModificationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_volumes"]
    ) -> DescribeVolumesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vpc_classic_link_dns_support"]
    ) -> DescribeVpcClassicLinkDnsSupportPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vpc_endpoint_connection_notifications"]
    ) -> DescribeVpcEndpointConnectionNotificationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vpc_endpoint_connections"]
    ) -> DescribeVpcEndpointConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vpc_endpoint_service_configurations"]
    ) -> DescribeVpcEndpointServiceConfigurationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vpc_endpoint_service_permissions"]
    ) -> DescribeVpcEndpointServicePermissionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vpc_endpoint_services"]
    ) -> DescribeVpcEndpointServicesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vpc_endpoints"]
    ) -> DescribeVpcEndpointsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vpc_peering_connections"]
    ) -> DescribeVpcPeeringConnectionsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["describe_vpcs"]
    ) -> DescribeVpcsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_associated_ipv6_pool_cidrs"]
    ) -> GetAssociatedIpv6PoolCidrsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_aws_network_performance_data"]
    ) -> GetAwsNetworkPerformanceDataPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_groups_for_capacity_reservation"]
    ) -> GetGroupsForCapacityReservationPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_instance_types_from_instance_requirements"]
    ) -> GetInstanceTypesFromInstanceRequirementsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_ipam_address_history"]
    ) -> GetIpamAddressHistoryPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_ipam_discovered_accounts"]
    ) -> GetIpamDiscoveredAccountsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_ipam_discovered_resource_cidrs"]
    ) -> GetIpamDiscoveredResourceCidrsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_ipam_pool_allocations"]
    ) -> GetIpamPoolAllocationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_ipam_pool_cidrs"]
    ) -> GetIpamPoolCidrsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_ipam_resource_cidrs"]
    ) -> GetIpamResourceCidrsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_managed_prefix_list_associations"]
    ) -> GetManagedPrefixListAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_managed_prefix_list_entries"]
    ) -> GetManagedPrefixListEntriesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_network_insights_access_scope_analysis_findings"]
    ) -> GetNetworkInsightsAccessScopeAnalysisFindingsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_security_groups_for_vpc"]
    ) -> GetSecurityGroupsForVpcPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_spot_placement_scores"]
    ) -> GetSpotPlacementScoresPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_transit_gateway_attachment_propagations"]
    ) -> GetTransitGatewayAttachmentPropagationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_transit_gateway_multicast_domain_associations"]
    ) -> GetTransitGatewayMulticastDomainAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_transit_gateway_policy_table_associations"]
    ) -> GetTransitGatewayPolicyTableAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_transit_gateway_prefix_list_references"]
    ) -> GetTransitGatewayPrefixListReferencesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_transit_gateway_route_table_associations"]
    ) -> GetTransitGatewayRouteTableAssociationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_transit_gateway_route_table_propagations"]
    ) -> GetTransitGatewayRouteTablePropagationsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["get_vpn_connection_device_types"]
    ) -> GetVpnConnectionDeviceTypesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_images_in_recycle_bin"]
    ) -> ListImagesInRecycleBinPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["list_snapshots_in_recycle_bin"]
    ) -> ListSnapshotsInRecycleBinPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_local_gateway_routes"]
    ) -> SearchLocalGatewayRoutesPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_paginator(  # type: ignore[override]
        self, operation_name: Literal["search_transit_gateway_multicast_groups"]
    ) -> SearchTransitGatewayMulticastGroupsPaginator:
        """
        Create a paginator for an operation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_paginator.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_paginator)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["bundle_task_complete"]
    ) -> BundleTaskCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["conversion_task_cancelled"]
    ) -> ConversionTaskCancelledWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["conversion_task_completed"]
    ) -> ConversionTaskCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["conversion_task_deleted"]
    ) -> ConversionTaskDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["customer_gateway_available"]
    ) -> CustomerGatewayAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["export_task_cancelled"]
    ) -> ExportTaskCancelledWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["export_task_completed"]
    ) -> ExportTaskCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["image_available"]
    ) -> ImageAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["image_exists"]
    ) -> ImageExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["instance_exists"]
    ) -> InstanceExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["instance_running"]
    ) -> InstanceRunningWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["instance_status_ok"]
    ) -> InstanceStatusOkWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["instance_stopped"]
    ) -> InstanceStoppedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["instance_terminated"]
    ) -> InstanceTerminatedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["internet_gateway_exists"]
    ) -> InternetGatewayExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["key_pair_exists"]
    ) -> KeyPairExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["nat_gateway_available"]
    ) -> NatGatewayAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["nat_gateway_deleted"]
    ) -> NatGatewayDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["network_interface_available"]
    ) -> NetworkInterfaceAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["password_data_available"]
    ) -> PasswordDataAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["security_group_exists"]
    ) -> SecurityGroupExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["snapshot_completed"]
    ) -> SnapshotCompletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["snapshot_imported"]
    ) -> SnapshotImportedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["spot_instance_request_fulfilled"]
    ) -> SpotInstanceRequestFulfilledWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["store_image_task_complete"]
    ) -> StoreImageTaskCompleteWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["subnet_available"]
    ) -> SubnetAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["system_status_ok"]
    ) -> SystemStatusOkWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["volume_available"]
    ) -> VolumeAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["volume_deleted"]
    ) -> VolumeDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["volume_in_use"]
    ) -> VolumeInUseWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["vpc_available"]
    ) -> VpcAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["vpc_exists"]
    ) -> VpcExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["vpc_peering_connection_deleted"]
    ) -> VpcPeeringConnectionDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["vpc_peering_connection_exists"]
    ) -> VpcPeeringConnectionExistsWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["vpn_connection_available"]
    ) -> VpnConnectionAvailableWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """

    @overload  # type: ignore[override]
    def get_waiter(  # type: ignore[override]
        self, waiter_name: Literal["vpn_connection_deleted"]
    ) -> VpnConnectionDeletedWaiter:
        """
        Returns an object that can wait for some condition.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/get_waiter.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/client/#get_waiter)
        """
