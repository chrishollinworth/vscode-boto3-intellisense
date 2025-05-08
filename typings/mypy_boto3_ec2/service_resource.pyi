"""
Type annotations for ec2 service ServiceResource.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from boto3.session import Session

    from mypy_boto3_ec2.service_resource import EC2ServiceResource
    import mypy_boto3_ec2.service_resource as ec2_resources

    session = Session()
    resource: EC2ServiceResource = session.resource("ec2")

    my_classic_address: ec2_resources.ClassicAddress = resource.ClassicAddress(...)
    my_dhcp_options: ec2_resources.DhcpOptions = resource.DhcpOptions(...)
    my_image: ec2_resources.Image = resource.Image(...)
    my_instance: ec2_resources.Instance = resource.Instance(...)
    my_internet_gateway: ec2_resources.InternetGateway = resource.InternetGateway(...)
    my_key_pair: ec2_resources.KeyPair = resource.KeyPair(...)
    my_key_pair_info: ec2_resources.KeyPairInfo = resource.KeyPairInfo(...)
    my_network_acl: ec2_resources.NetworkAcl = resource.NetworkAcl(...)
    my_network_interface: ec2_resources.NetworkInterface = resource.NetworkInterface(...)
    my_network_interface_association: ec2_resources.NetworkInterfaceAssociation = resource.NetworkInterfaceAssociation(...)
    my_placement_group: ec2_resources.PlacementGroup = resource.PlacementGroup(...)
    my_route: ec2_resources.Route = resource.Route(...)
    my_route_table: ec2_resources.RouteTable = resource.RouteTable(...)
    my_route_table_association: ec2_resources.RouteTableAssociation = resource.RouteTableAssociation(...)
    my_security_group: ec2_resources.SecurityGroup = resource.SecurityGroup(...)
    my_snapshot: ec2_resources.Snapshot = resource.Snapshot(...)
    my_subnet: ec2_resources.Subnet = resource.Subnet(...)
    my_tag: ec2_resources.Tag = resource.Tag(...)
    my_volume: ec2_resources.Volume = resource.Volume(...)
    my_vpc: ec2_resources.Vpc = resource.Vpc(...)
    my_vpc_peering_connection: ec2_resources.VpcPeeringConnection = resource.VpcPeeringConnection(...)
    my_vpc_address: ec2_resources.VpcAddress = resource.VpcAddress(...)
```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Any

from boto3.resources.base import ResourceMeta, ServiceResource
from boto3.resources.collection import ResourceCollection

from .client import EC2Client
from .literals import (
    ArchitectureValuesType,
    BootModeValuesType,
    DeviceTypeType,
    DomainTypeType,
    HypervisorTypeType,
    ImageStateType,
    ImageTypeValuesType,
    InstanceBootModeValuesType,
    InstanceLifecycleTypeType,
    InstanceTypeType,
    KeyTypeType,
    NetworkInterfaceStatusType,
    NetworkInterfaceTypeType,
    PlacementGroupStateType,
    PlacementStrategyType,
    ResourceTypeType,
    RouteOriginType,
    RouteStateType,
    ServiceManagedType,
    SnapshotStateType,
    SpreadLevelType,
    SSETypeType,
    StorageTierType,
    SubnetStateType,
    TenancyType,
    TransferTypeType,
    VirtualizationTypeType,
    VolumeStateType,
    VolumeTypeType,
    VpcStateType,
)
from .type_defs import (
    AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef,
    AcceptVpcPeeringConnectionResultTypeDef,
    AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef,
    AssignPrivateIpAddressesResultTypeDef,
    AssociateAddressRequestClassicAddressAssociateTypeDef,
    AssociateAddressRequestVpcAddressAssociateTypeDef,
    AssociateAddressResultTypeDef,
    AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef,
    AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef,
    AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef,
    AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef,
    AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef,
    AttachClassicLinkVpcResultTypeDef,
    AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef,
    AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef,
    AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef,
    AttachNetworkInterfaceResultTypeDef,
    AttachVolumeRequestInstanceAttachVolumeTypeDef,
    AttachVolumeRequestVolumeAttachToInstanceTypeDef,
    AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef,
    AuthorizeSecurityGroupEgressResultTypeDef,
    AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef,
    AuthorizeSecurityGroupIngressResultTypeDef,
    BlockDeviceMappingTypeDef,
    BlockPublicAccessStatesTypeDef,
    CapacityReservationSpecificationResponseTypeDef,
    ConnectionTrackingConfigurationTypeDef,
    CopySnapshotRequestSnapshotCopyTypeDef,
    CopySnapshotResultTypeDef,
    CpuOptionsTypeDef,
    CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef,
    CreateImageRequestInstanceCreateImageTypeDef,
    CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef,
    CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef,
    CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef,
    CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef,
    CreateNetworkAclRequestVpcCreateNetworkAclTypeDef,
    CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef,
    CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef,
    CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef,
    CreateRouteRequestRouteTableCreateRouteTypeDef,
    CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef,
    CreateRouteTableRequestVpcCreateRouteTableTypeDef,
    CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef,
    CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef,
    CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef,
    CreateSnapshotRequestVolumeCreateSnapshotTypeDef,
    CreateSubnetRequestServiceResourceCreateSubnetTypeDef,
    CreateSubnetRequestVpcCreateSubnetTypeDef,
    CreateTagsRequestServiceResourceCreateTagsTypeDef,
    CreateVolumeRequestServiceResourceCreateVolumeTypeDef,
    CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef,
    CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef,
    CreateVpcRequestServiceResourceCreateVpcTypeDef,
    DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef,
    DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef,
    DeleteKeyPairRequestKeyPairDeleteTypeDef,
    DeleteKeyPairRequestKeyPairInfoDeleteTypeDef,
    DeleteKeyPairResultTypeDef,
    DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef,
    DeleteNetworkAclRequestNetworkAclDeleteTypeDef,
    DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef,
    DeletePlacementGroupRequestPlacementGroupDeleteTypeDef,
    DeleteRouteRequestRouteDeleteTypeDef,
    DeleteRouteTableRequestRouteTableDeleteTypeDef,
    DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef,
    DeleteSecurityGroupResultTypeDef,
    DeleteSnapshotRequestSnapshotDeleteTypeDef,
    DeleteSubnetRequestSubnetDeleteTypeDef,
    DeleteTagsRequestTagDeleteTypeDef,
    DeleteVolumeRequestVolumeDeleteTypeDef,
    DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef,
    DeleteVpcPeeringConnectionResultTypeDef,
    DeleteVpcRequestVpcDeleteTypeDef,
    DeregisterImageRequestImageDeregisterTypeDef,
    DescribeImageAttributeRequestImageDescribeAttributeTypeDef,
    DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef,
    DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef,
    DescribeNetworkInterfaceAttributeResultTypeDef,
    DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef,
    DescribeSnapshotAttributeResultTypeDef,
    DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef,
    DescribeVolumeAttributeResultTypeDef,
    DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef,
    DescribeVolumeStatusResultTypeDef,
    DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef,
    DescribeVpcAttributeResultTypeDef,
    DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef,
    DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef,
    DetachClassicLinkVpcResultTypeDef,
    DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef,
    DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef,
    DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef,
    DetachVolumeRequestInstanceDetachVolumeTypeDef,
    DetachVolumeRequestVolumeDetachFromInstanceTypeDef,
    DhcpConfigurationTypeDef,
    DhcpOptionsCreateTagsRequestTypeDef,
    DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef,
    DisableVpcClassicLinkResultTypeDef,
    DisassociateAddressRequestClassicAddressDisassociateTypeDef,
    DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef,
    DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef,
    DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef,
    ElasticGpuAssociationTypeDef,
    ElasticInferenceAcceleratorAssociationTypeDef,
    EnableVolumeIORequestVolumeEnableIoTypeDef,
    EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef,
    EnableVpcClassicLinkResultTypeDef,
    EnclaveOptionsTypeDef,
    FilterTypeDef,
    GetConsoleOutputRequestInstanceConsoleOutputTypeDef,
    GetConsoleOutputResultTypeDef,
    GetPasswordDataRequestInstancePasswordDataTypeDef,
    GetPasswordDataResultTypeDef,
    GroupIdentifierTypeDef,
    HibernationOptionsTypeDef,
    IamInstanceProfileTypeDef,
    ImageAttributeTypeDef,
    ImageCreateTagsRequestTypeDef,
    ImportKeyPairRequestServiceResourceImportKeyPairTypeDef,
    InstanceAttributeTypeDef,
    InstanceBlockDeviceMappingTypeDef,
    InstanceCreateTagsRequestTypeDef,
    InstanceDeleteTagsRequestTypeDef,
    InstanceMaintenanceOptionsTypeDef,
    InstanceMetadataOptionsResponseTypeDef,
    InstanceNetworkInterfaceTypeDef,
    InstanceNetworkPerformanceOptionsTypeDef,
    InstanceStateTypeDef,
    InternetGatewayAttachmentTypeDef,
    InternetGatewayCreateTagsRequestTypeDef,
    IpPermissionOutputTypeDef,
    Ipv4PrefixSpecificationTypeDef,
    Ipv6PrefixSpecificationTypeDef,
    LicenseConfigurationTypeDef,
    ModifyImageAttributeRequestImageModifyAttributeTypeDef,
    ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef,
    ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef,
    ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef,
    ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef,
    ModifyVpcAttributeRequestVpcModifyAttributeTypeDef,
    MonitoringTypeDef,
    MonitorInstancesRequestInstanceMonitorTypeDef,
    MonitorInstancesResultTypeDef,
    NetworkAclAssociationTypeDef,
    NetworkAclCreateTagsRequestTypeDef,
    NetworkAclEntryTypeDef,
    NetworkInterfaceAssociationTypeDef,
    NetworkInterfaceAttachmentTypeDef,
    NetworkInterfaceCreateTagsRequestTypeDef,
    NetworkInterfaceIpv6AddressTypeDef,
    NetworkInterfacePrivateIpAddressTypeDef,
    OperatorResponseTypeDef,
    PlacementTypeDef,
    PrivateDnsNameOptionsOnLaunchTypeDef,
    PrivateDnsNameOptionsResponseTypeDef,
    ProductCodeTypeDef,
    PropagatingVgwTypeDef,
    RebootInstancesRequestInstanceRebootTypeDef,
    RegisterImageRequestServiceResourceRegisterImageTypeDef,
    RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef,
    RejectVpcPeeringConnectionResultTypeDef,
    ReleaseAddressRequestClassicAddressReleaseTypeDef,
    ReleaseAddressRequestVpcAddressReleaseTypeDef,
    ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef,
    ReplaceNetworkAclAssociationResultTypeDef,
    ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef,
    ReplaceRouteRequestRouteReplaceTypeDef,
    ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef,
    ReportInstanceStatusRequestInstanceReportStatusTypeDef,
    ResetImageAttributeRequestImageResetAttributeTypeDef,
    ResetInstanceAttributeRequestInstanceResetAttributeTypeDef,
    ResetInstanceAttributeRequestInstanceResetKernelTypeDef,
    ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef,
    ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef,
    ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef,
    ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef,
    RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef,
    RevokeSecurityGroupEgressResultTypeDef,
    RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef,
    RevokeSecurityGroupIngressResultTypeDef,
    RouteTableAssociationStateTypeDef,
    RouteTableAssociationTypeDef,
    RouteTableCreateTagsRequestTypeDef,
    RouteTypeDef,
    RunInstancesRequestServiceResourceCreateInstancesTypeDef,
    RunInstancesRequestSubnetCreateInstancesTypeDef,
    SecurityGroupCreateTagsRequestTypeDef,
    SnapshotCreateTagsRequestTypeDef,
    StartInstancesRequestInstanceStartTypeDef,
    StartInstancesResultTypeDef,
    StateReasonTypeDef,
    StopInstancesRequestInstanceStopTypeDef,
    StopInstancesResultTypeDef,
    SubnetCreateTagsRequestTypeDef,
    SubnetIpv6CidrBlockAssociationTypeDef,
    TagTypeDef,
    TerminateInstancesRequestInstanceTerminateTypeDef,
    TerminateInstancesResultTypeDef,
    UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef,
    UnmonitorInstancesRequestInstanceUnmonitorTypeDef,
    UnmonitorInstancesResultTypeDef,
    VolumeAttachmentResponseTypeDef,
    VolumeAttachmentTypeDef,
    VolumeCreateTagsRequestTypeDef,
    VpcCidrBlockAssociationTypeDef,
    VpcCreateTagsRequestTypeDef,
    VpcEncryptionControlTypeDef,
    VpcIpv6CidrBlockAssociationTypeDef,
    VpcPeeringConnectionStateReasonTypeDef,
    VpcPeeringConnectionVpcInfoTypeDef,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Iterator, Sequence
else:
    from typing import Dict, Iterator, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, Unpack
else:
    from typing_extensions import Literal, Unpack

__all__ = (
    "ClassicAddress",
    "DhcpOptions",
    "EC2ServiceResource",
    "Image",
    "Instance",
    "InstanceVolumesCollection",
    "InstanceVpcAddressesCollection",
    "InternetGateway",
    "KeyPair",
    "KeyPairInfo",
    "NetworkAcl",
    "NetworkInterface",
    "NetworkInterfaceAssociation",
    "PlacementGroup",
    "PlacementGroupInstancesCollection",
    "Route",
    "RouteTable",
    "RouteTableAssociation",
    "SecurityGroup",
    "ServiceResourceClassicAddressesCollection",
    "ServiceResourceDhcpOptionsSetsCollection",
    "ServiceResourceImagesCollection",
    "ServiceResourceInstancesCollection",
    "ServiceResourceInternetGatewaysCollection",
    "ServiceResourceKeyPairsCollection",
    "ServiceResourceNetworkAclsCollection",
    "ServiceResourceNetworkInterfacesCollection",
    "ServiceResourcePlacementGroupsCollection",
    "ServiceResourceRouteTablesCollection",
    "ServiceResourceSecurityGroupsCollection",
    "ServiceResourceSnapshotsCollection",
    "ServiceResourceSubnetsCollection",
    "ServiceResourceVolumesCollection",
    "ServiceResourceVpcAddressesCollection",
    "ServiceResourceVpcPeeringConnectionsCollection",
    "ServiceResourceVpcsCollection",
    "Snapshot",
    "Subnet",
    "SubnetInstancesCollection",
    "SubnetNetworkInterfacesCollection",
    "Tag",
    "Volume",
    "VolumeSnapshotsCollection",
    "Vpc",
    "VpcAcceptedVpcPeeringConnectionsCollection",
    "VpcAddress",
    "VpcInstancesCollection",
    "VpcInternetGatewaysCollection",
    "VpcNetworkAclsCollection",
    "VpcNetworkInterfacesCollection",
    "VpcPeeringConnection",
    "VpcRequestedVpcPeeringConnectionsCollection",
    "VpcRouteTablesCollection",
    "VpcSecurityGroupsCollection",
    "VpcSubnetsCollection",
)

class ServiceResourceClassicAddressesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/classic_addresses.html#EC2.ServiceResource.classic_addresses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceclassicaddressescollection)
    """
    def all(self) -> ServiceResourceClassicAddressesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/classic_addresses.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        PublicIps: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        AllocationIds: Sequence[str] = ...,
    ) -> ServiceResourceClassicAddressesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/classic_addresses.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def limit(self, count: int) -> ServiceResourceClassicAddressesCollection:
        """
        Return at most this many ClassicAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/classic_addresses.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def page_size(self, count: int) -> ServiceResourceClassicAddressesCollection:
        """
        Fetch at most this many ClassicAddresss per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/classic_addresses.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def pages(self) -> Iterator[List[ClassicAddress]]:
        """
        A generator which yields pages of ClassicAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/classic_addresses.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

    def __iter__(self) -> Iterator[ClassicAddress]:
        """
        A generator which yields ClassicAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/classic_addresses.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceclassicaddressescollection)
        """

class ServiceResourceDhcpOptionsSetsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/dhcp_options_sets.html#EC2.ServiceResource.dhcp_options_sets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
    """
    def all(self) -> ServiceResourceDhcpOptionsSetsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/dhcp_options_sets.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        DhcpOptionsIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceDhcpOptionsSetsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/dhcp_options_sets.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def limit(self, count: int) -> ServiceResourceDhcpOptionsSetsCollection:
        """
        Return at most this many DhcpOptionss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/dhcp_options_sets.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def page_size(self, count: int) -> ServiceResourceDhcpOptionsSetsCollection:
        """
        Fetch at most this many DhcpOptionss per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/dhcp_options_sets.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def pages(self) -> Iterator[List[DhcpOptions]]:
        """
        A generator which yields pages of DhcpOptionss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/dhcp_options_sets.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

    def __iter__(self) -> Iterator[DhcpOptions]:
        """
        A generator which yields DhcpOptionss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/dhcp_options_sets.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcedhcpoptionssetscollection)
        """

class ServiceResourceImagesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/images.html#EC2.ServiceResource.images)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceimagescollection)
    """
    def all(self) -> ServiceResourceImagesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/images.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceimagescollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        ExecutableUsers: Sequence[str] = ...,
        ImageIds: Sequence[str] = ...,
        Owners: Sequence[str] = ...,
        IncludeDeprecated: bool = ...,
        IncludeDisabled: bool = ...,
        MaxResults: int = ...,
        NextToken: str = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceImagesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/images.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceimagescollection)
        """

    def limit(self, count: int) -> ServiceResourceImagesCollection:
        """
        Return at most this many Images.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/images.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceimagescollection)
        """

    def page_size(self, count: int) -> ServiceResourceImagesCollection:
        """
        Fetch at most this many Images per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/images.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceimagescollection)
        """

    def pages(self) -> Iterator[List[Image]]:
        """
        A generator which yields pages of Images.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/images.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceimagescollection)
        """

    def __iter__(self) -> Iterator[Image]:
        """
        A generator which yields Images.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/images.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceimagescollection)
        """

class ServiceResourceInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#EC2.ServiceResource.instances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
    """
    def all(self) -> ServiceResourceInstancesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        InstanceIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ServiceResourceInstancesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def create_tags(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#create_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def monitor(self, *, DryRun: bool = ...) -> List[MonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#monitor)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def reboot(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#reboot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def start(
        self, *, AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> List[StartInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#start)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def stop(
        self, *, Hibernate: bool = ..., DryRun: bool = ..., Force: bool = ...
    ) -> List[StopInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#stop)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def terminate(self, *, DryRun: bool = ...) -> List[TerminateInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#terminate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def unmonitor(self, *, DryRun: bool = ...) -> List[UnmonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#unmonitor)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def limit(self, count: int) -> ServiceResourceInstancesCollection:
        """
        Return at most this many Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def page_size(self, count: int) -> ServiceResourceInstancesCollection:
        """
        Fetch at most this many Instances per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def pages(self) -> Iterator[List[Instance]]:
        """
        A generator which yields pages of Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

    def __iter__(self) -> Iterator[Instance]:
        """
        A generator which yields Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/instances.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinstancescollection)
        """

class ServiceResourceInternetGatewaysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/internet_gateways.html#EC2.ServiceResource.internet_gateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinternetgatewayscollection)
    """
    def all(self) -> ServiceResourceInternetGatewaysCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/internet_gateways.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        InternetGatewayIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceInternetGatewaysCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/internet_gateways.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def limit(self, count: int) -> ServiceResourceInternetGatewaysCollection:
        """
        Return at most this many InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/internet_gateways.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def page_size(self, count: int) -> ServiceResourceInternetGatewaysCollection:
        """
        Fetch at most this many InternetGateways per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/internet_gateways.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def pages(self) -> Iterator[List[InternetGateway]]:
        """
        A generator which yields pages of InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/internet_gateways.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

    def __iter__(self) -> Iterator[InternetGateway]:
        """
        A generator which yields InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/internet_gateways.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceinternetgatewayscollection)
        """

class ServiceResourceKeyPairsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/key_pairs.html#EC2.ServiceResource.key_pairs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcekeypairscollection)
    """
    def all(self) -> ServiceResourceKeyPairsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/key_pairs.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        KeyNames: Sequence[str] = ...,
        KeyPairIds: Sequence[str] = ...,
        IncludePublicKey: bool = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceKeyPairsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/key_pairs.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def limit(self, count: int) -> ServiceResourceKeyPairsCollection:
        """
        Return at most this many KeyPairInfos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/key_pairs.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def page_size(self, count: int) -> ServiceResourceKeyPairsCollection:
        """
        Fetch at most this many KeyPairInfos per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/key_pairs.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def pages(self) -> Iterator[List[KeyPairInfo]]:
        """
        A generator which yields pages of KeyPairInfos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/key_pairs.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcekeypairscollection)
        """

    def __iter__(self) -> Iterator[KeyPairInfo]:
        """
        A generator which yields KeyPairInfos.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/key_pairs.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcekeypairscollection)
        """

class ServiceResourceNetworkAclsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_acls.html#EC2.ServiceResource.network_acls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkaclscollection)
    """
    def all(self) -> ServiceResourceNetworkAclsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_acls.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        NetworkAclIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceNetworkAclsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_acls.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def limit(self, count: int) -> ServiceResourceNetworkAclsCollection:
        """
        Return at most this many NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_acls.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def page_size(self, count: int) -> ServiceResourceNetworkAclsCollection:
        """
        Fetch at most this many NetworkAcls per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_acls.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def pages(self) -> Iterator[List[NetworkAcl]]:
        """
        A generator which yields pages of NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_acls.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

    def __iter__(self) -> Iterator[NetworkAcl]:
        """
        A generator which yields NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_acls.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkaclscollection)
        """

class ServiceResourceNetworkInterfacesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_interfaces.html#EC2.ServiceResource.network_interfaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
    """
    def all(self) -> ServiceResourceNetworkInterfacesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_interfaces.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        NetworkInterfaceIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceNetworkInterfacesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_interfaces.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def limit(self, count: int) -> ServiceResourceNetworkInterfacesCollection:
        """
        Return at most this many NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_interfaces.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def page_size(self, count: int) -> ServiceResourceNetworkInterfacesCollection:
        """
        Fetch at most this many NetworkInterfaces per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_interfaces.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def pages(self) -> Iterator[List[NetworkInterface]]:
        """
        A generator which yields pages of NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_interfaces.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

    def __iter__(self) -> Iterator[NetworkInterface]:
        """
        A generator which yields NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/network_interfaces.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcenetworkinterfacescollection)
        """

class ServiceResourcePlacementGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/placement_groups.html#EC2.ServiceResource.placement_groups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceplacementgroupscollection)
    """
    def all(self) -> ServiceResourcePlacementGroupsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/placement_groups.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        GroupIds: Sequence[str] = ...,
        DryRun: bool = ...,
        GroupNames: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourcePlacementGroupsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/placement_groups.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def limit(self, count: int) -> ServiceResourcePlacementGroupsCollection:
        """
        Return at most this many PlacementGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/placement_groups.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def page_size(self, count: int) -> ServiceResourcePlacementGroupsCollection:
        """
        Fetch at most this many PlacementGroups per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/placement_groups.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def pages(self) -> Iterator[List[PlacementGroup]]:
        """
        A generator which yields pages of PlacementGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/placement_groups.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

    def __iter__(self) -> Iterator[PlacementGroup]:
        """
        A generator which yields PlacementGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/placement_groups.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceplacementgroupscollection)
        """

class ServiceResourceRouteTablesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/route_tables.html#EC2.ServiceResource.route_tables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceroutetablescollection)
    """
    def all(self) -> ServiceResourceRouteTablesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/route_tables.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        RouteTableIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceRouteTablesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/route_tables.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def limit(self, count: int) -> ServiceResourceRouteTablesCollection:
        """
        Return at most this many RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/route_tables.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def page_size(self, count: int) -> ServiceResourceRouteTablesCollection:
        """
        Fetch at most this many RouteTables per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/route_tables.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def pages(self) -> Iterator[List[RouteTable]]:
        """
        A generator which yields pages of RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/route_tables.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceroutetablescollection)
        """

    def __iter__(self) -> Iterator[RouteTable]:
        """
        A generator which yields RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/route_tables.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourceroutetablescollection)
        """

class ServiceResourceSecurityGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/security_groups.html#EC2.ServiceResource.security_groups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesecuritygroupscollection)
    """
    def all(self) -> ServiceResourceSecurityGroupsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/security_groups.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        GroupIds: Sequence[str] = ...,
        GroupNames: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceSecurityGroupsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/security_groups.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def limit(self, count: int) -> ServiceResourceSecurityGroupsCollection:
        """
        Return at most this many SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/security_groups.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def page_size(self, count: int) -> ServiceResourceSecurityGroupsCollection:
        """
        Fetch at most this many SecurityGroups per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/security_groups.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def pages(self) -> Iterator[List[SecurityGroup]]:
        """
        A generator which yields pages of SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/security_groups.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

    def __iter__(self) -> Iterator[SecurityGroup]:
        """
        A generator which yields SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/security_groups.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesecuritygroupscollection)
        """

class ServiceResourceSnapshotsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/snapshots.html#EC2.ServiceResource.snapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesnapshotscollection)
    """
    def all(self) -> ServiceResourceSnapshotsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/snapshots.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        OwnerIds: Sequence[str] = ...,
        RestorableByUserIds: Sequence[str] = ...,
        SnapshotIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceSnapshotsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/snapshots.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def limit(self, count: int) -> ServiceResourceSnapshotsCollection:
        """
        Return at most this many Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/snapshots.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def page_size(self, count: int) -> ServiceResourceSnapshotsCollection:
        """
        Fetch at most this many Snapshots per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/snapshots.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def pages(self) -> Iterator[List[Snapshot]]:
        """
        A generator which yields pages of Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/snapshots.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

    def __iter__(self) -> Iterator[Snapshot]:
        """
        A generator which yields Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/snapshots.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesnapshotscollection)
        """

class ServiceResourceSubnetsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/subnets.html#EC2.ServiceResource.subnets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesubnetscollection)
    """
    def all(self) -> ServiceResourceSubnetsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/subnets.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        SubnetIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
    ) -> ServiceResourceSubnetsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/subnets.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def limit(self, count: int) -> ServiceResourceSubnetsCollection:
        """
        Return at most this many Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/subnets.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def page_size(self, count: int) -> ServiceResourceSubnetsCollection:
        """
        Fetch at most this many Subnets per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/subnets.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def pages(self) -> Iterator[List[Subnet]]:
        """
        A generator which yields pages of Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/subnets.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesubnetscollection)
        """

    def __iter__(self) -> Iterator[Subnet]:
        """
        A generator which yields Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/subnets.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcesubnetscollection)
        """

class ServiceResourceVolumesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/volumes.html#EC2.ServiceResource.volumes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevolumescollection)
    """
    def all(self) -> ServiceResourceVolumesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/volumes.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        VolumeIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> ServiceResourceVolumesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/volumes.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def limit(self, count: int) -> ServiceResourceVolumesCollection:
        """
        Return at most this many Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/volumes.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def page_size(self, count: int) -> ServiceResourceVolumesCollection:
        """
        Fetch at most this many Volumes per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/volumes.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def pages(self) -> Iterator[List[Volume]]:
        """
        A generator which yields pages of Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/volumes.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevolumescollection)
        """

    def __iter__(self) -> Iterator[Volume]:
        """
        A generator which yields Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/volumes.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevolumescollection)
        """

class ServiceResourceVpcAddressesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_addresses.html#EC2.ServiceResource.vpc_addresses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcaddressescollection)
    """
    def all(self) -> ServiceResourceVpcAddressesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_addresses.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        PublicIps: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        AllocationIds: Sequence[str] = ...,
    ) -> ServiceResourceVpcAddressesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_addresses.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def limit(self, count: int) -> ServiceResourceVpcAddressesCollection:
        """
        Return at most this many VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_addresses.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def page_size(self, count: int) -> ServiceResourceVpcAddressesCollection:
        """
        Fetch at most this many VpcAddresss per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_addresses.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def pages(self) -> Iterator[List[VpcAddress]]:
        """
        A generator which yields pages of VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_addresses.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

    def __iter__(self) -> Iterator[VpcAddress]:
        """
        A generator which yields VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_addresses.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcaddressescollection)
        """

class ServiceResourceVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_peering_connections.html#EC2.ServiceResource.vpc_peering_connections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
    """
    def all(self) -> ServiceResourceVpcPeeringConnectionsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_peering_connections.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        VpcPeeringConnectionIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> ServiceResourceVpcPeeringConnectionsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_peering_connections.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def limit(self, count: int) -> ServiceResourceVpcPeeringConnectionsCollection:
        """
        Return at most this many VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_peering_connections.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def page_size(self, count: int) -> ServiceResourceVpcPeeringConnectionsCollection:
        """
        Fetch at most this many VpcPeeringConnections per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_peering_connections.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def pages(self) -> Iterator[List[VpcPeeringConnection]]:
        """
        A generator which yields pages of VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_peering_connections.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

    def __iter__(self) -> Iterator[VpcPeeringConnection]:
        """
        A generator which yields VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpc_peering_connections.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcpeeringconnectionscollection)
        """

class ServiceResourceVpcsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpcs.html#EC2.ServiceResource.vpcs)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcscollection)
    """
    def all(self) -> ServiceResourceVpcsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpcs.html#EC2.ServiceResource.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        VpcIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
    ) -> ServiceResourceVpcsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpcs.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def limit(self, count: int) -> ServiceResourceVpcsCollection:
        """
        Return at most this many Vpcs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpcs.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def page_size(self, count: int) -> ServiceResourceVpcsCollection:
        """
        Fetch at most this many Vpcs per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpcs.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def pages(self) -> Iterator[List[Vpc]]:
        """
        A generator which yields pages of Vpcs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpcs.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcscollection)
        """

    def __iter__(self) -> Iterator[Vpc]:
        """
        A generator which yields Vpcs.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/vpcs.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#serviceresourcevpcscollection)
        """

class InstanceVolumesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/volumes.html#EC2.Instance.volumes)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevolumes)
    """
    def all(self) -> InstanceVolumesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/volumes.html#EC2.Instance.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevolumes)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        VolumeIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> InstanceVolumesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/volumes.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevolumes)
        """

    def limit(self, count: int) -> InstanceVolumesCollection:
        """
        Return at most this many Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/volumes.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevolumes)
        """

    def page_size(self, count: int) -> InstanceVolumesCollection:
        """
        Fetch at most this many Volumes per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/volumes.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevolumes)
        """

    def pages(self) -> Iterator[List[Volume]]:
        """
        A generator which yields pages of Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/volumes.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevolumes)
        """

    def __iter__(self) -> Iterator[Volume]:
        """
        A generator which yields Volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/volumes.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevolumes)
        """

class InstanceVpcAddressesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/vpc_addresses.html#EC2.Instance.vpc_addresses)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevpc_addresses)
    """
    def all(self) -> InstanceVpcAddressesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/vpc_addresses.html#EC2.Instance.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevpc_addresses)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        PublicIps: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        AllocationIds: Sequence[str] = ...,
    ) -> InstanceVpcAddressesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/vpc_addresses.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevpc_addresses)
        """

    def limit(self, count: int) -> InstanceVpcAddressesCollection:
        """
        Return at most this many VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/vpc_addresses.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevpc_addresses)
        """

    def page_size(self, count: int) -> InstanceVpcAddressesCollection:
        """
        Fetch at most this many VpcAddresss per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/vpc_addresses.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevpc_addresses)
        """

    def pages(self) -> Iterator[List[VpcAddress]]:
        """
        A generator which yields pages of VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/vpc_addresses.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevpc_addresses)
        """

    def __iter__(self) -> Iterator[VpcAddress]:
        """
        A generator which yields VpcAddresss.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/vpc_addresses.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancevpc_addresses)
        """

class PlacementGroupInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#EC2.PlacementGroup.instances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
    """
    def all(self) -> PlacementGroupInstancesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#EC2.PlacementGroup.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        InstanceIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> PlacementGroupInstancesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def create_tags(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#create_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def monitor(self, *, DryRun: bool = ...) -> List[MonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#monitor)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def reboot(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#reboot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def start(
        self, *, AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> List[StartInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#start)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def stop(
        self, *, Hibernate: bool = ..., DryRun: bool = ..., Force: bool = ...
    ) -> List[StopInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#stop)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def terminate(self, *, DryRun: bool = ...) -> List[TerminateInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#terminate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def unmonitor(self, *, DryRun: bool = ...) -> List[UnmonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#unmonitor)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def limit(self, count: int) -> PlacementGroupInstancesCollection:
        """
        Return at most this many Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def page_size(self, count: int) -> PlacementGroupInstancesCollection:
        """
        Fetch at most this many Instances per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def pages(self) -> Iterator[List[Instance]]:
        """
        A generator which yields pages of Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

    def __iter__(self) -> Iterator[Instance]:
        """
        A generator which yields Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/instances.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupinstances)
        """

class SubnetInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#EC2.Subnet.instances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
    """
    def all(self) -> SubnetInstancesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#EC2.Subnet.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        InstanceIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> SubnetInstancesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def create_tags(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#create_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def monitor(self, *, DryRun: bool = ...) -> List[MonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#monitor)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def reboot(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#reboot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def start(
        self, *, AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> List[StartInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#start)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def stop(
        self, *, Hibernate: bool = ..., DryRun: bool = ..., Force: bool = ...
    ) -> List[StopInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#stop)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def terminate(self, *, DryRun: bool = ...) -> List[TerminateInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#terminate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def unmonitor(self, *, DryRun: bool = ...) -> List[UnmonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#unmonitor)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def limit(self, count: int) -> SubnetInstancesCollection:
        """
        Return at most this many Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def page_size(self, count: int) -> SubnetInstancesCollection:
        """
        Fetch at most this many Instances per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def pages(self) -> Iterator[List[Instance]]:
        """
        A generator which yields pages of Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

    def __iter__(self) -> Iterator[Instance]:
        """
        A generator which yields Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/instances.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetinstances)
        """

class SubnetNetworkInterfacesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/network_interfaces.html#EC2.Subnet.network_interfaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetnetwork_interfaces)
    """
    def all(self) -> SubnetNetworkInterfacesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/network_interfaces.html#EC2.Subnet.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetnetwork_interfaces)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        NetworkInterfaceIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> SubnetNetworkInterfacesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/network_interfaces.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetnetwork_interfaces)
        """

    def limit(self, count: int) -> SubnetNetworkInterfacesCollection:
        """
        Return at most this many NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/network_interfaces.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetnetwork_interfaces)
        """

    def page_size(self, count: int) -> SubnetNetworkInterfacesCollection:
        """
        Fetch at most this many NetworkInterfaces per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/network_interfaces.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetnetwork_interfaces)
        """

    def pages(self) -> Iterator[List[NetworkInterface]]:
        """
        A generator which yields pages of NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/network_interfaces.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetnetwork_interfaces)
        """

    def __iter__(self) -> Iterator[NetworkInterface]:
        """
        A generator which yields NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/network_interfaces.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetnetwork_interfaces)
        """

class VolumeSnapshotsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/snapshots.html#EC2.Volume.snapshots)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumesnapshots)
    """
    def all(self) -> VolumeSnapshotsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/snapshots.html#EC2.Volume.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumesnapshots)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        MaxResults: int = ...,
        NextToken: str = ...,
        OwnerIds: Sequence[str] = ...,
        RestorableByUserIds: Sequence[str] = ...,
        SnapshotIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> VolumeSnapshotsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/snapshots.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumesnapshots)
        """

    def limit(self, count: int) -> VolumeSnapshotsCollection:
        """
        Return at most this many Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/snapshots.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumesnapshots)
        """

    def page_size(self, count: int) -> VolumeSnapshotsCollection:
        """
        Fetch at most this many Snapshots per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/snapshots.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumesnapshots)
        """

    def pages(self) -> Iterator[List[Snapshot]]:
        """
        A generator which yields pages of Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/snapshots.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumesnapshots)
        """

    def __iter__(self) -> Iterator[Snapshot]:
        """
        A generator which yields Snapshots.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/snapshots.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumesnapshots)
        """

class VpcAcceptedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/accepted_vpc_peering_connections.html#EC2.Vpc.accepted_vpc_peering_connections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaccepted_vpc_peering_connections)
    """
    def all(self) -> VpcAcceptedVpcPeeringConnectionsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/accepted_vpc_peering_connections.html#EC2.Vpc.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaccepted_vpc_peering_connections)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        VpcPeeringConnectionIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> VpcAcceptedVpcPeeringConnectionsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/accepted_vpc_peering_connections.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaccepted_vpc_peering_connections)
        """

    def limit(self, count: int) -> VpcAcceptedVpcPeeringConnectionsCollection:
        """
        Return at most this many VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/accepted_vpc_peering_connections.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaccepted_vpc_peering_connections)
        """

    def page_size(self, count: int) -> VpcAcceptedVpcPeeringConnectionsCollection:
        """
        Fetch at most this many VpcPeeringConnections per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/accepted_vpc_peering_connections.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaccepted_vpc_peering_connections)
        """

    def pages(self) -> Iterator[List[VpcPeeringConnection]]:
        """
        A generator which yields pages of VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/accepted_vpc_peering_connections.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaccepted_vpc_peering_connections)
        """

    def __iter__(self) -> Iterator[VpcPeeringConnection]:
        """
        A generator which yields VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/accepted_vpc_peering_connections.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaccepted_vpc_peering_connections)
        """

class VpcInstancesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#EC2.Vpc.instances)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
    """
    def all(self) -> VpcInstancesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#EC2.Vpc.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        InstanceIds: Sequence[str] = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
    ) -> VpcInstancesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def create_tags(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#create_tags)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def monitor(self, *, DryRun: bool = ...) -> List[MonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#monitor)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def reboot(self, *, DryRun: bool = ...) -> None:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#reboot)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def start(
        self, *, AdditionalInfo: str = ..., DryRun: bool = ...
    ) -> List[StartInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#start)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def stop(
        self, *, Hibernate: bool = ..., DryRun: bool = ..., Force: bool = ...
    ) -> List[StopInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#stop)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def terminate(self, *, DryRun: bool = ...) -> List[TerminateInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#terminate)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def unmonitor(self, *, DryRun: bool = ...) -> List[UnmonitorInstancesResultTypeDef]:
        """
        Batch method.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#unmonitor)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def limit(self, count: int) -> VpcInstancesCollection:
        """
        Return at most this many Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def page_size(self, count: int) -> VpcInstancesCollection:
        """
        Fetch at most this many Instances per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def pages(self) -> Iterator[List[Instance]]:
        """
        A generator which yields pages of Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

    def __iter__(self) -> Iterator[Instance]:
        """
        A generator which yields Instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/instances.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinstances)
        """

class VpcInternetGatewaysCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/internet_gateways.html#EC2.Vpc.internet_gateways)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinternet_gateways)
    """
    def all(self) -> VpcInternetGatewaysCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/internet_gateways.html#EC2.Vpc.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinternet_gateways)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        InternetGatewayIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> VpcInternetGatewaysCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/internet_gateways.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinternet_gateways)
        """

    def limit(self, count: int) -> VpcInternetGatewaysCollection:
        """
        Return at most this many InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/internet_gateways.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinternet_gateways)
        """

    def page_size(self, count: int) -> VpcInternetGatewaysCollection:
        """
        Fetch at most this many InternetGateways per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/internet_gateways.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinternet_gateways)
        """

    def pages(self) -> Iterator[List[InternetGateway]]:
        """
        A generator which yields pages of InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/internet_gateways.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinternet_gateways)
        """

    def __iter__(self) -> Iterator[InternetGateway]:
        """
        A generator which yields InternetGateways.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/internet_gateways.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcinternet_gateways)
        """

class VpcNetworkAclsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_acls.html#EC2.Vpc.network_acls)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_acls)
    """
    def all(self) -> VpcNetworkAclsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_acls.html#EC2.Vpc.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_acls)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        NetworkAclIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> VpcNetworkAclsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_acls.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_acls)
        """

    def limit(self, count: int) -> VpcNetworkAclsCollection:
        """
        Return at most this many NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_acls.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_acls)
        """

    def page_size(self, count: int) -> VpcNetworkAclsCollection:
        """
        Fetch at most this many NetworkAcls per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_acls.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_acls)
        """

    def pages(self) -> Iterator[List[NetworkAcl]]:
        """
        A generator which yields pages of NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_acls.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_acls)
        """

    def __iter__(self) -> Iterator[NetworkAcl]:
        """
        A generator which yields NetworkAcls.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_acls.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_acls)
        """

class VpcNetworkInterfacesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_interfaces.html#EC2.Vpc.network_interfaces)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_interfaces)
    """
    def all(self) -> VpcNetworkInterfacesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_interfaces.html#EC2.Vpc.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_interfaces)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        NetworkInterfaceIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> VpcNetworkInterfacesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_interfaces.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_interfaces)
        """

    def limit(self, count: int) -> VpcNetworkInterfacesCollection:
        """
        Return at most this many NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_interfaces.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_interfaces)
        """

    def page_size(self, count: int) -> VpcNetworkInterfacesCollection:
        """
        Fetch at most this many NetworkInterfaces per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_interfaces.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_interfaces)
        """

    def pages(self) -> Iterator[List[NetworkInterface]]:
        """
        A generator which yields pages of NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_interfaces.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_interfaces)
        """

    def __iter__(self) -> Iterator[NetworkInterface]:
        """
        A generator which yields NetworkInterfaces.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/network_interfaces.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcnetwork_interfaces)
        """

class VpcRequestedVpcPeeringConnectionsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/requested_vpc_peering_connections.html#EC2.Vpc.requested_vpc_peering_connections)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcrequested_vpc_peering_connections)
    """
    def all(self) -> VpcRequestedVpcPeeringConnectionsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/requested_vpc_peering_connections.html#EC2.Vpc.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcrequested_vpc_peering_connections)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        VpcPeeringConnectionIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> VpcRequestedVpcPeeringConnectionsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/requested_vpc_peering_connections.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcrequested_vpc_peering_connections)
        """

    def limit(self, count: int) -> VpcRequestedVpcPeeringConnectionsCollection:
        """
        Return at most this many VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/requested_vpc_peering_connections.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcrequested_vpc_peering_connections)
        """

    def page_size(self, count: int) -> VpcRequestedVpcPeeringConnectionsCollection:
        """
        Fetch at most this many VpcPeeringConnections per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/requested_vpc_peering_connections.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcrequested_vpc_peering_connections)
        """

    def pages(self) -> Iterator[List[VpcPeeringConnection]]:
        """
        A generator which yields pages of VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/requested_vpc_peering_connections.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcrequested_vpc_peering_connections)
        """

    def __iter__(self) -> Iterator[VpcPeeringConnection]:
        """
        A generator which yields VpcPeeringConnections.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/requested_vpc_peering_connections.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcrequested_vpc_peering_connections)
        """

class VpcRouteTablesCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/route_tables.html#EC2.Vpc.route_tables)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcroute_tables)
    """
    def all(self) -> VpcRouteTablesCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/route_tables.html#EC2.Vpc.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcroute_tables)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        RouteTableIds: Sequence[str] = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> VpcRouteTablesCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/route_tables.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcroute_tables)
        """

    def limit(self, count: int) -> VpcRouteTablesCollection:
        """
        Return at most this many RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/route_tables.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcroute_tables)
        """

    def page_size(self, count: int) -> VpcRouteTablesCollection:
        """
        Fetch at most this many RouteTables per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/route_tables.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcroute_tables)
        """

    def pages(self) -> Iterator[List[RouteTable]]:
        """
        A generator which yields pages of RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/route_tables.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcroute_tables)
        """

    def __iter__(self) -> Iterator[RouteTable]:
        """
        A generator which yields RouteTables.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/route_tables.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcroute_tables)
        """

class VpcSecurityGroupsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/security_groups.html#EC2.Vpc.security_groups)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsecurity_groups)
    """
    def all(self) -> VpcSecurityGroupsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/security_groups.html#EC2.Vpc.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsecurity_groups)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        GroupIds: Sequence[str] = ...,
        GroupNames: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
        Filters: Sequence[FilterTypeDef] = ...,
    ) -> VpcSecurityGroupsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/security_groups.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsecurity_groups)
        """

    def limit(self, count: int) -> VpcSecurityGroupsCollection:
        """
        Return at most this many SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/security_groups.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsecurity_groups)
        """

    def page_size(self, count: int) -> VpcSecurityGroupsCollection:
        """
        Fetch at most this many SecurityGroups per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/security_groups.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsecurity_groups)
        """

    def pages(self) -> Iterator[List[SecurityGroup]]:
        """
        A generator which yields pages of SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/security_groups.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsecurity_groups)
        """

    def __iter__(self) -> Iterator[SecurityGroup]:
        """
        A generator which yields SecurityGroups.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/security_groups.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsecurity_groups)
        """

class VpcSubnetsCollection(ResourceCollection):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/subnets.html#EC2.Vpc.subnets)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsubnets)
    """
    def all(self) -> VpcSubnetsCollection:
        """
        Get all items from the collection, optionally with a custom page size and item
        count limit.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/subnets.html#EC2.Vpc.all)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsubnets)
        """

    def filter(  # type: ignore[override]
        self,
        *,
        Filters: Sequence[FilterTypeDef] = ...,
        SubnetIds: Sequence[str] = ...,
        NextToken: str = ...,
        MaxResults: int = ...,
        DryRun: bool = ...,
    ) -> VpcSubnetsCollection:
        """
        Get items from the collection, passing keyword arguments along as parameters to
        the underlying service operation, which are typically used to filter the
        results.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/subnets.html#filter)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsubnets)
        """

    def limit(self, count: int) -> VpcSubnetsCollection:
        """
        Return at most this many Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/subnets.html#limit)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsubnets)
        """

    def page_size(self, count: int) -> VpcSubnetsCollection:
        """
        Fetch at most this many Subnets per service request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/subnets.html#page_size)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsubnets)
        """

    def pages(self) -> Iterator[List[Subnet]]:
        """
        A generator which yields pages of Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/subnets.html#pages)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsubnets)
        """

    def __iter__(self) -> Iterator[Subnet]:
        """
        A generator which yields Subnets.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/subnets.html#__iter__)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcsubnets)
        """

class ClassicAddress(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/classicaddress/index.html#EC2.ClassicAddress)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#classicaddress)
    """

    public_ip: str
    allocation_id: str
    association_id: str
    domain: DomainTypeType
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[TagTypeDef]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    carrier_ip: str
    service_managed: ServiceManagedType
    instance_id: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this ClassicAddress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/classicaddress/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#classicaddressget_available_subresources-method)
        """

    def associate(
        self, **kwargs: Unpack[AssociateAddressRequestClassicAddressAssociateTypeDef]
    ) -> AssociateAddressResultTypeDef:
        """
        Associates an Elastic IP address, or carrier IP address (for instances that are
        in subnets in Wavelength Zones) with an instance or a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/classicaddress/associate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#classicaddressassociate-method)
        """

    def disassociate(
        self, **kwargs: Unpack[DisassociateAddressRequestClassicAddressDisassociateTypeDef]
    ) -> None:
        """
        Disassociates an Elastic IP address from the instance or network interface it's
        associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/classicaddress/disassociate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#classicaddressdisassociate-method)
        """

    def release(self, **kwargs: Unpack[ReleaseAddressRequestClassicAddressReleaseTypeDef]) -> None:
        """
        Releases the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/classicaddress/release.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#classicaddressrelease-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/classicaddress/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#classicaddressload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/classicaddress/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#classicaddressreload-method)
        """

_ClassicAddress = ClassicAddress

class DhcpOptions(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/dhcpoptions/index.html#EC2.DhcpOptions)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#dhcpoptions)
    """

    id: str
    owner_id: str
    tags: List[TagTypeDef]
    dhcp_options_id: str
    dhcp_configurations: List[DhcpConfigurationTypeDef]
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this DhcpOptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/dhcpoptions/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#dhcpoptionsget_available_subresources-method)
        """

    def associate_with_vpc(
        self, **kwargs: Unpack[AssociateDhcpOptionsRequestDhcpOptionsAssociateWithVpcTypeDef]
    ) -> None:
        """
        Associates a set of DHCP options (that you've previously created) with the
        specified VPC, or associates no DHCP options with the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/dhcpoptions/associate_with_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#dhcpoptionsassociate_with_vpc-method)
        """

    def create_tags(self, **kwargs: Unpack[DhcpOptionsCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/dhcpoptions/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#dhcpoptionscreate_tags-method)
        """

    def delete(self, **kwargs: Unpack[DeleteDhcpOptionsRequestDhcpOptionsDeleteTypeDef]) -> None:
        """
        Deletes the specified set of DHCP options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/dhcpoptions/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#dhcpoptionsdelete-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/dhcpoptions/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#dhcpoptionsload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/dhcpoptions/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#dhcpoptionsreload-method)
        """

_DhcpOptions = DhcpOptions

class Image(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/index.html#EC2.Image)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#image)
    """

    id: str
    platform_details: str
    usage_operation: str
    block_device_mappings: List[BlockDeviceMappingTypeDef]
    description: str
    ena_support: bool
    hypervisor: HypervisorTypeType
    image_owner_alias: str
    name: str
    root_device_name: str
    root_device_type: DeviceTypeType
    sriov_net_support: str
    state_reason: StateReasonTypeDef
    tags: List[TagTypeDef]
    virtualization_type: VirtualizationTypeType
    boot_mode: BootModeValuesType
    tpm_support: Literal["v2.0"]
    deprecation_time: str
    imds_support: Literal["v2.0"]
    source_instance_id: str
    deregistration_protection: str
    last_launched_time: str
    image_allowed: bool
    source_image_id: str
    source_image_region: str
    image_id: str
    image_location: str
    state: ImageStateType
    owner_id: str
    creation_date: str
    public: bool
    product_codes: List[ProductCodeTypeDef]
    architecture: ArchitectureValuesType
    image_type: ImageTypeValuesType
    kernel_id: str
    ramdisk_id: str
    platform: Literal["windows"]
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Image.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#imageget_available_subresources-method)
        """

    def create_tags(self, **kwargs: Unpack[ImageCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#imagecreate_tags-method)
        """

    def deregister(
        self, **kwargs: Unpack[DeregisterImageRequestImageDeregisterTypeDef]
    ) -> Dict[str, Any]:
        """
        Deregisters the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/deregister.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#imagederegister-method)
        """

    def describe_attribute(
        self, **kwargs: Unpack[DescribeImageAttributeRequestImageDescribeAttributeTypeDef]
    ) -> ImageAttributeTypeDef:
        """
        Describes the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/describe_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#imagedescribe_attribute-method)
        """

    def modify_attribute(
        self, **kwargs: Unpack[ModifyImageAttributeRequestImageModifyAttributeTypeDef]
    ) -> None:
        """
        Modifies the specified attribute of the specified AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/modify_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#imagemodify_attribute-method)
        """

    def reset_attribute(
        self, **kwargs: Unpack[ResetImageAttributeRequestImageResetAttributeTypeDef]
    ) -> None:
        """
        Resets an attribute of an AMI to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/reset_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#imagereset_attribute-method)
        """

    def wait_until_exists(self) -> None:
        """
        Waits until Image is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/wait_until_exists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#imagewait_until_exists-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#imageload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/image/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#imagereload-method)
        """

_Image = Image

class Instance(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/index.html#EC2.Instance)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instance)
    """

    id: str
    classic_address: ClassicAddress
    image: Image
    key_pair: KeyPairInfo
    network_interfaces: List[NetworkInterface]
    placement_group: PlacementGroup
    subnet: Subnet
    vpc: Vpc
    volumes: InstanceVolumesCollection
    vpc_addresses: InstanceVpcAddressesCollection
    architecture: ArchitectureValuesType
    block_device_mappings: List[InstanceBlockDeviceMappingTypeDef]
    client_token: str
    ebs_optimized: bool
    ena_support: bool
    hypervisor: HypervisorTypeType
    iam_instance_profile: IamInstanceProfileTypeDef
    instance_lifecycle: InstanceLifecycleTypeType
    elastic_gpu_associations: List[ElasticGpuAssociationTypeDef]
    elastic_inference_accelerator_associations: List[ElasticInferenceAcceleratorAssociationTypeDef]
    network_interfaces_attribute: List[InstanceNetworkInterfaceTypeDef]
    outpost_arn: str
    root_device_name: str
    root_device_type: DeviceTypeType
    security_groups: List[GroupIdentifierTypeDef]
    source_dest_check: bool
    spot_instance_request_id: str
    sriov_net_support: str
    state_reason: StateReasonTypeDef
    tags: List[TagTypeDef]
    virtualization_type: VirtualizationTypeType
    cpu_options: CpuOptionsTypeDef
    capacity_reservation_id: str
    capacity_reservation_specification: CapacityReservationSpecificationResponseTypeDef
    hibernation_options: HibernationOptionsTypeDef
    licenses: List[LicenseConfigurationTypeDef]
    metadata_options: InstanceMetadataOptionsResponseTypeDef
    enclave_options: EnclaveOptionsTypeDef
    boot_mode: BootModeValuesType
    platform_details: str
    usage_operation: str
    usage_operation_update_time: datetime
    private_dns_name_options: PrivateDnsNameOptionsResponseTypeDef
    ipv6_address: str
    tpm_support: str
    maintenance_options: InstanceMaintenanceOptionsTypeDef
    current_instance_boot_mode: InstanceBootModeValuesType
    network_performance_options: InstanceNetworkPerformanceOptionsTypeDef
    operator: OperatorResponseTypeDef
    instance_id: str
    image_id: str
    state: InstanceStateTypeDef
    private_dns_name: str
    public_dns_name: str
    state_transition_reason: str
    key_name: str
    ami_launch_index: int
    product_codes: List[ProductCodeTypeDef]
    instance_type: InstanceTypeType
    launch_time: datetime
    placement: PlacementTypeDef
    kernel_id: str
    ramdisk_id: str
    platform: Literal["windows"]
    monitoring: MonitoringTypeDef
    subnet_id: str
    vpc_id: str
    private_ip_address: str
    public_ip_address: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instanceget_available_subresources-method)
        """

    def attach_classic_link_vpc(
        self, **kwargs: Unpack[AttachClassicLinkVpcRequestInstanceAttachClassicLinkVpcTypeDef]
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/attach_classic_link_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instanceattach_classic_link_vpc-method)
        """

    def attach_volume(
        self, **kwargs: Unpack[AttachVolumeRequestInstanceAttachVolumeTypeDef]
    ) -> VolumeAttachmentResponseTypeDef:
        """
        Attaches an EBS volume to a running or stopped instance and exposes it to the
        instance with the specified device name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/attach_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instanceattach_volume-method)
        """

    def console_output(
        self, **kwargs: Unpack[GetConsoleOutputRequestInstanceConsoleOutputTypeDef]
    ) -> GetConsoleOutputResultTypeDef:
        """
        Gets the console output for the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/console_output.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instanceconsole_output-method)
        """

    def create_image(
        self, **kwargs: Unpack[CreateImageRequestInstanceCreateImageTypeDef]
    ) -> _Image:
        """
        Creates an Amazon EBS-backed AMI from an Amazon EBS-backed instance that is
        either running or stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/create_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancecreate_image-method)
        """

    def create_tags(self, **kwargs: Unpack[InstanceCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancecreate_tags-method)
        """

    def describe_attribute(
        self, **kwargs: Unpack[DescribeInstanceAttributeRequestInstanceDescribeAttributeTypeDef]
    ) -> InstanceAttributeTypeDef:
        """
        Describes the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/describe_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancedescribe_attribute-method)
        """

    def detach_classic_link_vpc(
        self, **kwargs: Unpack[DetachClassicLinkVpcRequestInstanceDetachClassicLinkVpcTypeDef]
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/detach_classic_link_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancedetach_classic_link_vpc-method)
        """

    def detach_volume(
        self, **kwargs: Unpack[DetachVolumeRequestInstanceDetachVolumeTypeDef]
    ) -> VolumeAttachmentResponseTypeDef:
        """
        Detaches an EBS volume from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/detach_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancedetach_volume-method)
        """

    def modify_attribute(
        self, **kwargs: Unpack[ModifyInstanceAttributeRequestInstanceModifyAttributeTypeDef]
    ) -> None:
        """
        Modifies the specified attribute of the specified instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/modify_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancemodify_attribute-method)
        """

    def monitor(
        self, **kwargs: Unpack[MonitorInstancesRequestInstanceMonitorTypeDef]
    ) -> MonitorInstancesResultTypeDef:
        """
        Enables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/monitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancemonitor-method)
        """

    def password_data(
        self, **kwargs: Unpack[GetPasswordDataRequestInstancePasswordDataTypeDef]
    ) -> GetPasswordDataResultTypeDef:
        """
        Retrieves the encrypted administrator password for a running Windows instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/password_data.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancepassword_data-method)
        """

    def reboot(self, **kwargs: Unpack[RebootInstancesRequestInstanceRebootTypeDef]) -> None:
        """
        Requests a reboot of the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/reboot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancereboot-method)
        """

    def report_status(
        self, **kwargs: Unpack[ReportInstanceStatusRequestInstanceReportStatusTypeDef]
    ) -> None:
        """
        Submits feedback about the status of an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/report_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancereport_status-method)
        """

    def reset_attribute(
        self, **kwargs: Unpack[ResetInstanceAttributeRequestInstanceResetAttributeTypeDef]
    ) -> None:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/reset_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancereset_attribute-method)
        """

    def reset_kernel(
        self, **kwargs: Unpack[ResetInstanceAttributeRequestInstanceResetKernelTypeDef]
    ) -> None:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/reset_kernel.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancereset_kernel-method)
        """

    def reset_ramdisk(
        self, **kwargs: Unpack[ResetInstanceAttributeRequestInstanceResetRamdiskTypeDef]
    ) -> None:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/reset_ramdisk.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancereset_ramdisk-method)
        """

    def reset_source_dest_check(
        self, **kwargs: Unpack[ResetInstanceAttributeRequestInstanceResetSourceDestCheckTypeDef]
    ) -> None:
        """
        Resets an attribute of an instance to its default value.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/reset_source_dest_check.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancereset_source_dest_check-method)
        """

    def start(
        self, **kwargs: Unpack[StartInstancesRequestInstanceStartTypeDef]
    ) -> StartInstancesResultTypeDef:
        """
        Starts an Amazon EBS-backed instance that you've previously stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/start.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancestart-method)
        """

    def stop(
        self, **kwargs: Unpack[StopInstancesRequestInstanceStopTypeDef]
    ) -> StopInstancesResultTypeDef:
        """
        Stops an Amazon EBS-backed instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/stop.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancestop-method)
        """

    def terminate(
        self, **kwargs: Unpack[TerminateInstancesRequestInstanceTerminateTypeDef]
    ) -> TerminateInstancesResultTypeDef:
        """
        Shuts down the specified instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/terminate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instanceterminate-method)
        """

    def unmonitor(
        self, **kwargs: Unpack[UnmonitorInstancesRequestInstanceUnmonitorTypeDef]
    ) -> UnmonitorInstancesResultTypeDef:
        """
        Disables detailed monitoring for a running instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/unmonitor.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instanceunmonitor-method)
        """

    def wait_until_exists(self) -> None:
        """
        Waits until Instance is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/wait_until_exists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancewait_until_exists-method)
        """

    def wait_until_running(self) -> None:
        """
        Waits until Instance is running.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/wait_until_running.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancewait_until_running-method)
        """

    def wait_until_stopped(self) -> None:
        """
        Waits until Instance is stopped.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/wait_until_stopped.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancewait_until_stopped-method)
        """

    def wait_until_terminated(self) -> None:
        """
        Waits until Instance is terminated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/wait_until_terminated.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancewait_until_terminated-method)
        """

    def delete_tags(self, **kwargs: Unpack[InstanceDeleteTagsRequestTypeDef]) -> None:
        """
        Deletes the specified set of tags from the specified set of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/delete_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancedelete_tags-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instanceload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/instance/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#instancereload-method)
        """

_Instance = Instance

class InternetGateway(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/internetgateway/index.html#EC2.InternetGateway)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#internetgateway)
    """

    id: str
    attachments: List[InternetGatewayAttachmentTypeDef]
    internet_gateway_id: str
    owner_id: str
    tags: List[TagTypeDef]
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this InternetGateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/internetgateway/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#internetgatewayget_available_subresources-method)
        """

    def attach_to_vpc(
        self, **kwargs: Unpack[AttachInternetGatewayRequestInternetGatewayAttachToVpcTypeDef]
    ) -> None:
        """
        Attaches an internet gateway or a virtual private gateway to a VPC, enabling
        connectivity between the internet and the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/internetgateway/attach_to_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#internetgatewayattach_to_vpc-method)
        """

    def create_tags(self, **kwargs: Unpack[InternetGatewayCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/internetgateway/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#internetgatewaycreate_tags-method)
        """

    def delete(
        self, **kwargs: Unpack[DeleteInternetGatewayRequestInternetGatewayDeleteTypeDef]
    ) -> None:
        """
        Deletes the specified internet gateway.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/internetgateway/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#internetgatewaydelete-method)
        """

    def detach_from_vpc(
        self, **kwargs: Unpack[DetachInternetGatewayRequestInternetGatewayDetachFromVpcTypeDef]
    ) -> None:
        """
        Detaches an internet gateway from a VPC, disabling connectivity between the
        internet and the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/internetgateway/detach_from_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#internetgatewaydetach_from_vpc-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/internetgateway/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#internetgatewayload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/internetgateway/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#internetgatewayreload-method)
        """

_InternetGateway = InternetGateway

class KeyPair(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/keypair/index.html#EC2.KeyPair)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#keypair)
    """

    name: str
    key_pair_id: str
    tags: List[TagTypeDef]
    key_name: str
    key_fingerprint: str
    key_material: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this KeyPair.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/keypair/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#keypairget_available_subresources-method)
        """

    def delete(
        self, **kwargs: Unpack[DeleteKeyPairRequestKeyPairDeleteTypeDef]
    ) -> DeleteKeyPairResultTypeDef:
        """
        Deletes the specified key pair, by removing the public key from Amazon EC2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/keypair/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#keypairdelete-method)
        """

_KeyPair = KeyPair

class KeyPairInfo(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/keypairinfo/index.html#EC2.KeyPairInfo)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#keypairinfo)
    """

    name: str
    key_pair_id: str
    key_type: KeyTypeType
    tags: List[TagTypeDef]
    public_key: str
    create_time: datetime
    key_name: str
    key_fingerprint: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this KeyPairInfo.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/keypairinfo/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#keypairinfoget_available_subresources-method)
        """

    def delete(
        self, **kwargs: Unpack[DeleteKeyPairRequestKeyPairInfoDeleteTypeDef]
    ) -> DeleteKeyPairResultTypeDef:
        """
        Deletes the specified key pair, by removing the public key from Amazon EC2.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/keypairinfo/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#keypairinfodelete-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/keypairinfo/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#keypairinfoload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/keypairinfo/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#keypairinforeload-method)
        """

_KeyPairInfo = KeyPairInfo

class NetworkAcl(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/index.html#EC2.NetworkAcl)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkacl)
    """

    id: str
    vpc: Vpc
    associations: List[NetworkAclAssociationTypeDef]
    entries: List[NetworkAclEntryTypeDef]
    is_default: bool
    network_acl_id: str
    tags: List[TagTypeDef]
    vpc_id: str
    owner_id: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this NetworkAcl.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkaclget_available_subresources-method)
        """

    def create_entry(
        self, **kwargs: Unpack[CreateNetworkAclEntryRequestNetworkAclCreateEntryTypeDef]
    ) -> None:
        """
        Creates an entry (a rule) in a network ACL with the specified rule number.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/create_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkaclcreate_entry-method)
        """

    def create_tags(self, **kwargs: Unpack[NetworkAclCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkaclcreate_tags-method)
        """

    def delete(self, **kwargs: Unpack[DeleteNetworkAclRequestNetworkAclDeleteTypeDef]) -> None:
        """
        Deletes the specified network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkacldelete-method)
        """

    def delete_entry(
        self, **kwargs: Unpack[DeleteNetworkAclEntryRequestNetworkAclDeleteEntryTypeDef]
    ) -> None:
        """
        Deletes the specified ingress or egress entry (rule) from the specified network
        ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/delete_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkacldelete_entry-method)
        """

    def replace_association(
        self,
        **kwargs: Unpack[ReplaceNetworkAclAssociationRequestNetworkAclReplaceAssociationTypeDef],
    ) -> ReplaceNetworkAclAssociationResultTypeDef:
        """
        Changes which network ACL a subnet is associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/replace_association.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkaclreplace_association-method)
        """

    def replace_entry(
        self, **kwargs: Unpack[ReplaceNetworkAclEntryRequestNetworkAclReplaceEntryTypeDef]
    ) -> None:
        """
        Replaces an entry (rule) in a network ACL.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/replace_entry.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkaclreplace_entry-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkaclload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkacl/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkaclreload-method)
        """

_NetworkAcl = NetworkAcl

class NetworkInterface(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/index.html#EC2.NetworkInterface)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterface)
    """

    id: str
    association: NetworkInterfaceAssociation
    subnet: Subnet
    vpc: Vpc
    association_attribute: NetworkInterfaceAssociationTypeDef
    attachment: NetworkInterfaceAttachmentTypeDef
    availability_zone: str
    connection_tracking_configuration: ConnectionTrackingConfigurationTypeDef
    description: str
    groups: List[GroupIdentifierTypeDef]
    interface_type: NetworkInterfaceTypeType
    ipv6_addresses: List[NetworkInterfaceIpv6AddressTypeDef]
    mac_address: str
    network_interface_id: str
    outpost_arn: str
    owner_id: str
    private_dns_name: str
    private_ip_address: str
    private_ip_addresses: List[NetworkInterfacePrivateIpAddressTypeDef]
    ipv4_prefixes: List[Ipv4PrefixSpecificationTypeDef]
    ipv6_prefixes: List[Ipv6PrefixSpecificationTypeDef]
    requester_id: str
    requester_managed: bool
    source_dest_check: bool
    status: NetworkInterfaceStatusType
    subnet_id: str
    tag_set: List[TagTypeDef]
    vpc_id: str
    deny_all_igw_traffic: bool
    ipv6_native: bool
    ipv6_address: str
    operator: OperatorResponseTypeDef
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this NetworkInterface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceget_available_subresources-method)
        """

    def assign_private_ip_addresses(
        self,
        **kwargs: Unpack[
            AssignPrivateIpAddressesRequestNetworkInterfaceAssignPrivateIpAddressesTypeDef
        ],
    ) -> AssignPrivateIpAddressesResultTypeDef:
        """
        Assigns the specified secondary private IP addresses to the specified network
        interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/assign_private_ip_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceassign_private_ip_addresses-method)
        """

    def attach(
        self, **kwargs: Unpack[AttachNetworkInterfaceRequestNetworkInterfaceAttachTypeDef]
    ) -> AttachNetworkInterfaceResultTypeDef:
        """
        Attaches a network interface to an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/attach.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceattach-method)
        """

    def create_tags(self, **kwargs: Unpack[NetworkInterfaceCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfacecreate_tags-method)
        """

    def delete(
        self, **kwargs: Unpack[DeleteNetworkInterfaceRequestNetworkInterfaceDeleteTypeDef]
    ) -> None:
        """
        Deletes the specified network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfacedelete-method)
        """

    def describe_attribute(
        self,
        **kwargs: Unpack[
            DescribeNetworkInterfaceAttributeRequestNetworkInterfaceDescribeAttributeTypeDef
        ],
    ) -> DescribeNetworkInterfaceAttributeResultTypeDef:
        """
        Describes a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/describe_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfacedescribe_attribute-method)
        """

    def detach(
        self, **kwargs: Unpack[DetachNetworkInterfaceRequestNetworkInterfaceDetachTypeDef]
    ) -> None:
        """
        Detaches a network interface from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/detach.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfacedetach-method)
        """

    def modify_attribute(
        self,
        **kwargs: Unpack[
            ModifyNetworkInterfaceAttributeRequestNetworkInterfaceModifyAttributeTypeDef
        ],
    ) -> None:
        """
        Modifies the specified network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/modify_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfacemodify_attribute-method)
        """

    def reset_attribute(
        self,
        **kwargs: Unpack[
            ResetNetworkInterfaceAttributeRequestNetworkInterfaceResetAttributeTypeDef
        ],
    ) -> None:
        """
        Resets a network interface attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/reset_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfacereset_attribute-method)
        """

    def unassign_private_ip_addresses(
        self,
        **kwargs: Unpack[
            UnassignPrivateIpAddressesRequestNetworkInterfaceUnassignPrivateIpAddressesTypeDef
        ],
    ) -> None:
        """
        Unassigns the specified secondary private IP addresses or IPv4 Prefix
        Delegation prefixes from a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/unassign_private_ip_addresses.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceunassign_private_ip_addresses-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterface/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfacereload-method)
        """

_NetworkInterface = NetworkInterface

class NetworkInterfaceAssociation(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterfaceassociation/index.html#EC2.NetworkInterfaceAssociation)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceassociation)
    """

    id: str
    address: VpcAddress
    carrier_ip: str
    customer_owned_ip: str
    ip_owner_id: str
    public_dns_name: str
    public_ip: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this
        NetworkInterfaceAssociation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterfaceassociation/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceassociationget_available_subresources-method)
        """

    def delete(
        self, **kwargs: Unpack[DisassociateAddressRequestNetworkInterfaceAssociationDeleteTypeDef]
    ) -> None:
        """
        Disassociates an Elastic IP address from the instance or network interface it's
        associated with.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterfaceassociation/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceassociationdelete-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterfaceassociation/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceassociationload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/networkinterfaceassociation/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#networkinterfaceassociationreload-method)
        """

_NetworkInterfaceAssociation = NetworkInterfaceAssociation

class PlacementGroup(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/index.html#EC2.PlacementGroup)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroup)
    """

    name: str
    instances: PlacementGroupInstancesCollection
    group_name: str
    state: PlacementGroupStateType
    strategy: PlacementStrategyType
    partition_count: int
    group_id: str
    tags: List[TagTypeDef]
    group_arn: str
    spread_level: SpreadLevelType
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this PlacementGroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupget_available_subresources-method)
        """

    def delete(
        self, **kwargs: Unpack[DeletePlacementGroupRequestPlacementGroupDeleteTypeDef]
    ) -> None:
        """
        Deletes the specified placement group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupdelete-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/placementgroup/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#placementgroupreload-method)
        """

_PlacementGroup = PlacementGroup

class Route(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/route/index.html#EC2.Route)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#route)
    """

    route_table_id: str
    destination_cidr_block: str
    destination_ipv6_cidr_block: str
    destination_prefix_list_id: str
    egress_only_internet_gateway_id: str
    gateway_id: str
    instance_id: str
    instance_owner_id: str
    nat_gateway_id: str
    transit_gateway_id: str
    local_gateway_id: str
    carrier_gateway_id: str
    network_interface_id: str
    origin: RouteOriginType
    state: RouteStateType
    vpc_peering_connection_id: str
    core_network_arn: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Route.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/route/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routeget_available_subresources-method)
        """

    def delete(self, **kwargs: Unpack[DeleteRouteRequestRouteDeleteTypeDef]) -> None:
        """
        Deletes the specified route from the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/route/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routedelete-method)
        """

    def replace(self, **kwargs: Unpack[ReplaceRouteRequestRouteReplaceTypeDef]) -> None:
        """
        Replaces an existing route within a route table in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/route/replace.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routereplace-method)
        """

    def RouteTable(self) -> _RouteTable:
        """
        Creates a RouteTable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/route/RouteTable.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routeroutetable-method)
        """

_Route = Route

class RouteTable(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetable/index.html#EC2.RouteTable)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetable)
    """

    id: str
    associations: List[RouteTableAssociation]
    routes: List[Route]
    vpc: Vpc
    associations_attribute: List[RouteTableAssociationTypeDef]
    propagating_vgws: List[PropagatingVgwTypeDef]
    route_table_id: str
    routes_attribute: List[RouteTypeDef]
    tags: List[TagTypeDef]
    vpc_id: str
    owner_id: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this RouteTable.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetable/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetableget_available_subresources-method)
        """

    def associate_with_subnet(
        self, **kwargs: Unpack[AssociateRouteTableRequestRouteTableAssociateWithSubnetTypeDef]
    ) -> _RouteTableAssociation:
        """
        Associates a subnet in your VPC or an internet gateway or virtual private
        gateway attached to your VPC with a route table in your VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetable/associate_with_subnet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetableassociate_with_subnet-method)
        """

    def create_route(
        self, **kwargs: Unpack[CreateRouteRequestRouteTableCreateRouteTypeDef]
    ) -> _Route:
        """
        Creates a route in a route table within a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetable/create_route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetablecreate_route-method)
        """

    def create_tags(self, **kwargs: Unpack[RouteTableCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetable/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetablecreate_tags-method)
        """

    def delete(self, **kwargs: Unpack[DeleteRouteTableRequestRouteTableDeleteTypeDef]) -> None:
        """
        Deletes the specified route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetable/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetabledelete-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetable/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetableload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetable/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetablereload-method)
        """

_RouteTable = RouteTable

class RouteTableAssociation(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetableassociation/index.html#EC2.RouteTableAssociation)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetableassociation)
    """

    id: str
    route_table: RouteTable
    subnet: Subnet
    main: bool
    route_table_association_id: str
    route_table_id: str
    subnet_id: str
    gateway_id: str
    association_state: RouteTableAssociationStateTypeDef
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this
        RouteTableAssociation.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetableassociation/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetableassociationget_available_subresources-method)
        """

    def delete(
        self, **kwargs: Unpack[DisassociateRouteTableRequestRouteTableAssociationDeleteTypeDef]
    ) -> None:
        """
        Disassociates a subnet or gateway from a route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetableassociation/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetableassociationdelete-method)
        """

    def replace_subnet(
        self,
        **kwargs: Unpack[
            ReplaceRouteTableAssociationRequestRouteTableAssociationReplaceSubnetTypeDef
        ],
    ) -> _RouteTableAssociation:
        """
        Changes the route table associated with a given subnet, internet gateway, or
        virtual private gateway in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/routetableassociation/replace_subnet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#routetableassociationreplace_subnet-method)
        """

_RouteTableAssociation = RouteTableAssociation

class SecurityGroup(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/index.html#EC2.SecurityGroup)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygroup)
    """

    id: str
    group_id: str
    ip_permissions_egress: List[IpPermissionOutputTypeDef]
    tags: List[TagTypeDef]
    vpc_id: str
    security_group_arn: str
    owner_id: str
    group_name: str
    description: str
    ip_permissions: List[IpPermissionOutputTypeDef]
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this SecurityGroup.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygroupget_available_subresources-method)
        """

    def authorize_egress(
        self,
        **kwargs: Unpack[AuthorizeSecurityGroupEgressRequestSecurityGroupAuthorizeEgressTypeDef],
    ) -> AuthorizeSecurityGroupEgressResultTypeDef:
        """
        Adds the specified outbound (egress) rules to a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/authorize_egress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygroupauthorize_egress-method)
        """

    def authorize_ingress(
        self,
        **kwargs: Unpack[AuthorizeSecurityGroupIngressRequestSecurityGroupAuthorizeIngressTypeDef],
    ) -> AuthorizeSecurityGroupIngressResultTypeDef:
        """
        Adds the specified inbound (ingress) rules to a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/authorize_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygroupauthorize_ingress-method)
        """

    def create_tags(self, **kwargs: Unpack[SecurityGroupCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygroupcreate_tags-method)
        """

    def delete(
        self, **kwargs: Unpack[DeleteSecurityGroupRequestSecurityGroupDeleteTypeDef]
    ) -> DeleteSecurityGroupResultTypeDef:
        """
        Deletes a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygroupdelete-method)
        """

    def revoke_egress(
        self, **kwargs: Unpack[RevokeSecurityGroupEgressRequestSecurityGroupRevokeEgressTypeDef]
    ) -> RevokeSecurityGroupEgressResultTypeDef:
        """
        Removes the specified outbound (egress) rules from the specified security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/revoke_egress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygrouprevoke_egress-method)
        """

    def revoke_ingress(
        self, **kwargs: Unpack[RevokeSecurityGroupIngressRequestSecurityGroupRevokeIngressTypeDef]
    ) -> RevokeSecurityGroupIngressResultTypeDef:
        """
        Removes the specified inbound (ingress) rules from a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/revoke_ingress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygrouprevoke_ingress-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygroupload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/securitygroup/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#securitygroupreload-method)
        """

_SecurityGroup = SecurityGroup

class Snapshot(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/index.html#EC2.Snapshot)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshot)
    """

    id: str
    volume: Volume
    owner_alias: str
    outpost_arn: str
    tags: List[TagTypeDef]
    storage_tier: StorageTierType
    restore_expiry_time: datetime
    sse_type: SSETypeType
    availability_zone: str
    transfer_type: TransferTypeType
    completion_duration_minutes: int
    completion_time: datetime
    full_snapshot_size_in_bytes: int
    snapshot_id: str
    volume_id: str
    state: SnapshotStateType
    state_message: str
    start_time: datetime
    progress: str
    owner_id: str
    description: str
    volume_size: int
    encrypted: bool
    kms_key_id: str
    data_encryption_key_id: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotget_available_subresources-method)
        """

    def copy(
        self, **kwargs: Unpack[CopySnapshotRequestSnapshotCopyTypeDef]
    ) -> CopySnapshotResultTypeDef:
        """
        Copies a point-in-time snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/copy.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotcopy-method)
        """

    def create_tags(self, **kwargs: Unpack[SnapshotCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotcreate_tags-method)
        """

    def delete(self, **kwargs: Unpack[DeleteSnapshotRequestSnapshotDeleteTypeDef]) -> None:
        """
        Deletes the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotdelete-method)
        """

    def describe_attribute(
        self, **kwargs: Unpack[DescribeSnapshotAttributeRequestSnapshotDescribeAttributeTypeDef]
    ) -> DescribeSnapshotAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/describe_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotdescribe_attribute-method)
        """

    def modify_attribute(
        self, **kwargs: Unpack[ModifySnapshotAttributeRequestSnapshotModifyAttributeTypeDef]
    ) -> None:
        """
        Adds or removes permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/modify_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotmodify_attribute-method)
        """

    def reset_attribute(
        self, **kwargs: Unpack[ResetSnapshotAttributeRequestSnapshotResetAttributeTypeDef]
    ) -> None:
        """
        Resets permission settings for the specified snapshot.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/reset_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotreset_attribute-method)
        """

    def wait_until_completed(self) -> None:
        """
        Waits until Snapshot is completed.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/wait_until_completed.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotwait_until_completed-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/snapshot/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#snapshotreload-method)
        """

_Snapshot = Snapshot

class Subnet(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/index.html#EC2.Subnet)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnet)
    """

    id: str
    vpc: Vpc
    instances: SubnetInstancesCollection
    network_interfaces: SubnetNetworkInterfacesCollection
    availability_zone_id: str
    enable_lni_at_device_index: int
    map_customer_owned_ip_on_launch: bool
    customer_owned_ipv4_pool: str
    owner_id: str
    assign_ipv6_address_on_creation: bool
    ipv6_cidr_block_association_set: List[SubnetIpv6CidrBlockAssociationTypeDef]
    tags: List[TagTypeDef]
    subnet_arn: str
    outpost_arn: str
    enable_dns64: bool
    ipv6_native: bool
    private_dns_name_options_on_launch: PrivateDnsNameOptionsOnLaunchTypeDef
    block_public_access_states: BlockPublicAccessStatesTypeDef
    subnet_id: str
    state: SubnetStateType
    vpc_id: str
    cidr_block: str
    available_ip_address_count: int
    availability_zone: str
    default_for_az: bool
    map_public_ip_on_launch: bool
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetget_available_subresources-method)
        """

    def create_instances(
        self, **kwargs: Unpack[RunInstancesRequestSubnetCreateInstancesTypeDef]
    ) -> List[_Instance]:
        """
        Launches the specified number of instances using an AMI for which you have
        permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/create_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetcreate_instances-method)
        """

    def create_network_interface(
        self, **kwargs: Unpack[CreateNetworkInterfaceRequestSubnetCreateNetworkInterfaceTypeDef]
    ) -> _NetworkInterface:
        """
        Creates a network interface in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/create_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetcreate_network_interface-method)
        """

    def create_tags(self, **kwargs: Unpack[SubnetCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetcreate_tags-method)
        """

    def delete(self, **kwargs: Unpack[DeleteSubnetRequestSubnetDeleteTypeDef]) -> None:
        """
        Deletes the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetdelete-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/subnet/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#subnetreload-method)
        """

_Subnet = Subnet

class Tag(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/tag/index.html#EC2.Tag)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#tag)
    """

    resource_id: str
    key: str
    value: str
    resource_type: ResourceTypeType
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Tag.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/tag/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#tagget_available_subresources-method)
        """

    def delete(self, **kwargs: Unpack[DeleteTagsRequestTagDeleteTypeDef]) -> None:
        """
        Deletes the specified set of tags from the specified set of resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/tag/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#tagdelete-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/tag/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#tagload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/tag/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#tagreload-method)
        """

_Tag = Tag

class Volume(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/index.html#EC2.Volume)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volume)
    """

    id: str
    snapshots: VolumeSnapshotsCollection
    outpost_arn: str
    iops: int
    tags: List[TagTypeDef]
    volume_type: VolumeTypeType
    fast_restored: bool
    multi_attach_enabled: bool
    throughput: int
    sse_type: SSETypeType
    operator: OperatorResponseTypeDef
    volume_initialization_rate: int
    volume_id: str
    size: int
    snapshot_id: str
    availability_zone: str
    state: VolumeStateType
    create_time: datetime
    attachments: List[VolumeAttachmentTypeDef]
    encrypted: bool
    kms_key_id: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumeget_available_subresources-method)
        """

    def attach_to_instance(
        self, **kwargs: Unpack[AttachVolumeRequestVolumeAttachToInstanceTypeDef]
    ) -> VolumeAttachmentResponseTypeDef:
        """
        Attaches an EBS volume to a running or stopped instance and exposes it to the
        instance with the specified device name.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/attach_to_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumeattach_to_instance-method)
        """

    def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotRequestVolumeCreateSnapshotTypeDef]
    ) -> _Snapshot:
        """
        Creates a snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/create_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumecreate_snapshot-method)
        """

    def create_tags(self, **kwargs: Unpack[VolumeCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumecreate_tags-method)
        """

    def delete(self, **kwargs: Unpack[DeleteVolumeRequestVolumeDeleteTypeDef]) -> None:
        """
        Deletes the specified EBS volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumedelete-method)
        """

    def describe_attribute(
        self, **kwargs: Unpack[DescribeVolumeAttributeRequestVolumeDescribeAttributeTypeDef]
    ) -> DescribeVolumeAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified volume.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/describe_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumedescribe_attribute-method)
        """

    def describe_status(
        self, **kwargs: Unpack[DescribeVolumeStatusRequestVolumeDescribeStatusTypeDef]
    ) -> DescribeVolumeStatusResultTypeDef:
        """
        Describes the status of the specified volumes.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/describe_status.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumedescribe_status-method)
        """

    def detach_from_instance(
        self, **kwargs: Unpack[DetachVolumeRequestVolumeDetachFromInstanceTypeDef]
    ) -> VolumeAttachmentResponseTypeDef:
        """
        Detaches an EBS volume from an instance.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/detach_from_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumedetach_from_instance-method)
        """

    def enable_io(self, **kwargs: Unpack[EnableVolumeIORequestVolumeEnableIoTypeDef]) -> None:
        """
        Enables I/O operations for a volume that had I/O operations disabled because
        the data on the volume was potentially inconsistent.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/enable_io.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumeenable_io-method)
        """

    def modify_attribute(
        self, **kwargs: Unpack[ModifyVolumeAttributeRequestVolumeModifyAttributeTypeDef]
    ) -> None:
        """
        Modifies a volume attribute.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/modify_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumemodify_attribute-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumeload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/volume/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#volumereload-method)
        """

_Volume = Volume

class Vpc(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/index.html#EC2.Vpc)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpc)
    """

    id: str
    dhcp_options: DhcpOptions
    accepted_vpc_peering_connections: VpcAcceptedVpcPeeringConnectionsCollection
    instances: VpcInstancesCollection
    internet_gateways: VpcInternetGatewaysCollection
    network_acls: VpcNetworkAclsCollection
    network_interfaces: VpcNetworkInterfacesCollection
    requested_vpc_peering_connections: VpcRequestedVpcPeeringConnectionsCollection
    route_tables: VpcRouteTablesCollection
    security_groups: VpcSecurityGroupsCollection
    subnets: VpcSubnetsCollection
    owner_id: str
    instance_tenancy: TenancyType
    ipv6_cidr_block_association_set: List[VpcIpv6CidrBlockAssociationTypeDef]
    cidr_block_association_set: List[VpcCidrBlockAssociationTypeDef]
    is_default: bool
    encryption_control: VpcEncryptionControlTypeDef
    tags: List[TagTypeDef]
    block_public_access_states: BlockPublicAccessStatesTypeDef
    vpc_id: str
    state: VpcStateType
    cidr_block: str
    dhcp_options_id: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this Vpc.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcget_available_subresources-method)
        """

    def associate_dhcp_options(
        self, **kwargs: Unpack[AssociateDhcpOptionsRequestVpcAssociateDhcpOptionsTypeDef]
    ) -> None:
        """
        Associates a set of DHCP options (that you've previously created) with the
        specified VPC, or associates no DHCP options with the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/associate_dhcp_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcassociate_dhcp_options-method)
        """

    def attach_classic_link_instance(
        self, **kwargs: Unpack[AttachClassicLinkVpcRequestVpcAttachClassicLinkInstanceTypeDef]
    ) -> AttachClassicLinkVpcResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/attach_classic_link_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcattach_classic_link_instance-method)
        """

    def attach_internet_gateway(
        self, **kwargs: Unpack[AttachInternetGatewayRequestVpcAttachInternetGatewayTypeDef]
    ) -> None:
        """
        Attaches an internet gateway or a virtual private gateway to a VPC, enabling
        connectivity between the internet and the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/attach_internet_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcattach_internet_gateway-method)
        """

    def create_network_acl(
        self, **kwargs: Unpack[CreateNetworkAclRequestVpcCreateNetworkAclTypeDef]
    ) -> _NetworkAcl:
        """
        Creates a network ACL in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/create_network_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpccreate_network_acl-method)
        """

    def create_route_table(
        self, **kwargs: Unpack[CreateRouteTableRequestVpcCreateRouteTableTypeDef]
    ) -> _RouteTable:
        """
        Creates a route table for the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/create_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpccreate_route_table-method)
        """

    def create_security_group(
        self, **kwargs: Unpack[CreateSecurityGroupRequestVpcCreateSecurityGroupTypeDef]
    ) -> _SecurityGroup:
        """
        Creates a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/create_security_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpccreate_security_group-method)
        """

    def create_subnet(self, **kwargs: Unpack[CreateSubnetRequestVpcCreateSubnetTypeDef]) -> _Subnet:
        """
        Creates a subnet in the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/create_subnet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpccreate_subnet-method)
        """

    def create_tags(self, **kwargs: Unpack[VpcCreateTagsRequestTypeDef]) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpccreate_tags-method)
        """

    def delete(self, **kwargs: Unpack[DeleteVpcRequestVpcDeleteTypeDef]) -> None:
        """
        Deletes the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcdelete-method)
        """

    def describe_attribute(
        self, **kwargs: Unpack[DescribeVpcAttributeRequestVpcDescribeAttributeTypeDef]
    ) -> DescribeVpcAttributeResultTypeDef:
        """
        Describes the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/describe_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcdescribe_attribute-method)
        """

    def detach_classic_link_instance(
        self, **kwargs: Unpack[DetachClassicLinkVpcRequestVpcDetachClassicLinkInstanceTypeDef]
    ) -> DetachClassicLinkVpcResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/detach_classic_link_instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcdetach_classic_link_instance-method)
        """

    def detach_internet_gateway(
        self, **kwargs: Unpack[DetachInternetGatewayRequestVpcDetachInternetGatewayTypeDef]
    ) -> None:
        """
        Detaches an internet gateway from a VPC, disabling connectivity between the
        internet and the VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/detach_internet_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcdetach_internet_gateway-method)
        """

    def disable_classic_link(
        self, **kwargs: Unpack[DisableVpcClassicLinkRequestVpcDisableClassicLinkTypeDef]
    ) -> DisableVpcClassicLinkResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/disable_classic_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcdisable_classic_link-method)
        """

    def enable_classic_link(
        self, **kwargs: Unpack[EnableVpcClassicLinkRequestVpcEnableClassicLinkTypeDef]
    ) -> EnableVpcClassicLinkResultTypeDef:
        """
        This action is deprecated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/enable_classic_link.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcenable_classic_link-method)
        """

    def modify_attribute(
        self, **kwargs: Unpack[ModifyVpcAttributeRequestVpcModifyAttributeTypeDef]
    ) -> None:
        """
        Modifies the specified attribute of the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/modify_attribute.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcmodify_attribute-method)
        """

    def request_vpc_peering_connection(
        self,
        **kwargs: Unpack[CreateVpcPeeringConnectionRequestVpcRequestVpcPeeringConnectionTypeDef],
    ) -> _VpcPeeringConnection:
        """
        Requests a VPC peering connection between two VPCs: a requester VPC that you
        own and an accepter VPC with which to create the connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/request_vpc_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcrequest_vpc_peering_connection-method)
        """

    def wait_until_available(self) -> None:
        """
        Waits until Vpc is available.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/wait_until_available.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcwait_until_available-method)
        """

    def wait_until_exists(self) -> None:
        """
        Waits until Vpc is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/wait_until_exists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcwait_until_exists-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpc/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcreload-method)
        """

_Vpc = Vpc

class VpcPeeringConnection(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcpeeringconnection/index.html#EC2.VpcPeeringConnection)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcpeeringconnection)
    """

    id: str
    accepter_vpc: Vpc
    requester_vpc: Vpc
    accepter_vpc_info: VpcPeeringConnectionVpcInfoTypeDef
    expiration_time: datetime
    requester_vpc_info: VpcPeeringConnectionVpcInfoTypeDef
    status: VpcPeeringConnectionStateReasonTypeDef
    tags: List[TagTypeDef]
    vpc_peering_connection_id: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this VpcPeeringConnection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcpeeringconnection/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcpeeringconnectionget_available_subresources-method)
        """

    def accept(
        self, **kwargs: Unpack[AcceptVpcPeeringConnectionRequestVpcPeeringConnectionAcceptTypeDef]
    ) -> AcceptVpcPeeringConnectionResultTypeDef:
        """
        Accept a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcpeeringconnection/accept.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcpeeringconnectionaccept-method)
        """

    def delete(
        self, **kwargs: Unpack[DeleteVpcPeeringConnectionRequestVpcPeeringConnectionDeleteTypeDef]
    ) -> DeleteVpcPeeringConnectionResultTypeDef:
        """
        Deletes a VPC peering connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcpeeringconnection/delete.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcpeeringconnectiondelete-method)
        """

    def reject(
        self, **kwargs: Unpack[RejectVpcPeeringConnectionRequestVpcPeeringConnectionRejectTypeDef]
    ) -> RejectVpcPeeringConnectionResultTypeDef:
        """
        Rejects a VPC peering connection request.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcpeeringconnection/reject.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcpeeringconnectionreject-method)
        """

    def wait_until_exists(self) -> None:
        """
        Waits until VpcPeeringConnection is exists.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcpeeringconnection/wait_until_exists.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcpeeringconnectionwait_until_exists-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcpeeringconnection/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcpeeringconnectionload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcpeeringconnection/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcpeeringconnectionreload-method)
        """

_VpcPeeringConnection = VpcPeeringConnection

class VpcAddress(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcaddress/index.html#EC2.VpcAddress)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaddress)
    """

    allocation_id: str
    association: NetworkInterfaceAssociation
    association_id: str
    domain: DomainTypeType
    network_interface_id: str
    network_interface_owner_id: str
    private_ip_address: str
    tags: List[TagTypeDef]
    public_ipv4_pool: str
    network_border_group: str
    customer_owned_ip: str
    customer_owned_ipv4_pool: str
    carrier_ip: str
    service_managed: ServiceManagedType
    instance_id: str
    public_ip: str
    meta: EC2ResourceMeta  # type: ignore[override]

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this VpcAddress.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcaddress/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaddressget_available_subresources-method)
        """

    def associate(
        self, **kwargs: Unpack[AssociateAddressRequestVpcAddressAssociateTypeDef]
    ) -> AssociateAddressResultTypeDef:
        """
        Associates an Elastic IP address, or carrier IP address (for instances that are
        in subnets in Wavelength Zones) with an instance or a network interface.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcaddress/associate.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaddressassociate-method)
        """

    def release(self, **kwargs: Unpack[ReleaseAddressRequestVpcAddressReleaseTypeDef]) -> None:
        """
        Releases the specified Elastic IP address.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcaddress/release.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaddressrelease-method)
        """

    def load(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcaddress/load.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaddressload-method)
        """

    def reload(self) -> None:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/vpcaddress/reload.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#vpcaddressreload-method)
        """

_VpcAddress = VpcAddress

class EC2ResourceMeta(ResourceMeta):
    client: EC2Client  # type: ignore[override]

class EC2ServiceResource(ServiceResource):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/index.html)
    [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/)
    """

    meta: EC2ResourceMeta  # type: ignore[override]
    classic_addresses: ServiceResourceClassicAddressesCollection
    dhcp_options_sets: ServiceResourceDhcpOptionsSetsCollection
    images: ServiceResourceImagesCollection
    instances: ServiceResourceInstancesCollection
    internet_gateways: ServiceResourceInternetGatewaysCollection
    key_pairs: ServiceResourceKeyPairsCollection
    network_acls: ServiceResourceNetworkAclsCollection
    network_interfaces: ServiceResourceNetworkInterfacesCollection
    placement_groups: ServiceResourcePlacementGroupsCollection
    route_tables: ServiceResourceRouteTablesCollection
    security_groups: ServiceResourceSecurityGroupsCollection
    snapshots: ServiceResourceSnapshotsCollection
    subnets: ServiceResourceSubnetsCollection
    volumes: ServiceResourceVolumesCollection
    vpc_addresses: ServiceResourceVpcAddressesCollection
    vpc_peering_connections: ServiceResourceVpcPeeringConnectionsCollection
    vpcs: ServiceResourceVpcsCollection

    def get_available_subresources(self) -> Sequence[str]:
        """
        Returns a list of all the available sub-resources for this resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/get_available_subresources.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceget_available_subresources-method)
        """

    def create_dhcp_options(
        self, **kwargs: Unpack[CreateDhcpOptionsRequestServiceResourceCreateDhcpOptionsTypeDef]
    ) -> _DhcpOptions:
        """
        Creates a custom set of DHCP options.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_dhcp_options.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_dhcp_options-method)
        """

    def create_instances(
        self, **kwargs: Unpack[RunInstancesRequestServiceResourceCreateInstancesTypeDef]
    ) -> List[_Instance]:
        """
        Launches the specified number of instances using an AMI for which you have
        permissions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_instances.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_instances-method)
        """

    def create_internet_gateway(
        self,
        **kwargs: Unpack[CreateInternetGatewayRequestServiceResourceCreateInternetGatewayTypeDef],
    ) -> _InternetGateway:
        """
        Creates an internet gateway for use with a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_internet_gateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_internet_gateway-method)
        """

    def create_key_pair(
        self, **kwargs: Unpack[CreateKeyPairRequestServiceResourceCreateKeyPairTypeDef]
    ) -> _KeyPair:
        """
        Creates an ED25519 or 2048-bit RSA key pair with the specified name and in the
        specified format.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_key_pair-method)
        """

    def create_network_acl(
        self, **kwargs: Unpack[CreateNetworkAclRequestServiceResourceCreateNetworkAclTypeDef]
    ) -> _NetworkAcl:
        """
        Creates a network ACL in a VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_network_acl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_network_acl-method)
        """

    def create_network_interface(
        self,
        **kwargs: Unpack[CreateNetworkInterfaceRequestServiceResourceCreateNetworkInterfaceTypeDef],
    ) -> _NetworkInterface:
        """
        Creates a network interface in the specified subnet.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_network_interface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_network_interface-method)
        """

    def create_placement_group(
        self,
        **kwargs: Unpack[CreatePlacementGroupRequestServiceResourceCreatePlacementGroupTypeDef],
    ) -> _PlacementGroup:
        """
        Creates a placement group in which to launch instances.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_placement_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_placement_group-method)
        """

    def create_route_table(
        self, **kwargs: Unpack[CreateRouteTableRequestServiceResourceCreateRouteTableTypeDef]
    ) -> _RouteTable:
        """
        Creates a route table for the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_route_table-method)
        """

    def create_security_group(
        self, **kwargs: Unpack[CreateSecurityGroupRequestServiceResourceCreateSecurityGroupTypeDef]
    ) -> _SecurityGroup:
        """
        Creates a security group.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_security_group.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_security_group-method)
        """

    def create_snapshot(
        self, **kwargs: Unpack[CreateSnapshotRequestServiceResourceCreateSnapshotTypeDef]
    ) -> _Snapshot:
        """
        Creates a snapshot of an EBS volume and stores it in Amazon S3.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_snapshot-method)
        """

    def create_subnet(
        self, **kwargs: Unpack[CreateSubnetRequestServiceResourceCreateSubnetTypeDef]
    ) -> _Subnet:
        """
        Creates a subnet in the specified VPC.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_subnet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_subnet-method)
        """

    def create_tags(
        self, **kwargs: Unpack[CreateTagsRequestServiceResourceCreateTagsTypeDef]
    ) -> None:
        """
        Adds or overwrites only the specified tags for the specified Amazon EC2
        resource or resources.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_tags.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_tags-method)
        """

    def create_volume(
        self, **kwargs: Unpack[CreateVolumeRequestServiceResourceCreateVolumeTypeDef]
    ) -> _Volume:
        """
        Creates an EBS volume that can be attached to an instance in the same
        Availability Zone.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_volume-method)
        """

    def create_vpc(self, **kwargs: Unpack[CreateVpcRequestServiceResourceCreateVpcTypeDef]) -> _Vpc:
        """
        Creates a VPC with the specified CIDR blocks.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_vpc-method)
        """

    def create_vpc_peering_connection(
        self,
        **kwargs: Unpack[
            CreateVpcPeeringConnectionRequestServiceResourceCreateVpcPeeringConnectionTypeDef
        ],
    ) -> _VpcPeeringConnection:
        """
        Requests a VPC peering connection between two VPCs: a requester VPC that you
        own and an accepter VPC with which to create the connection.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/create_vpc_peering_connection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcecreate_vpc_peering_connection-method)
        """

    def disassociate_route_table(
        self,
        **kwargs: Unpack[DisassociateRouteTableRequestServiceResourceDisassociateRouteTableTypeDef],
    ) -> None:
        """
        Disassociates a subnet or gateway from a route table.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/disassociate_route_table.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcedisassociate_route_table-method)
        """

    def import_key_pair(
        self, **kwargs: Unpack[ImportKeyPairRequestServiceResourceImportKeyPairTypeDef]
    ) -> _KeyPairInfo:
        """
        Imports the public key from an RSA or ED25519 key pair that you created using a
        third-party tool.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/import_key_pair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceimport_key_pair-method)
        """

    def register_image(
        self, **kwargs: Unpack[RegisterImageRequestServiceResourceRegisterImageTypeDef]
    ) -> _Image:
        """
        Registers an AMI.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/register_image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceregister_image-method)
        """

    def ClassicAddress(self, public_ip: str) -> _ClassicAddress:
        """
        Creates a ClassicAddress resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/ClassicAddress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceclassicaddress-method)
        """

    def DhcpOptions(self, id: str) -> _DhcpOptions:
        """
        Creates a DhcpOptions resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/DhcpOptions.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcedhcpoptions-method)
        """

    def Image(self, id: str) -> _Image:
        """
        Creates a Image resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/Image.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceimage-method)
        """

    def Instance(self, id: str) -> _Instance:
        """
        Creates a Instance resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/Instance.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceinstance-method)
        """

    def InternetGateway(self, id: str) -> _InternetGateway:
        """
        Creates a InternetGateway resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/InternetGateway.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceinternetgateway-method)
        """

    def KeyPair(self, name: str) -> _KeyPair:
        """
        Creates a KeyPair resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/KeyPair.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcekeypair-method)
        """

    def NetworkAcl(self, id: str) -> _NetworkAcl:
        """
        Creates a NetworkAcl resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/NetworkAcl.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcenetworkacl-method)
        """

    def NetworkInterface(self, id: str) -> _NetworkInterface:
        """
        Creates a NetworkInterface resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/NetworkInterface.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcenetworkinterface-method)
        """

    def NetworkInterfaceAssociation(self, id: str) -> _NetworkInterfaceAssociation:
        """
        Creates a NetworkInterfaceAssociation resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/NetworkInterfaceAssociation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcenetworkinterfaceassociation-method)
        """

    def PlacementGroup(self, name: str) -> _PlacementGroup:
        """
        Creates a PlacementGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/PlacementGroup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceplacementgroup-method)
        """

    def Route(self, route_table_id: str, destination_cidr_block: str) -> _Route:
        """
        Creates a Route resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/Route.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceroute-method)
        """

    def RouteTable(self, id: str) -> _RouteTable:
        """
        Creates a RouteTable resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/RouteTable.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceroutetable-method)
        """

    def RouteTableAssociation(self, id: str) -> _RouteTableAssociation:
        """
        Creates a RouteTableAssociation resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/RouteTableAssociation.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourceroutetableassociation-method)
        """

    def SecurityGroup(self, id: str) -> _SecurityGroup:
        """
        Creates a SecurityGroup resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/SecurityGroup.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcesecuritygroup-method)
        """

    def Snapshot(self, id: str) -> _Snapshot:
        """
        Creates a Snapshot resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/Snapshot.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcesnapshot-method)
        """

    def Subnet(self, id: str) -> _Subnet:
        """
        Creates a Subnet resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/Subnet.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcesubnet-method)
        """

    def Tag(self, resource_id: str, key: str, value: str) -> _Tag:
        """
        Creates a Tag resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/Tag.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcetag-method)
        """

    def Volume(self, id: str) -> _Volume:
        """
        Creates a Volume resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/Volume.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcevolume-method)
        """

    def Vpc(self, id: str) -> _Vpc:
        """
        Creates a Vpc resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/Vpc.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcevpc-method)
        """

    def VpcPeeringConnection(self, id: str) -> _VpcPeeringConnection:
        """
        Creates a VpcPeeringConnection resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/VpcPeeringConnection.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcevpcpeeringconnection-method)
        """

    def VpcAddress(self, allocation_id: str) -> _VpcAddress:
        """
        Creates a VpcAddress resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/service-resource/VpcAddress.html)
        [Show boto3-stubs documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_ec2/service_resource/#ec2serviceresourcevpcaddress-method)
        """
