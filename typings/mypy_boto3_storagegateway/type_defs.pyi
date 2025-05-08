"""
Type annotations for storagegateway service type definitions.

[Documentation](https://youtype.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/type_defs/)

Copyright 2025 Vlad Emelianov

Usage::

    ```python
    from mypy_boto3_storagegateway.type_defs import TagTypeDef

    data: TagTypeDef = ...
    ```
"""

from __future__ import annotations

import sys
from datetime import datetime
from typing import Union

from .literals import (
    ActiveDirectoryStatusType,
    AutomaticUpdatePolicyType,
    AvailabilityMonitorTestStatusType,
    CacheReportFilterNameType,
    CacheReportStatusType,
    CaseSensitivityType,
    EncryptionTypeType,
    FileShareTypeType,
    GatewayCapacityType,
    HostEnvironmentType,
    ObjectACLType,
    PoolStatusType,
    RetentionLockTypeType,
    SMBSecurityStrategyType,
    TapeStorageClassType,
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
    "ActivateGatewayInputTypeDef",
    "ActivateGatewayOutputTypeDef",
    "AddCacheInputTypeDef",
    "AddCacheOutputTypeDef",
    "AddTagsToResourceInputTypeDef",
    "AddTagsToResourceOutputTypeDef",
    "AddUploadBufferInputTypeDef",
    "AddUploadBufferOutputTypeDef",
    "AddWorkingStorageInputTypeDef",
    "AddWorkingStorageOutputTypeDef",
    "AssignTapePoolInputTypeDef",
    "AssignTapePoolOutputTypeDef",
    "AssociateFileSystemInputTypeDef",
    "AssociateFileSystemOutputTypeDef",
    "AttachVolumeInputTypeDef",
    "AttachVolumeOutputTypeDef",
    "AutomaticTapeCreationPolicyInfoTypeDef",
    "AutomaticTapeCreationRuleTypeDef",
    "BandwidthRateLimitIntervalOutputTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "BandwidthRateLimitIntervalUnionTypeDef",
    "CacheAttributesTypeDef",
    "CacheReportFilterOutputTypeDef",
    "CacheReportFilterTypeDef",
    "CacheReportFilterUnionTypeDef",
    "CacheReportInfoTypeDef",
    "CachediSCSIVolumeTypeDef",
    "CancelArchivalInputTypeDef",
    "CancelArchivalOutputTypeDef",
    "CancelCacheReportInputTypeDef",
    "CancelCacheReportOutputTypeDef",
    "CancelRetrievalInputTypeDef",
    "CancelRetrievalOutputTypeDef",
    "ChapInfoTypeDef",
    "CreateCachediSCSIVolumeInputTypeDef",
    "CreateCachediSCSIVolumeOutputTypeDef",
    "CreateNFSFileShareInputTypeDef",
    "CreateNFSFileShareOutputTypeDef",
    "CreateSMBFileShareInputTypeDef",
    "CreateSMBFileShareOutputTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointInputTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    "CreateSnapshotInputTypeDef",
    "CreateSnapshotOutputTypeDef",
    "CreateStorediSCSIVolumeInputTypeDef",
    "CreateStorediSCSIVolumeOutputTypeDef",
    "CreateTapePoolInputTypeDef",
    "CreateTapePoolOutputTypeDef",
    "CreateTapeWithBarcodeInputTypeDef",
    "CreateTapeWithBarcodeOutputTypeDef",
    "CreateTapesInputTypeDef",
    "CreateTapesOutputTypeDef",
    "DeleteAutomaticTapeCreationPolicyInputTypeDef",
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    "DeleteBandwidthRateLimitInputTypeDef",
    "DeleteBandwidthRateLimitOutputTypeDef",
    "DeleteCacheReportInputTypeDef",
    "DeleteCacheReportOutputTypeDef",
    "DeleteChapCredentialsInputTypeDef",
    "DeleteChapCredentialsOutputTypeDef",
    "DeleteFileShareInputTypeDef",
    "DeleteFileShareOutputTypeDef",
    "DeleteGatewayInputTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteSnapshotScheduleInputTypeDef",
    "DeleteSnapshotScheduleOutputTypeDef",
    "DeleteTapeArchiveInputTypeDef",
    "DeleteTapeArchiveOutputTypeDef",
    "DeleteTapeInputTypeDef",
    "DeleteTapeOutputTypeDef",
    "DeleteTapePoolInputTypeDef",
    "DeleteTapePoolOutputTypeDef",
    "DeleteVolumeInputTypeDef",
    "DeleteVolumeOutputTypeDef",
    "DescribeAvailabilityMonitorTestInputTypeDef",
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    "DescribeBandwidthRateLimitInputTypeDef",
    "DescribeBandwidthRateLimitOutputTypeDef",
    "DescribeBandwidthRateLimitScheduleInputTypeDef",
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    "DescribeCacheInputTypeDef",
    "DescribeCacheOutputTypeDef",
    "DescribeCacheReportInputTypeDef",
    "DescribeCacheReportOutputTypeDef",
    "DescribeCachediSCSIVolumesInputTypeDef",
    "DescribeCachediSCSIVolumesOutputTypeDef",
    "DescribeChapCredentialsInputTypeDef",
    "DescribeChapCredentialsOutputTypeDef",
    "DescribeFileSystemAssociationsInputTypeDef",
    "DescribeFileSystemAssociationsOutputTypeDef",
    "DescribeGatewayInformationInputTypeDef",
    "DescribeGatewayInformationOutputTypeDef",
    "DescribeMaintenanceStartTimeInputTypeDef",
    "DescribeMaintenanceStartTimeOutputTypeDef",
    "DescribeNFSFileSharesInputTypeDef",
    "DescribeNFSFileSharesOutputTypeDef",
    "DescribeSMBFileSharesInputTypeDef",
    "DescribeSMBFileSharesOutputTypeDef",
    "DescribeSMBSettingsInputTypeDef",
    "DescribeSMBSettingsOutputTypeDef",
    "DescribeSnapshotScheduleInputTypeDef",
    "DescribeSnapshotScheduleOutputTypeDef",
    "DescribeStorediSCSIVolumesInputTypeDef",
    "DescribeStorediSCSIVolumesOutputTypeDef",
    "DescribeTapeArchivesInputPaginateTypeDef",
    "DescribeTapeArchivesInputTypeDef",
    "DescribeTapeArchivesOutputTypeDef",
    "DescribeTapeRecoveryPointsInputPaginateTypeDef",
    "DescribeTapeRecoveryPointsInputTypeDef",
    "DescribeTapeRecoveryPointsOutputTypeDef",
    "DescribeTapesInputPaginateTypeDef",
    "DescribeTapesInputTypeDef",
    "DescribeTapesOutputTypeDef",
    "DescribeUploadBufferInputTypeDef",
    "DescribeUploadBufferOutputTypeDef",
    "DescribeVTLDevicesInputPaginateTypeDef",
    "DescribeVTLDevicesInputTypeDef",
    "DescribeVTLDevicesOutputTypeDef",
    "DescribeWorkingStorageInputTypeDef",
    "DescribeWorkingStorageOutputTypeDef",
    "DetachVolumeInputTypeDef",
    "DetachVolumeOutputTypeDef",
    "DeviceiSCSIAttributesTypeDef",
    "DisableGatewayInputTypeDef",
    "DisableGatewayOutputTypeDef",
    "DisassociateFileSystemInputTypeDef",
    "DisassociateFileSystemOutputTypeDef",
    "DiskTypeDef",
    "EndpointNetworkConfigurationOutputTypeDef",
    "EndpointNetworkConfigurationTypeDef",
    "EndpointNetworkConfigurationUnionTypeDef",
    "EvictFilesFailingUploadInputTypeDef",
    "EvictFilesFailingUploadOutputTypeDef",
    "FileShareInfoTypeDef",
    "FileSystemAssociationInfoTypeDef",
    "FileSystemAssociationStatusDetailTypeDef",
    "FileSystemAssociationSummaryTypeDef",
    "GatewayInfoTypeDef",
    "JoinDomainInputTypeDef",
    "JoinDomainOutputTypeDef",
    "ListAutomaticTapeCreationPoliciesInputTypeDef",
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    "ListCacheReportsInputPaginateTypeDef",
    "ListCacheReportsInputTypeDef",
    "ListCacheReportsOutputTypeDef",
    "ListFileSharesInputPaginateTypeDef",
    "ListFileSharesInputTypeDef",
    "ListFileSharesOutputTypeDef",
    "ListFileSystemAssociationsInputPaginateTypeDef",
    "ListFileSystemAssociationsInputTypeDef",
    "ListFileSystemAssociationsOutputTypeDef",
    "ListGatewaysInputPaginateTypeDef",
    "ListGatewaysInputTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListLocalDisksInputTypeDef",
    "ListLocalDisksOutputTypeDef",
    "ListTagsForResourceInputPaginateTypeDef",
    "ListTagsForResourceInputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTapePoolsInputPaginateTypeDef",
    "ListTapePoolsInputTypeDef",
    "ListTapePoolsOutputTypeDef",
    "ListTapesInputPaginateTypeDef",
    "ListTapesInputTypeDef",
    "ListTapesOutputTypeDef",
    "ListVolumeInitiatorsInputTypeDef",
    "ListVolumeInitiatorsOutputTypeDef",
    "ListVolumeRecoveryPointsInputTypeDef",
    "ListVolumeRecoveryPointsOutputTypeDef",
    "ListVolumesInputPaginateTypeDef",
    "ListVolumesInputTypeDef",
    "ListVolumesOutputTypeDef",
    "NFSFileShareDefaultsTypeDef",
    "NFSFileShareInfoTypeDef",
    "NetworkInterfaceTypeDef",
    "NotifyWhenUploadedInputTypeDef",
    "NotifyWhenUploadedOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PoolInfoTypeDef",
    "RefreshCacheInputTypeDef",
    "RefreshCacheOutputTypeDef",
    "RemoveTagsFromResourceInputTypeDef",
    "RemoveTagsFromResourceOutputTypeDef",
    "ResetCacheInputTypeDef",
    "ResetCacheOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieveTapeArchiveInputTypeDef",
    "RetrieveTapeArchiveOutputTypeDef",
    "RetrieveTapeRecoveryPointInputTypeDef",
    "RetrieveTapeRecoveryPointOutputTypeDef",
    "SMBFileShareInfoTypeDef",
    "SMBLocalGroupsOutputTypeDef",
    "SMBLocalGroupsTypeDef",
    "SMBLocalGroupsUnionTypeDef",
    "SetLocalConsolePasswordInputTypeDef",
    "SetLocalConsolePasswordOutputTypeDef",
    "SetSMBGuestPasswordInputTypeDef",
    "SetSMBGuestPasswordOutputTypeDef",
    "ShutdownGatewayInputTypeDef",
    "ShutdownGatewayOutputTypeDef",
    "SoftwareUpdatePreferencesTypeDef",
    "StartAvailabilityMonitorTestInputTypeDef",
    "StartAvailabilityMonitorTestOutputTypeDef",
    "StartCacheReportInputTypeDef",
    "StartCacheReportOutputTypeDef",
    "StartGatewayInputTypeDef",
    "StartGatewayOutputTypeDef",
    "StorediSCSIVolumeTypeDef",
    "TagTypeDef",
    "TapeArchiveTypeDef",
    "TapeInfoTypeDef",
    "TapeRecoveryPointInfoTypeDef",
    "TapeTypeDef",
    "UpdateAutomaticTapeCreationPolicyInputTypeDef",
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    "UpdateBandwidthRateLimitInputTypeDef",
    "UpdateBandwidthRateLimitOutputTypeDef",
    "UpdateBandwidthRateLimitScheduleInputTypeDef",
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    "UpdateChapCredentialsInputTypeDef",
    "UpdateChapCredentialsOutputTypeDef",
    "UpdateFileSystemAssociationInputTypeDef",
    "UpdateFileSystemAssociationOutputTypeDef",
    "UpdateGatewayInformationInputTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowInputTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateMaintenanceStartTimeInputTypeDef",
    "UpdateMaintenanceStartTimeOutputTypeDef",
    "UpdateNFSFileShareInputTypeDef",
    "UpdateNFSFileShareOutputTypeDef",
    "UpdateSMBFileShareInputTypeDef",
    "UpdateSMBFileShareOutputTypeDef",
    "UpdateSMBFileShareVisibilityInputTypeDef",
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    "UpdateSMBLocalGroupsInputTypeDef",
    "UpdateSMBLocalGroupsOutputTypeDef",
    "UpdateSMBSecurityStrategyInputTypeDef",
    "UpdateSMBSecurityStrategyOutputTypeDef",
    "UpdateSnapshotScheduleInputTypeDef",
    "UpdateSnapshotScheduleOutputTypeDef",
    "UpdateVTLDeviceTypeInputTypeDef",
    "UpdateVTLDeviceTypeOutputTypeDef",
    "VTLDeviceTypeDef",
    "VolumeInfoTypeDef",
    "VolumeRecoveryPointInfoTypeDef",
    "VolumeiSCSIAttributesTypeDef",
)

class TagTypeDef(TypedDict):
    Key: str
    Value: str

class ResponseMetadataTypeDef(TypedDict):
    RequestId: str
    HTTPStatusCode: int
    HTTPHeaders: Dict[str, str]
    RetryAttempts: int
    HostId: NotRequired[str]

class AddCacheInputTypeDef(TypedDict):
    GatewayARN: str
    DiskIds: Sequence[str]

class AddUploadBufferInputTypeDef(TypedDict):
    GatewayARN: str
    DiskIds: Sequence[str]

class AddWorkingStorageInputTypeDef(TypedDict):
    GatewayARN: str
    DiskIds: Sequence[str]

class AssignTapePoolInputTypeDef(TypedDict):
    TapeARN: str
    PoolId: str
    BypassGovernanceRetention: NotRequired[bool]

class CacheAttributesTypeDef(TypedDict):
    CacheStaleTimeoutInSeconds: NotRequired[int]

class AttachVolumeInputTypeDef(TypedDict):
    GatewayARN: str
    VolumeARN: str
    NetworkInterfaceId: str
    TargetName: NotRequired[str]
    DiskId: NotRequired[str]

class AutomaticTapeCreationRuleTypeDef(TypedDict):
    TapeBarcodePrefix: str
    PoolId: str
    TapeSizeInBytes: int
    MinimumNumTapes: int
    Worm: NotRequired[bool]

class BandwidthRateLimitIntervalOutputTypeDef(TypedDict):
    StartHourOfDay: int
    StartMinuteOfHour: int
    EndHourOfDay: int
    EndMinuteOfHour: int
    DaysOfWeek: List[int]
    AverageUploadRateLimitInBitsPerSec: NotRequired[int]
    AverageDownloadRateLimitInBitsPerSec: NotRequired[int]

class BandwidthRateLimitIntervalTypeDef(TypedDict):
    StartHourOfDay: int
    StartMinuteOfHour: int
    EndHourOfDay: int
    EndMinuteOfHour: int
    DaysOfWeek: Sequence[int]
    AverageUploadRateLimitInBitsPerSec: NotRequired[int]
    AverageDownloadRateLimitInBitsPerSec: NotRequired[int]

class CacheReportFilterOutputTypeDef(TypedDict):
    Name: CacheReportFilterNameType
    Values: List[str]

class CacheReportFilterTypeDef(TypedDict):
    Name: CacheReportFilterNameType
    Values: Sequence[str]

class VolumeiSCSIAttributesTypeDef(TypedDict):
    TargetARN: NotRequired[str]
    NetworkInterfaceId: NotRequired[str]
    NetworkInterfacePort: NotRequired[int]
    LunNumber: NotRequired[int]
    ChapEnabled: NotRequired[bool]

class CancelArchivalInputTypeDef(TypedDict):
    GatewayARN: str
    TapeARN: str

class CancelCacheReportInputTypeDef(TypedDict):
    CacheReportARN: str

class CancelRetrievalInputTypeDef(TypedDict):
    GatewayARN: str
    TapeARN: str

class ChapInfoTypeDef(TypedDict):
    TargetARN: NotRequired[str]
    SecretToAuthenticateInitiator: NotRequired[str]
    InitiatorName: NotRequired[str]
    SecretToAuthenticateTarget: NotRequired[str]

class NFSFileShareDefaultsTypeDef(TypedDict):
    FileMode: NotRequired[str]
    DirectoryMode: NotRequired[str]
    GroupId: NotRequired[int]
    OwnerId: NotRequired[int]

class DeleteAutomaticTapeCreationPolicyInputTypeDef(TypedDict):
    GatewayARN: str

class DeleteBandwidthRateLimitInputTypeDef(TypedDict):
    GatewayARN: str
    BandwidthType: str

class DeleteCacheReportInputTypeDef(TypedDict):
    CacheReportARN: str

class DeleteChapCredentialsInputTypeDef(TypedDict):
    TargetARN: str
    InitiatorName: str

class DeleteFileShareInputTypeDef(TypedDict):
    FileShareARN: str
    ForceDelete: NotRequired[bool]

class DeleteGatewayInputTypeDef(TypedDict):
    GatewayARN: str

class DeleteSnapshotScheduleInputTypeDef(TypedDict):
    VolumeARN: str

class DeleteTapeArchiveInputTypeDef(TypedDict):
    TapeARN: str
    BypassGovernanceRetention: NotRequired[bool]

class DeleteTapeInputTypeDef(TypedDict):
    GatewayARN: str
    TapeARN: str
    BypassGovernanceRetention: NotRequired[bool]

class DeleteTapePoolInputTypeDef(TypedDict):
    PoolARN: str

class DeleteVolumeInputTypeDef(TypedDict):
    VolumeARN: str

class DescribeAvailabilityMonitorTestInputTypeDef(TypedDict):
    GatewayARN: str

class DescribeBandwidthRateLimitInputTypeDef(TypedDict):
    GatewayARN: str

class DescribeBandwidthRateLimitScheduleInputTypeDef(TypedDict):
    GatewayARN: str

class DescribeCacheInputTypeDef(TypedDict):
    GatewayARN: str

class DescribeCacheReportInputTypeDef(TypedDict):
    CacheReportARN: str

class DescribeCachediSCSIVolumesInputTypeDef(TypedDict):
    VolumeARNs: Sequence[str]

class DescribeChapCredentialsInputTypeDef(TypedDict):
    TargetARN: str

class DescribeFileSystemAssociationsInputTypeDef(TypedDict):
    FileSystemAssociationARNList: Sequence[str]

class DescribeGatewayInformationInputTypeDef(TypedDict):
    GatewayARN: str

class NetworkInterfaceTypeDef(TypedDict):
    Ipv4Address: NotRequired[str]
    MacAddress: NotRequired[str]
    Ipv6Address: NotRequired[str]

class DescribeMaintenanceStartTimeInputTypeDef(TypedDict):
    GatewayARN: str

class SoftwareUpdatePreferencesTypeDef(TypedDict):
    AutomaticUpdatePolicy: NotRequired[AutomaticUpdatePolicyType]

class DescribeNFSFileSharesInputTypeDef(TypedDict):
    FileShareARNList: Sequence[str]

class DescribeSMBFileSharesInputTypeDef(TypedDict):
    FileShareARNList: Sequence[str]

class DescribeSMBSettingsInputTypeDef(TypedDict):
    GatewayARN: str

class SMBLocalGroupsOutputTypeDef(TypedDict):
    GatewayAdmins: NotRequired[List[str]]

class DescribeSnapshotScheduleInputTypeDef(TypedDict):
    VolumeARN: str

class DescribeStorediSCSIVolumesInputTypeDef(TypedDict):
    VolumeARNs: Sequence[str]

class PaginatorConfigTypeDef(TypedDict):
    MaxItems: NotRequired[int]
    PageSize: NotRequired[int]
    StartingToken: NotRequired[str]

class DescribeTapeArchivesInputTypeDef(TypedDict):
    TapeARNs: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class TapeArchiveTypeDef(TypedDict):
    TapeARN: NotRequired[str]
    TapeBarcode: NotRequired[str]
    TapeCreatedDate: NotRequired[datetime]
    TapeSizeInBytes: NotRequired[int]
    CompletionTime: NotRequired[datetime]
    RetrievedTo: NotRequired[str]
    TapeStatus: NotRequired[str]
    TapeUsedInBytes: NotRequired[int]
    KMSKey: NotRequired[str]
    PoolId: NotRequired[str]
    Worm: NotRequired[bool]
    RetentionStartDate: NotRequired[datetime]
    PoolEntryDate: NotRequired[datetime]

class DescribeTapeRecoveryPointsInputTypeDef(TypedDict):
    GatewayARN: str
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class TapeRecoveryPointInfoTypeDef(TypedDict):
    TapeARN: NotRequired[str]
    TapeRecoveryPointTime: NotRequired[datetime]
    TapeSizeInBytes: NotRequired[int]
    TapeStatus: NotRequired[str]

class DescribeTapesInputTypeDef(TypedDict):
    GatewayARN: str
    TapeARNs: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class TapeTypeDef(TypedDict):
    TapeARN: NotRequired[str]
    TapeBarcode: NotRequired[str]
    TapeCreatedDate: NotRequired[datetime]
    TapeSizeInBytes: NotRequired[int]
    TapeStatus: NotRequired[str]
    VTLDevice: NotRequired[str]
    Progress: NotRequired[float]
    TapeUsedInBytes: NotRequired[int]
    KMSKey: NotRequired[str]
    PoolId: NotRequired[str]
    Worm: NotRequired[bool]
    RetentionStartDate: NotRequired[datetime]
    PoolEntryDate: NotRequired[datetime]

class DescribeUploadBufferInputTypeDef(TypedDict):
    GatewayARN: str

class DescribeVTLDevicesInputTypeDef(TypedDict):
    GatewayARN: str
    VTLDeviceARNs: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class DescribeWorkingStorageInputTypeDef(TypedDict):
    GatewayARN: str

class DetachVolumeInputTypeDef(TypedDict):
    VolumeARN: str
    ForceDetach: NotRequired[bool]

class DeviceiSCSIAttributesTypeDef(TypedDict):
    TargetARN: NotRequired[str]
    NetworkInterfaceId: NotRequired[str]
    NetworkInterfacePort: NotRequired[int]
    ChapEnabled: NotRequired[bool]

class DisableGatewayInputTypeDef(TypedDict):
    GatewayARN: str

class DisassociateFileSystemInputTypeDef(TypedDict):
    FileSystemAssociationARN: str
    ForceDelete: NotRequired[bool]

class DiskTypeDef(TypedDict):
    DiskId: NotRequired[str]
    DiskPath: NotRequired[str]
    DiskNode: NotRequired[str]
    DiskStatus: NotRequired[str]
    DiskSizeInBytes: NotRequired[int]
    DiskAllocationType: NotRequired[str]
    DiskAllocationResource: NotRequired[str]
    DiskAttributeList: NotRequired[List[str]]

class EndpointNetworkConfigurationOutputTypeDef(TypedDict):
    IpAddresses: NotRequired[List[str]]

class EndpointNetworkConfigurationTypeDef(TypedDict):
    IpAddresses: NotRequired[Sequence[str]]

class EvictFilesFailingUploadInputTypeDef(TypedDict):
    FileShareARN: str
    ForceRemove: NotRequired[bool]

class FileShareInfoTypeDef(TypedDict):
    FileShareType: NotRequired[FileShareTypeType]
    FileShareARN: NotRequired[str]
    FileShareId: NotRequired[str]
    FileShareStatus: NotRequired[str]
    GatewayARN: NotRequired[str]

class FileSystemAssociationStatusDetailTypeDef(TypedDict):
    ErrorCode: NotRequired[str]

class FileSystemAssociationSummaryTypeDef(TypedDict):
    FileSystemAssociationId: NotRequired[str]
    FileSystemAssociationARN: NotRequired[str]
    FileSystemAssociationStatus: NotRequired[str]
    GatewayARN: NotRequired[str]

class GatewayInfoTypeDef(TypedDict):
    GatewayId: NotRequired[str]
    GatewayARN: NotRequired[str]
    GatewayType: NotRequired[str]
    GatewayOperationalState: NotRequired[str]
    GatewayName: NotRequired[str]
    Ec2InstanceId: NotRequired[str]
    Ec2InstanceRegion: NotRequired[str]
    HostEnvironment: NotRequired[HostEnvironmentType]
    HostEnvironmentId: NotRequired[str]
    DeprecationDate: NotRequired[str]
    SoftwareVersion: NotRequired[str]

class JoinDomainInputTypeDef(TypedDict):
    GatewayARN: str
    DomainName: str
    UserName: str
    Password: str
    OrganizationalUnit: NotRequired[str]
    DomainControllers: NotRequired[Sequence[str]]
    TimeoutInSeconds: NotRequired[int]

class ListAutomaticTapeCreationPoliciesInputTypeDef(TypedDict):
    GatewayARN: NotRequired[str]

class ListCacheReportsInputTypeDef(TypedDict):
    Marker: NotRequired[str]

class ListFileSharesInputTypeDef(TypedDict):
    GatewayARN: NotRequired[str]
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class ListFileSystemAssociationsInputTypeDef(TypedDict):
    GatewayARN: NotRequired[str]
    Limit: NotRequired[int]
    Marker: NotRequired[str]

class ListGatewaysInputTypeDef(TypedDict):
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class ListLocalDisksInputTypeDef(TypedDict):
    GatewayARN: str

class ListTagsForResourceInputTypeDef(TypedDict):
    ResourceARN: str
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class ListTapePoolsInputTypeDef(TypedDict):
    PoolARNs: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class PoolInfoTypeDef(TypedDict):
    PoolARN: NotRequired[str]
    PoolName: NotRequired[str]
    StorageClass: NotRequired[TapeStorageClassType]
    RetentionLockType: NotRequired[RetentionLockTypeType]
    RetentionLockTimeInDays: NotRequired[int]
    PoolStatus: NotRequired[PoolStatusType]

class ListTapesInputTypeDef(TypedDict):
    TapeARNs: NotRequired[Sequence[str]]
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class TapeInfoTypeDef(TypedDict):
    TapeARN: NotRequired[str]
    TapeBarcode: NotRequired[str]
    TapeSizeInBytes: NotRequired[int]
    TapeStatus: NotRequired[str]
    GatewayARN: NotRequired[str]
    PoolId: NotRequired[str]
    RetentionStartDate: NotRequired[datetime]
    PoolEntryDate: NotRequired[datetime]

class ListVolumeInitiatorsInputTypeDef(TypedDict):
    VolumeARN: str

class ListVolumeRecoveryPointsInputTypeDef(TypedDict):
    GatewayARN: str

class VolumeRecoveryPointInfoTypeDef(TypedDict):
    VolumeARN: NotRequired[str]
    VolumeSizeInBytes: NotRequired[int]
    VolumeUsageInBytes: NotRequired[int]
    VolumeRecoveryPointTime: NotRequired[str]

class ListVolumesInputTypeDef(TypedDict):
    GatewayARN: NotRequired[str]
    Marker: NotRequired[str]
    Limit: NotRequired[int]

class VolumeInfoTypeDef(TypedDict):
    VolumeARN: NotRequired[str]
    VolumeId: NotRequired[str]
    GatewayARN: NotRequired[str]
    GatewayId: NotRequired[str]
    VolumeType: NotRequired[str]
    VolumeSizeInBytes: NotRequired[int]
    VolumeAttachmentStatus: NotRequired[str]

class NotifyWhenUploadedInputTypeDef(TypedDict):
    FileShareARN: str

class RefreshCacheInputTypeDef(TypedDict):
    FileShareARN: str
    FolderList: NotRequired[Sequence[str]]
    Recursive: NotRequired[bool]

class RemoveTagsFromResourceInputTypeDef(TypedDict):
    ResourceARN: str
    TagKeys: Sequence[str]

class ResetCacheInputTypeDef(TypedDict):
    GatewayARN: str

class RetrieveTapeArchiveInputTypeDef(TypedDict):
    TapeARN: str
    GatewayARN: str

class RetrieveTapeRecoveryPointInputTypeDef(TypedDict):
    TapeARN: str
    GatewayARN: str

class SMBLocalGroupsTypeDef(TypedDict):
    GatewayAdmins: NotRequired[Sequence[str]]

class SetLocalConsolePasswordInputTypeDef(TypedDict):
    GatewayARN: str
    LocalConsolePassword: str

class SetSMBGuestPasswordInputTypeDef(TypedDict):
    GatewayARN: str
    Password: str

class ShutdownGatewayInputTypeDef(TypedDict):
    GatewayARN: str

class StartAvailabilityMonitorTestInputTypeDef(TypedDict):
    GatewayARN: str

class StartGatewayInputTypeDef(TypedDict):
    GatewayARN: str

class UpdateBandwidthRateLimitInputTypeDef(TypedDict):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: NotRequired[int]
    AverageDownloadRateLimitInBitsPerSec: NotRequired[int]

class UpdateChapCredentialsInputTypeDef(TypedDict):
    TargetARN: str
    SecretToAuthenticateInitiator: str
    InitiatorName: str
    SecretToAuthenticateTarget: NotRequired[str]

class UpdateGatewayInformationInputTypeDef(TypedDict):
    GatewayARN: str
    GatewayName: NotRequired[str]
    GatewayTimezone: NotRequired[str]
    CloudWatchLogGroupARN: NotRequired[str]
    GatewayCapacity: NotRequired[GatewayCapacityType]

class UpdateGatewaySoftwareNowInputTypeDef(TypedDict):
    GatewayARN: str

class UpdateSMBFileShareVisibilityInputTypeDef(TypedDict):
    GatewayARN: str
    FileSharesVisible: bool

class UpdateSMBSecurityStrategyInputTypeDef(TypedDict):
    GatewayARN: str
    SMBSecurityStrategy: SMBSecurityStrategyType

class UpdateVTLDeviceTypeInputTypeDef(TypedDict):
    VTLDeviceARN: str
    DeviceType: str

class ActivateGatewayInputTypeDef(TypedDict):
    ActivationKey: str
    GatewayName: str
    GatewayTimezone: str
    GatewayRegion: str
    GatewayType: NotRequired[str]
    TapeDriveType: NotRequired[str]
    MediumChangerType: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class AddTagsToResourceInputTypeDef(TypedDict):
    ResourceARN: str
    Tags: Sequence[TagTypeDef]

class CreateCachediSCSIVolumeInputTypeDef(TypedDict):
    GatewayARN: str
    VolumeSizeInBytes: int
    TargetName: str
    NetworkInterfaceId: str
    ClientToken: str
    SnapshotId: NotRequired[str]
    SourceVolumeARN: NotRequired[str]
    KMSEncrypted: NotRequired[bool]
    KMSKey: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateSnapshotFromVolumeRecoveryPointInputTypeDef(TypedDict):
    VolumeARN: str
    SnapshotDescription: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateSnapshotInputTypeDef(TypedDict):
    VolumeARN: str
    SnapshotDescription: str
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateStorediSCSIVolumeInputTypeDef(TypedDict):
    GatewayARN: str
    DiskId: str
    PreserveExistingData: bool
    TargetName: str
    NetworkInterfaceId: str
    SnapshotId: NotRequired[str]
    KMSEncrypted: NotRequired[bool]
    KMSKey: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateTapePoolInputTypeDef(TypedDict):
    PoolName: str
    StorageClass: TapeStorageClassType
    RetentionLockType: NotRequired[RetentionLockTypeType]
    RetentionLockTimeInDays: NotRequired[int]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateTapeWithBarcodeInputTypeDef(TypedDict):
    GatewayARN: str
    TapeSizeInBytes: int
    TapeBarcode: str
    KMSEncrypted: NotRequired[bool]
    KMSKey: NotRequired[str]
    PoolId: NotRequired[str]
    Worm: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class CreateTapesInputTypeDef(TypedDict):
    GatewayARN: str
    TapeSizeInBytes: int
    ClientToken: str
    NumTapesToCreate: int
    TapeBarcodePrefix: str
    KMSEncrypted: NotRequired[bool]
    KMSKey: NotRequired[str]
    PoolId: NotRequired[str]
    Worm: NotRequired[bool]
    Tags: NotRequired[Sequence[TagTypeDef]]

class UpdateSnapshotScheduleInputTypeDef(TypedDict):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: NotRequired[str]
    Tags: NotRequired[Sequence[TagTypeDef]]

class ActivateGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddCacheOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddTagsToResourceOutputTypeDef(TypedDict):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddUploadBufferOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AddWorkingStorageOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssignTapePoolOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateFileSystemOutputTypeDef(TypedDict):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class AttachVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelArchivalOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelCacheReportOutputTypeDef(TypedDict):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CancelRetrievalOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateCachediSCSIVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    TargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateNFSFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSMBFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotFromVolumeRecoveryPointOutputTypeDef(TypedDict):
    SnapshotId: str
    VolumeARN: str
    VolumeRecoveryPointTime: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateSnapshotOutputTypeDef(TypedDict):
    VolumeARN: str
    SnapshotId: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateStorediSCSIVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    VolumeSizeInBytes: int
    TargetARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTapePoolOutputTypeDef(TypedDict):
    PoolARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTapeWithBarcodeOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class CreateTapesOutputTypeDef(TypedDict):
    TapeARNs: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteAutomaticTapeCreationPolicyOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteBandwidthRateLimitOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteCacheReportOutputTypeDef(TypedDict):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteChapCredentialsOutputTypeDef(TypedDict):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteSnapshotScheduleOutputTypeDef(TypedDict):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTapeArchiveOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTapeOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteTapePoolOutputTypeDef(TypedDict):
    PoolARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DeleteVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeAvailabilityMonitorTestOutputTypeDef(TypedDict):
    GatewayARN: str
    Status: AvailabilityMonitorTestStatusType
    StartTime: datetime
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeBandwidthRateLimitOutputTypeDef(TypedDict):
    GatewayARN: str
    AverageUploadRateLimitInBitsPerSec: int
    AverageDownloadRateLimitInBitsPerSec: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeCacheOutputTypeDef(TypedDict):
    GatewayARN: str
    DiskIds: List[str]
    CacheAllocatedInBytes: int
    CacheUsedPercentage: float
    CacheDirtyPercentage: float
    CacheHitPercentage: float
    CacheMissPercentage: float
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeSnapshotScheduleOutputTypeDef(TypedDict):
    VolumeARN: str
    StartAt: int
    RecurrenceInHours: int
    Description: str
    Timezone: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeUploadBufferOutputTypeDef(TypedDict):
    GatewayARN: str
    DiskIds: List[str]
    UploadBufferUsedInBytes: int
    UploadBufferAllocatedInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeWorkingStorageOutputTypeDef(TypedDict):
    GatewayARN: str
    DiskIds: List[str]
    WorkingStorageUsedInBytes: int
    WorkingStorageAllocatedInBytes: int
    ResponseMetadata: ResponseMetadataTypeDef

class DetachVolumeOutputTypeDef(TypedDict):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisableGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class DisassociateFileSystemOutputTypeDef(TypedDict):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class EvictFilesFailingUploadOutputTypeDef(TypedDict):
    NotificationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class JoinDomainOutputTypeDef(TypedDict):
    GatewayARN: str
    ActiveDirectoryStatus: ActiveDirectoryStatusType
    ResponseMetadata: ResponseMetadataTypeDef

class ListTagsForResourceOutputTypeDef(TypedDict):
    ResourceARN: str
    Marker: str
    Tags: List[TagTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVolumeInitiatorsOutputTypeDef(TypedDict):
    Initiators: List[str]
    ResponseMetadata: ResponseMetadataTypeDef

class NotifyWhenUploadedOutputTypeDef(TypedDict):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RefreshCacheOutputTypeDef(TypedDict):
    FileShareARN: str
    NotificationId: str
    ResponseMetadata: ResponseMetadataTypeDef

class RemoveTagsFromResourceOutputTypeDef(TypedDict):
    ResourceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class ResetCacheOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class RetrieveTapeArchiveOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class RetrieveTapeRecoveryPointOutputTypeDef(TypedDict):
    TapeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetLocalConsolePasswordOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class SetSMBGuestPasswordOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class ShutdownGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartAvailabilityMonitorTestOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCacheReportOutputTypeDef(TypedDict):
    CacheReportARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartGatewayOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateAutomaticTapeCreationPolicyOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBandwidthRateLimitOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBandwidthRateLimitScheduleOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateChapCredentialsOutputTypeDef(TypedDict):
    TargetARN: str
    InitiatorName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateFileSystemAssociationOutputTypeDef(TypedDict):
    FileSystemAssociationARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewayInformationOutputTypeDef(TypedDict):
    GatewayARN: str
    GatewayName: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateGatewaySoftwareNowOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMaintenanceStartTimeOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateNFSFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBFileShareOutputTypeDef(TypedDict):
    FileShareARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBFileShareVisibilityOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBLocalGroupsOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBSecurityStrategyOutputTypeDef(TypedDict):
    GatewayARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSnapshotScheduleOutputTypeDef(TypedDict):
    VolumeARN: str
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateVTLDeviceTypeOutputTypeDef(TypedDict):
    VTLDeviceARN: str
    ResponseMetadata: ResponseMetadataTypeDef

CreateSMBFileShareInputTypeDef = TypedDict(
    "CreateSMBFileShareInputTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "SMBACLEnabled": NotRequired[bool],
        "AccessBasedEnumeration": NotRequired[bool],
        "AdminUserList": NotRequired[Sequence[str]],
        "ValidUserList": NotRequired[Sequence[str]],
        "InvalidUserList": NotRequired[Sequence[str]],
        "AuditDestinationARN": NotRequired[str],
        "Authentication": NotRequired[str],
        "CaseSensitivity": NotRequired[CaseSensitivityType],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "OplocksEnabled": NotRequired[bool],
    },
)
SMBFileShareInfoTypeDef = TypedDict(
    "SMBFileShareInfoTypeDef",
    {
        "FileShareARN": NotRequired[str],
        "FileShareId": NotRequired[str],
        "FileShareStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Path": NotRequired[str],
        "Role": NotRequired[str],
        "LocationARN": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "SMBACLEnabled": NotRequired[bool],
        "AccessBasedEnumeration": NotRequired[bool],
        "AdminUserList": NotRequired[List[str]],
        "ValidUserList": NotRequired[List[str]],
        "InvalidUserList": NotRequired[List[str]],
        "AuditDestinationARN": NotRequired[str],
        "Authentication": NotRequired[str],
        "CaseSensitivity": NotRequired[CaseSensitivityType],
        "Tags": NotRequired[List[TagTypeDef]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "OplocksEnabled": NotRequired[bool],
    },
)

class UpdateFileSystemAssociationInputTypeDef(TypedDict):
    FileSystemAssociationARN: str
    UserName: NotRequired[str]
    Password: NotRequired[str]
    AuditDestinationARN: NotRequired[str]
    CacheAttributes: NotRequired[CacheAttributesTypeDef]

UpdateSMBFileShareInputTypeDef = TypedDict(
    "UpdateSMBFileShareInputTypeDef",
    {
        "FileShareARN": str,
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "SMBACLEnabled": NotRequired[bool],
        "AccessBasedEnumeration": NotRequired[bool],
        "AdminUserList": NotRequired[Sequence[str]],
        "ValidUserList": NotRequired[Sequence[str]],
        "InvalidUserList": NotRequired[Sequence[str]],
        "AuditDestinationARN": NotRequired[str],
        "CaseSensitivity": NotRequired[CaseSensitivityType],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "OplocksEnabled": NotRequired[bool],
    },
)

class AutomaticTapeCreationPolicyInfoTypeDef(TypedDict):
    AutomaticTapeCreationRules: NotRequired[List[AutomaticTapeCreationRuleTypeDef]]
    GatewayARN: NotRequired[str]

class UpdateAutomaticTapeCreationPolicyInputTypeDef(TypedDict):
    AutomaticTapeCreationRules: Sequence[AutomaticTapeCreationRuleTypeDef]
    GatewayARN: str

class DescribeBandwidthRateLimitScheduleOutputTypeDef(TypedDict):
    GatewayARN: str
    BandwidthRateLimitIntervals: List[BandwidthRateLimitIntervalOutputTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

BandwidthRateLimitIntervalUnionTypeDef = Union[
    BandwidthRateLimitIntervalTypeDef, BandwidthRateLimitIntervalOutputTypeDef
]

class CacheReportInfoTypeDef(TypedDict):
    CacheReportARN: NotRequired[str]
    CacheReportStatus: NotRequired[CacheReportStatusType]
    ReportCompletionPercent: NotRequired[int]
    EndTime: NotRequired[datetime]
    Role: NotRequired[str]
    FileShareARN: NotRequired[str]
    LocationARN: NotRequired[str]
    StartTime: NotRequired[datetime]
    InclusionFilters: NotRequired[List[CacheReportFilterOutputTypeDef]]
    ExclusionFilters: NotRequired[List[CacheReportFilterOutputTypeDef]]
    ReportName: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]

CacheReportFilterUnionTypeDef = Union[CacheReportFilterTypeDef, CacheReportFilterOutputTypeDef]

class CachediSCSIVolumeTypeDef(TypedDict):
    VolumeARN: NotRequired[str]
    VolumeId: NotRequired[str]
    VolumeType: NotRequired[str]
    VolumeStatus: NotRequired[str]
    VolumeAttachmentStatus: NotRequired[str]
    VolumeSizeInBytes: NotRequired[int]
    VolumeProgress: NotRequired[float]
    SourceSnapshotId: NotRequired[str]
    VolumeiSCSIAttributes: NotRequired[VolumeiSCSIAttributesTypeDef]
    CreatedDate: NotRequired[datetime]
    VolumeUsedInBytes: NotRequired[int]
    KMSKey: NotRequired[str]
    TargetName: NotRequired[str]

class StorediSCSIVolumeTypeDef(TypedDict):
    VolumeARN: NotRequired[str]
    VolumeId: NotRequired[str]
    VolumeType: NotRequired[str]
    VolumeStatus: NotRequired[str]
    VolumeAttachmentStatus: NotRequired[str]
    VolumeSizeInBytes: NotRequired[int]
    VolumeProgress: NotRequired[float]
    VolumeDiskId: NotRequired[str]
    SourceSnapshotId: NotRequired[str]
    PreservedExistingData: NotRequired[bool]
    VolumeiSCSIAttributes: NotRequired[VolumeiSCSIAttributesTypeDef]
    CreatedDate: NotRequired[datetime]
    VolumeUsedInBytes: NotRequired[int]
    KMSKey: NotRequired[str]
    TargetName: NotRequired[str]

class DescribeChapCredentialsOutputTypeDef(TypedDict):
    ChapCredentials: List[ChapInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

CreateNFSFileShareInputTypeDef = TypedDict(
    "CreateNFSFileShareInputTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
        "NFSFileShareDefaults": NotRequired[NFSFileShareDefaultsTypeDef],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ClientList": NotRequired[Sequence[str]],
        "Squash": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "Tags": NotRequired[Sequence[TagTypeDef]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
    },
)
NFSFileShareInfoTypeDef = TypedDict(
    "NFSFileShareInfoTypeDef",
    {
        "NFSFileShareDefaults": NotRequired[NFSFileShareDefaultsTypeDef],
        "FileShareARN": NotRequired[str],
        "FileShareId": NotRequired[str],
        "FileShareStatus": NotRequired[str],
        "GatewayARN": NotRequired[str],
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "Path": NotRequired[str],
        "Role": NotRequired[str],
        "LocationARN": NotRequired[str],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ClientList": NotRequired[List[str]],
        "Squash": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "Tags": NotRequired[List[TagTypeDef]],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "VPCEndpointDNSName": NotRequired[str],
        "BucketRegion": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
    },
)
UpdateNFSFileShareInputTypeDef = TypedDict(
    "UpdateNFSFileShareInputTypeDef",
    {
        "FileShareARN": str,
        "EncryptionType": NotRequired[EncryptionTypeType],
        "KMSEncrypted": NotRequired[bool],
        "KMSKey": NotRequired[str],
        "NFSFileShareDefaults": NotRequired[NFSFileShareDefaultsTypeDef],
        "DefaultStorageClass": NotRequired[str],
        "ObjectACL": NotRequired[ObjectACLType],
        "ClientList": NotRequired[Sequence[str]],
        "Squash": NotRequired[str],
        "ReadOnly": NotRequired[bool],
        "GuessMIMETypeEnabled": NotRequired[bool],
        "RequesterPays": NotRequired[bool],
        "FileShareName": NotRequired[str],
        "CacheAttributes": NotRequired[CacheAttributesTypeDef],
        "NotificationPolicy": NotRequired[str],
        "AuditDestinationARN": NotRequired[str],
    },
)

class DescribeGatewayInformationOutputTypeDef(TypedDict):
    GatewayARN: str
    GatewayId: str
    GatewayName: str
    GatewayTimezone: str
    GatewayState: str
    GatewayNetworkInterfaces: List[NetworkInterfaceTypeDef]
    GatewayType: str
    NextUpdateAvailabilityDate: str
    LastSoftwareUpdate: str
    Ec2InstanceId: str
    Ec2InstanceRegion: str
    Tags: List[TagTypeDef]
    VPCEndpoint: str
    CloudWatchLogGroupARN: str
    HostEnvironment: HostEnvironmentType
    EndpointType: str
    SoftwareUpdatesEndDate: str
    DeprecationDate: str
    GatewayCapacity: GatewayCapacityType
    SupportedGatewayCapacities: List[GatewayCapacityType]
    HostEnvironmentId: str
    SoftwareVersion: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeMaintenanceStartTimeOutputTypeDef(TypedDict):
    GatewayARN: str
    HourOfDay: int
    MinuteOfHour: int
    DayOfWeek: int
    DayOfMonth: int
    Timezone: str
    SoftwareUpdatePreferences: SoftwareUpdatePreferencesTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateMaintenanceStartTimeInputTypeDef(TypedDict):
    GatewayARN: str
    HourOfDay: NotRequired[int]
    MinuteOfHour: NotRequired[int]
    DayOfWeek: NotRequired[int]
    DayOfMonth: NotRequired[int]
    SoftwareUpdatePreferences: NotRequired[SoftwareUpdatePreferencesTypeDef]

class DescribeSMBSettingsOutputTypeDef(TypedDict):
    GatewayARN: str
    DomainName: str
    ActiveDirectoryStatus: ActiveDirectoryStatusType
    SMBGuestPasswordSet: bool
    SMBSecurityStrategy: SMBSecurityStrategyType
    FileSharesVisible: bool
    SMBLocalGroups: SMBLocalGroupsOutputTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTapeArchivesInputPaginateTypeDef(TypedDict):
    TapeARNs: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTapeRecoveryPointsInputPaginateTypeDef(TypedDict):
    GatewayARN: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTapesInputPaginateTypeDef(TypedDict):
    GatewayARN: str
    TapeARNs: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeVTLDevicesInputPaginateTypeDef(TypedDict):
    GatewayARN: str
    VTLDeviceARNs: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListCacheReportsInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFileSharesInputPaginateTypeDef(TypedDict):
    GatewayARN: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListFileSystemAssociationsInputPaginateTypeDef(TypedDict):
    GatewayARN: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListGatewaysInputPaginateTypeDef(TypedDict):
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTagsForResourceInputPaginateTypeDef(TypedDict):
    ResourceARN: str
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTapePoolsInputPaginateTypeDef(TypedDict):
    PoolARNs: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListTapesInputPaginateTypeDef(TypedDict):
    TapeARNs: NotRequired[Sequence[str]]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class ListVolumesInputPaginateTypeDef(TypedDict):
    GatewayARN: NotRequired[str]
    PaginationConfig: NotRequired[PaginatorConfigTypeDef]

class DescribeTapeArchivesOutputTypeDef(TypedDict):
    TapeArchives: List[TapeArchiveTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTapeRecoveryPointsOutputTypeDef(TypedDict):
    GatewayARN: str
    TapeRecoveryPointInfos: List[TapeRecoveryPointInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeTapesOutputTypeDef(TypedDict):
    Tapes: List[TapeTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class VTLDeviceTypeDef(TypedDict):
    VTLDeviceARN: NotRequired[str]
    VTLDeviceType: NotRequired[str]
    VTLDeviceVendor: NotRequired[str]
    VTLDeviceProductIdentifier: NotRequired[str]
    DeviceiSCSIAttributes: NotRequired[DeviceiSCSIAttributesTypeDef]

class ListLocalDisksOutputTypeDef(TypedDict):
    GatewayARN: str
    Disks: List[DiskTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

EndpointNetworkConfigurationUnionTypeDef = Union[
    EndpointNetworkConfigurationTypeDef, EndpointNetworkConfigurationOutputTypeDef
]

class ListFileSharesOutputTypeDef(TypedDict):
    Marker: str
    NextMarker: str
    FileShareInfoList: List[FileShareInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class FileSystemAssociationInfoTypeDef(TypedDict):
    FileSystemAssociationARN: NotRequired[str]
    LocationARN: NotRequired[str]
    FileSystemAssociationStatus: NotRequired[str]
    AuditDestinationARN: NotRequired[str]
    GatewayARN: NotRequired[str]
    Tags: NotRequired[List[TagTypeDef]]
    CacheAttributes: NotRequired[CacheAttributesTypeDef]
    EndpointNetworkConfiguration: NotRequired[EndpointNetworkConfigurationOutputTypeDef]
    FileSystemAssociationStatusDetails: NotRequired[List[FileSystemAssociationStatusDetailTypeDef]]

class ListFileSystemAssociationsOutputTypeDef(TypedDict):
    Marker: str
    NextMarker: str
    FileSystemAssociationSummaryList: List[FileSystemAssociationSummaryTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListGatewaysOutputTypeDef(TypedDict):
    Gateways: List[GatewayInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTapePoolsOutputTypeDef(TypedDict):
    PoolInfos: List[PoolInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListTapesOutputTypeDef(TypedDict):
    TapeInfos: List[TapeInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class ListVolumeRecoveryPointsOutputTypeDef(TypedDict):
    GatewayARN: str
    VolumeRecoveryPointInfos: List[VolumeRecoveryPointInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListVolumesOutputTypeDef(TypedDict):
    GatewayARN: str
    Marker: str
    VolumeInfos: List[VolumeInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

SMBLocalGroupsUnionTypeDef = Union[SMBLocalGroupsTypeDef, SMBLocalGroupsOutputTypeDef]

class DescribeSMBFileSharesOutputTypeDef(TypedDict):
    SMBFileShareInfoList: List[SMBFileShareInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class ListAutomaticTapeCreationPoliciesOutputTypeDef(TypedDict):
    AutomaticTapeCreationPolicyInfos: List[AutomaticTapeCreationPolicyInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateBandwidthRateLimitScheduleInputTypeDef(TypedDict):
    GatewayARN: str
    BandwidthRateLimitIntervals: Sequence[BandwidthRateLimitIntervalUnionTypeDef]

class DescribeCacheReportOutputTypeDef(TypedDict):
    CacheReportInfo: CacheReportInfoTypeDef
    ResponseMetadata: ResponseMetadataTypeDef

class ListCacheReportsOutputTypeDef(TypedDict):
    CacheReportList: List[CacheReportInfoTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class StartCacheReportInputTypeDef(TypedDict):
    FileShareARN: str
    Role: str
    LocationARN: str
    BucketRegion: str
    ClientToken: str
    VPCEndpointDNSName: NotRequired[str]
    InclusionFilters: NotRequired[Sequence[CacheReportFilterUnionTypeDef]]
    ExclusionFilters: NotRequired[Sequence[CacheReportFilterUnionTypeDef]]
    Tags: NotRequired[Sequence[TagTypeDef]]

class DescribeCachediSCSIVolumesOutputTypeDef(TypedDict):
    CachediSCSIVolumes: List[CachediSCSIVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeStorediSCSIVolumesOutputTypeDef(TypedDict):
    StorediSCSIVolumes: List[StorediSCSIVolumeTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeNFSFileSharesOutputTypeDef(TypedDict):
    NFSFileShareInfoList: List[NFSFileShareInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class DescribeVTLDevicesOutputTypeDef(TypedDict):
    GatewayARN: str
    VTLDevices: List[VTLDeviceTypeDef]
    Marker: str
    ResponseMetadata: ResponseMetadataTypeDef

class AssociateFileSystemInputTypeDef(TypedDict):
    UserName: str
    Password: str
    ClientToken: str
    GatewayARN: str
    LocationARN: str
    Tags: NotRequired[Sequence[TagTypeDef]]
    AuditDestinationARN: NotRequired[str]
    CacheAttributes: NotRequired[CacheAttributesTypeDef]
    EndpointNetworkConfiguration: NotRequired[EndpointNetworkConfigurationUnionTypeDef]

class DescribeFileSystemAssociationsOutputTypeDef(TypedDict):
    FileSystemAssociationInfoList: List[FileSystemAssociationInfoTypeDef]
    ResponseMetadata: ResponseMetadataTypeDef

class UpdateSMBLocalGroupsInputTypeDef(TypedDict):
    GatewayARN: str
    SMBLocalGroups: SMBLocalGroupsUnionTypeDef
