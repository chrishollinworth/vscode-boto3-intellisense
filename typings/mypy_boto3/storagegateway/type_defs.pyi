"""
Type annotations for storagegateway service type definitions.

[Open documentation](https://vemel.github.io/boto3_stubs_docs/mypy_boto3_storagegateway/type_defs.html)

Usage::

    ```python
    from mypy_boto3_storagegateway.type_defs import ActivateGatewayInputRequestTypeDef

    data: ActivateGatewayInputRequestTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Any, Dict, List

from .literals import (
    ActiveDirectoryStatusType,
    AvailabilityMonitorTestStatusType,
    CaseSensitivityType,
    FileShareTypeType,
    GatewayCapacityType,
    HostEnvironmentType,
    ObjectACLType,
    PoolStatusType,
    RetentionLockTypeType,
    SMBSecurityStrategyType,
    TapeStorageClassType,
)

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "ActivateGatewayInputRequestTypeDef",
    "ActivateGatewayOutputTypeDef",
    "AddCacheInputRequestTypeDef",
    "AddCacheOutputTypeDef",
    "AddTagsToResourceInputRequestTypeDef",
    "AddTagsToResourceOutputTypeDef",
    "AddUploadBufferInputRequestTypeDef",
    "AddUploadBufferOutputTypeDef",
    "AddWorkingStorageInputRequestTypeDef",
    "AddWorkingStorageOutputTypeDef",
    "AssignTapePoolInputRequestTypeDef",
    "AssignTapePoolOutputTypeDef",
    "AssociateFileSystemInputRequestTypeDef",
    "AssociateFileSystemOutputTypeDef",
    "AttachVolumeInputRequestTypeDef",
    "AttachVolumeOutputTypeDef",
    "AutomaticTapeCreationPolicyInfoTypeDef",
    "AutomaticTapeCreationRuleTypeDef",
    "BandwidthRateLimitIntervalTypeDef",
    "CacheAttributesTypeDef",
    "CachediSCSIVolumeTypeDef",
    "CancelArchivalInputRequestTypeDef",
    "CancelArchivalOutputTypeDef",
    "CancelRetrievalInputRequestTypeDef",
    "CancelRetrievalOutputTypeDef",
    "ChapInfoTypeDef",
    "CreateCachediSCSIVolumeInputRequestTypeDef",
    "CreateCachediSCSIVolumeOutputTypeDef",
    "CreateNFSFileShareInputRequestTypeDef",
    "CreateNFSFileShareOutputTypeDef",
    "CreateSMBFileShareInputRequestTypeDef",
    "CreateSMBFileShareOutputTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef",
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    "CreateSnapshotInputRequestTypeDef",
    "CreateSnapshotOutputTypeDef",
    "CreateStorediSCSIVolumeInputRequestTypeDef",
    "CreateStorediSCSIVolumeOutputTypeDef",
    "CreateTapePoolInputRequestTypeDef",
    "CreateTapePoolOutputTypeDef",
    "CreateTapeWithBarcodeInputRequestTypeDef",
    "CreateTapeWithBarcodeOutputTypeDef",
    "CreateTapesInputRequestTypeDef",
    "CreateTapesOutputTypeDef",
    "DeleteAutomaticTapeCreationPolicyInputRequestTypeDef",
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    "DeleteBandwidthRateLimitInputRequestTypeDef",
    "DeleteBandwidthRateLimitOutputTypeDef",
    "DeleteChapCredentialsInputRequestTypeDef",
    "DeleteChapCredentialsOutputTypeDef",
    "DeleteFileShareInputRequestTypeDef",
    "DeleteFileShareOutputTypeDef",
    "DeleteGatewayInputRequestTypeDef",
    "DeleteGatewayOutputTypeDef",
    "DeleteSnapshotScheduleInputRequestTypeDef",
    "DeleteSnapshotScheduleOutputTypeDef",
    "DeleteTapeArchiveInputRequestTypeDef",
    "DeleteTapeArchiveOutputTypeDef",
    "DeleteTapeInputRequestTypeDef",
    "DeleteTapeOutputTypeDef",
    "DeleteTapePoolInputRequestTypeDef",
    "DeleteTapePoolOutputTypeDef",
    "DeleteVolumeInputRequestTypeDef",
    "DeleteVolumeOutputTypeDef",
    "DescribeAvailabilityMonitorTestInputRequestTypeDef",
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    "DescribeBandwidthRateLimitInputRequestTypeDef",
    "DescribeBandwidthRateLimitOutputTypeDef",
    "DescribeBandwidthRateLimitScheduleInputRequestTypeDef",
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    "DescribeCacheInputRequestTypeDef",
    "DescribeCacheOutputTypeDef",
    "DescribeCachediSCSIVolumesInputRequestTypeDef",
    "DescribeCachediSCSIVolumesOutputTypeDef",
    "DescribeChapCredentialsInputRequestTypeDef",
    "DescribeChapCredentialsOutputTypeDef",
    "DescribeFileSystemAssociationsInputRequestTypeDef",
    "DescribeFileSystemAssociationsOutputTypeDef",
    "DescribeGatewayInformationInputRequestTypeDef",
    "DescribeGatewayInformationOutputTypeDef",
    "DescribeMaintenanceStartTimeInputRequestTypeDef",
    "DescribeMaintenanceStartTimeOutputTypeDef",
    "DescribeNFSFileSharesInputRequestTypeDef",
    "DescribeNFSFileSharesOutputTypeDef",
    "DescribeSMBFileSharesInputRequestTypeDef",
    "DescribeSMBFileSharesOutputTypeDef",
    "DescribeSMBSettingsInputRequestTypeDef",
    "DescribeSMBSettingsOutputTypeDef",
    "DescribeSnapshotScheduleInputRequestTypeDef",
    "DescribeSnapshotScheduleOutputTypeDef",
    "DescribeStorediSCSIVolumesInputRequestTypeDef",
    "DescribeStorediSCSIVolumesOutputTypeDef",
    "DescribeTapeArchivesInputRequestTypeDef",
    "DescribeTapeArchivesOutputTypeDef",
    "DescribeTapeRecoveryPointsInputRequestTypeDef",
    "DescribeTapeRecoveryPointsOutputTypeDef",
    "DescribeTapesInputRequestTypeDef",
    "DescribeTapesOutputTypeDef",
    "DescribeUploadBufferInputRequestTypeDef",
    "DescribeUploadBufferOutputTypeDef",
    "DescribeVTLDevicesInputRequestTypeDef",
    "DescribeVTLDevicesOutputTypeDef",
    "DescribeWorkingStorageInputRequestTypeDef",
    "DescribeWorkingStorageOutputTypeDef",
    "DetachVolumeInputRequestTypeDef",
    "DetachVolumeOutputTypeDef",
    "DeviceiSCSIAttributesTypeDef",
    "DisableGatewayInputRequestTypeDef",
    "DisableGatewayOutputTypeDef",
    "DisassociateFileSystemInputRequestTypeDef",
    "DisassociateFileSystemOutputTypeDef",
    "DiskTypeDef",
    "EndpointNetworkConfigurationTypeDef",
    "FileShareInfoTypeDef",
    "FileSystemAssociationInfoTypeDef",
    "FileSystemAssociationSummaryTypeDef",
    "GatewayInfoTypeDef",
    "JoinDomainInputRequestTypeDef",
    "JoinDomainOutputTypeDef",
    "ListAutomaticTapeCreationPoliciesInputRequestTypeDef",
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    "ListFileSharesInputRequestTypeDef",
    "ListFileSharesOutputTypeDef",
    "ListFileSystemAssociationsInputRequestTypeDef",
    "ListFileSystemAssociationsOutputTypeDef",
    "ListGatewaysInputRequestTypeDef",
    "ListGatewaysOutputTypeDef",
    "ListLocalDisksInputRequestTypeDef",
    "ListLocalDisksOutputTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTapePoolsInputRequestTypeDef",
    "ListTapePoolsOutputTypeDef",
    "ListTapesInputRequestTypeDef",
    "ListTapesOutputTypeDef",
    "ListVolumeInitiatorsInputRequestTypeDef",
    "ListVolumeInitiatorsOutputTypeDef",
    "ListVolumeRecoveryPointsInputRequestTypeDef",
    "ListVolumeRecoveryPointsOutputTypeDef",
    "ListVolumesInputRequestTypeDef",
    "ListVolumesOutputTypeDef",
    "NFSFileShareDefaultsTypeDef",
    "NFSFileShareInfoTypeDef",
    "NetworkInterfaceTypeDef",
    "NotifyWhenUploadedInputRequestTypeDef",
    "NotifyWhenUploadedOutputTypeDef",
    "PaginatorConfigTypeDef",
    "PoolInfoTypeDef",
    "RefreshCacheInputRequestTypeDef",
    "RefreshCacheOutputTypeDef",
    "RemoveTagsFromResourceInputRequestTypeDef",
    "RemoveTagsFromResourceOutputTypeDef",
    "ResetCacheInputRequestTypeDef",
    "ResetCacheOutputTypeDef",
    "ResponseMetadataTypeDef",
    "RetrieveTapeArchiveInputRequestTypeDef",
    "RetrieveTapeArchiveOutputTypeDef",
    "RetrieveTapeRecoveryPointInputRequestTypeDef",
    "RetrieveTapeRecoveryPointOutputTypeDef",
    "SMBFileShareInfoTypeDef",
    "SetLocalConsolePasswordInputRequestTypeDef",
    "SetLocalConsolePasswordOutputTypeDef",
    "SetSMBGuestPasswordInputRequestTypeDef",
    "SetSMBGuestPasswordOutputTypeDef",
    "ShutdownGatewayInputRequestTypeDef",
    "ShutdownGatewayOutputTypeDef",
    "StartAvailabilityMonitorTestInputRequestTypeDef",
    "StartAvailabilityMonitorTestOutputTypeDef",
    "StartGatewayInputRequestTypeDef",
    "StartGatewayOutputTypeDef",
    "StorediSCSIVolumeTypeDef",
    "TagTypeDef",
    "TapeArchiveTypeDef",
    "TapeInfoTypeDef",
    "TapeRecoveryPointInfoTypeDef",
    "TapeTypeDef",
    "UpdateAutomaticTapeCreationPolicyInputRequestTypeDef",
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    "UpdateBandwidthRateLimitInputRequestTypeDef",
    "UpdateBandwidthRateLimitOutputTypeDef",
    "UpdateBandwidthRateLimitScheduleInputRequestTypeDef",
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    "UpdateChapCredentialsInputRequestTypeDef",
    "UpdateChapCredentialsOutputTypeDef",
    "UpdateFileSystemAssociationInputRequestTypeDef",
    "UpdateFileSystemAssociationOutputTypeDef",
    "UpdateGatewayInformationInputRequestTypeDef",
    "UpdateGatewayInformationOutputTypeDef",
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    "UpdateGatewaySoftwareNowOutputTypeDef",
    "UpdateMaintenanceStartTimeInputRequestTypeDef",
    "UpdateMaintenanceStartTimeOutputTypeDef",
    "UpdateNFSFileShareInputRequestTypeDef",
    "UpdateNFSFileShareOutputTypeDef",
    "UpdateSMBFileShareInputRequestTypeDef",
    "UpdateSMBFileShareOutputTypeDef",
    "UpdateSMBFileShareVisibilityInputRequestTypeDef",
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    "UpdateSMBSecurityStrategyInputRequestTypeDef",
    "UpdateSMBSecurityStrategyOutputTypeDef",
    "UpdateSnapshotScheduleInputRequestTypeDef",
    "UpdateSnapshotScheduleOutputTypeDef",
    "UpdateVTLDeviceTypeInputRequestTypeDef",
    "UpdateVTLDeviceTypeOutputTypeDef",
    "VTLDeviceTypeDef",
    "VolumeInfoTypeDef",
    "VolumeRecoveryPointInfoTypeDef",
    "VolumeiSCSIAttributesTypeDef",
)

_RequiredActivateGatewayInputRequestTypeDef = TypedDict(
    "_RequiredActivateGatewayInputRequestTypeDef",
    {
        "ActivationKey": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayRegion": str,
    },
)
_OptionalActivateGatewayInputRequestTypeDef = TypedDict(
    "_OptionalActivateGatewayInputRequestTypeDef",
    {
        "GatewayType": str,
        "TapeDriveType": str,
        "MediumChangerType": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class ActivateGatewayInputRequestTypeDef(
    _RequiredActivateGatewayInputRequestTypeDef, _OptionalActivateGatewayInputRequestTypeDef
):
    pass

ActivateGatewayOutputTypeDef = TypedDict(
    "ActivateGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddCacheInputRequestTypeDef = TypedDict(
    "AddCacheInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
    },
)

AddCacheOutputTypeDef = TypedDict(
    "AddCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddTagsToResourceInputRequestTypeDef = TypedDict(
    "AddTagsToResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": List["TagTypeDef"],
    },
)

AddTagsToResourceOutputTypeDef = TypedDict(
    "AddTagsToResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddUploadBufferInputRequestTypeDef = TypedDict(
    "AddUploadBufferInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
    },
)

AddUploadBufferOutputTypeDef = TypedDict(
    "AddUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AddWorkingStorageInputRequestTypeDef = TypedDict(
    "AddWorkingStorageInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
    },
)

AddWorkingStorageOutputTypeDef = TypedDict(
    "AddWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssignTapePoolInputRequestTypeDef = TypedDict(
    "_RequiredAssignTapePoolInputRequestTypeDef",
    {
        "TapeARN": str,
        "PoolId": str,
    },
)
_OptionalAssignTapePoolInputRequestTypeDef = TypedDict(
    "_OptionalAssignTapePoolInputRequestTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)

class AssignTapePoolInputRequestTypeDef(
    _RequiredAssignTapePoolInputRequestTypeDef, _OptionalAssignTapePoolInputRequestTypeDef
):
    pass

AssignTapePoolOutputTypeDef = TypedDict(
    "AssignTapePoolOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAssociateFileSystemInputRequestTypeDef = TypedDict(
    "_RequiredAssociateFileSystemInputRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
        "ClientToken": str,
        "GatewayARN": str,
        "LocationARN": str,
    },
)
_OptionalAssociateFileSystemInputRequestTypeDef = TypedDict(
    "_OptionalAssociateFileSystemInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
        "AuditDestinationARN": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "EndpointNetworkConfiguration": "EndpointNetworkConfigurationTypeDef",
    },
    total=False,
)

class AssociateFileSystemInputRequestTypeDef(
    _RequiredAssociateFileSystemInputRequestTypeDef, _OptionalAssociateFileSystemInputRequestTypeDef
):
    pass

AssociateFileSystemOutputTypeDef = TypedDict(
    "AssociateFileSystemOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredAttachVolumeInputRequestTypeDef = TypedDict(
    "_RequiredAttachVolumeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "VolumeARN": str,
        "NetworkInterfaceId": str,
    },
)
_OptionalAttachVolumeInputRequestTypeDef = TypedDict(
    "_OptionalAttachVolumeInputRequestTypeDef",
    {
        "TargetName": str,
        "DiskId": str,
    },
    total=False,
)

class AttachVolumeInputRequestTypeDef(
    _RequiredAttachVolumeInputRequestTypeDef, _OptionalAttachVolumeInputRequestTypeDef
):
    pass

AttachVolumeOutputTypeDef = TypedDict(
    "AttachVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

AutomaticTapeCreationPolicyInfoTypeDef = TypedDict(
    "AutomaticTapeCreationPolicyInfoTypeDef",
    {
        "AutomaticTapeCreationRules": List["AutomaticTapeCreationRuleTypeDef"],
        "GatewayARN": str,
    },
    total=False,
)

_RequiredAutomaticTapeCreationRuleTypeDef = TypedDict(
    "_RequiredAutomaticTapeCreationRuleTypeDef",
    {
        "TapeBarcodePrefix": str,
        "PoolId": str,
        "TapeSizeInBytes": int,
        "MinimumNumTapes": int,
    },
)
_OptionalAutomaticTapeCreationRuleTypeDef = TypedDict(
    "_OptionalAutomaticTapeCreationRuleTypeDef",
    {
        "Worm": bool,
    },
    total=False,
)

class AutomaticTapeCreationRuleTypeDef(
    _RequiredAutomaticTapeCreationRuleTypeDef, _OptionalAutomaticTapeCreationRuleTypeDef
):
    pass

_RequiredBandwidthRateLimitIntervalTypeDef = TypedDict(
    "_RequiredBandwidthRateLimitIntervalTypeDef",
    {
        "StartHourOfDay": int,
        "StartMinuteOfHour": int,
        "EndHourOfDay": int,
        "EndMinuteOfHour": int,
        "DaysOfWeek": List[int],
    },
)
_OptionalBandwidthRateLimitIntervalTypeDef = TypedDict(
    "_OptionalBandwidthRateLimitIntervalTypeDef",
    {
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
    },
    total=False,
)

class BandwidthRateLimitIntervalTypeDef(
    _RequiredBandwidthRateLimitIntervalTypeDef, _OptionalBandwidthRateLimitIntervalTypeDef
):
    pass

CacheAttributesTypeDef = TypedDict(
    "CacheAttributesTypeDef",
    {
        "CacheStaleTimeoutInSeconds": int,
    },
    total=False,
)

CachediSCSIVolumeTypeDef = TypedDict(
    "CachediSCSIVolumeTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "SourceSnapshotId": str,
        "VolumeiSCSIAttributes": "VolumeiSCSIAttributesTypeDef",
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)

CancelArchivalInputRequestTypeDef = TypedDict(
    "CancelArchivalInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)

CancelArchivalOutputTypeDef = TypedDict(
    "CancelArchivalOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

CancelRetrievalInputRequestTypeDef = TypedDict(
    "CancelRetrievalInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)

CancelRetrievalOutputTypeDef = TypedDict(
    "CancelRetrievalOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ChapInfoTypeDef = TypedDict(
    "ChapInfoTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
        "SecretToAuthenticateTarget": str,
    },
    total=False,
)

_RequiredCreateCachediSCSIVolumeInputRequestTypeDef = TypedDict(
    "_RequiredCreateCachediSCSIVolumeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "VolumeSizeInBytes": int,
        "TargetName": str,
        "NetworkInterfaceId": str,
        "ClientToken": str,
    },
)
_OptionalCreateCachediSCSIVolumeInputRequestTypeDef = TypedDict(
    "_OptionalCreateCachediSCSIVolumeInputRequestTypeDef",
    {
        "SnapshotId": str,
        "SourceVolumeARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateCachediSCSIVolumeInputRequestTypeDef(
    _RequiredCreateCachediSCSIVolumeInputRequestTypeDef,
    _OptionalCreateCachediSCSIVolumeInputRequestTypeDef,
):
    pass

CreateCachediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateCachediSCSIVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateNFSFileShareInputRequestTypeDef = TypedDict(
    "_RequiredCreateNFSFileShareInputRequestTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
    },
)
_OptionalCreateNFSFileShareInputRequestTypeDef = TypedDict(
    "_OptionalCreateNFSFileShareInputRequestTypeDef",
    {
        "NFSFileShareDefaults": "NFSFileShareDefaultsTypeDef",
        "KMSEncrypted": bool,
        "KMSKey": str,
        "DefaultStorageClass": str,
        "ObjectACL": ObjectACLType,
        "ClientList": List[str],
        "Squash": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "Tags": List["TagTypeDef"],
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
        "VPCEndpointDNSName": str,
        "BucketRegion": str,
    },
    total=False,
)

class CreateNFSFileShareInputRequestTypeDef(
    _RequiredCreateNFSFileShareInputRequestTypeDef, _OptionalCreateNFSFileShareInputRequestTypeDef
):
    pass

CreateNFSFileShareOutputTypeDef = TypedDict(
    "CreateNFSFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSMBFileShareInputRequestTypeDef = TypedDict(
    "_RequiredCreateSMBFileShareInputRequestTypeDef",
    {
        "ClientToken": str,
        "GatewayARN": str,
        "Role": str,
        "LocationARN": str,
    },
)
_OptionalCreateSMBFileShareInputRequestTypeDef = TypedDict(
    "_OptionalCreateSMBFileShareInputRequestTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
        "DefaultStorageClass": str,
        "ObjectACL": ObjectACLType,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "SMBACLEnabled": bool,
        "AccessBasedEnumeration": bool,
        "AdminUserList": List[str],
        "ValidUserList": List[str],
        "InvalidUserList": List[str],
        "AuditDestinationARN": str,
        "Authentication": str,
        "CaseSensitivity": CaseSensitivityType,
        "Tags": List["TagTypeDef"],
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
        "VPCEndpointDNSName": str,
        "BucketRegion": str,
        "OplocksEnabled": bool,
    },
    total=False,
)

class CreateSMBFileShareInputRequestTypeDef(
    _RequiredCreateSMBFileShareInputRequestTypeDef, _OptionalCreateSMBFileShareInputRequestTypeDef
):
    pass

CreateSMBFileShareOutputTypeDef = TypedDict(
    "CreateSMBFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef",
    {
        "VolumeARN": str,
        "SnapshotDescription": str,
    },
)
_OptionalCreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef(
    _RequiredCreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef,
    _OptionalCreateSnapshotFromVolumeRecoveryPointInputRequestTypeDef,
):
    pass

CreateSnapshotFromVolumeRecoveryPointOutputTypeDef = TypedDict(
    "CreateSnapshotFromVolumeRecoveryPointOutputTypeDef",
    {
        "SnapshotId": str,
        "VolumeARN": str,
        "VolumeRecoveryPointTime": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateSnapshotInputRequestTypeDef = TypedDict(
    "_RequiredCreateSnapshotInputRequestTypeDef",
    {
        "VolumeARN": str,
        "SnapshotDescription": str,
    },
)
_OptionalCreateSnapshotInputRequestTypeDef = TypedDict(
    "_OptionalCreateSnapshotInputRequestTypeDef",
    {
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateSnapshotInputRequestTypeDef(
    _RequiredCreateSnapshotInputRequestTypeDef, _OptionalCreateSnapshotInputRequestTypeDef
):
    pass

CreateSnapshotOutputTypeDef = TypedDict(
    "CreateSnapshotOutputTypeDef",
    {
        "VolumeARN": str,
        "SnapshotId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateStorediSCSIVolumeInputRequestTypeDef = TypedDict(
    "_RequiredCreateStorediSCSIVolumeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DiskId": str,
        "PreserveExistingData": bool,
        "TargetName": str,
        "NetworkInterfaceId": str,
    },
)
_OptionalCreateStorediSCSIVolumeInputRequestTypeDef = TypedDict(
    "_OptionalCreateStorediSCSIVolumeInputRequestTypeDef",
    {
        "SnapshotId": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateStorediSCSIVolumeInputRequestTypeDef(
    _RequiredCreateStorediSCSIVolumeInputRequestTypeDef,
    _OptionalCreateStorediSCSIVolumeInputRequestTypeDef,
):
    pass

CreateStorediSCSIVolumeOutputTypeDef = TypedDict(
    "CreateStorediSCSIVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "TargetARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTapePoolInputRequestTypeDef = TypedDict(
    "_RequiredCreateTapePoolInputRequestTypeDef",
    {
        "PoolName": str,
        "StorageClass": TapeStorageClassType,
    },
)
_OptionalCreateTapePoolInputRequestTypeDef = TypedDict(
    "_OptionalCreateTapePoolInputRequestTypeDef",
    {
        "RetentionLockType": RetentionLockTypeType,
        "RetentionLockTimeInDays": int,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTapePoolInputRequestTypeDef(
    _RequiredCreateTapePoolInputRequestTypeDef, _OptionalCreateTapePoolInputRequestTypeDef
):
    pass

CreateTapePoolOutputTypeDef = TypedDict(
    "CreateTapePoolOutputTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTapeWithBarcodeInputRequestTypeDef = TypedDict(
    "_RequiredCreateTapeWithBarcodeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeSizeInBytes": int,
        "TapeBarcode": str,
    },
)
_OptionalCreateTapeWithBarcodeInputRequestTypeDef = TypedDict(
    "_OptionalCreateTapeWithBarcodeInputRequestTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTapeWithBarcodeInputRequestTypeDef(
    _RequiredCreateTapeWithBarcodeInputRequestTypeDef,
    _OptionalCreateTapeWithBarcodeInputRequestTypeDef,
):
    pass

CreateTapeWithBarcodeOutputTypeDef = TypedDict(
    "CreateTapeWithBarcodeOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredCreateTapesInputRequestTypeDef = TypedDict(
    "_RequiredCreateTapesInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeSizeInBytes": int,
        "ClientToken": str,
        "NumTapesToCreate": int,
        "TapeBarcodePrefix": str,
    },
)
_OptionalCreateTapesInputRequestTypeDef = TypedDict(
    "_OptionalCreateTapesInputRequestTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class CreateTapesInputRequestTypeDef(
    _RequiredCreateTapesInputRequestTypeDef, _OptionalCreateTapesInputRequestTypeDef
):
    pass

CreateTapesOutputTypeDef = TypedDict(
    "CreateTapesOutputTypeDef",
    {
        "TapeARNs": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteAutomaticTapeCreationPolicyInputRequestTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DeleteAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "DeleteAutomaticTapeCreationPolicyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "DeleteBandwidthRateLimitInputRequestTypeDef",
    {
        "GatewayARN": str,
        "BandwidthType": str,
    },
)

DeleteBandwidthRateLimitOutputTypeDef = TypedDict(
    "DeleteBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteChapCredentialsInputRequestTypeDef = TypedDict(
    "DeleteChapCredentialsInputRequestTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
    },
)

DeleteChapCredentialsOutputTypeDef = TypedDict(
    "DeleteChapCredentialsOutputTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteFileShareInputRequestTypeDef = TypedDict(
    "_RequiredDeleteFileShareInputRequestTypeDef",
    {
        "FileShareARN": str,
    },
)
_OptionalDeleteFileShareInputRequestTypeDef = TypedDict(
    "_OptionalDeleteFileShareInputRequestTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)

class DeleteFileShareInputRequestTypeDef(
    _RequiredDeleteFileShareInputRequestTypeDef, _OptionalDeleteFileShareInputRequestTypeDef
):
    pass

DeleteFileShareOutputTypeDef = TypedDict(
    "DeleteFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteGatewayInputRequestTypeDef = TypedDict(
    "DeleteGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DeleteGatewayOutputTypeDef = TypedDict(
    "DeleteGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteSnapshotScheduleInputRequestTypeDef = TypedDict(
    "DeleteSnapshotScheduleInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)

DeleteSnapshotScheduleOutputTypeDef = TypedDict(
    "DeleteSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTapeArchiveInputRequestTypeDef = TypedDict(
    "_RequiredDeleteTapeArchiveInputRequestTypeDef",
    {
        "TapeARN": str,
    },
)
_OptionalDeleteTapeArchiveInputRequestTypeDef = TypedDict(
    "_OptionalDeleteTapeArchiveInputRequestTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)

class DeleteTapeArchiveInputRequestTypeDef(
    _RequiredDeleteTapeArchiveInputRequestTypeDef, _OptionalDeleteTapeArchiveInputRequestTypeDef
):
    pass

DeleteTapeArchiveOutputTypeDef = TypedDict(
    "DeleteTapeArchiveOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDeleteTapeInputRequestTypeDef = TypedDict(
    "_RequiredDeleteTapeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "TapeARN": str,
    },
)
_OptionalDeleteTapeInputRequestTypeDef = TypedDict(
    "_OptionalDeleteTapeInputRequestTypeDef",
    {
        "BypassGovernanceRetention": bool,
    },
    total=False,
)

class DeleteTapeInputRequestTypeDef(
    _RequiredDeleteTapeInputRequestTypeDef, _OptionalDeleteTapeInputRequestTypeDef
):
    pass

DeleteTapeOutputTypeDef = TypedDict(
    "DeleteTapeOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteTapePoolInputRequestTypeDef = TypedDict(
    "DeleteTapePoolInputRequestTypeDef",
    {
        "PoolARN": str,
    },
)

DeleteTapePoolOutputTypeDef = TypedDict(
    "DeleteTapePoolOutputTypeDef",
    {
        "PoolARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeleteVolumeInputRequestTypeDef = TypedDict(
    "DeleteVolumeInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)

DeleteVolumeOutputTypeDef = TypedDict(
    "DeleteVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeAvailabilityMonitorTestInputRequestTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "DescribeAvailabilityMonitorTestOutputTypeDef",
    {
        "GatewayARN": str,
        "Status": AvailabilityMonitorTestStatusType,
        "StartTime": datetime,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "DescribeBandwidthRateLimitInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeBandwidthRateLimitOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "DescribeBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": List["BandwidthRateLimitIntervalTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCacheInputRequestTypeDef = TypedDict(
    "DescribeCacheInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeCacheOutputTypeDef = TypedDict(
    "DescribeCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "CacheAllocatedInBytes": int,
        "CacheUsedPercentage": float,
        "CacheDirtyPercentage": float,
        "CacheHitPercentage": float,
        "CacheMissPercentage": float,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeCachediSCSIVolumesInputRequestTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesInputRequestTypeDef",
    {
        "VolumeARNs": List[str],
    },
)

DescribeCachediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeCachediSCSIVolumesOutputTypeDef",
    {
        "CachediSCSIVolumes": List["CachediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeChapCredentialsInputRequestTypeDef = TypedDict(
    "DescribeChapCredentialsInputRequestTypeDef",
    {
        "TargetARN": str,
    },
)

DescribeChapCredentialsOutputTypeDef = TypedDict(
    "DescribeChapCredentialsOutputTypeDef",
    {
        "ChapCredentials": List["ChapInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeFileSystemAssociationsInputRequestTypeDef = TypedDict(
    "DescribeFileSystemAssociationsInputRequestTypeDef",
    {
        "FileSystemAssociationARNList": List[str],
    },
)

DescribeFileSystemAssociationsOutputTypeDef = TypedDict(
    "DescribeFileSystemAssociationsOutputTypeDef",
    {
        "FileSystemAssociationInfoList": List["FileSystemAssociationInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeGatewayInformationInputRequestTypeDef = TypedDict(
    "DescribeGatewayInformationInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeGatewayInformationOutputTypeDef = TypedDict(
    "DescribeGatewayInformationOutputTypeDef",
    {
        "GatewayARN": str,
        "GatewayId": str,
        "GatewayName": str,
        "GatewayTimezone": str,
        "GatewayState": str,
        "GatewayNetworkInterfaces": List["NetworkInterfaceTypeDef"],
        "GatewayType": str,
        "NextUpdateAvailabilityDate": str,
        "LastSoftwareUpdate": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
        "Tags": List["TagTypeDef"],
        "VPCEndpoint": str,
        "CloudWatchLogGroupARN": str,
        "HostEnvironment": HostEnvironmentType,
        "EndpointType": str,
        "SoftwareUpdatesEndDate": str,
        "DeprecationDate": str,
        "GatewayCapacity": GatewayCapacityType,
        "SupportedGatewayCapacities": List[GatewayCapacityType],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeMaintenanceStartTimeOutputTypeDef = TypedDict(
    "DescribeMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
        "DayOfWeek": int,
        "DayOfMonth": int,
        "Timezone": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeNFSFileSharesInputRequestTypeDef = TypedDict(
    "DescribeNFSFileSharesInputRequestTypeDef",
    {
        "FileShareARNList": List[str],
    },
)

DescribeNFSFileSharesOutputTypeDef = TypedDict(
    "DescribeNFSFileSharesOutputTypeDef",
    {
        "NFSFileShareInfoList": List["NFSFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSMBFileSharesInputRequestTypeDef = TypedDict(
    "DescribeSMBFileSharesInputRequestTypeDef",
    {
        "FileShareARNList": List[str],
    },
)

DescribeSMBFileSharesOutputTypeDef = TypedDict(
    "DescribeSMBFileSharesOutputTypeDef",
    {
        "SMBFileShareInfoList": List["SMBFileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSMBSettingsInputRequestTypeDef = TypedDict(
    "DescribeSMBSettingsInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeSMBSettingsOutputTypeDef = TypedDict(
    "DescribeSMBSettingsOutputTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "ActiveDirectoryStatus": ActiveDirectoryStatusType,
        "SMBGuestPasswordSet": bool,
        "SMBSecurityStrategy": SMBSecurityStrategyType,
        "FileSharesVisible": bool,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeSnapshotScheduleInputRequestTypeDef = TypedDict(
    "DescribeSnapshotScheduleInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)

DescribeSnapshotScheduleOutputTypeDef = TypedDict(
    "DescribeSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
        "Description": str,
        "Timezone": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeStorediSCSIVolumesInputRequestTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesInputRequestTypeDef",
    {
        "VolumeARNs": List[str],
    },
)

DescribeStorediSCSIVolumesOutputTypeDef = TypedDict(
    "DescribeStorediSCSIVolumesOutputTypeDef",
    {
        "StorediSCSIVolumes": List["StorediSCSIVolumeTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeTapeArchivesInputRequestTypeDef = TypedDict(
    "DescribeTapeArchivesInputRequestTypeDef",
    {
        "TapeARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

DescribeTapeArchivesOutputTypeDef = TypedDict(
    "DescribeTapeArchivesOutputTypeDef",
    {
        "TapeArchives": List["TapeArchiveTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTapeRecoveryPointsInputRequestTypeDef = TypedDict(
    "_RequiredDescribeTapeRecoveryPointsInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalDescribeTapeRecoveryPointsInputRequestTypeDef = TypedDict(
    "_OptionalDescribeTapeRecoveryPointsInputRequestTypeDef",
    {
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

class DescribeTapeRecoveryPointsInputRequestTypeDef(
    _RequiredDescribeTapeRecoveryPointsInputRequestTypeDef,
    _OptionalDescribeTapeRecoveryPointsInputRequestTypeDef,
):
    pass

DescribeTapeRecoveryPointsOutputTypeDef = TypedDict(
    "DescribeTapeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "TapeRecoveryPointInfos": List["TapeRecoveryPointInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeTapesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeTapesInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalDescribeTapesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeTapesInputRequestTypeDef",
    {
        "TapeARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

class DescribeTapesInputRequestTypeDef(
    _RequiredDescribeTapesInputRequestTypeDef, _OptionalDescribeTapesInputRequestTypeDef
):
    pass

DescribeTapesOutputTypeDef = TypedDict(
    "DescribeTapesOutputTypeDef",
    {
        "Tapes": List["TapeTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeUploadBufferInputRequestTypeDef = TypedDict(
    "DescribeUploadBufferInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeUploadBufferOutputTypeDef = TypedDict(
    "DescribeUploadBufferOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "UploadBufferUsedInBytes": int,
        "UploadBufferAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDescribeVTLDevicesInputRequestTypeDef = TypedDict(
    "_RequiredDescribeVTLDevicesInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalDescribeVTLDevicesInputRequestTypeDef = TypedDict(
    "_OptionalDescribeVTLDevicesInputRequestTypeDef",
    {
        "VTLDeviceARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

class DescribeVTLDevicesInputRequestTypeDef(
    _RequiredDescribeVTLDevicesInputRequestTypeDef, _OptionalDescribeVTLDevicesInputRequestTypeDef
):
    pass

DescribeVTLDevicesOutputTypeDef = TypedDict(
    "DescribeVTLDevicesOutputTypeDef",
    {
        "GatewayARN": str,
        "VTLDevices": List["VTLDeviceTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DescribeWorkingStorageInputRequestTypeDef = TypedDict(
    "DescribeWorkingStorageInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DescribeWorkingStorageOutputTypeDef = TypedDict(
    "DescribeWorkingStorageOutputTypeDef",
    {
        "GatewayARN": str,
        "DiskIds": List[str],
        "WorkingStorageUsedInBytes": int,
        "WorkingStorageAllocatedInBytes": int,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDetachVolumeInputRequestTypeDef = TypedDict(
    "_RequiredDetachVolumeInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)
_OptionalDetachVolumeInputRequestTypeDef = TypedDict(
    "_OptionalDetachVolumeInputRequestTypeDef",
    {
        "ForceDetach": bool,
    },
    total=False,
)

class DetachVolumeInputRequestTypeDef(
    _RequiredDetachVolumeInputRequestTypeDef, _OptionalDetachVolumeInputRequestTypeDef
):
    pass

DetachVolumeOutputTypeDef = TypedDict(
    "DetachVolumeOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DeviceiSCSIAttributesTypeDef = TypedDict(
    "DeviceiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "ChapEnabled": bool,
    },
    total=False,
)

DisableGatewayInputRequestTypeDef = TypedDict(
    "DisableGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

DisableGatewayOutputTypeDef = TypedDict(
    "DisableGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredDisassociateFileSystemInputRequestTypeDef = TypedDict(
    "_RequiredDisassociateFileSystemInputRequestTypeDef",
    {
        "FileSystemAssociationARN": str,
    },
)
_OptionalDisassociateFileSystemInputRequestTypeDef = TypedDict(
    "_OptionalDisassociateFileSystemInputRequestTypeDef",
    {
        "ForceDelete": bool,
    },
    total=False,
)

class DisassociateFileSystemInputRequestTypeDef(
    _RequiredDisassociateFileSystemInputRequestTypeDef,
    _OptionalDisassociateFileSystemInputRequestTypeDef,
):
    pass

DisassociateFileSystemOutputTypeDef = TypedDict(
    "DisassociateFileSystemOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

DiskTypeDef = TypedDict(
    "DiskTypeDef",
    {
        "DiskId": str,
        "DiskPath": str,
        "DiskNode": str,
        "DiskStatus": str,
        "DiskSizeInBytes": int,
        "DiskAllocationType": str,
        "DiskAllocationResource": str,
        "DiskAttributeList": List[str],
    },
    total=False,
)

EndpointNetworkConfigurationTypeDef = TypedDict(
    "EndpointNetworkConfigurationTypeDef",
    {
        "IpAddresses": List[str],
    },
    total=False,
)

FileShareInfoTypeDef = TypedDict(
    "FileShareInfoTypeDef",
    {
        "FileShareType": FileShareTypeType,
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
    },
    total=False,
)

FileSystemAssociationInfoTypeDef = TypedDict(
    "FileSystemAssociationInfoTypeDef",
    {
        "FileSystemAssociationARN": str,
        "LocationARN": str,
        "FileSystemAssociationStatus": str,
        "AuditDestinationARN": str,
        "GatewayARN": str,
        "Tags": List["TagTypeDef"],
        "CacheAttributes": "CacheAttributesTypeDef",
        "EndpointNetworkConfiguration": "EndpointNetworkConfigurationTypeDef",
    },
    total=False,
)

FileSystemAssociationSummaryTypeDef = TypedDict(
    "FileSystemAssociationSummaryTypeDef",
    {
        "FileSystemAssociationId": str,
        "FileSystemAssociationARN": str,
        "FileSystemAssociationStatus": str,
        "GatewayARN": str,
    },
    total=False,
)

GatewayInfoTypeDef = TypedDict(
    "GatewayInfoTypeDef",
    {
        "GatewayId": str,
        "GatewayARN": str,
        "GatewayType": str,
        "GatewayOperationalState": str,
        "GatewayName": str,
        "Ec2InstanceId": str,
        "Ec2InstanceRegion": str,
    },
    total=False,
)

_RequiredJoinDomainInputRequestTypeDef = TypedDict(
    "_RequiredJoinDomainInputRequestTypeDef",
    {
        "GatewayARN": str,
        "DomainName": str,
        "UserName": str,
        "Password": str,
    },
)
_OptionalJoinDomainInputRequestTypeDef = TypedDict(
    "_OptionalJoinDomainInputRequestTypeDef",
    {
        "OrganizationalUnit": str,
        "DomainControllers": List[str],
        "TimeoutInSeconds": int,
    },
    total=False,
)

class JoinDomainInputRequestTypeDef(
    _RequiredJoinDomainInputRequestTypeDef, _OptionalJoinDomainInputRequestTypeDef
):
    pass

JoinDomainOutputTypeDef = TypedDict(
    "JoinDomainOutputTypeDef",
    {
        "GatewayARN": str,
        "ActiveDirectoryStatus": ActiveDirectoryStatusType,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListAutomaticTapeCreationPoliciesInputRequestTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
    total=False,
)

ListAutomaticTapeCreationPoliciesOutputTypeDef = TypedDict(
    "ListAutomaticTapeCreationPoliciesOutputTypeDef",
    {
        "AutomaticTapeCreationPolicyInfos": List["AutomaticTapeCreationPolicyInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFileSharesInputRequestTypeDef = TypedDict(
    "ListFileSharesInputRequestTypeDef",
    {
        "GatewayARN": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

ListFileSharesOutputTypeDef = TypedDict(
    "ListFileSharesOutputTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileShareInfoList": List["FileShareInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListFileSystemAssociationsInputRequestTypeDef = TypedDict(
    "ListFileSystemAssociationsInputRequestTypeDef",
    {
        "GatewayARN": str,
        "Limit": int,
        "Marker": str,
    },
    total=False,
)

ListFileSystemAssociationsOutputTypeDef = TypedDict(
    "ListFileSystemAssociationsOutputTypeDef",
    {
        "Marker": str,
        "NextMarker": str,
        "FileSystemAssociationSummaryList": List["FileSystemAssociationSummaryTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListGatewaysInputRequestTypeDef = TypedDict(
    "ListGatewaysInputRequestTypeDef",
    {
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

ListGatewaysOutputTypeDef = TypedDict(
    "ListGatewaysOutputTypeDef",
    {
        "Gateways": List["GatewayInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListLocalDisksInputRequestTypeDef = TypedDict(
    "ListLocalDisksInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

ListLocalDisksOutputTypeDef = TypedDict(
    "ListLocalDisksOutputTypeDef",
    {
        "GatewayARN": str,
        "Disks": List["DiskTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "Marker": str,
        "Tags": List["TagTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTapePoolsInputRequestTypeDef = TypedDict(
    "ListTapePoolsInputRequestTypeDef",
    {
        "PoolARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

ListTapePoolsOutputTypeDef = TypedDict(
    "ListTapePoolsOutputTypeDef",
    {
        "PoolInfos": List["PoolInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListTapesInputRequestTypeDef = TypedDict(
    "ListTapesInputRequestTypeDef",
    {
        "TapeARNs": List[str],
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

ListTapesOutputTypeDef = TypedDict(
    "ListTapesOutputTypeDef",
    {
        "TapeInfos": List["TapeInfoTypeDef"],
        "Marker": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumeInitiatorsInputRequestTypeDef = TypedDict(
    "ListVolumeInitiatorsInputRequestTypeDef",
    {
        "VolumeARN": str,
    },
)

ListVolumeInitiatorsOutputTypeDef = TypedDict(
    "ListVolumeInitiatorsOutputTypeDef",
    {
        "Initiators": List[str],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumeRecoveryPointsInputRequestTypeDef = TypedDict(
    "ListVolumeRecoveryPointsInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

ListVolumeRecoveryPointsOutputTypeDef = TypedDict(
    "ListVolumeRecoveryPointsOutputTypeDef",
    {
        "GatewayARN": str,
        "VolumeRecoveryPointInfos": List["VolumeRecoveryPointInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ListVolumesInputRequestTypeDef = TypedDict(
    "ListVolumesInputRequestTypeDef",
    {
        "GatewayARN": str,
        "Marker": str,
        "Limit": int,
    },
    total=False,
)

ListVolumesOutputTypeDef = TypedDict(
    "ListVolumesOutputTypeDef",
    {
        "GatewayARN": str,
        "Marker": str,
        "VolumeInfos": List["VolumeInfoTypeDef"],
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

NFSFileShareDefaultsTypeDef = TypedDict(
    "NFSFileShareDefaultsTypeDef",
    {
        "FileMode": str,
        "DirectoryMode": str,
        "GroupId": int,
        "OwnerId": int,
    },
    total=False,
)

NFSFileShareInfoTypeDef = TypedDict(
    "NFSFileShareInfoTypeDef",
    {
        "NFSFileShareDefaults": "NFSFileShareDefaultsTypeDef",
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": ObjectACLType,
        "ClientList": List[str],
        "Squash": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "Tags": List["TagTypeDef"],
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
        "VPCEndpointDNSName": str,
        "BucketRegion": str,
    },
    total=False,
)

NetworkInterfaceTypeDef = TypedDict(
    "NetworkInterfaceTypeDef",
    {
        "Ipv4Address": str,
        "MacAddress": str,
        "Ipv6Address": str,
    },
    total=False,
)

NotifyWhenUploadedInputRequestTypeDef = TypedDict(
    "NotifyWhenUploadedInputRequestTypeDef",
    {
        "FileShareARN": str,
    },
)

NotifyWhenUploadedOutputTypeDef = TypedDict(
    "NotifyWhenUploadedOutputTypeDef",
    {
        "FileShareARN": str,
        "NotificationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

PoolInfoTypeDef = TypedDict(
    "PoolInfoTypeDef",
    {
        "PoolARN": str,
        "PoolName": str,
        "StorageClass": TapeStorageClassType,
        "RetentionLockType": RetentionLockTypeType,
        "RetentionLockTimeInDays": int,
        "PoolStatus": PoolStatusType,
    },
    total=False,
)

_RequiredRefreshCacheInputRequestTypeDef = TypedDict(
    "_RequiredRefreshCacheInputRequestTypeDef",
    {
        "FileShareARN": str,
    },
)
_OptionalRefreshCacheInputRequestTypeDef = TypedDict(
    "_OptionalRefreshCacheInputRequestTypeDef",
    {
        "FolderList": List[str],
        "Recursive": bool,
    },
    total=False,
)

class RefreshCacheInputRequestTypeDef(
    _RequiredRefreshCacheInputRequestTypeDef, _OptionalRefreshCacheInputRequestTypeDef
):
    pass

RefreshCacheOutputTypeDef = TypedDict(
    "RefreshCacheOutputTypeDef",
    {
        "FileShareARN": str,
        "NotificationId": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RemoveTagsFromResourceInputRequestTypeDef = TypedDict(
    "RemoveTagsFromResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeys": List[str],
    },
)

RemoveTagsFromResourceOutputTypeDef = TypedDict(
    "RemoveTagsFromResourceOutputTypeDef",
    {
        "ResourceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ResetCacheInputRequestTypeDef = TypedDict(
    "ResetCacheInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

ResetCacheOutputTypeDef = TypedDict(
    "ResetCacheOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
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

RetrieveTapeArchiveInputRequestTypeDef = TypedDict(
    "RetrieveTapeArchiveInputRequestTypeDef",
    {
        "TapeARN": str,
        "GatewayARN": str,
    },
)

RetrieveTapeArchiveOutputTypeDef = TypedDict(
    "RetrieveTapeArchiveOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

RetrieveTapeRecoveryPointInputRequestTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointInputRequestTypeDef",
    {
        "TapeARN": str,
        "GatewayARN": str,
    },
)

RetrieveTapeRecoveryPointOutputTypeDef = TypedDict(
    "RetrieveTapeRecoveryPointOutputTypeDef",
    {
        "TapeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SMBFileShareInfoTypeDef = TypedDict(
    "SMBFileShareInfoTypeDef",
    {
        "FileShareARN": str,
        "FileShareId": str,
        "FileShareStatus": str,
        "GatewayARN": str,
        "KMSEncrypted": bool,
        "KMSKey": str,
        "Path": str,
        "Role": str,
        "LocationARN": str,
        "DefaultStorageClass": str,
        "ObjectACL": ObjectACLType,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "SMBACLEnabled": bool,
        "AccessBasedEnumeration": bool,
        "AdminUserList": List[str],
        "ValidUserList": List[str],
        "InvalidUserList": List[str],
        "AuditDestinationARN": str,
        "Authentication": str,
        "CaseSensitivity": CaseSensitivityType,
        "Tags": List["TagTypeDef"],
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
        "VPCEndpointDNSName": str,
        "BucketRegion": str,
        "OplocksEnabled": bool,
    },
    total=False,
)

SetLocalConsolePasswordInputRequestTypeDef = TypedDict(
    "SetLocalConsolePasswordInputRequestTypeDef",
    {
        "GatewayARN": str,
        "LocalConsolePassword": str,
    },
)

SetLocalConsolePasswordOutputTypeDef = TypedDict(
    "SetLocalConsolePasswordOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

SetSMBGuestPasswordInputRequestTypeDef = TypedDict(
    "SetSMBGuestPasswordInputRequestTypeDef",
    {
        "GatewayARN": str,
        "Password": str,
    },
)

SetSMBGuestPasswordOutputTypeDef = TypedDict(
    "SetSMBGuestPasswordOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

ShutdownGatewayInputRequestTypeDef = TypedDict(
    "ShutdownGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

ShutdownGatewayOutputTypeDef = TypedDict(
    "ShutdownGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartAvailabilityMonitorTestInputRequestTypeDef = TypedDict(
    "StartAvailabilityMonitorTestInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

StartAvailabilityMonitorTestOutputTypeDef = TypedDict(
    "StartAvailabilityMonitorTestOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StartGatewayInputRequestTypeDef = TypedDict(
    "StartGatewayInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

StartGatewayOutputTypeDef = TypedDict(
    "StartGatewayOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

StorediSCSIVolumeTypeDef = TypedDict(
    "StorediSCSIVolumeTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "VolumeType": str,
        "VolumeStatus": str,
        "VolumeAttachmentStatus": str,
        "VolumeSizeInBytes": int,
        "VolumeProgress": float,
        "VolumeDiskId": str,
        "SourceSnapshotId": str,
        "PreservedExistingData": bool,
        "VolumeiSCSIAttributes": "VolumeiSCSIAttributesTypeDef",
        "CreatedDate": datetime,
        "VolumeUsedInBytes": int,
        "KMSKey": str,
        "TargetName": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
)

TapeArchiveTypeDef = TypedDict(
    "TapeArchiveTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "CompletionTime": datetime,
        "RetrievedTo": str,
        "TapeStatus": str,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "RetentionStartDate": datetime,
        "PoolEntryDate": datetime,
    },
    total=False,
)

TapeInfoTypeDef = TypedDict(
    "TapeInfoTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "GatewayARN": str,
        "PoolId": str,
        "RetentionStartDate": datetime,
        "PoolEntryDate": datetime,
    },
    total=False,
)

TapeRecoveryPointInfoTypeDef = TypedDict(
    "TapeRecoveryPointInfoTypeDef",
    {
        "TapeARN": str,
        "TapeRecoveryPointTime": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
    },
    total=False,
)

TapeTypeDef = TypedDict(
    "TapeTypeDef",
    {
        "TapeARN": str,
        "TapeBarcode": str,
        "TapeCreatedDate": datetime,
        "TapeSizeInBytes": int,
        "TapeStatus": str,
        "VTLDevice": str,
        "Progress": float,
        "TapeUsedInBytes": int,
        "KMSKey": str,
        "PoolId": str,
        "Worm": bool,
        "RetentionStartDate": datetime,
        "PoolEntryDate": datetime,
    },
    total=False,
)

UpdateAutomaticTapeCreationPolicyInputRequestTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyInputRequestTypeDef",
    {
        "AutomaticTapeCreationRules": List["AutomaticTapeCreationRuleTypeDef"],
        "GatewayARN": str,
    },
)

UpdateAutomaticTapeCreationPolicyOutputTypeDef = TypedDict(
    "UpdateAutomaticTapeCreationPolicyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "_RequiredUpdateBandwidthRateLimitInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalUpdateBandwidthRateLimitInputRequestTypeDef = TypedDict(
    "_OptionalUpdateBandwidthRateLimitInputRequestTypeDef",
    {
        "AverageUploadRateLimitInBitsPerSec": int,
        "AverageDownloadRateLimitInBitsPerSec": int,
    },
    total=False,
)

class UpdateBandwidthRateLimitInputRequestTypeDef(
    _RequiredUpdateBandwidthRateLimitInputRequestTypeDef,
    _OptionalUpdateBandwidthRateLimitInputRequestTypeDef,
):
    pass

UpdateBandwidthRateLimitOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateBandwidthRateLimitScheduleInputRequestTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleInputRequestTypeDef",
    {
        "GatewayARN": str,
        "BandwidthRateLimitIntervals": List["BandwidthRateLimitIntervalTypeDef"],
    },
)

UpdateBandwidthRateLimitScheduleOutputTypeDef = TypedDict(
    "UpdateBandwidthRateLimitScheduleOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateChapCredentialsInputRequestTypeDef = TypedDict(
    "_RequiredUpdateChapCredentialsInputRequestTypeDef",
    {
        "TargetARN": str,
        "SecretToAuthenticateInitiator": str,
        "InitiatorName": str,
    },
)
_OptionalUpdateChapCredentialsInputRequestTypeDef = TypedDict(
    "_OptionalUpdateChapCredentialsInputRequestTypeDef",
    {
        "SecretToAuthenticateTarget": str,
    },
    total=False,
)

class UpdateChapCredentialsInputRequestTypeDef(
    _RequiredUpdateChapCredentialsInputRequestTypeDef,
    _OptionalUpdateChapCredentialsInputRequestTypeDef,
):
    pass

UpdateChapCredentialsOutputTypeDef = TypedDict(
    "UpdateChapCredentialsOutputTypeDef",
    {
        "TargetARN": str,
        "InitiatorName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateFileSystemAssociationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateFileSystemAssociationInputRequestTypeDef",
    {
        "FileSystemAssociationARN": str,
    },
)
_OptionalUpdateFileSystemAssociationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateFileSystemAssociationInputRequestTypeDef",
    {
        "UserName": str,
        "Password": str,
        "AuditDestinationARN": str,
        "CacheAttributes": "CacheAttributesTypeDef",
    },
    total=False,
)

class UpdateFileSystemAssociationInputRequestTypeDef(
    _RequiredUpdateFileSystemAssociationInputRequestTypeDef,
    _OptionalUpdateFileSystemAssociationInputRequestTypeDef,
):
    pass

UpdateFileSystemAssociationOutputTypeDef = TypedDict(
    "UpdateFileSystemAssociationOutputTypeDef",
    {
        "FileSystemAssociationARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateGatewayInformationInputRequestTypeDef = TypedDict(
    "_RequiredUpdateGatewayInformationInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)
_OptionalUpdateGatewayInformationInputRequestTypeDef = TypedDict(
    "_OptionalUpdateGatewayInformationInputRequestTypeDef",
    {
        "GatewayName": str,
        "GatewayTimezone": str,
        "CloudWatchLogGroupARN": str,
        "GatewayCapacity": GatewayCapacityType,
    },
    total=False,
)

class UpdateGatewayInformationInputRequestTypeDef(
    _RequiredUpdateGatewayInformationInputRequestTypeDef,
    _OptionalUpdateGatewayInformationInputRequestTypeDef,
):
    pass

UpdateGatewayInformationOutputTypeDef = TypedDict(
    "UpdateGatewayInformationOutputTypeDef",
    {
        "GatewayARN": str,
        "GatewayName": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateGatewaySoftwareNowInputRequestTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowInputRequestTypeDef",
    {
        "GatewayARN": str,
    },
)

UpdateGatewaySoftwareNowOutputTypeDef = TypedDict(
    "UpdateGatewaySoftwareNowOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "_RequiredUpdateMaintenanceStartTimeInputRequestTypeDef",
    {
        "GatewayARN": str,
        "HourOfDay": int,
        "MinuteOfHour": int,
    },
)
_OptionalUpdateMaintenanceStartTimeInputRequestTypeDef = TypedDict(
    "_OptionalUpdateMaintenanceStartTimeInputRequestTypeDef",
    {
        "DayOfWeek": int,
        "DayOfMonth": int,
    },
    total=False,
)

class UpdateMaintenanceStartTimeInputRequestTypeDef(
    _RequiredUpdateMaintenanceStartTimeInputRequestTypeDef,
    _OptionalUpdateMaintenanceStartTimeInputRequestTypeDef,
):
    pass

UpdateMaintenanceStartTimeOutputTypeDef = TypedDict(
    "UpdateMaintenanceStartTimeOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateNFSFileShareInputRequestTypeDef = TypedDict(
    "_RequiredUpdateNFSFileShareInputRequestTypeDef",
    {
        "FileShareARN": str,
    },
)
_OptionalUpdateNFSFileShareInputRequestTypeDef = TypedDict(
    "_OptionalUpdateNFSFileShareInputRequestTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
        "NFSFileShareDefaults": "NFSFileShareDefaultsTypeDef",
        "DefaultStorageClass": str,
        "ObjectACL": ObjectACLType,
        "ClientList": List[str],
        "Squash": str,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
    },
    total=False,
)

class UpdateNFSFileShareInputRequestTypeDef(
    _RequiredUpdateNFSFileShareInputRequestTypeDef, _OptionalUpdateNFSFileShareInputRequestTypeDef
):
    pass

UpdateNFSFileShareOutputTypeDef = TypedDict(
    "UpdateNFSFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSMBFileShareInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSMBFileShareInputRequestTypeDef",
    {
        "FileShareARN": str,
    },
)
_OptionalUpdateSMBFileShareInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSMBFileShareInputRequestTypeDef",
    {
        "KMSEncrypted": bool,
        "KMSKey": str,
        "DefaultStorageClass": str,
        "ObjectACL": ObjectACLType,
        "ReadOnly": bool,
        "GuessMIMETypeEnabled": bool,
        "RequesterPays": bool,
        "SMBACLEnabled": bool,
        "AccessBasedEnumeration": bool,
        "AdminUserList": List[str],
        "ValidUserList": List[str],
        "InvalidUserList": List[str],
        "AuditDestinationARN": str,
        "CaseSensitivity": CaseSensitivityType,
        "FileShareName": str,
        "CacheAttributes": "CacheAttributesTypeDef",
        "NotificationPolicy": str,
        "OplocksEnabled": bool,
    },
    total=False,
)

class UpdateSMBFileShareInputRequestTypeDef(
    _RequiredUpdateSMBFileShareInputRequestTypeDef, _OptionalUpdateSMBFileShareInputRequestTypeDef
):
    pass

UpdateSMBFileShareOutputTypeDef = TypedDict(
    "UpdateSMBFileShareOutputTypeDef",
    {
        "FileShareARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBFileShareVisibilityInputRequestTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityInputRequestTypeDef",
    {
        "GatewayARN": str,
        "FileSharesVisible": bool,
    },
)

UpdateSMBFileShareVisibilityOutputTypeDef = TypedDict(
    "UpdateSMBFileShareVisibilityOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateSMBSecurityStrategyInputRequestTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyInputRequestTypeDef",
    {
        "GatewayARN": str,
        "SMBSecurityStrategy": SMBSecurityStrategyType,
    },
)

UpdateSMBSecurityStrategyOutputTypeDef = TypedDict(
    "UpdateSMBSecurityStrategyOutputTypeDef",
    {
        "GatewayARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

_RequiredUpdateSnapshotScheduleInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSnapshotScheduleInputRequestTypeDef",
    {
        "VolumeARN": str,
        "StartAt": int,
        "RecurrenceInHours": int,
    },
)
_OptionalUpdateSnapshotScheduleInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSnapshotScheduleInputRequestTypeDef",
    {
        "Description": str,
        "Tags": List["TagTypeDef"],
    },
    total=False,
)

class UpdateSnapshotScheduleInputRequestTypeDef(
    _RequiredUpdateSnapshotScheduleInputRequestTypeDef,
    _OptionalUpdateSnapshotScheduleInputRequestTypeDef,
):
    pass

UpdateSnapshotScheduleOutputTypeDef = TypedDict(
    "UpdateSnapshotScheduleOutputTypeDef",
    {
        "VolumeARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

UpdateVTLDeviceTypeInputRequestTypeDef = TypedDict(
    "UpdateVTLDeviceTypeInputRequestTypeDef",
    {
        "VTLDeviceARN": str,
        "DeviceType": str,
    },
)

UpdateVTLDeviceTypeOutputTypeDef = TypedDict(
    "UpdateVTLDeviceTypeOutputTypeDef",
    {
        "VTLDeviceARN": str,
        "ResponseMetadata": "ResponseMetadataTypeDef",
    },
)

VTLDeviceTypeDef = TypedDict(
    "VTLDeviceTypeDef",
    {
        "VTLDeviceARN": str,
        "VTLDeviceType": str,
        "VTLDeviceVendor": str,
        "VTLDeviceProductIdentifier": str,
        "DeviceiSCSIAttributes": "DeviceiSCSIAttributesTypeDef",
    },
    total=False,
)

VolumeInfoTypeDef = TypedDict(
    "VolumeInfoTypeDef",
    {
        "VolumeARN": str,
        "VolumeId": str,
        "GatewayARN": str,
        "GatewayId": str,
        "VolumeType": str,
        "VolumeSizeInBytes": int,
        "VolumeAttachmentStatus": str,
    },
    total=False,
)

VolumeRecoveryPointInfoTypeDef = TypedDict(
    "VolumeRecoveryPointInfoTypeDef",
    {
        "VolumeARN": str,
        "VolumeSizeInBytes": int,
        "VolumeUsageInBytes": int,
        "VolumeRecoveryPointTime": str,
    },
    total=False,
)

VolumeiSCSIAttributesTypeDef = TypedDict(
    "VolumeiSCSIAttributesTypeDef",
    {
        "TargetARN": str,
        "NetworkInterfaceId": str,
        "NetworkInterfacePort": int,
        "LunNumber": int,
        "ChapEnabled": bool,
    },
    total=False,
)
