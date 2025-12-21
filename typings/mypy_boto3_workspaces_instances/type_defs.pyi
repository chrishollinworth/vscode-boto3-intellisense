"""
Type annotations for workspaces-instances service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_workspaces_instances/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_workspaces_instances.type_defs import AssociateVolumeRequestTypeDef

    data: AssociateVolumeRequestTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AmdSevSnpEnumType,
    AutoRecoveryEnumType,
    BandwidthWeightingEnumType,
    CapacityReservationPreferenceEnumType,
    CpuCreditsEnumType,
    DisassociateModeEnumType,
    HostnameTypeEnumType,
    HttpEndpointEnumType,
    HttpProtocolIpv6EnumType,
    HttpTokensEnumType,
    InstanceInterruptionBehaviorEnumType,
    InstanceMetadataTagsEnumType,
    InterfaceTypeEnumType,
    MarketTypeEnumType,
    ProvisionStateEnumType,
    ResourceTypeEnumType,
    SpotInstanceTypeEnumType,
    TenancyEnumType,
    VolumeTypeEnumType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import NotRequired, TypedDict
else:
    from typing_extensions import NotRequired, TypedDict

__all__ = (
    "AssociateVolumeRequestTypeDef",
    "BlockDeviceMappingRequestTypeDef",
    "CapacityReservationSpecificationTypeDef",
    "CapacityReservationTargetTypeDef",
    "ConnectionTrackingSpecificationRequestTypeDef",
    "CpuOptionsRequestTypeDef",
    "CreateVolumeRequestTypeDef",
    "CreateVolumeResponseTypeDef",
    "CreateWorkspaceInstanceRequestTypeDef",
    "CreateWorkspaceInstanceResponseTypeDef",
    "CreditSpecificationRequestTypeDef",
    "DeleteVolumeRequestTypeDef",
    "DeleteWorkspaceInstanceRequestTypeDef",
    "DisassociateVolumeRequestTypeDef",
    "EC2InstanceErrorTypeDef",
    "EC2ManagedInstanceTypeDef",
    "EbsBlockDeviceTypeDef",
    "EnaSrdSpecificationRequestTypeDef",
    "EnaSrdUdpSpecificationRequestTypeDef",
    "EnclaveOptionsRequestTypeDef",
    "GetWorkspaceInstanceRequestTypeDef",
    "GetWorkspaceInstanceResponseTypeDef",
    "HibernationOptionsRequestTypeDef",
    "IamInstanceProfileSpecificationTypeDef",
    "InstanceIpv6AddressTypeDef",
    "InstanceMaintenanceOptionsRequestTypeDef",
    "InstanceMarketOptionsRequestTypeDef",
    "InstanceMetadataOptionsRequestTypeDef",
    "InstanceNetworkInterfaceSpecificationTypeDef",
    "InstanceNetworkPerformanceOptionsRequestTypeDef",
    "InstanceTypeInfoTypeDef",
    "Ipv4PrefixSpecificationRequestTypeDef",
    "Ipv6PrefixSpecificationRequestTypeDef",
    "LicenseConfigurationRequestTypeDef",
    "ListInstanceTypesRequestPaginateTypeDef",
    "ListInstanceTypesRequestTypeDef",
    "ListInstanceTypesResponseTypeDef",
    "ListRegionsRequestPaginateTypeDef",
    "ListRegionsRequestTypeDef",
    "ListRegionsResponseTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ListWorkspaceInstancesRequestPaginateTypeDef",
    "ListWorkspaceInstancesRequestTypeDef",
    "ListWorkspaceInstancesResponseTypeDef",
    "ManagedInstanceRequestTypeDef",
    "PaginatorConfigTypeDef",
    "PlacementTypeDef",
    "PrivateDnsNameOptionsRequestTypeDef",
    "PrivateIpAddressSpecificationTypeDef",
    "RegionTypeDef",
    "ResponseMetadataTypeDef",
    "RunInstancesMonitoringEnabledTypeDef",
    "SpotMarketOptionsTypeDef",
    "TagResourceRequestTypeDef",
    "TagSpecificationTypeDef",
    "TagTypeDef",
    "TimestampTypeDef",
    "UntagResourceRequestTypeDef",
    "WorkspaceInstanceErrorTypeDef",
    "WorkspaceInstanceTypeDef",
)

class AssociateVolumeRequestTypeDef(TypedDict):
    WorkspaceInstanceId: str
    VolumeId: str
    Device: str

class EbsBlockDeviceTypeDef(TypedDict):
    VolumeType: NotRequired[VolumeTypeEnumType]
    Encrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    Iops: NotRequired[int]
    Throughput: NotRequired[int]
    VolumeSize: NotRequired[int]

class CapacityReservationTargetTypeDef(TypedDict):
    CapacityReservationId: NotRequired[str]
    CapacityReservationResourceGroupArn: NotRequired[str]

class ConnectionTrackingSpecificationRequestTypeDef(TypedDict):
    TcpEstablishedTimeout: NotRequired[int]
    UdpStreamTimeout: NotRequired[int]
    UdpTimeout: NotRequired[int]

class CpuOptionsRequestTypeDef(TypedDict):
    AmdSevSnp: NotRequired[AmdSevSnpEnumType]
    CoreCount: NotRequired[int]
    ThreadsPerCore: NotRequired[int]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: NotRequired[str]
    Value: NotRequired[str]

class CreditSpecificationRequestTypeDef(TypedDict):
    CpuCredits: NotRequired[CpuCreditsEnumType]

class DeleteVolumeRequestTypeDef(TypedDict):
    VolumeId: str

class DeleteWorkspaceInstanceRequestTypeDef(TypedDict):
    WorkspaceInstanceId: str

class DisassociateVolumeRequestTypeDef(TypedDict):
    WorkspaceInstanceId: str
    VolumeId: str
    Device: NotRequired[str]
    DisassociateMode: NotRequired[DisassociateModeEnumType]

class EC2InstanceErrorTypeDef(TypedDict):
    EC2ErrorCode: NotRequired[str]
    EC2ExceptionType: NotRequired[str]
    EC2ErrorMessage: NotRequired[str]

class EC2ManagedInstanceTypeDef(TypedDict):
    InstanceId: NotRequired[str]

class EnaSrdUdpSpecificationRequestTypeDef(TypedDict):
    EnaSrdUdpEnabled: NotRequired[bool]

class EnclaveOptionsRequestTypeDef(TypedDict):
    Enabled: NotRequired[bool]

class GetWorkspaceInstanceRequestTypeDef(TypedDict):
    WorkspaceInstanceId: str

class WorkspaceInstanceErrorTypeDef(TypedDict):
    ErrorCode: NotRequired[str]
    ErrorMessage: NotRequired[str]

class HibernationOptionsRequestTypeDef(TypedDict):
    Configured: NotRequired[bool]

class IamInstanceProfileSpecificationTypeDef(TypedDict):
    Arn: NotRequired[str]
    Name: NotRequired[str]

class InstanceIpv6AddressTypeDef(TypedDict):
    Ipv6Address: NotRequired[str]
    IsPrimaryIpv6: NotRequired[bool]

class InstanceMaintenanceOptionsRequestTypeDef(TypedDict):
    AutoRecovery: NotRequired[AutoRecoveryEnumType]

class InstanceMetadataOptionsRequestTypeDef(TypedDict):
    HttpEndpoint: NotRequired[HttpEndpointEnumType]
    HttpProtocolIpv6: NotRequired[HttpProtocolIpv6EnumType]
    HttpPutResponseHopLimit: NotRequired[int]
    HttpTokens: NotRequired[HttpTokensEnumType]
    InstanceMetadataTags: NotRequired[InstanceMetadataTagsEnumType]

class Ipv4PrefixSpecificationRequestTypeDef(TypedDict):
    Ipv4Prefix: NotRequired[str]

class Ipv6PrefixSpecificationRequestTypeDef(TypedDict):
    Ipv6Prefix: NotRequired[str]

class PrivateIpAddressSpecificationTypeDef(TypedDict):
    Primary: NotRequired[bool]
    PrivateIpAddress: NotRequired[str]

class InstanceNetworkPerformanceOptionsRequestTypeDef(TypedDict):
    BandwidthWeighting: NotRequired[BandwidthWeightingEnumType]

class InstanceTypeInfoTypeDef(TypedDict):
    InstanceType: NotRequired[str]

class LicenseConfigurationRequestTypeDef(TypedDict):
    LicenseConfigurationArn: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListInstanceTypesRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ListRegionsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class RegionTypeDef(TypedDict):
    RegionName: NotRequired[str]

class ListTagsForResourceRequestTypeDef(TypedDict):
    WorkspaceInstanceId: str

class ListWorkspaceInstancesRequestTypeDef(TypedDict):
    ProvisionStates: NotRequired[Sequence[ProvisionStateEnumType]]
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class PlacementTypeDef(TypedDict):
    Affinity: NotRequired[str]
    AvailabilityZone: NotRequired[str]
    GroupId: NotRequired[str]
    GroupName: NotRequired[str]
    HostId: NotRequired[str]
    HostResourceGroupArn: NotRequired[str]
    PartitionNumber: NotRequired[int]
    Tenancy: NotRequired[TenancyEnumType]

class PrivateDnsNameOptionsRequestTypeDef(TypedDict):
    HostnameType: NotRequired[HostnameTypeEnumType]
    EnableResourceNameDnsARecord: NotRequired[bool]
    EnableResourceNameDnsAAAARecord: NotRequired[bool]

class RunInstancesMonitoringEnabledTypeDef(TypedDict):
    Enabled: NotRequired[bool]

TimestampTypeDef = Union[datetime, str]

class UntagResourceRequestTypeDef(TypedDict):
    WorkspaceInstanceId: str
    TagKeys: Sequence[str]

class BlockDeviceMappingRequestTypeDef(TypedDict):
    DeviceName: NotRequired[str]
    Ebs: NotRequired[EbsBlockDeviceTypeDef]
    NoDevice: NotRequired[str]
    VirtualName: NotRequired[str]

class CapacityReservationSpecificationTypeDef(TypedDict):
    CapacityReservationPreference: NotRequired[CapacityReservationPreferenceEnumType]
    CapacityReservationTarget: NotRequired[CapacityReservationTargetTypeDef]

class CreateVolumeResponseTypeDef(TypedDict):
    VolumeId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateWorkspaceInstanceResponseTypeDef(TypedDict):
    WorkspaceInstanceId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class TagResourceRequestTypeDef(TypedDict):
    WorkspaceInstanceId: str
    Tags: Sequence[TagTypeDef]

class TagSpecificationTypeDef(TypedDict):
    ResourceType: NotRequired[ResourceTypeEnumType]
    Tags: NotRequired[Sequence[TagTypeDef]]

class WorkspaceInstanceTypeDef(TypedDict):
    ProvisionState: NotRequired[ProvisionStateEnumType]
    WorkspaceInstanceId: NotRequired[str]
    EC2ManagedInstance: NotRequired[EC2ManagedInstanceTypeDef]

class EnaSrdSpecificationRequestTypeDef(TypedDict):
    EnaSrdEnabled: NotRequired[bool]
    EnaSrdUdpSpecification: NotRequired[EnaSrdUdpSpecificationRequestTypeDef]

class GetWorkspaceInstanceResponseTypeDef(TypedDict):
    WorkspaceInstanceErrors: List[WorkspaceInstanceErrorTypeDef]
    EC2InstanceErrors: List[EC2InstanceErrorTypeDef]
    ProvisionState: ProvisionStateEnumType
    WorkspaceInstanceId: str
    EC2ManagedInstance: EC2ManagedInstanceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListInstanceTypesResponseTypeDef(TypedDict):
    InstanceTypes: List[InstanceTypeInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class ListInstanceTypesRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegionsRequestPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListWorkspaceInstancesRequestPaginateTypeDef(TypedDict):
    ProvisionStates: NotRequired[Sequence[ProvisionStateEnumType]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListRegionsResponseTypeDef(TypedDict):
    Regions: List[RegionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class SpotMarketOptionsTypeDef(TypedDict):
    BlockDurationMinutes: NotRequired[int]
    InstanceInterruptionBehavior: NotRequired[InstanceInterruptionBehaviorEnumType]
    MaxPrice: NotRequired[str]
    SpotInstanceType: NotRequired[SpotInstanceTypeEnumType]
    ValidUntilUtc: NotRequired[TimestampTypeDef]

class CreateVolumeRequestTypeDef(TypedDict):
    AvailabilityZone: str
    ClientToken: NotRequired[str]
    Encrypted: NotRequired[bool]
    Iops: NotRequired[int]
    KmsKeyId: NotRequired[str]
    SizeInGB: NotRequired[int]
    SnapshotId: NotRequired[str]
    TagSpecifications: NotRequired[Sequence[TagSpecificationTypeDef]]
    Throughput: NotRequired[int]
    VolumeType: NotRequired[VolumeTypeEnumType]

class ListWorkspaceInstancesResponseTypeDef(TypedDict):
    WorkspaceInstances: List[WorkspaceInstanceTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class InstanceNetworkInterfaceSpecificationTypeDef(TypedDict):
    AssociateCarrierIpAddress: NotRequired[bool]
    AssociatePublicIpAddress: NotRequired[bool]
    ConnectionTrackingSpecification: NotRequired[ConnectionTrackingSpecificationRequestTypeDef]
    Description: NotRequired[str]
    DeviceIndex: NotRequired[int]
    EnaSrdSpecification: NotRequired[EnaSrdSpecificationRequestTypeDef]
    InterfaceType: NotRequired[InterfaceTypeEnumType]
    Ipv4Prefixes: NotRequired[Sequence[Ipv4PrefixSpecificationRequestTypeDef]]
    Ipv4PrefixCount: NotRequired[int]
    Ipv6AddressCount: NotRequired[int]
    Ipv6Addresses: NotRequired[Sequence[InstanceIpv6AddressTypeDef]]
    Ipv6Prefixes: NotRequired[Sequence[Ipv6PrefixSpecificationRequestTypeDef]]
    Ipv6PrefixCount: NotRequired[int]
    NetworkCardIndex: NotRequired[int]
    NetworkInterfaceId: NotRequired[str]
    PrimaryIpv6: NotRequired[bool]
    PrivateIpAddress: NotRequired[str]
    PrivateIpAddresses: NotRequired[Sequence[PrivateIpAddressSpecificationTypeDef]]
    SecondaryPrivateIpAddressCount: NotRequired[int]
    Groups: NotRequired[Sequence[str]]
    SubnetId: NotRequired[str]

class InstanceMarketOptionsRequestTypeDef(TypedDict):
    MarketType: NotRequired[MarketTypeEnumType]
    SpotOptions: NotRequired[SpotMarketOptionsTypeDef]

class ManagedInstanceRequestTypeDef(TypedDict):
    BlockDeviceMappings: NotRequired[Sequence[BlockDeviceMappingRequestTypeDef]]
    CapacityReservationSpecification: NotRequired[CapacityReservationSpecificationTypeDef]
    CpuOptions: NotRequired[CpuOptionsRequestTypeDef]
    CreditSpecification: NotRequired[CreditSpecificationRequestTypeDef]
    DisableApiStop: NotRequired[bool]
    EbsOptimized: NotRequired[bool]
    EnablePrimaryIpv6: NotRequired[bool]
    EnclaveOptions: NotRequired[EnclaveOptionsRequestTypeDef]
    HibernationOptions: NotRequired[HibernationOptionsRequestTypeDef]
    IamInstanceProfile: NotRequired[IamInstanceProfileSpecificationTypeDef]
    ImageId: NotRequired[str]
    InstanceMarketOptions: NotRequired[InstanceMarketOptionsRequestTypeDef]
    InstanceType: NotRequired[str]
    Ipv6Addresses: NotRequired[Sequence[InstanceIpv6AddressTypeDef]]
    Ipv6AddressCount: NotRequired[int]
    KernelId: NotRequired[str]
    KeyName: NotRequired[str]
    LicenseSpecifications: NotRequired[Sequence[LicenseConfigurationRequestTypeDef]]
    MaintenanceOptions: NotRequired[InstanceMaintenanceOptionsRequestTypeDef]
    MetadataOptions: NotRequired[InstanceMetadataOptionsRequestTypeDef]
    Monitoring: NotRequired[RunInstancesMonitoringEnabledTypeDef]
    NetworkInterfaces: NotRequired[Sequence[InstanceNetworkInterfaceSpecificationTypeDef]]
    NetworkPerformanceOptions: NotRequired[InstanceNetworkPerformanceOptionsRequestTypeDef]
    Placement: NotRequired[PlacementTypeDef]
    PrivateDnsNameOptions: NotRequired[PrivateDnsNameOptionsRequestTypeDef]
    PrivateIpAddress: NotRequired[str]
    RamdiskId: NotRequired[str]
    SecurityGroupIds: NotRequired[Sequence[str]]
    SecurityGroups: NotRequired[Sequence[str]]
    SubnetId: NotRequired[str]
    TagSpecifications: NotRequired[Sequence[TagSpecificationTypeDef]]
    UserData: NotRequired[str]

class CreateWorkspaceInstanceRequestTypeDef(TypedDict):
    ManagedInstance: ManagedInstanceRequestTypeDef
    ClientToken: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]
