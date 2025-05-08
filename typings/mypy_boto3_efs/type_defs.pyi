"""
Type annotations for efs service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_efs/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_efs.type_defs import PosixUserOutputTypeDef

    data: PosixUserOutputTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    DeletionModeType,
    LifeCycleStateType,
    PerformanceModeType,
    ReplicationOverwriteProtectionType,
    ReplicationStatusType,
    ResourceIdTypeType,
    ResourceType,
    StatusType,
    ThroughputModeType,
    TransitionToArchiveRulesType,
    TransitionToIARulesType,
)

if sys.version_info >= (3, 9):
    from builtins import dict as Dict
    from builtins import list as List
    from collections.abc import Sequence
else:
    from typing import Dict, List, Sequence
if sys.version_info >= (3, 12):
    from typing import Literal, NotRequired, TypedDict
else:
    from typing_extensions import Literal, NotRequired, TypedDict

__all__ = (
    "AccessPointDescriptionResponseTypeDef",
    "AccessPointDescriptionTypeDef",
    "BackupPolicyDescriptionTypeDef",
    "BackupPolicyTypeDef",
    "CreateAccessPointRequestTypeDef",
    "CreateFileSystemRequestTypeDef",
    "CreateMountTargetRequestTypeDef",
    "CreateReplicationConfigurationRequestTypeDef",
    "CreateTagsRequestTypeDef",
    "CreationInfoTypeDef",
    "DeleteAccessPointRequestTypeDef",
    "DeleteFileSystemPolicyRequestTypeDef",
    "DeleteFileSystemRequestTypeDef",
    "DeleteMountTargetRequestTypeDef",
    "DeleteReplicationConfigurationRequestTypeDef",
    "DeleteTagsRequestTypeDef",
    "DescribeAccessPointsRequestPaginateTypeDef",
    "DescribeAccessPointsRequestTypeDef",
    "DescribeAccessPointsResponseTypeDef",
    "DescribeAccountPreferencesRequestTypeDef",
    "DescribeAccountPreferencesResponseTypeDef",
    "DescribeBackupPolicyRequestTypeDef",
    "DescribeFileSystemPolicyRequestTypeDef",
    "DescribeFileSystemsRequestPaginateTypeDef",
    "DescribeFileSystemsRequestTypeDef",
    "DescribeFileSystemsResponseTypeDef",
    "DescribeLifecycleConfigurationRequestTypeDef",
    "DescribeMountTargetSecurityGroupsRequestTypeDef",
    "DescribeMountTargetSecurityGroupsResponseTypeDef",
    "DescribeMountTargetsRequestPaginateTypeDef",
    "DescribeMountTargetsRequestTypeDef",
    "DescribeMountTargetsResponseTypeDef",
    "DescribeReplicationConfigurationsRequestPaginateTypeDef",
    "DescribeReplicationConfigurationsRequestTypeDef",
    "DescribeReplicationConfigurationsResponseTypeDef",
    "DescribeTagsRequestPaginateTypeDef",
    "DescribeTagsRequestTypeDef",
    "DescribeTagsResponseTypeDef",
    "DestinationToCreateTypeDef",
    "DestinationTypeDef",
    "EmptyResponseMetadataTypeDef",
    "FileSystemDescriptionResponseTypeDef",
    "FileSystemDescriptionTypeDef",
    "FileSystemPolicyDescriptionTypeDef",
    "FileSystemProtectionDescriptionResponseTypeDef",
    "FileSystemProtectionDescriptionTypeDef",
    "FileSystemSizeTypeDef",
    "LifecycleConfigurationDescriptionTypeDef",
    "LifecyclePolicyTypeDef",
    "ListTagsForResourceRequestTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "ModifyMountTargetSecurityGroupsRequestTypeDef",
    "MountTargetDescriptionResponseTypeDef",
    "MountTargetDescriptionTypeDef",
    "PaginatorConfigTypeDef",
    "PosixUserOutputTypeDef",
    "PosixUserTypeDef",
    "PosixUserUnionTypeDef",
    "PutAccountPreferencesRequestTypeDef",
    "PutAccountPreferencesResponseTypeDef",
    "PutBackupPolicyRequestTypeDef",
    "PutFileSystemPolicyRequestTypeDef",
    "PutLifecycleConfigurationRequestTypeDef",
    "ReplicationConfigurationDescriptionResponseTypeDef",
    "ReplicationConfigurationDescriptionTypeDef",
    "ResourceIdPreferenceTypeDef",
    "ResponseMetadataTypeDef",
    "RootDirectoryTypeDef",
    "TagResourceRequestTypeDef",
    "TagTypeDef",
    "UntagResourceRequestTypeDef",
    "UpdateFileSystemProtectionRequestTypeDef",
    "UpdateFileSystemRequestTypeDef",
)

class PosixUserOutputTypeDef(TypedDict):
    Uid: int
    Gid: int
    SecondaryGids: NotRequired[List[int]]

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class BackupPolicyTypeDef(TypedDict):
    Status: StatusType

class CreateMountTargetRequestTypeDef(TypedDict):
    FileSystemId: str
    SubnetId: str
    IpAddress: NotRequired[str]
    SecurityGroups: NotRequired[Sequence[str]]

class DestinationToCreateTypeDef(TypedDict):
    Region: NotRequired[str]
    AvailabilityZoneName: NotRequired[str]
    KmsKeyId: NotRequired[str]
    FileSystemId: NotRequired[str]
    RoleArn: NotRequired[str]

class CreationInfoTypeDef(TypedDict):
    OwnerUid: int
    OwnerGid: int
    Permissions: str

class DeleteAccessPointRequestTypeDef(TypedDict):
    AccessPointId: str

class DeleteFileSystemPolicyRequestTypeDef(TypedDict):
    FileSystemId: str

class DeleteFileSystemRequestTypeDef(TypedDict):
    FileSystemId: str

class DeleteMountTargetRequestTypeDef(TypedDict):
    MountTargetId: str

class DeleteReplicationConfigurationRequestTypeDef(TypedDict):
    SourceFileSystemId: str
    DeletionMode: NotRequired[DeletionModeType]

class DeleteTagsRequestTypeDef(TypedDict):
    FileSystemId: str
    TagKeys: Sequence[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeAccessPointsRequestTypeDef(TypedDict):
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]
    AccessPointId: NotRequired[str]
    FileSystemId: NotRequired[str]

class DescribeAccountPreferencesRequestTypeDef(TypedDict):
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class ResourceIdPreferenceTypeDef(TypedDict):
    ResourceIdType: NotRequired[ResourceIdTypeType]
    Resources: NotRequired[List[ResourceType]]

class DescribeBackupPolicyRequestTypeDef(TypedDict):
    FileSystemId: str

class DescribeFileSystemPolicyRequestTypeDef(TypedDict):
    FileSystemId: str

class DescribeFileSystemsRequestTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]
    CreationToken: NotRequired[str]
    FileSystemId: NotRequired[str]

class DescribeLifecycleConfigurationRequestTypeDef(TypedDict):
    FileSystemId: str

class DescribeMountTargetSecurityGroupsRequestTypeDef(TypedDict):
    MountTargetId: str

class DescribeMountTargetsRequestTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]
    FileSystemId: NotRequired[str]
    MountTargetId: NotRequired[str]
    AccessPointId: NotRequired[str]

class MountTargetDescriptionTypeDef(TypedDict):
    MountTargetId: str
    FileSystemId: str
    SubnetId: str
    LifeCycleState: LifeCycleStateType
    OwnerId: NotRequired[str]
    IpAddress: NotRequired[str]
    NetworkInterfaceId: NotRequired[str]
    AvailabilityZoneId: NotRequired[str]
    AvailabilityZoneName: NotRequired[str]
    VpcId: NotRequired[str]

class DescribeReplicationConfigurationsRequestTypeDef(TypedDict):
    FileSystemId: NotRequired[str]
    NextToken: NotRequired[str]
    MaxResults: NotRequired[int]

class DescribeTagsRequestTypeDef(TypedDict):
    FileSystemId: str
    MaxItems: NotRequired[int]
    Marker: NotRequired[str]

class DestinationTypeDef(TypedDict):
    Status: ReplicationStatusType
    FileSystemId: str
    Region: str
    LastReplicatedTimestamp: NotRequired[datetime]
    OwnerId: NotRequired[str]
    StatusMessage: NotRequired[str]
    RoleArn: NotRequired[str]

class FileSystemProtectionDescriptionTypeDef(TypedDict):
    ReplicationOverwriteProtection: NotRequired[ReplicationOverwriteProtectionType]

class FileSystemSizeTypeDef(TypedDict):
    Value: int
    Timestamp: NotRequired[datetime]
    ValueInIA: NotRequired[int]
    ValueInStandard: NotRequired[int]
    ValueInArchive: NotRequired[int]

class LifecyclePolicyTypeDef(TypedDict):
    TransitionToIA: NotRequired[TransitionToIARulesType]
    TransitionToPrimaryStorageClass: NotRequired[Literal["AFTER_1_ACCESS"]]
    TransitionToArchive: NotRequired[TransitionToArchiveRulesType]

class ListTagsForResourceRequestTypeDef(TypedDict):
    ResourceId: str
    MaxResults: NotRequired[int]
    NextToken: NotRequired[str]

class ModifyMountTargetSecurityGroupsRequestTypeDef(TypedDict):
    MountTargetId: str
    SecurityGroups: NotRequired[Sequence[str]]

class PosixUserTypeDef(TypedDict):
    Uid: int
    Gid: int
    SecondaryGids: NotRequired[Sequence[int]]

class PutAccountPreferencesRequestTypeDef(TypedDict):
    ResourceIdType: ResourceIdTypeType

class PutFileSystemPolicyRequestTypeDef(TypedDict):
    FileSystemId: str
    Policy: str
    BypassPolicyLockoutSafetyCheck: NotRequired[bool]

class UntagResourceRequestTypeDef(TypedDict):
    ResourceId: str
    TagKeys: Sequence[str]

class UpdateFileSystemProtectionRequestTypeDef(TypedDict):
    FileSystemId: str
    ReplicationOverwriteProtection: NotRequired[ReplicationOverwriteProtectionType]

class UpdateFileSystemRequestTypeDef(TypedDict):
    FileSystemId: str
    ThroughputMode: NotRequired[ThroughputModeType]
    ProvisionedThroughputInMibps: NotRequired[float]

class DescribeMountTargetSecurityGroupsResponseTypeDef(TypedDict):
    SecurityGroups: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class EmptyResponseMetadataTypeDef(TypedDict):
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemPolicyDescriptionTypeDef(TypedDict):
    FileSystemId: str
    Policy: str
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemProtectionDescriptionResponseTypeDef(TypedDict):
    ReplicationOverwriteProtection: ReplicationOverwriteProtectionType
    ResponseMetadata: ResponseMetadataTypeDef

class MountTargetDescriptionResponseTypeDef(TypedDict):
    OwnerId: str
    MountTargetId: str
    FileSystemId: str
    SubnetId: str
    LifeCycleState: LifeCycleStateType
    IpAddress: str
    NetworkInterfaceId: str
    AvailabilityZoneId: str
    AvailabilityZoneName: str
    VpcId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateFileSystemRequestTypeDef(TypedDict):
    CreationToken: str
    PerformanceMode: NotRequired[PerformanceModeType]
    Encrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    ThroughputMode: NotRequired[ThroughputModeType]
    ProvisionedThroughputInMibps: NotRequired[float]
    AvailabilityZoneName: NotRequired[str]
    Backup: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateTagsRequestTypeDef(TypedDict):
    FileSystemId: str
    Tags: Sequence[TagTypeDef]

class DescribeTagsResponseTypeDef(TypedDict):
    Marker: str
    Tags: List[TagTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceResponseTypeDef(TypedDict):
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class TagResourceRequestTypeDef(TypedDict):
    ResourceId: str
    Tags: Sequence[TagTypeDef]

class BackupPolicyDescriptionTypeDef(TypedDict):
    BackupPolicy: BackupPolicyTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class PutBackupPolicyRequestTypeDef(TypedDict):
    FileSystemId: str
    BackupPolicy: BackupPolicyTypeDef

class CreateReplicationConfigurationRequestTypeDef(TypedDict):
    SourceFileSystemId: str
    Destinations: Sequence[DestinationToCreateTypeDef]

class RootDirectoryTypeDef(TypedDict):
    Path: NotRequired[str]
    CreationInfo: NotRequired[CreationInfoTypeDef]

class DescribeAccessPointsRequestPaginateTypeDef(TypedDict):
    AccessPointId: NotRequired[str]
    FileSystemId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeFileSystemsRequestPaginateTypeDef(TypedDict):
    CreationToken: NotRequired[str]
    FileSystemId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeMountTargetsRequestPaginateTypeDef(TypedDict):
    FileSystemId: NotRequired[str]
    MountTargetId: NotRequired[str]
    AccessPointId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeReplicationConfigurationsRequestPaginateTypeDef(TypedDict):
    FileSystemId: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTagsRequestPaginateTypeDef(TypedDict):
    FileSystemId: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeAccountPreferencesResponseTypeDef(TypedDict):
    ResourceIdPreference: ResourceIdPreferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class PutAccountPreferencesResponseTypeDef(TypedDict):
    ResourceIdPreference: ResourceIdPreferenceTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMountTargetsResponseTypeDef(TypedDict):
    Marker: str
    MountTargets: List[MountTargetDescriptionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationDescriptionResponseTypeDef(TypedDict):
    SourceFileSystemId: str
    SourceFileSystemRegion: str
    SourceFileSystemArn: str
    OriginalSourceFileSystemArn: str
    CreationTime: datetime
    Destinations: List[DestinationTypeDef]
    SourceFileSystemOwnerId: str
    ResponseMetadata: ResponseMetadataTypeDef

class ReplicationConfigurationDescriptionTypeDef(TypedDict):
    SourceFileSystemId: str
    SourceFileSystemRegion: str
    SourceFileSystemArn: str
    OriginalSourceFileSystemArn: str
    CreationTime: datetime
    Destinations: List[DestinationTypeDef]
    SourceFileSystemOwnerId: NotRequired[str]

class FileSystemDescriptionResponseTypeDef(TypedDict):
    OwnerId: str
    CreationToken: str
    FileSystemId: str
    FileSystemArn: str
    CreationTime: datetime
    LifeCycleState: LifeCycleStateType
    Name: str
    NumberOfMountTargets: int
    SizeInBytes: FileSystemSizeTypeDef
    PerformanceMode: PerformanceModeType
    Encrypted: bool
    KmsKeyId: str
    ThroughputMode: ThroughputModeType
    ProvisionedThroughputInMibps: float
    AvailabilityZoneName: str
    AvailabilityZoneId: str
    Tags: List[TagTypeDef]
    FileSystemProtection: FileSystemProtectionDescriptionTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemDescriptionTypeDef(TypedDict):
    OwnerId: str
    CreationToken: str
    FileSystemId: str
    CreationTime: datetime
    LifeCycleState: LifeCycleStateType
    NumberOfMountTargets: int
    SizeInBytes: FileSystemSizeTypeDef
    PerformanceMode: PerformanceModeType
    Tags: List[TagTypeDef]
    FileSystemArn: NotRequired[str]
    Name: NotRequired[str]
    Encrypted: NotRequired[bool]
    KmsKeyId: NotRequired[str]
    ThroughputMode: NotRequired[ThroughputModeType]
    ProvisionedThroughputInMibps: NotRequired[float]
    AvailabilityZoneName: NotRequired[str]
    AvailabilityZoneId: NotRequired[str]
    FileSystemProtection: NotRequired[FileSystemProtectionDescriptionTypeDef]

class LifecycleConfigurationDescriptionTypeDef(TypedDict):
    LifecyclePolicies: List[LifecyclePolicyTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class PutLifecycleConfigurationRequestTypeDef(TypedDict):
    FileSystemId: str
    LifecyclePolicies: Sequence[LifecyclePolicyTypeDef]

PosixUserUnionTypeDef = Union[PosixUserTypeDef, PosixUserOutputTypeDef]

class AccessPointDescriptionResponseTypeDef(TypedDict):
    ClientToken: str
    Name: str
    Tags: List[TagTypeDef]
    AccessPointId: str
    AccessPointArn: str
    FileSystemId: str
    PosixUser: PosixUserOutputTypeDef
    RootDirectory: RootDirectoryTypeDef
    OwnerId: str
    LifeCycleState: LifeCycleStateType
    ResponseMetadata: ResponseMetadataTypeDef

class AccessPointDescriptionTypeDef(TypedDict):
    ClientToken: NotRequired[str]
    Name: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    AccessPointId: NotRequired[str]
    AccessPointArn: NotRequired[str]
    FileSystemId: NotRequired[str]
    PosixUser: NotRequired[PosixUserOutputTypeDef]
    RootDirectory: NotRequired[RootDirectoryTypeDef]
    OwnerId: NotRequired[str]
    LifeCycleState: NotRequired[LifeCycleStateType]

class DescribeReplicationConfigurationsResponseTypeDef(TypedDict):
    Replications: List[ReplicationConfigurationDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]

class DescribeFileSystemsResponseTypeDef(TypedDict):
    Marker: str
    FileSystems: List[FileSystemDescriptionTypeDef]
    NextMarker: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateAccessPointRequestTypeDef(TypedDict):
    ClientToken: str
    FileSystemId: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    PosixUser: NotRequired[PosixUserUnionTypeDef]
    RootDirectory: NotRequired[RootDirectoryTypeDef]

class DescribeAccessPointsResponseTypeDef(TypedDict):
    AccessPoints: List[AccessPointDescriptionTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef
    NextToken: NotRequired[str]
