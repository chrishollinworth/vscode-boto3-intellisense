"""
Type annotations for odb service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_odb/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_odb.type_defs import AcceptMarketplaceRegistrationInputTypeDef

    data: AcceptMarketplaceRegistrationInputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    AccessType,
    ComputeModelType,
    DayOfWeekNameType,
    DbNodeResourceStatusType,
    DbServerPatchingStatusType,
    DiskRedundancyType,
    IamRoleStatusType,
    IormLifecycleStateType,
    LicenseModelType,
    ManagedResourceStatusType,
    MonthNameType,
    ObjectiveType,
    OciOnboardingStatusType,
    PatchingModeTypeType,
    PreferenceTypeType,
    ResourceStatusType,
    ShapeTypeType,
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
    "AcceptMarketplaceRegistrationInputTypeDef",
    "AssociateIamRoleToResourceInputTypeDef",
    "AutonomousVirtualMachineSummaryTypeDef",
    "CloudAutonomousVmClusterResourceDetailsTypeDef",
    "CloudAutonomousVmClusterSummaryTypeDef",
    "CloudAutonomousVmClusterTypeDef",
    "CloudExadataInfrastructureSummaryTypeDef",
    "CloudExadataInfrastructureTypeDef",
    "CloudExadataInfrastructureUnallocatedResourcesTypeDef",
    "CloudVmClusterSummaryTypeDef",
    "CloudVmClusterTypeDef",
    "CreateCloudAutonomousVmClusterInputTypeDef",
    "CreateCloudAutonomousVmClusterOutputTypeDef",
    "CreateCloudExadataInfrastructureInputTypeDef",
    "CreateCloudExadataInfrastructureOutputTypeDef",
    "CreateCloudVmClusterInputTypeDef",
    "CreateCloudVmClusterOutputTypeDef",
    "CreateOdbNetworkInputTypeDef",
    "CreateOdbNetworkOutputTypeDef",
    "CreateOdbPeeringConnectionInputTypeDef",
    "CreateOdbPeeringConnectionOutputTypeDef",
    "CrossRegionS3RestoreSourcesAccessTypeDef",
    "CustomerContactTypeDef",
    "DataCollectionOptionsTypeDef",
    "DayOfWeekTypeDef",
    "DbIormConfigTypeDef",
    "DbNodeSummaryTypeDef",
    "DbNodeTypeDef",
    "DbServerPatchingDetailsTypeDef",
    "DbServerSummaryTypeDef",
    "DbServerTypeDef",
    "DbSystemShapeSummaryTypeDef",
    "DeleteCloudAutonomousVmClusterInputTypeDef",
    "DeleteCloudExadataInfrastructureInputTypeDef",
    "DeleteCloudVmClusterInputTypeDef",
    "DeleteOdbNetworkInputTypeDef",
    "DeleteOdbPeeringConnectionInputTypeDef",
    "DisassociateIamRoleFromResourceInputTypeDef",
    "ExadataIormConfigTypeDef",
    "GetCloudAutonomousVmClusterInputTypeDef",
    "GetCloudAutonomousVmClusterOutputTypeDef",
    "GetCloudExadataInfrastructureInputTypeDef",
    "GetCloudExadataInfrastructureOutputTypeDef",
    "GetCloudExadataInfrastructureUnallocatedResourcesInputTypeDef",
    "GetCloudExadataInfrastructureUnallocatedResourcesOutputTypeDef",
    "GetCloudVmClusterInputTypeDef",
    "GetCloudVmClusterOutputTypeDef",
    "GetDbNodeInputTypeDef",
    "GetDbNodeOutputTypeDef",
    "GetDbServerInputTypeDef",
    "GetDbServerOutputTypeDef",
    "GetOciOnboardingStatusOutputTypeDef",
    "GetOdbNetworkInputTypeDef",
    "GetOdbNetworkOutputTypeDef",
    "GetOdbPeeringConnectionInputTypeDef",
    "GetOdbPeeringConnectionOutputTypeDef",
    "GiVersionSummaryTypeDef",
    "IamRoleTypeDef",
    "InitializeServiceInputTypeDef",
    "KmsAccessTypeDef",
    "ListAutonomousVirtualMachinesInputPaginateTypeDef",
    "ListAutonomousVirtualMachinesInputTypeDef",
    "ListAutonomousVirtualMachinesOutputTypeDef",
    "ListCloudAutonomousVmClustersInputPaginateTypeDef",
    "ListCloudAutonomousVmClustersInputTypeDef",
    "ListCloudAutonomousVmClustersOutputTypeDef",
    "ListCloudExadataInfrastructuresInputPaginateTypeDef",
    "ListCloudExadataInfrastructuresInputTypeDef",
    "ListCloudExadataInfrastructuresOutputTypeDef",
    "ListCloudVmClustersInputPaginateTypeDef",
    "ListCloudVmClustersInputTypeDef",
    "ListCloudVmClustersOutputTypeDef",
    "ListDbNodesInputPaginateTypeDef",
    "ListDbNodesInputTypeDef",
    "ListDbNodesOutputTypeDef",
    "ListDbServersInputPaginateTypeDef",
    "ListDbServersInputTypeDef",
    "ListDbServersOutputTypeDef",
    "ListDbSystemShapesInputPaginateTypeDef",
    "ListDbSystemShapesInputTypeDef",
    "ListDbSystemShapesOutputTypeDef",
    "ListGiVersionsInputPaginateTypeDef",
    "ListGiVersionsInputTypeDef",
    "ListGiVersionsOutputTypeDef",
    "ListOdbNetworksInputPaginateTypeDef",
    "ListOdbNetworksInputTypeDef",
    "ListOdbNetworksOutputTypeDef",
    "ListOdbPeeringConnectionsInputPaginateTypeDef",
    "ListOdbPeeringConnectionsInputTypeDef",
    "ListOdbPeeringConnectionsOutputTypeDef",
    "ListSystemVersionsInputPaginateTypeDef",
    "ListSystemVersionsInputTypeDef",
    "ListSystemVersionsOutputTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "MaintenanceWindowOutputTypeDef",
    "MaintenanceWindowTypeDef",
    "MaintenanceWindowUnionTypeDef",
    "ManagedS3BackupAccessTypeDef",
    "ManagedServicesTypeDef",
    "MonthTypeDef",
    "OciDnsForwardingConfigTypeDef",
    "OciIdentityDomainTypeDef",
    "OdbNetworkSummaryTypeDef",
    "OdbNetworkTypeDef",
    "OdbPeeringConnectionSummaryTypeDef",
    "OdbPeeringConnectionTypeDef",
    "PaginatorConfigTypeDef",
    "RebootDbNodeInputTypeDef",
    "RebootDbNodeOutputTypeDef",
    "ResponseMetadataTypeDef",
    "S3AccessTypeDef",
    "ServiceNetworkEndpointTypeDef",
    "StartDbNodeInputTypeDef",
    "StartDbNodeOutputTypeDef",
    "StopDbNodeInputTypeDef",
    "StopDbNodeOutputTypeDef",
    "StsAccessTypeDef",
    "SystemVersionSummaryTypeDef",
    "TagResourceRequestTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateCloudExadataInfrastructureInputTypeDef",
    "UpdateCloudExadataInfrastructureOutputTypeDef",
    "UpdateOdbNetworkInputTypeDef",
    "UpdateOdbNetworkOutputTypeDef",
    "UpdateOdbPeeringConnectionInputTypeDef",
    "UpdateOdbPeeringConnectionOutputTypeDef",
    "ZeroEtlAccessTypeDef",
)

class AcceptMarketplaceRegistrationInputTypeDef(TypedDict):
    marketplaceRegistrationToken: str

class AssociateIamRoleToResourceInputTypeDef(TypedDict):
    iamRoleArn: str
    awsIntegration: Literal["KmsTde"]
    resourceArn: str

class AutonomousVirtualMachineSummaryTypeDef(TypedDict):
    autonomousVirtualMachineId: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    vmName: NotRequired[str]
    dbServerId: NotRequired[str]
    dbServerDisplayName: NotRequired[str]
    cpuCoreCount: NotRequired[int]
    memorySizeInGBs: NotRequired[int]
    dbNodeStorageSizeInGBs: NotRequired[int]
    clientIpAddress: NotRequired[str]
    cloudAutonomousVmClusterId: NotRequired[str]
    ocid: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]

class CloudAutonomousVmClusterResourceDetailsTypeDef(TypedDict):
    cloudAutonomousVmClusterId: NotRequired[str]
    unallocatedAdbStorageInTBs: NotRequired[float]

class CustomerContactTypeDef(TypedDict):
    email: NotRequired[str]

class DataCollectionOptionsTypeDef(TypedDict):
    isDiagnosticsEventsEnabled: NotRequired[bool]
    isHealthMonitoringEnabled: NotRequired[bool]
    isIncidentLogsEnabled: NotRequired[bool]

class IamRoleTypeDef(TypedDict):
    iamRoleArn: NotRequired[str]
    status: NotRequired[IamRoleStatusType]
    statusReason: NotRequired[str]
    awsIntegration: NotRequired[Literal["KmsTde"]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class CreateOdbNetworkInputTypeDef(TypedDict):
    displayName: str
    clientSubnetCidr: str
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]
    backupSubnetCidr: NotRequired[str]
    customDomainName: NotRequired[str]
    defaultDnsPrefix: NotRequired[str]
    clientToken: NotRequired[str]
    s3Access: NotRequired[AccessType]
    zeroEtlAccess: NotRequired[AccessType]
    stsAccess: NotRequired[AccessType]
    kmsAccess: NotRequired[AccessType]
    s3PolicyDocument: NotRequired[str]
    stsPolicyDocument: NotRequired[str]
    kmsPolicyDocument: NotRequired[str]
    crossRegionS3RestoreSourcesToEnable: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]

class CreateOdbPeeringConnectionInputTypeDef(TypedDict):
    odbNetworkId: str
    peerNetworkId: str
    displayName: NotRequired[str]
    peerNetworkCidrsToBeAdded: NotRequired[Sequence[str]]
    clientToken: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]

class CrossRegionS3RestoreSourcesAccessTypeDef(TypedDict):
    region: NotRequired[str]
    ipv4Addresses: NotRequired[List[str]]
    status: NotRequired[ManagedResourceStatusType]

class DayOfWeekTypeDef(TypedDict):
    name: NotRequired[DayOfWeekNameType]

class DbIormConfigTypeDef(TypedDict):
    dbName: NotRequired[str]
    flashCacheLimit: NotRequired[str]
    share: NotRequired[int]

class DbNodeSummaryTypeDef(TypedDict):
    dbNodeId: NotRequired[str]
    dbNodeArn: NotRequired[str]
    status: NotRequired[DbNodeResourceStatusType]
    statusReason: NotRequired[str]
    additionalDetails: NotRequired[str]
    backupIpId: NotRequired[str]
    backupVnic2Id: NotRequired[str]
    backupVnicId: NotRequired[str]
    cpuCoreCount: NotRequired[int]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServerId: NotRequired[str]
    dbSystemId: NotRequired[str]
    faultDomain: NotRequired[str]
    hostIpId: NotRequired[str]
    hostname: NotRequired[str]
    ocid: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    maintenanceType: NotRequired[Literal["VMDB_REBOOT_MIGRATION"]]
    memorySizeInGBs: NotRequired[int]
    softwareStorageSizeInGB: NotRequired[int]
    createdAt: NotRequired[datetime]
    timeMaintenanceWindowEnd: NotRequired[str]
    timeMaintenanceWindowStart: NotRequired[str]
    totalCpuCoreCount: NotRequired[int]
    vnic2Id: NotRequired[str]
    vnicId: NotRequired[str]

class DbNodeTypeDef(TypedDict):
    dbNodeId: NotRequired[str]
    dbNodeArn: NotRequired[str]
    status: NotRequired[DbNodeResourceStatusType]
    statusReason: NotRequired[str]
    additionalDetails: NotRequired[str]
    backupIpId: NotRequired[str]
    backupVnic2Id: NotRequired[str]
    backupVnicId: NotRequired[str]
    cpuCoreCount: NotRequired[int]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServerId: NotRequired[str]
    dbSystemId: NotRequired[str]
    faultDomain: NotRequired[str]
    hostIpId: NotRequired[str]
    hostname: NotRequired[str]
    ocid: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    maintenanceType: NotRequired[Literal["VMDB_REBOOT_MIGRATION"]]
    memorySizeInGBs: NotRequired[int]
    softwareStorageSizeInGB: NotRequired[int]
    createdAt: NotRequired[datetime]
    timeMaintenanceWindowEnd: NotRequired[str]
    timeMaintenanceWindowStart: NotRequired[str]
    totalCpuCoreCount: NotRequired[int]
    vnic2Id: NotRequired[str]
    vnicId: NotRequired[str]
    privateIpAddress: NotRequired[str]
    floatingIpAddress: NotRequired[str]

class DbServerPatchingDetailsTypeDef(TypedDict):
    estimatedPatchDuration: NotRequired[int]
    patchingStatus: NotRequired[DbServerPatchingStatusType]
    timePatchingEnded: NotRequired[str]
    timePatchingStarted: NotRequired[str]

class DbSystemShapeSummaryTypeDef(TypedDict):
    availableCoreCount: NotRequired[int]
    availableCoreCountPerNode: NotRequired[int]
    availableDataStorageInTBs: NotRequired[int]
    availableDataStoragePerServerInTBs: NotRequired[int]
    availableDbNodePerNodeInGBs: NotRequired[int]
    availableDbNodeStorageInGBs: NotRequired[int]
    availableMemoryInGBs: NotRequired[int]
    availableMemoryPerNodeInGBs: NotRequired[int]
    coreCountIncrement: NotRequired[int]
    maxStorageCount: NotRequired[int]
    maximumNodeCount: NotRequired[int]
    minCoreCountPerNode: NotRequired[int]
    minDataStorageInTBs: NotRequired[int]
    minDbNodeStoragePerNodeInGBs: NotRequired[int]
    minMemoryPerNodeInGBs: NotRequired[int]
    minStorageCount: NotRequired[int]
    minimumCoreCount: NotRequired[int]
    minimumNodeCount: NotRequired[int]
    runtimeMinimumCoreCount: NotRequired[int]
    shapeFamily: NotRequired[str]
    shapeType: NotRequired[ShapeTypeType]
    name: NotRequired[str]
    computeModel: NotRequired[ComputeModelType]
    areServerTypesSupported: NotRequired[bool]

class DeleteCloudAutonomousVmClusterInputTypeDef(TypedDict):
    cloudAutonomousVmClusterId: str

class DeleteCloudExadataInfrastructureInputTypeDef(TypedDict):
    cloudExadataInfrastructureId: str

class DeleteCloudVmClusterInputTypeDef(TypedDict):
    cloudVmClusterId: str

class DeleteOdbNetworkInputTypeDef(TypedDict):
    odbNetworkId: str
    deleteAssociatedResources: bool

class DeleteOdbPeeringConnectionInputTypeDef(TypedDict):
    odbPeeringConnectionId: str

class DisassociateIamRoleFromResourceInputTypeDef(TypedDict):
    iamRoleArn: str
    awsIntegration: Literal["KmsTde"]
    resourceArn: str

class GetCloudAutonomousVmClusterInputTypeDef(TypedDict):
    cloudAutonomousVmClusterId: str

class GetCloudExadataInfrastructureInputTypeDef(TypedDict):
    cloudExadataInfrastructureId: str

class GetCloudExadataInfrastructureUnallocatedResourcesInputTypeDef(TypedDict):
    cloudExadataInfrastructureId: str
    dbServers: NotRequired[Sequence[str]]

class GetCloudVmClusterInputTypeDef(TypedDict):
    cloudVmClusterId: str

class GetDbNodeInputTypeDef(TypedDict):
    cloudVmClusterId: str
    dbNodeId: str

class GetDbServerInputTypeDef(TypedDict):
    cloudExadataInfrastructureId: str
    dbServerId: str

class OciIdentityDomainTypeDef(TypedDict):
    ociIdentityDomainId: NotRequired[str]
    ociIdentityDomainResourceUrl: NotRequired[str]
    ociIdentityDomainUrl: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    accountSetupCloudFormationUrl: NotRequired[str]

class GetOdbNetworkInputTypeDef(TypedDict):
    odbNetworkId: str

class GetOdbPeeringConnectionInputTypeDef(TypedDict):
    odbPeeringConnectionId: str

class OdbPeeringConnectionTypeDef(TypedDict):
    odbPeeringConnectionId: str
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    odbPeeringConnectionArn: NotRequired[str]
    odbNetworkArn: NotRequired[str]
    peerNetworkArn: NotRequired[str]
    odbPeeringConnectionType: NotRequired[str]
    peerNetworkCidrs: NotRequired[List[str]]
    createdAt: NotRequired[datetime]
    percentProgress: NotRequired[float]

class GiVersionSummaryTypeDef(TypedDict):
    version: NotRequired[str]

class InitializeServiceInputTypeDef(TypedDict):
    ociIdentityDomain: NotRequired[bool]

class KmsAccessTypeDef(TypedDict):
    status: NotRequired[ManagedResourceStatusType]
    ipv4Addresses: NotRequired[List[str]]
    domainName: NotRequired[str]
    kmsPolicyDocument: NotRequired[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class ListAutonomousVirtualMachinesInputTypeDef(TypedDict):
    cloudAutonomousVmClusterId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListCloudAutonomousVmClustersInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    cloudExadataInfrastructureId: NotRequired[str]

class ListCloudExadataInfrastructuresInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListCloudVmClustersInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    cloudExadataInfrastructureId: NotRequired[str]

class ListDbNodesInputTypeDef(TypedDict):
    cloudVmClusterId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDbServersInputTypeDef(TypedDict):
    cloudExadataInfrastructureId: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListDbSystemShapesInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]

class ListGiVersionsInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    shape: NotRequired[str]

class ListOdbNetworksInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class ListOdbPeeringConnectionsInputTypeDef(TypedDict):
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]
    odbNetworkId: NotRequired[str]

class OdbPeeringConnectionSummaryTypeDef(TypedDict):
    odbPeeringConnectionId: str
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    odbPeeringConnectionArn: NotRequired[str]
    odbNetworkArn: NotRequired[str]
    peerNetworkArn: NotRequired[str]
    odbPeeringConnectionType: NotRequired[str]
    peerNetworkCidrs: NotRequired[List[str]]
    createdAt: NotRequired[datetime]
    percentProgress: NotRequired[float]

class ListSystemVersionsInputTypeDef(TypedDict):
    giVersion: str
    shape: str
    maxResults: NotRequired[int]
    nextToken: NotRequired[str]

class SystemVersionSummaryTypeDef(TypedDict):
    giVersion: NotRequired[str]
    shape: NotRequired[str]
    systemVersions: NotRequired[List[str]]

class ListTagsForResourceRequestTypeDef(TypedDict):
    resourceArn: str

class MonthTypeDef(TypedDict):
    name: NotRequired[MonthNameType]

class ManagedS3BackupAccessTypeDef(TypedDict):
    status: NotRequired[ManagedResourceStatusType]
    ipv4Addresses: NotRequired[List[str]]

class S3AccessTypeDef(TypedDict):
    status: NotRequired[ManagedResourceStatusType]
    ipv4Addresses: NotRequired[List[str]]
    domainName: NotRequired[str]
    s3PolicyDocument: NotRequired[str]

class ServiceNetworkEndpointTypeDef(TypedDict):
    vpcEndpointId: NotRequired[str]
    vpcEndpointType: NotRequired[Literal["SERVICENETWORK"]]

class StsAccessTypeDef(TypedDict):
    status: NotRequired[ManagedResourceStatusType]
    ipv4Addresses: NotRequired[List[str]]
    domainName: NotRequired[str]
    stsPolicyDocument: NotRequired[str]

class ZeroEtlAccessTypeDef(TypedDict):
    status: NotRequired[ManagedResourceStatusType]
    cidr: NotRequired[str]

class OciDnsForwardingConfigTypeDef(TypedDict):
    domainName: NotRequired[str]
    ociDnsListenerIp: NotRequired[str]

class RebootDbNodeInputTypeDef(TypedDict):
    cloudVmClusterId: str
    dbNodeId: str

class StartDbNodeInputTypeDef(TypedDict):
    cloudVmClusterId: str
    dbNodeId: str

class StopDbNodeInputTypeDef(TypedDict):
    cloudVmClusterId: str
    dbNodeId: str

class TagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tags: Mapping[str, str]

class UntagResourceRequestTypeDef(TypedDict):
    resourceArn: str
    tagKeys: Sequence[str]

class UpdateOdbNetworkInputTypeDef(TypedDict):
    odbNetworkId: str
    displayName: NotRequired[str]
    peeredCidrsToBeAdded: NotRequired[Sequence[str]]
    peeredCidrsToBeRemoved: NotRequired[Sequence[str]]
    s3Access: NotRequired[AccessType]
    zeroEtlAccess: NotRequired[AccessType]
    stsAccess: NotRequired[AccessType]
    kmsAccess: NotRequired[AccessType]
    s3PolicyDocument: NotRequired[str]
    stsPolicyDocument: NotRequired[str]
    kmsPolicyDocument: NotRequired[str]
    crossRegionS3RestoreSourcesToEnable: NotRequired[Sequence[str]]
    crossRegionS3RestoreSourcesToDisable: NotRequired[Sequence[str]]

class UpdateOdbPeeringConnectionInputTypeDef(TypedDict):
    odbPeeringConnectionId: str
    displayName: NotRequired[str]
    peerNetworkCidrsToBeAdded: NotRequired[Sequence[str]]
    peerNetworkCidrsToBeRemoved: NotRequired[Sequence[str]]

class CloudExadataInfrastructureUnallocatedResourcesTypeDef(TypedDict):
    cloudAutonomousVmClusters: NotRequired[List[CloudAutonomousVmClusterResourceDetailsTypeDef]]
    cloudExadataInfrastructureDisplayName: NotRequired[str]
    exadataStorageInTBs: NotRequired[float]
    cloudExadataInfrastructureId: NotRequired[str]
    localStorageInGBs: NotRequired[int]
    memoryInGBs: NotRequired[int]
    ocpus: NotRequired[int]

class CreateCloudVmClusterInputTypeDef(TypedDict):
    cloudExadataInfrastructureId: str
    cpuCoreCount: int
    displayName: str
    giVersion: str
    hostname: str
    sshPublicKeys: Sequence[str]
    odbNetworkId: str
    clusterName: NotRequired[str]
    dataCollectionOptions: NotRequired[DataCollectionOptionsTypeDef]
    dataStorageSizeInTBs: NotRequired[float]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServers: NotRequired[Sequence[str]]
    tags: NotRequired[Mapping[str, str]]
    isLocalBackupEnabled: NotRequired[bool]
    isSparseDiskgroupEnabled: NotRequired[bool]
    licenseModel: NotRequired[LicenseModelType]
    memorySizeInGBs: NotRequired[int]
    systemVersion: NotRequired[str]
    timeZone: NotRequired[str]
    clientToken: NotRequired[str]
    scanListenerPortTcp: NotRequired[int]

class CreateCloudAutonomousVmClusterOutputTypeDef(TypedDict):
    displayName: str
    status: ResourceStatusType
    statusReason: str
    cloudAutonomousVmClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudExadataInfrastructureOutputTypeDef(TypedDict):
    displayName: str
    status: ResourceStatusType
    statusReason: str
    cloudExadataInfrastructureId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudVmClusterOutputTypeDef(TypedDict):
    displayName: str
    status: ResourceStatusType
    statusReason: str
    cloudVmClusterId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOdbNetworkOutputTypeDef(TypedDict):
    displayName: str
    status: ResourceStatusType
    statusReason: str
    odbNetworkId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateOdbPeeringConnectionOutputTypeDef(TypedDict):
    displayName: str
    status: ResourceStatusType
    statusReason: str
    odbPeeringConnectionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutonomousVirtualMachinesOutputTypeDef(TypedDict):
    autonomousVirtualMachines: List[AutonomousVirtualMachineSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListTagsForResourceResponseTypeDef(TypedDict):
    tags: Dict[str, str]
    ResponseMetadata: ResponseMetadataTypeDef

class RebootDbNodeOutputTypeDef(TypedDict):
    dbNodeId: str
    status: DbNodeResourceStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartDbNodeOutputTypeDef(TypedDict):
    dbNodeId: str
    status: DbNodeResourceStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class StopDbNodeOutputTypeDef(TypedDict):
    dbNodeId: str
    status: DbNodeResourceStatusType
    statusReason: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateCloudExadataInfrastructureOutputTypeDef(TypedDict):
    displayName: str
    status: ResourceStatusType
    statusReason: str
    cloudExadataInfrastructureId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOdbNetworkOutputTypeDef(TypedDict):
    displayName: str
    status: ResourceStatusType
    statusReason: str
    odbNetworkId: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateOdbPeeringConnectionOutputTypeDef(TypedDict):
    displayName: str
    status: ResourceStatusType
    statusReason: str
    odbPeeringConnectionId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ExadataIormConfigTypeDef(TypedDict):
    dbPlans: NotRequired[List[DbIormConfigTypeDef]]
    lifecycleDetails: NotRequired[str]
    lifecycleState: NotRequired[IormLifecycleStateType]
    objective: NotRequired[ObjectiveType]

class ListDbNodesOutputTypeDef(TypedDict):
    dbNodes: List[DbNodeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetDbNodeOutputTypeDef(TypedDict):
    dbNode: DbNodeTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DbServerSummaryTypeDef(TypedDict):
    dbServerId: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    cpuCoreCount: NotRequired[int]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServerPatchingDetails: NotRequired[DbServerPatchingDetailsTypeDef]
    displayName: NotRequired[str]
    exadataInfrastructureId: NotRequired[str]
    ocid: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    maxCpuCount: NotRequired[int]
    maxDbNodeStorageInGBs: NotRequired[int]
    maxMemoryInGBs: NotRequired[int]
    memorySizeInGBs: NotRequired[int]
    shape: NotRequired[str]
    createdAt: NotRequired[datetime]
    vmClusterIds: NotRequired[List[str]]
    computeModel: NotRequired[ComputeModelType]
    autonomousVmClusterIds: NotRequired[List[str]]
    autonomousVirtualMachineIds: NotRequired[List[str]]

class DbServerTypeDef(TypedDict):
    dbServerId: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    cpuCoreCount: NotRequired[int]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServerPatchingDetails: NotRequired[DbServerPatchingDetailsTypeDef]
    displayName: NotRequired[str]
    exadataInfrastructureId: NotRequired[str]
    ocid: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    maxCpuCount: NotRequired[int]
    maxDbNodeStorageInGBs: NotRequired[int]
    maxMemoryInGBs: NotRequired[int]
    memorySizeInGBs: NotRequired[int]
    shape: NotRequired[str]
    createdAt: NotRequired[datetime]
    vmClusterIds: NotRequired[List[str]]
    computeModel: NotRequired[ComputeModelType]
    autonomousVmClusterIds: NotRequired[List[str]]
    autonomousVirtualMachineIds: NotRequired[List[str]]

class ListDbSystemShapesOutputTypeDef(TypedDict):
    dbSystemShapes: List[DbSystemShapeSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetOciOnboardingStatusOutputTypeDef(TypedDict):
    status: OciOnboardingStatusType
    existingTenancyActivationLink: str
    newTenancyActivationLink: str
    ociIdentityDomain: OciIdentityDomainTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class GetOdbPeeringConnectionOutputTypeDef(TypedDict):
    odbPeeringConnection: OdbPeeringConnectionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListGiVersionsOutputTypeDef(TypedDict):
    giVersions: List[GiVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListAutonomousVirtualMachinesInputPaginateTypeDef(TypedDict):
    cloudAutonomousVmClusterId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCloudAutonomousVmClustersInputPaginateTypeDef(TypedDict):
    cloudExadataInfrastructureId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCloudExadataInfrastructuresInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCloudVmClustersInputPaginateTypeDef(TypedDict):
    cloudExadataInfrastructureId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDbNodesInputPaginateTypeDef(TypedDict):
    cloudVmClusterId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDbServersInputPaginateTypeDef(TypedDict):
    cloudExadataInfrastructureId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListDbSystemShapesInputPaginateTypeDef(TypedDict):
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGiVersionsInputPaginateTypeDef(TypedDict):
    shape: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOdbNetworksInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOdbPeeringConnectionsInputPaginateTypeDef(TypedDict):
    odbNetworkId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListSystemVersionsInputPaginateTypeDef(TypedDict):
    giVersion: str
    shape: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListOdbPeeringConnectionsOutputTypeDef(TypedDict):
    odbPeeringConnections: List[OdbPeeringConnectionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class ListSystemVersionsOutputTypeDef(TypedDict):
    systemVersions: List[SystemVersionSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class MaintenanceWindowOutputTypeDef(TypedDict):
    customActionTimeoutInMins: NotRequired[int]
    daysOfWeek: NotRequired[List[DayOfWeekTypeDef]]
    hoursOfDay: NotRequired[List[int]]
    isCustomActionTimeoutEnabled: NotRequired[bool]
    leadTimeInWeeks: NotRequired[int]
    months: NotRequired[List[MonthTypeDef]]
    patchingMode: NotRequired[PatchingModeTypeType]
    preference: NotRequired[PreferenceTypeType]
    skipRu: NotRequired[bool]
    weeksOfMonth: NotRequired[List[int]]

class MaintenanceWindowTypeDef(TypedDict):
    customActionTimeoutInMins: NotRequired[int]
    daysOfWeek: NotRequired[Sequence[DayOfWeekTypeDef]]
    hoursOfDay: NotRequired[Sequence[int]]
    isCustomActionTimeoutEnabled: NotRequired[bool]
    leadTimeInWeeks: NotRequired[int]
    months: NotRequired[Sequence[MonthTypeDef]]
    patchingMode: NotRequired[PatchingModeTypeType]
    preference: NotRequired[PreferenceTypeType]
    skipRu: NotRequired[bool]
    weeksOfMonth: NotRequired[Sequence[int]]

class ManagedServicesTypeDef(TypedDict):
    serviceNetworkArn: NotRequired[str]
    resourceGatewayArn: NotRequired[str]
    managedServicesIpv4Cidrs: NotRequired[List[str]]
    serviceNetworkEndpoint: NotRequired[ServiceNetworkEndpointTypeDef]
    managedS3BackupAccess: NotRequired[ManagedS3BackupAccessTypeDef]
    zeroEtlAccess: NotRequired[ZeroEtlAccessTypeDef]
    s3Access: NotRequired[S3AccessTypeDef]
    stsAccess: NotRequired[StsAccessTypeDef]
    kmsAccess: NotRequired[KmsAccessTypeDef]
    crossRegionS3RestoreSourcesAccess: NotRequired[List[CrossRegionS3RestoreSourcesAccessTypeDef]]

class GetCloudExadataInfrastructureUnallocatedResourcesOutputTypeDef(TypedDict):
    cloudExadataInfrastructureUnallocatedResources: (
        CloudExadataInfrastructureUnallocatedResourcesTypeDef
    )
    ResponseMetadata: ResponseMetadataTypeDef

class CloudVmClusterSummaryTypeDef(TypedDict):
    cloudVmClusterId: str
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    cloudVmClusterArn: NotRequired[str]
    cloudExadataInfrastructureId: NotRequired[str]
    cloudExadataInfrastructureArn: NotRequired[str]
    clusterName: NotRequired[str]
    cpuCoreCount: NotRequired[int]
    dataCollectionOptions: NotRequired[DataCollectionOptionsTypeDef]
    dataStorageSizeInTBs: NotRequired[float]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServers: NotRequired[List[str]]
    diskRedundancy: NotRequired[DiskRedundancyType]
    giVersion: NotRequired[str]
    hostname: NotRequired[str]
    iormConfigCache: NotRequired[ExadataIormConfigTypeDef]
    isLocalBackupEnabled: NotRequired[bool]
    isSparseDiskgroupEnabled: NotRequired[bool]
    lastUpdateHistoryEntryId: NotRequired[str]
    licenseModel: NotRequired[LicenseModelType]
    listenerPort: NotRequired[int]
    memorySizeInGBs: NotRequired[int]
    nodeCount: NotRequired[int]
    ocid: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    ociUrl: NotRequired[str]
    domain: NotRequired[str]
    scanDnsName: NotRequired[str]
    scanDnsRecordId: NotRequired[str]
    scanIpIds: NotRequired[List[str]]
    shape: NotRequired[str]
    sshPublicKeys: NotRequired[List[str]]
    storageSizeInGBs: NotRequired[int]
    systemVersion: NotRequired[str]
    createdAt: NotRequired[datetime]
    timeZone: NotRequired[str]
    vipIds: NotRequired[List[str]]
    odbNetworkId: NotRequired[str]
    odbNetworkArn: NotRequired[str]
    percentProgress: NotRequired[float]
    computeModel: NotRequired[ComputeModelType]
    iamRoles: NotRequired[List[IamRoleTypeDef]]

class CloudVmClusterTypeDef(TypedDict):
    cloudVmClusterId: str
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    cloudVmClusterArn: NotRequired[str]
    cloudExadataInfrastructureId: NotRequired[str]
    cloudExadataInfrastructureArn: NotRequired[str]
    clusterName: NotRequired[str]
    cpuCoreCount: NotRequired[int]
    dataCollectionOptions: NotRequired[DataCollectionOptionsTypeDef]
    dataStorageSizeInTBs: NotRequired[float]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServers: NotRequired[List[str]]
    diskRedundancy: NotRequired[DiskRedundancyType]
    giVersion: NotRequired[str]
    hostname: NotRequired[str]
    iormConfigCache: NotRequired[ExadataIormConfigTypeDef]
    isLocalBackupEnabled: NotRequired[bool]
    isSparseDiskgroupEnabled: NotRequired[bool]
    lastUpdateHistoryEntryId: NotRequired[str]
    licenseModel: NotRequired[LicenseModelType]
    listenerPort: NotRequired[int]
    memorySizeInGBs: NotRequired[int]
    nodeCount: NotRequired[int]
    ocid: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    ociUrl: NotRequired[str]
    domain: NotRequired[str]
    scanDnsName: NotRequired[str]
    scanDnsRecordId: NotRequired[str]
    scanIpIds: NotRequired[List[str]]
    shape: NotRequired[str]
    sshPublicKeys: NotRequired[List[str]]
    storageSizeInGBs: NotRequired[int]
    systemVersion: NotRequired[str]
    createdAt: NotRequired[datetime]
    timeZone: NotRequired[str]
    vipIds: NotRequired[List[str]]
    odbNetworkId: NotRequired[str]
    odbNetworkArn: NotRequired[str]
    percentProgress: NotRequired[float]
    computeModel: NotRequired[ComputeModelType]
    iamRoles: NotRequired[List[IamRoleTypeDef]]

class ListDbServersOutputTypeDef(TypedDict):
    dbServers: List[DbServerSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetDbServerOutputTypeDef(TypedDict):
    dbServer: DbServerTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CloudAutonomousVmClusterSummaryTypeDef(TypedDict):
    cloudAutonomousVmClusterId: str
    cloudAutonomousVmClusterArn: NotRequired[str]
    odbNetworkId: NotRequired[str]
    odbNetworkArn: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    percentProgress: NotRequired[float]
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    cloudExadataInfrastructureId: NotRequired[str]
    cloudExadataInfrastructureArn: NotRequired[str]
    autonomousDataStoragePercentage: NotRequired[float]
    autonomousDataStorageSizeInTBs: NotRequired[float]
    availableAutonomousDataStorageSizeInTBs: NotRequired[float]
    availableContainerDatabases: NotRequired[int]
    availableCpus: NotRequired[float]
    computeModel: NotRequired[ComputeModelType]
    cpuCoreCount: NotRequired[int]
    cpuCoreCountPerNode: NotRequired[int]
    cpuPercentage: NotRequired[float]
    dataStorageSizeInGBs: NotRequired[float]
    dataStorageSizeInTBs: NotRequired[float]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServers: NotRequired[List[str]]
    description: NotRequired[str]
    domain: NotRequired[str]
    exadataStorageInTBsLowestScaledValue: NotRequired[float]
    hostname: NotRequired[str]
    ocid: NotRequired[str]
    ociUrl: NotRequired[str]
    isMtlsEnabledVmCluster: NotRequired[bool]
    licenseModel: NotRequired[LicenseModelType]
    maintenanceWindow: NotRequired[MaintenanceWindowOutputTypeDef]
    maxAcdsLowestScaledValue: NotRequired[int]
    memoryPerOracleComputeUnitInGBs: NotRequired[int]
    memorySizeInGBs: NotRequired[int]
    nodeCount: NotRequired[int]
    nonProvisionableAutonomousContainerDatabases: NotRequired[int]
    provisionableAutonomousContainerDatabases: NotRequired[int]
    provisionedAutonomousContainerDatabases: NotRequired[int]
    provisionedCpus: NotRequired[float]
    reclaimableCpus: NotRequired[float]
    reservedCpus: NotRequired[float]
    scanListenerPortNonTls: NotRequired[int]
    scanListenerPortTls: NotRequired[int]
    shape: NotRequired[str]
    createdAt: NotRequired[datetime]
    timeDatabaseSslCertificateExpires: NotRequired[datetime]
    timeOrdsCertificateExpires: NotRequired[datetime]
    timeZone: NotRequired[str]
    totalContainerDatabases: NotRequired[int]

class CloudAutonomousVmClusterTypeDef(TypedDict):
    cloudAutonomousVmClusterId: str
    cloudAutonomousVmClusterArn: NotRequired[str]
    odbNetworkId: NotRequired[str]
    odbNetworkArn: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    percentProgress: NotRequired[float]
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    cloudExadataInfrastructureId: NotRequired[str]
    cloudExadataInfrastructureArn: NotRequired[str]
    autonomousDataStoragePercentage: NotRequired[float]
    autonomousDataStorageSizeInTBs: NotRequired[float]
    availableAutonomousDataStorageSizeInTBs: NotRequired[float]
    availableContainerDatabases: NotRequired[int]
    availableCpus: NotRequired[float]
    computeModel: NotRequired[ComputeModelType]
    cpuCoreCount: NotRequired[int]
    cpuCoreCountPerNode: NotRequired[int]
    cpuPercentage: NotRequired[float]
    dataStorageSizeInGBs: NotRequired[float]
    dataStorageSizeInTBs: NotRequired[float]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServers: NotRequired[List[str]]
    description: NotRequired[str]
    domain: NotRequired[str]
    exadataStorageInTBsLowestScaledValue: NotRequired[float]
    hostname: NotRequired[str]
    ocid: NotRequired[str]
    ociUrl: NotRequired[str]
    isMtlsEnabledVmCluster: NotRequired[bool]
    licenseModel: NotRequired[LicenseModelType]
    maintenanceWindow: NotRequired[MaintenanceWindowOutputTypeDef]
    maxAcdsLowestScaledValue: NotRequired[int]
    memoryPerOracleComputeUnitInGBs: NotRequired[int]
    memorySizeInGBs: NotRequired[int]
    nodeCount: NotRequired[int]
    nonProvisionableAutonomousContainerDatabases: NotRequired[int]
    provisionableAutonomousContainerDatabases: NotRequired[int]
    provisionedAutonomousContainerDatabases: NotRequired[int]
    provisionedCpus: NotRequired[float]
    reclaimableCpus: NotRequired[float]
    reservedCpus: NotRequired[float]
    scanListenerPortNonTls: NotRequired[int]
    scanListenerPortTls: NotRequired[int]
    shape: NotRequired[str]
    createdAt: NotRequired[datetime]
    timeDatabaseSslCertificateExpires: NotRequired[datetime]
    timeOrdsCertificateExpires: NotRequired[datetime]
    timeZone: NotRequired[str]
    totalContainerDatabases: NotRequired[int]

class CloudExadataInfrastructureSummaryTypeDef(TypedDict):
    cloudExadataInfrastructureId: str
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    cloudExadataInfrastructureArn: NotRequired[str]
    activatedStorageCount: NotRequired[int]
    additionalStorageCount: NotRequired[int]
    availableStorageSizeInGBs: NotRequired[int]
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]
    computeCount: NotRequired[int]
    cpuCount: NotRequired[int]
    customerContactsToSendToOCI: NotRequired[List[CustomerContactTypeDef]]
    dataStorageSizeInTBs: NotRequired[float]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServerVersion: NotRequired[str]
    lastMaintenanceRunId: NotRequired[str]
    maintenanceWindow: NotRequired[MaintenanceWindowOutputTypeDef]
    maxCpuCount: NotRequired[int]
    maxDataStorageInTBs: NotRequired[float]
    maxDbNodeStorageSizeInGBs: NotRequired[int]
    maxMemoryInGBs: NotRequired[int]
    memorySizeInGBs: NotRequired[int]
    monthlyDbServerVersion: NotRequired[str]
    monthlyStorageServerVersion: NotRequired[str]
    nextMaintenanceRunId: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    ociUrl: NotRequired[str]
    ocid: NotRequired[str]
    shape: NotRequired[str]
    storageCount: NotRequired[int]
    storageServerVersion: NotRequired[str]
    createdAt: NotRequired[datetime]
    totalStorageSizeInGBs: NotRequired[int]
    percentProgress: NotRequired[float]
    databaseServerType: NotRequired[str]
    storageServerType: NotRequired[str]
    computeModel: NotRequired[ComputeModelType]

class CloudExadataInfrastructureTypeDef(TypedDict):
    cloudExadataInfrastructureId: str
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    cloudExadataInfrastructureArn: NotRequired[str]
    activatedStorageCount: NotRequired[int]
    additionalStorageCount: NotRequired[int]
    availableStorageSizeInGBs: NotRequired[int]
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]
    computeCount: NotRequired[int]
    cpuCount: NotRequired[int]
    customerContactsToSendToOCI: NotRequired[List[CustomerContactTypeDef]]
    dataStorageSizeInTBs: NotRequired[float]
    dbNodeStorageSizeInGBs: NotRequired[int]
    dbServerVersion: NotRequired[str]
    lastMaintenanceRunId: NotRequired[str]
    maintenanceWindow: NotRequired[MaintenanceWindowOutputTypeDef]
    maxCpuCount: NotRequired[int]
    maxDataStorageInTBs: NotRequired[float]
    maxDbNodeStorageSizeInGBs: NotRequired[int]
    maxMemoryInGBs: NotRequired[int]
    memorySizeInGBs: NotRequired[int]
    monthlyDbServerVersion: NotRequired[str]
    monthlyStorageServerVersion: NotRequired[str]
    nextMaintenanceRunId: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    ociUrl: NotRequired[str]
    ocid: NotRequired[str]
    shape: NotRequired[str]
    storageCount: NotRequired[int]
    storageServerVersion: NotRequired[str]
    createdAt: NotRequired[datetime]
    totalStorageSizeInGBs: NotRequired[int]
    percentProgress: NotRequired[float]
    databaseServerType: NotRequired[str]
    storageServerType: NotRequired[str]
    computeModel: NotRequired[ComputeModelType]

MaintenanceWindowUnionTypeDef = Union[MaintenanceWindowTypeDef, MaintenanceWindowOutputTypeDef]

class OdbNetworkSummaryTypeDef(TypedDict):
    odbNetworkId: str
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    odbNetworkArn: NotRequired[str]
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]
    clientSubnetCidr: NotRequired[str]
    backupSubnetCidr: NotRequired[str]
    customDomainName: NotRequired[str]
    defaultDnsPrefix: NotRequired[str]
    peeredCidrs: NotRequired[List[str]]
    ociNetworkAnchorId: NotRequired[str]
    ociNetworkAnchorUrl: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    ociVcnId: NotRequired[str]
    ociVcnUrl: NotRequired[str]
    ociDnsForwardingConfigs: NotRequired[List[OciDnsForwardingConfigTypeDef]]
    createdAt: NotRequired[datetime]
    percentProgress: NotRequired[float]
    managedServices: NotRequired[ManagedServicesTypeDef]

class OdbNetworkTypeDef(TypedDict):
    odbNetworkId: str
    displayName: NotRequired[str]
    status: NotRequired[ResourceStatusType]
    statusReason: NotRequired[str]
    odbNetworkArn: NotRequired[str]
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]
    clientSubnetCidr: NotRequired[str]
    backupSubnetCidr: NotRequired[str]
    customDomainName: NotRequired[str]
    defaultDnsPrefix: NotRequired[str]
    peeredCidrs: NotRequired[List[str]]
    ociNetworkAnchorId: NotRequired[str]
    ociNetworkAnchorUrl: NotRequired[str]
    ociResourceAnchorName: NotRequired[str]
    ociVcnId: NotRequired[str]
    ociVcnUrl: NotRequired[str]
    ociDnsForwardingConfigs: NotRequired[List[OciDnsForwardingConfigTypeDef]]
    createdAt: NotRequired[datetime]
    percentProgress: NotRequired[float]
    managedServices: NotRequired[ManagedServicesTypeDef]

class ListCloudVmClustersOutputTypeDef(TypedDict):
    cloudVmClusters: List[CloudVmClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetCloudVmClusterOutputTypeDef(TypedDict):
    cloudVmCluster: CloudVmClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCloudAutonomousVmClustersOutputTypeDef(TypedDict):
    cloudAutonomousVmClusters: List[CloudAutonomousVmClusterSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetCloudAutonomousVmClusterOutputTypeDef(TypedDict):
    cloudAutonomousVmCluster: CloudAutonomousVmClusterTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCloudExadataInfrastructuresOutputTypeDef(TypedDict):
    cloudExadataInfrastructures: List[CloudExadataInfrastructureSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetCloudExadataInfrastructureOutputTypeDef(TypedDict):
    cloudExadataInfrastructure: CloudExadataInfrastructureTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCloudAutonomousVmClusterInputTypeDef(TypedDict):
    cloudExadataInfrastructureId: str
    odbNetworkId: str
    displayName: str
    autonomousDataStorageSizeInTBs: float
    cpuCoreCountPerNode: int
    memoryPerOracleComputeUnitInGBs: int
    totalContainerDatabases: int
    clientToken: NotRequired[str]
    dbServers: NotRequired[Sequence[str]]
    description: NotRequired[str]
    isMtlsEnabledVmCluster: NotRequired[bool]
    licenseModel: NotRequired[LicenseModelType]
    maintenanceWindow: NotRequired[MaintenanceWindowUnionTypeDef]
    scanListenerPortNonTls: NotRequired[int]
    scanListenerPortTls: NotRequired[int]
    tags: NotRequired[Mapping[str, str]]
    timeZone: NotRequired[str]

class CreateCloudExadataInfrastructureInputTypeDef(TypedDict):
    displayName: str
    shape: str
    computeCount: int
    storageCount: int
    availabilityZone: NotRequired[str]
    availabilityZoneId: NotRequired[str]
    tags: NotRequired[Mapping[str, str]]
    customerContactsToSendToOCI: NotRequired[Sequence[CustomerContactTypeDef]]
    maintenanceWindow: NotRequired[MaintenanceWindowUnionTypeDef]
    clientToken: NotRequired[str]
    databaseServerType: NotRequired[str]
    storageServerType: NotRequired[str]

class UpdateCloudExadataInfrastructureInputTypeDef(TypedDict):
    cloudExadataInfrastructureId: str
    maintenanceWindow: NotRequired[MaintenanceWindowUnionTypeDef]

class ListOdbNetworksOutputTypeDef(TypedDict):
    odbNetworks: List[OdbNetworkSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    nextToken: NotRequired[str]

class GetOdbNetworkOutputTypeDef(TypedDict):
    odbNetwork: OdbNetworkTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
